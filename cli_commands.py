# job_board_ats/lib/cli.py

import click
from job_board_ats.lib.models import Session, Employer, JobListing, Applicant, Application
import ipdb  # for debugging purposes

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

# Adding commands to the CLI
@click.group()
def cli():
    """Job Board & Applicant Tracking System CLI"""
    pass

# Register commands
cli.add_command(create_employer)
cli.add_command(post_job)
cli.add_command(create_applicant)
cli.add_command(apply)
cli.add_command(delete_applicant)
cli.add_command(display_all_applicants)
cli.add_command(update_application_status)
cli.add_command(delete_application)
cli.add_command(display_all_applications)

if __name__ == '__main__':
    cli()
