from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from khoj.database.models import Base

class InsurancePolicy(Base):
    __tablename__ = "insurance_policies"
    
    id = Column(Integer, primary_key=True)
    policy_number = Column(String, unique=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"))
    product_name = Column(String)
    coverage_amount = Column(Float)
    premium_annual = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String)  # active, expired, cancelled

class InsuranceClaim(Base):
    __tablename__ = "insurance_claims"
    
    id = Column(Integer, primary_key=True)
    claim_id = Column(String, unique=True, index=True)
    policy_id = Column(Integer, ForeignKey("insurance_policies.id"))
    claim_amount = Column(Float)
    submitted_date = Column(DateTime)
    status = Column(String)  # submitted, processing, approved, rejected
    notes = Column(String)