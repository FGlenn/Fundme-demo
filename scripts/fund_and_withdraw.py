from brownie import FundMe
from scripts.helpful_scripts import get_account

# this function interacts with the "fund" function from the deployed contract
# "FundMe[-1]" is the most recently deployed FundMe contract
# it builds a tranction "fund_me.fund" with required parameters for execution"({"from": account, "value": entrance_fee})"
def fund():
    print("funding account...")
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


# this function interacts with the "withdraw" function from the deployed contract
# "FundMe[-1]" is the most recently deployed FundMe contract
# it builds a tranction "fund_me.withdraw" with required parameter for execution"({"from": account})"
def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
