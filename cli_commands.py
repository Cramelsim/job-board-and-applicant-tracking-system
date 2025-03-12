import click
from model import Session, Employer, JobListing, Applicant, Application

# Create a session
session = Session()

# Commands for managing Employers
@click.command()
@click.argument('name')
def create_employer(name):
    employer = Employer(name=name)
    session.add(employer)
    session.commit()
    click.echo(f"Employer {name} added.")

@click.command()
@click.argument('id', type=int)
def delete_employer(id):
    employer = session.query(Employer).filter_by(id=id).first()
    if employer:
        session.delete(employer)
        session.commit()
        click.echo(f"Employer with ID {id} deleted.")
    else:
        click.echo("Employer not found.")

@click.command()
def display_all_employers():
    employers = session.query(Employer).all()
    if employers:
        for employer in employers:
            click.echo(f"Employer ID: {employer.id}, Name: {employer.name}")
    else:
        click.echo("No employers found.")

@click.command()
@click.argument('name')
def find_employer_by_name(name):
    employers = session.query(Employer).filter_by(name=name).all()
    if employers:
        for employer in employers:
            click.echo(f"Employer ID: {employer.id}, Name: {employer.name}")
    else:
        click.echo("No employer found with that name.")

# Commands for managing Job Listings
@click.command()
@click.argument('title')
@click.argument('employer_id', type=int)
@click.argument('description')
@click.argument('qualifications')
@click.argument('salary_range')
@click.argument('benefits')
@click.argument('deadline')
def post_job(title, employer_id, description, qualifications, salary_range, benefits, deadline):
    job = JobListing(
        title=title,
        employer_id=employer_id,
        description=description,
        qualifications=qualifications,
        salary_range=salary_range,
        benefits=benefits,
        deadline=deadline
    )
    session.add(job)
    session.commit()
    click.echo(f"Job {title} posted.")

@click.command()
@click.argument('id', type=int)
def delete_job(id):
    job = session.query(JobListing).filter_by(id=id).first()
    if job:
        session.delete(job)
        session.commit()
        click.echo(f"Job with ID {id} deleted.")
    else:
        click.echo("Job not found.")

@click.command()
def display_all_jobs():
    jobs = session.query(JobListing).all()
    if jobs:
        for job in jobs:
            click.echo(f"Job ID: {job.id}, Title: {job.title}")
    else:
        click.echo("No jobs found.")

# Commands for managing Applicants
@click.command()
@click.argument('name')
@click.argument('email')
@click.argument('resume')
def create_applicant(name, email, resume):
    applicant = Applicant(name=name, email=email, resume=resume)
    session.add(applicant)
    session.commit()
    click.echo(f"Applicant {name} added.")

@click.command()
@click.argument('id', type=int)
def delete_applicant(id):
    applicant = session.query(Applicant).filter_by(id=id).first()
    if applicant:
        session.delete(applicant)
        session.commit()
        click.echo(f"Applicant with ID {id} deleted.")
    else:
        click.echo("Applicant not found.")

@click.command()
def display_all_applicants():
    applicants = session.query(Applicant).all()
    if applicants:
        for applicant in applicants:
            click.echo(f"Applicant ID: {applicant.id}, Name: {applicant.name}")
    else:
        click.echo("No applicants found.")

# Commands for managing Applications
@click.command()
@click.argument('job_id', type=int)
@click.argument('applicant_id', type=int)
def apply(job_id, applicant_id):
    application = Application(job_id=job_id, applicant_id=applicant_id)
    session.add(application)
    session.commit()
    click.echo(f"Application submitted.")

@click.command()
@click.argument('application_id', type=int)
@click.argument('status')
def update_application_status(application_id, status):
    application = session.query(Application).filter_by(id=application_id).first()
    if application:
        application.status = status
        session.commit()
        click.echo(f"Application {application_id} updated to {status}.")
    else:
        click.echo("Application not found.")

@click.command()
@click.argument('id', type=int)
def delete_application(id):
    application = session.query(Application).filter_by(id=id).first()
    if application:
        session.delete(application)
        session.commit()
        click.echo(f"Application with ID {id} deleted.")
    else:
        click.echo("Application not found.")

@click.command()
def display_all_applications():
    applications = session.query(Application).all()
    if applications:
        for application in applications:
            click.echo(f"Application ID: {application.id}, Job ID: {application.job_id}, Applicant ID: {application.applicant_id}, Status: {application.status}")
    else:
        click.echo("No applications found.")
