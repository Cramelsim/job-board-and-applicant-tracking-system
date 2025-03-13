# job_board_ats/lib/cli.py

import click
from job_board_ats.lib.models import Session, Employer, JobListing, Applicant, Application, Interview, InterviewFeedback
import ipdb  # for debugging purposes
from job_board_ats.lib.models import init_db 
from datetime import datetime

@click.command()
def init_db_command():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized.")

# Command to create an employer
@click.command()
@click.argument('name')
def create_employer(name):
    """Create a new employer in the system"""
    employer = Employer(name=name)
    session = Session()
    session.add(employer)
    session.commit()
    click.echo(f"Employer {name} added.")

# Command to delete an employer
@click.command()
@click.argument('employer_id', type=int)
def delete_employer(employer_id):
    """Delete an employer from the system"""
    session = Session()
    employer = session.query(Employer).filter_by(id=employer_id).first()
    if employer:
        # If the employer has any associated job listings, delete them first
        session.query(JobListing).filter_by(employer_id=employer_id).delete()
        
        session.delete(employer)
        session.commit()
        click.echo(f"Employer {employer_id} deleted.")
    else:
        click.echo(f"Employer {employer_id} not found.")


# Command to display all employers
@click.command()
def display_all_employers():
    """Display all employers"""
    session = Session()
    employers = session.query(Employer).all()
    if employers:
        click.echo("All Employers:")
        for employer in employers:
            click.echo(f"ID: {employer.id}, Name: {employer.name}")
    else:
        click.echo("No employers found.")

        # Command to find an employer by name
@click.command()
@click.argument('name')
def find_employer_by_name(name):
    """Find an employer by name"""
    session = Session()
    employer = session.query(Employer).filter_by(name=name).first()
    if employer:
        click.echo(f"Employer found: ID: {employer.id}, Name: {employer.name}")
    else:
        click.echo(f"Employer with name '{name}' not found.")


# Command to post a job
@click.command()
@click.argument('title')
@click.argument('employer_id', type=int)
@click.argument('description')
@click.argument('qualifications')
@click.argument('salary_range')
@click.argument('benefits')
@click.argument('deadline')
def post_job(title, employer_id, description, qualifications, salary_range, benefits, deadline):
    """Post a job listing"""
    job = JobListing(
        title=title,
        employer_id=employer_id,
        description=description,
        qualifications=qualifications,
        salary_range=salary_range,
        benefits=benefits,
        deadline=deadline
    )
    session = Session()
    session.add(job)
    session.commit()
    click.echo(f"Job '{title}' posted.")

 # Command to delete a job
@click.command()
@click.argument('job_id', type=int)
def delete_job(job_id):
    """Delete a job posting"""
    session = Session()
    job = session.query(JobListing).filter_by(id=job_id).first()
    if job:
        session.delete(job)
        session.commit()
        click.echo(f"Job {job_id} deleted.")
    else:
        click.echo(f"Job {job_id} not found.")

        
# Command to display all jobs with their timeline (created_at and deadline)
@click.command()
def display_all_jobs():
    """Display all jobs with their posting date and deadline"""
    session = Session()
    jobs = session.query(JobListing).all()
    if jobs:
        click.echo("All Jobs:")
        for job in jobs:
            # Check if created_at and deadline are available
            created_at = job.created_at.strftime("%Y-%m-%d %H:%M:%S") if job.created_at else "N/A"
            deadline = job.deadline.strftime("%Y-%m-%d %H:%M:%S") if job.deadline else "N/A"
            click.echo(f"ID: {job.id}, Title: {job.title}, Employer ID: {job.employer_id}, Created At: {created_at}, Deadline: {deadline}")
    else:
        click.echo("No jobs found.")


   

# Command to create an applicant
@click.command()
@click.argument('name')
@click.argument('email')
@click.argument('resume')
def create_applicant(name, email, resume):
    """Create a new applicant in the system"""
    applicant = Applicant(name=name, email=email, resume=resume)
    session = Session()
    session.add(applicant)
    session.commit()
    click.echo(f"Applicant {name} added.")

# Command to apply for a job
@click.command()
@click.argument('job_id', type=int)
@click.argument('applicant_id', type=int)
def apply(job_id, applicant_id):
    """Applicant applies for a job"""
    application = Application(job_id=job_id, applicant_id=applicant_id)
    session = Session()
    session.add(application)
    session.commit()
    
     # Fetch the applicant's email
    applicant = session.query(Applicant).filter_by(id=applicant_id).first()
    if applicant:
        subject = "Application Received"
        message = f"Dear {applicant.name},\n\nYour application for job {job_id} has been received. We will get back to you soon."
        send_email(subject, message, applicant.email)
        
    click.echo(f"Applicant {applicant_id} applied for job {job_id}.")

