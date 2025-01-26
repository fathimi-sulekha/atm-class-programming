from app.services.atm_service import ATMService
from sqlalchemy.orm import Session

class AccountController:
    def __init__(self, db: Session):
        self.service = ATMService(db)

    def create_account(self, username, pin, initial_deposit):
        return self.service.create_account(username, pin, initial_deposit)

    def deposit(self, username, amount):
        return self.service.deposit(username, amount)

    def withdraw(self, username, amount):
        return self.service.withdraw(username, amount)

    def show_balance(self, username):
        return self.service.show_balance(username)

    def show_transactions(self, username):
        return self.service.show_transactions(username)
