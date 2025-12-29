import pytest
from bank import BankAccount
# def test_deposit():
#     acc=BankAccount("Madhan",1000)
#     assert acc.deposite(500)==1500
    
# def test_balance():
#     acc = BankAccount("Madhan", 1000)
#     assert acc.get_balance()==1000
#     assert acc.balance>0
@pytest.fixture
def account():
    return BankAccount("Madhan",1000)

def test_withdrawal(account):
    assert account.withdrawal(300)==700

def test_deposite(account):
    assert account.deposite(1000)==2000
    
def test_exception(account):
    with pytest.raises(ValueError):
        account.withdrawal(2000)
    
@pytest.mark.parametrize("amount",[100,200,300])
def test_multiple_deposite(account,amount):
    assert account.deposite(amount)>0
    
@pytest.fixture(scope="module")
def shared_account():
    return BankAccount("Shared", 500)
