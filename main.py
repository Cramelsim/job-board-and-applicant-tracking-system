import click
from job_board_ats.lib.cli import cli
from job_board_ats.lib.cli import (
    create_employer, delete_employer, display_all_employers, find_employer_by_name,
    post_job, delete_job, display_all_jobs,
    create_applicant, delete_applicant, display_all_applicants,
    apply, update_application_status, delete_application, display_all_applications, init_db_command,
    schedule_interview_command, submit_feedback_command
)


@click.group()
def cli():
    """Job Board & Applicant Tracking System CLI"""
    pass

# Register Commands
cli.add_command(init_db_command)
cli.add_command(create_employer)
cli.add_command(delete_employer)
cli.add_command(display_all_employers)
cli.add_command(find_employer_by_name)

cli.add_command(post_job)
cli.add_command(delete_job)
cli.add_command(display_all_jobs)

cli.add_command(create_applicant)
cli.add_command(delete_applicant)
cli.add_command(display_all_applicants)

cli.add_command(apply)
cli.add_command(update_application_status)
cli.add_command(delete_application)
cli.add_command(display_all_applications)


cli.add_command(schedule_interview_command)
cli.add_command(submit_feedback_command)


if __name__ == "__main__":
    cli()
