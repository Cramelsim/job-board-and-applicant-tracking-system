from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()
db_url = "sqlite:///job_board.db"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)

def init_db():
    """Initialize the database"""
    Base.metadata.create_all(engine)


class Employer(Base):
    __tablename__ = 'employers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    job_listings = relationship("JobListing", back_populates="employer", cascade="all, delete-orphan")
    interviews = relationship("Interview", back_populates="employer")
    

class JobListing(Base):
    __tablename__ = 'job_listings'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    employer_id = Column(Integer, ForeignKey('employers.id'))
    description = Column(String, nullable=False)
    qualifications = Column(String, nullable=False)
    salary_range = Column(String, nullable=False)
    benefits = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=False)  # The application deadline
    created_at = Column(DateTime, default=datetime.utcnow)  # The time when the job was posted
    
    employer = relationship("Employer", back_populates="job_listings")

class Applicant(Base):
    __tablename__ = 'applicants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    resume = Column(Text)

    applications = relationship('Application', back_populates='applicant', cascade="all, delete")
    interviews = relationship("Interview", back_populates="applicant")


class Application(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey('job_listings.id'))
    applicant_id = Column(Integer, ForeignKey('applicants.id'))
    status = Column(String, default='Pending')
    job = relationship('JobListing')
    applicant = relationship('Applicant', back_populates='applications')

class Interview(Base):
    __tablename__ = 'interviews'
    
    id = Column(Integer, primary_key=True)
    applicant_id = Column(Integer, ForeignKey('applicants.id'), nullable=False)
    employer_id = Column(Integer, ForeignKey('employers.id'), nullable=False)
    interview_time = Column(DateTime, nullable=False)
    location = Column(String, nullable=True)  # e.g., Zoom link or office address
    status = Column(String, default="Scheduled")  # "Scheduled", "Completed", "Cancelled"
    
    applicant = relationship("Applicant", back_populates="interviews")
    employer = relationship("Employer", back_populates="interviews")
    feedbacks = relationship("InterviewFeedback", back_populates="interview")
    feedback = Column(String)

class InterviewFeedback(Base):
    __tablename__ = 'interview_feedback'
    
    id = Column(Integer, primary_key=True)
    interview_id = Column(Integer, ForeignKey('interviews.id'), nullable=False)
    interviewer_name = Column(String, nullable=False)
    feedback = Column(String, nullable=False)
    rating = Column(Integer)  # e.g., 1-5 stars
    
    interview = relationship("Interview", back_populates="feedbacks")
    