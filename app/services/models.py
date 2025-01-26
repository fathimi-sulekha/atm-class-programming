from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.dependencies.database import Base  # Import Base from database

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    pin = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    api_key = Column(String, nullable=True)

    transactions = relationship("Transaction", back_populates="user")

# Transaction model
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String, nullable=False)  # 'deposit' or 'withdrawal'
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")
