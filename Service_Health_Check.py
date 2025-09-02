import subprocess
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# ---------  Configuration ---------------------
SERVICES = ["services_examplecd"]
LOG_FILE = "Health_Check_log.log"

#------------ Email Alert Configuration -----------
ENABLE_EMAIL_ALERT = False
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SENDER_EMAIL = "SENDER@example.com"
SENDER_PASSWORD = "password"
RECEIVER_EMAIL = "receiver@example.com"
#------------------------------------------------

def service_check(service):
    """ Check the status of windows services using SC  query"""
    try:
        output = subprocess.check_output(
            ["sc", "query", service], stderr=subprocess.STDOUT, text=True
        )
        if "RUNNING" in output:
            return "RUNNING"
        elif "STOPPED" in output:
            return "STOPPED"
        else:
            return "UNKNOWN"
    
    except subprocess.CalledProcessError as e:
        return f"ERROR: {e.output.strip()}"
    

def log_status(service,status):
    """ Log the service status with timestamp"""
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {service}: {status}\n")

def send_email_alerts(down_services):
    """Send email alert if service is not running"""
    subject = "Service Health"
    body =  "The following services are not runnning :\n" +"\n" .join(down_services)
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL,SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL,msg.as_strip())
        print("Email Alert Sent")
    
    except Exception as e:
        print(f"Failed to send email alert: {e}")

def main():
    down_services = []
    for service in SERVICES:
        status = service_check(service)
        print(f"{service} : {status}")
        log_status(service, status)
    
        if status != "RUNNIG":
            down_services.append(service)
        
    if ENABLE_EMAIL_ALERT and down_services :
        send_email_alerts(down_services)


if __name__== "__main__":
    main()