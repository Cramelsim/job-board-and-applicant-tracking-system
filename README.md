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
git clone https://github.com/yourusername/job-board-application-tracking-system.git
cd job-board-application-tracking-system
```

## Install Dependencies
1. Create a virtual environment and install the required dependencies.
```bash
pipenv install && pipenv shell 
```
## Initialize Database
To initialize the SQLite database:
```bash
python main.py init-db
```
This will create the necessary tables in the job_board.db SQLite database.

## Usage
The project is controlled via a command-line interface (CLI). Use the following commands to interact with the system.

## Employer Management
### Create an employer:
```bash
python main.py create-employer "Company Name"
```

### Delete an employer:
```bash
python main.py delete-employer "employer-id"
```

### Display all employers:
```bash
python main.py display-all-employers
```

### Find an employer by name:
```bash
python main.py find-employer-by-name "Company Name"
```

## Job Listings

### Post a job:
```bash
python main.py post-job "Job Title" "job-id" "Job Description" "Qualifications" "Salary Range" "Benefits" "2025-03-30"
```

### Delete a job:
```bash
python main.py delete-job "job-id"
```

### Display all jobs:
```bash
python main.py display-all-jobs
```

## Applicant Management

### Create an applicant:
```bash
python main.py create-applicant "John Doe" "john@example.com" "resume.pdf"
```

### Delete an applicant:
```bash
python main.py delete-applicant "applicant-id"
```

### Display all applicants:
```bash
python main.py display-all-applicants
```

## Applications

### Apply for a job:
```bash
python main.py apply "job-id" "applicant-id"
```

### Update application status:
```bash
python main.py update-application-status "application-id" "Accepted"
```

### Delete an application:
```bash
python main.py delete-application "application-id"
```

### Display all applications:
```bash
python main.py display-all-applications
```

## Interview Scheduling

### Schedule an interview:
```bash
python main.py schedule-interview-command "applicant-id" "employer-id" "2025-03-15 10:00:00" "Company Office"
```

## Email Communication
The system sends email notifications when an interview is scheduled, using the `smtplib` module.

## Database Schema
The system uses an SQLite database (`job_board.db`) with the following tables:

- **Employers**: Contains employer information.
- **Job Listings**: Contains job postings, linked to employers.
- **Applicants**: Contains applicant information.
- **Applications**: Contains job applications submitted by applicants.
- **Interviews**: Contains interview schedules.
- **Interview Feedback**: Contains feedback submitted after interviews.

## Development
If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -am 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a new Pull Request.

## License
This project is licensed under the MIT License.

