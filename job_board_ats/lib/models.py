from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

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
    jobs = relationship('JobListing', back_populates='employer', cascade="all, delete")

class JobListing(Base):
    __tablename__ = 'job_listings'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    employer_id = Column(Integer, ForeignKey('employers.id'))
    description = Column(Text, nullable=False)
    qualifications = Column(Text, nullable=False)
    salary_range = Column(String)
    benefits = Column(Text)
    deadline = Column(Date)
    employer = relationship('Employer', back_populates='jobs')

class Applicant(Base):
    __tablename__ = 'applicants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    resume = Column(Text)
    applications = relationship('Application', back_populates='applicant', cascade="all, delete")
