from sqlalchemy.orm import sessionmaker
from job_board_ats.lib.models import engine, Employer, JobListing, Applicant, Application, Base
from datetime import date

# Create database tables
Base.metadata.create_all(engine)

# Start a session
Session = sessionmaker(bind=engine)
session = Session()

# Seed Employers
employer1 = Employer(name="Tech Corp")
employer2 = Employer(name="Innovate Ltd")
session.add_all([employer1, employer2])
session.commit()

# Seed Job Listings
job1 = JobListing(
    title="Software Engineer",
    employer_id=employer1.id,
    description="Develop and maintain software applications.",
    qualifications="BSc in Computer Science or related field.",
    salary_range="$70,000 - $90,000",
    benefits="Health insurance, Remote work options",
    deadline=date(2025, 12, 31)
)
job2 = JobListing(
    title="Data Analyst",
    employer_id=employer2.id,
    description="Analyze business data to generate insights.",
    qualifications="Experience with SQL and Python.",
    salary_range="$60,000 - $80,000",
    benefits="Flexible hours, Training programs",
    deadline=date(2025, 11, 15)
)
session.add_all([job1, job2])
session.commit()

# Seed Applicants
applicant1 = Applicant(name="John Doe", email="johndoe@example.com", resume="Experienced developer with Python skills.")
applicant2 = Applicant(name="Jane Smith", email="janesmith@example.com", resume="Data analyst with strong SQL knowledge.")
session.add_all([applicant1, applicant2])
session.commit()

# Seed Applications
application1 = Application(job_id=job1.id, applicant_id=applicant1.id, status="Pending")
application2 = Application(job_id=job2.id, applicant_id=applicant2.id, status="Pending")
session.add_all([application1, application2])
session.commit()

print("Database seeded successfully.")
