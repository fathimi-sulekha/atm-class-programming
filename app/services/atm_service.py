from sqlalchemy.orm import Session
from app.services.models import User, Transaction

class ATMService:
    def __init__(self, db: Session):
        self.db = db

    def create_account(self, username, pin, initial_deposit):
        existing_user = self.db.query(User).filter(User.username == username).first()
        if existing_user:
            return {"error": "Username already exists"}
        
        new_user = User(username=username, pin=pin, balance=initial_deposit)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return {"message": f"Account created successfully for {username}"}

    def deposit(self, username, amount):
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            return {"error": "User not found"}
        
        user.balance += amount
        transaction = Transaction(user_id=user.id, type="deposit", amount=amount)
        self.db.add(transaction)
        self.db.commit()
        return {"message": f"Deposited ${amount:.2f}. New balance: ${user.balance:.2f}"}

    def withdraw(self, username, amount):
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            return {"error": "User not found"}
        
        if user.balance < amount:
            return {"error": "Insufficient balance"}
        
        user.balance -= amount
        transaction = Transaction(user_id=user.id, type="withdrawal", amount=amount)
        self.db.add(transaction)
        self.db.commit()
        return {"message": f"Withdrew ${amount:.2f}. New balance: ${user.balance:.2f}"}

    def show_balance(self, username):
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            return {"error": "User not found"}
        return {"balance": user.balance}

    def show_transactions(self, username):
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            return {"error": "User not found"}
        
        transactions = self.db.query(Transaction).filter(Transaction.user_id == user.id).all()
        return [{"type": tx.type, "amount": tx.amount, "date": tx.date} for tx in transactions]
