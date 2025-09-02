🛠️ Python Automation Scripts for Support Engineers

This repository contains a collection of Python scripts designed for Support Engineers / Application Support professionals.
These scripts automate common support tasks like monitoring, troubleshooting, database checks, and ticket management.

📌 Features & Scripts Included

Service Health Check (Windows/Linux)

Check if critical services are running.

Log results and send email alerts if services are down.

Log Analyzer

Parse application logs for errors/warnings.

Summarize and highlight frequently occurring issues.

Database Health Check

Connect to MySQL/Postgres/SQL Server.

Check active sessions, table sizes, and long-running queries.

File/Folder Monitoring

Monitor disk usage, large files, and log rotation.

Trigger alerts if thresholds are crossed.

Incident Auto-Report

Collect logs, system info, and service status.

Generate a ZIP file for RCA or ticket attachments.

User/Access Management

Automate adding/removing users on Linux/Databases.

Check password expiry and access levels.

API Testing/Health Script

Hit REST APIs, validate response codes & response times.

Store results in CSV for analysis.

Backup & Restore Script

Automate DB dumps and file backups.

Includes restore validation.

Ticket System Integration (ServiceNow/JIRA)

Fetch open tickets via REST API.

Auto-update status after checks.

Deployment / Release Validation

Verify services, DB schema changes, and perform sample checks post-deployment.

🚀 Getting Started
🔧 Requirements

Python 3.8+

Required packages:

pip install -r requirements.txt


For email alerts:

SMTP server details

App Password (if using Gmail/Outlook)

▶️ Usage Example

Run the Service Health Check script:

python service_health_check.py


Output:

Logs stored in service_health_check.log

Email alert sent if any service is down (when configured).

📂 Repository Structure
support-scripts/
│── service_health_check.py
│── log_analyzer.py
│── db_health_check.py
│── file_monitor.py
│── incident_auto_report.py
│── user_access_mgmt.py
│── api_health_check.py
│── backup_restore.py
│── ticket_integration.py
│── release_validation.py
│── requirements.txt
└── README.md

✨ Why These Scripts?

Reduce manual effort in daily support activities.

Faster incident resolution & RCA.

Proactive monitoring & prevention.

Demonstrates automation skills in SQL, Linux, Windows, APIs.
