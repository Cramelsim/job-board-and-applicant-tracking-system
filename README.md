# job-board-and-applicant-tracking-system
This project is a Job Board & Applicant Tracking System (ATS) designed to manage job postings, job applications, interview scheduling, and feedback collection for employers and applicants. It provides a command-line interface (CLI) to interact with the system and allows employers to post jobs, hire applicants, schedule interviews, and collect feedback.

## Features

- **Employer Management**: Create, delete, and view employers.
- **Job Listings**: Post, delete, and view job listings.
- **Applicant Management**: Create, delete, and view applicants.
- **Applications**: Applicants can apply for jobs and employers can update the status of applications.
- **Interview Scheduling**: Schedule interviews for applicants and employers with date, time, and location.
- **Interview Feedback**: Collect feedback from interviewers after the interview.
- **Email Communication**: Send email notifications for interview schedules (via email communication integration).
  
## Requirements

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- SQLite (for the database)
- Necessary Python packages: `SQLAlchemy`, `Click`, `SQLite3`

## Setup

### Clone the repository

```bash
git clone https://github.com/yourusername/job-board-ats.git
cd job-board-ats
bashCopygit clone https://github.com/yourusername/job-board-ats.git
cd job-board-ats

## Install Dependencies
Create a virtual environment and install the required dependencies.
bashCopypython3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Initialize Database
To initialize the SQLite database:
bashCopypython main.py init-db
This will create the necessary tables in the job_board.db SQLite database.

## Usage
The project is controlled via a command-line interface (CLI). Use the following commands to interact with the system.
Employer Management
Create an employer:
bashCopypython main.py create-employer "Company Name"
Delete an employer:
bashCopypython main.py delete-employer 1
Display all employers:
bashCopypython main.py display-all-employers
Find an employer by name:
bashCopypython main.py find-employer-by-name "Company Name"
Job Listings
Post a job:
bashCopypython main.py post-job "Job Title" 1 "Job Description" "Qualifications" "Salary Range" "Benefits" "2025-03-30"
Delete a job:
bashCopypython main.py delete-job 1
Display all jobs:
bashCopypython main.py display-all-jobs
Applicant Management
Create an applicant:
bashCopypython main.py create-applicant "John Doe" "john@example.com" "resume.pdf"
Delete an applicant:
bashCopypython main.py delete-applicant 1
Display all applicants:
bashCopypython main.py display-all-applicants
Applications
Apply for a job:
bashCopypython main.py apply 1 1
Update application status:
bashCopypython main.py update-application-status 1 "Accepted"
Delete an application:
bashCopypython main.py delete-application 1
Display all applications:
bashCopypython main.py display-all-applications
Interview Scheduling
Schedule an interview:
bashCopypython main.py schedule-interview-command 1 1 "2025-03-15 10:00:00" "Company Office"
Email Communication
The system sends email notifications when an interview is scheduled, using the smtplib module. Make sure you have the email sending functionality configured properly in the system. The send_email function should be integrated with your email service (like Gmail, Outlook, etc.).

## Database Schema
The system uses an SQLite database (job_board.db) with the following tables:

Employers: Contains the employer's information.
Job Listings: Contains job postings, linked to employers.
Applicants: Contains applicant information.
Applications: Contains job applications submitted by applicants.
Interviews: Contains interview schedules.
Interview Feedback: Contains feedback submitted after interviews.

## Development
If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-name).
3. Commit your changes (git commit -am 'Add new feature').
4 .Push to the branch (git push origin feature-name).
5. Create a new Pull Request.

##License
This project is licensed under the MIT License - see the LICENSE file for details.