# Command to delete an applicant
@click.command()
@click.argument('applicant_id', type=int)
def delete_applicant(applicant_id):
    """Delete an applicant from the system"""
    session = Session()
    applicant = session.query(Applicant).filter_by(id=applicant_id).first()
    if applicant:
        session.delete(applicant)
        session.commit()
        click.echo(f"Applicant {applicant_id} deleted.")
    else:
        click.echo(f"Applicant {applicant_id} not found.")

# Command to display all applicants
@click.command()
def display_all_applicants():
    """Display all applicants"""
    session = Session()
    applicants = session.query(Applicant).all()
    if applicants:
        click.echo("All Applicants:")
        for applicant in applicants:
            click.echo(f"ID: {applicant.id}, Name: {applicant.name}, Email: {applicant.email}")
    else:
        click.echo("No applicants found.")

# Command to update application status
@click.command()
@click.argument('application_id', type=int)
@click.argument('status')
def update_application_status(application_id, status):
    """Update the status of an application"""
    session = Session()
    application = session.query(Application).filter_by(id=application_id).first()
    if application:
        application.status = status
        session.commit()
        click.echo(f"Application {application_id} updated to {status}.")
    else:
        click.echo(f"Application {application_id} not found.")

# Command to delete an application
@click.command()
@click.argument('application_id', type=int)
def delete_application(application_id):
    """Delete an application from the system"""
    session = Session()
    application = session.query(Application).filter_by(id=application_id).first()
    if application:
        session.delete(application)
        session.commit()
        click.echo(f"Application {application_id} deleted.")
    else:
        click.echo(f"Application {application_id} not found.")

# Command to display all applications
@click.command()
def display_all_applications():
    """Display all applications"""
    session = Session()
    applications = session.query(Application).all()
    if applications:
        click.echo("All Applications:")
        for application in applications:
            click.echo(f"ID: {application.id}, Job ID: {application.job_id}, Applicant ID: {application.applicant_id}, Status: {application.status}")
    else:
        click.echo("No applications found.")

# Command to schedule an interview
@click.command()
@click.argument('applicant_id', type=int)
@click.argument('employer_id', type=int)
@click.argument('interview_time')
@click.argument('location', required=False)
def schedule_interview_command(applicant_id, employer_id, interview_time, location=None):
    """Schedule an interview for an applicant"""
    session = Session()  # Initialize session
    try:
        interview_time = datetime.strptime(interview_time, "%Y-%m-%d %H:%M:%S")
        # Create the interview
        interview = Interview(
            applicant_id=applicant_id,
            employer_id=employer_id,
            interview_time=interview_time,
            location=location
        )
        session.add(interview)
        session.commit()  # Commit to the database

        # Send a calendar invite (this function can be expanded with actual calendar API integration)
        send_calendar_invite(interview)

        click.echo(f"Interview scheduled for Applicant {applicant_id} with Employer {employer_id} at {interview_time}.")
    except Exception as e:
        session.rollback()  # Rollback in case of error
        click.echo(f"Error scheduling interview: {e}")
    finally:
        session.close()  # Close the session


def send_calendar_invite(interview):
    # Code to send calendar invite (can integrate Google Calendar API or other services)
    click.echo(f"Sending calendar invite for interview scheduled on {interview.interview_time}.")


# Command to submit interview feedback
@click.command()
@click.argument('interview_id', type=int)
@click.argument('interviewer_name')
@click.argument('feedback')
@click.argument('rating', type=int)
def submit_feedback_command(interview_id, interviewer_name, feedback, rating):
    """Submit feedback for an interview"""
    session = Session()  # Initialize session
    try:
        # Create the interview feedback object
        interview_feedback = InterviewFeedback(
            interview_id=interview_id,
            interviewer_name=interviewer_name,
            feedback=feedback,
            rating=rating
        )
        session.add(interview_feedback)
        session.commit()  # Commit to the database

        click.echo(f"Feedback for Interview {interview_id} submitted by {interviewer_name}.")
    except Exception as e:
        session.rollback()  # Rollback in case of error
        click.echo(f"Error submitting feedback: {e}")
    finally:
        session.close()  # Close the session


# Adding commands to the CLI
@click.group()
def cli():
    """Job Board & Applicant Tracking System CLI"""
    pass

# Register commands
cli.add_command(create_employer)
cli.add_command(delete_employer)
cli.add_command(find_employer_by_name)
cli.add_command(post_job)
cli.add_command(delete_job)
cli.add_command(display_all_jobs)
cli.add_command(create_applicant)
cli.add_command(apply)
cli.add_command(delete_applicant)
cli.add_command(display_all_applicants)
cli.add_command(update_application_status)
cli.add_command(delete_application)
cli.add_command(display_all_applications)

if __name__ == '__main__':
    cli()
