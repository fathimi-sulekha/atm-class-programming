from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.controller.account_controller import AccountController
from app.core.config import CreateAccountRequest,DepositWithdrawRequest,BalanceTransactions

router = APIRouter()

@router.post("/create-account")
def create_account(request: CreateAccountRequest, db: Session = Depends(get_db)):
    controller = AccountController(db)
    return controller.create_account(request.username, request.pin, request.initial_deposit)

@router.post("/deposit")
def deposit(request: DepositWithdrawRequest, db: Session = Depends(get_db)):
    controller = AccountController(db)
    return controller.deposit(request.username, request.amount)

@router.post("/withdraw")
def withdraw(request: DepositWithdrawRequest, db: Session = Depends(get_db)):
    controller = AccountController(db)
    return controller.withdraw(request.username, request.amount)

@router.get("/balance")
def show_balance(request: BalanceTransactions, db: Session = Depends(get_db)):
    controller = AccountController(db)
    return controller.show_balance(request.username)

@router.get("/transactions")
def show_transactions(request: BalanceTransactions, db: Session = Depends(get_db)):
    controller = AccountController(db)
    return controller.show_transactions(request.username)
