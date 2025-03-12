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

