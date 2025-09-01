import subprocess
from datetime import datetime
import smtplib
from email.mime.text import MIMEText


# --------------- Configuration ---------------
SERVICES = ["MSSQLSERVER", "Unisys Data Exchange Development Workbench Service 7047", "Unisys Data Exchange Administrative Service 7047"]
LOG_FILE= "health_check.log"

# --------------- Email Alert Settings ---------
ENABLE_EMAIL_ALERT = False
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SENDER_EMAIL = "alert@example.com"
SENDER_PASSWORD = "password"
RECEIVER_EMAIL = "supportteam@email.com"
# ---------------------------------------------

def check_service(service_name):
    """ Check the windows service using sc query"""
    try:
        output = subprocess.check_output(
            ["SC", "query", service_name], stderr= subprocess.STDOUT, text= True
        )

        if "RUNNING" in output:
            return "RUNNING"
        elif "STOPPED" in output:
            return "STOPPED"
        else:
            return "UNKNOWN"

    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.strip()}"

    

def log_status(service_name, status):
    """ Log the service request with the timestamp"""
    with open(LOG_FILE, 'a') as log:
        log.write(f"{datetime.now()} -{service_name} :{status} \n")

def send_email_alert(down_services):
    """" Send an email alert if sevices are down"""
    Subject = "Service Health Alert"
    body = "The Following Services Are Down : \n" + "\n".join(down_services)
    msg = MIMEText(body)
    msg["Subject"] = Subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL,SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL, msg.as_string())
        print("Alert Email Sent")

    except Exception as e:
        print(f"Failed to send email alert:{e}")
        

def main():
    down_services = []

    for service in SERVICES:
        status = check_service(service)
        print(f"{service} : {status}")
        log_status(service,status)

        if status != "RUNNING":
            down_services.append(service)
            print(down_services)
    if ENABLE_EMAIL_ALERT and down_services:
        send_email_alert(down_services)

if __name__=="__main__":
    main()