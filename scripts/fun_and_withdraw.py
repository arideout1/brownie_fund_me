from brownie import FundMe

from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entracne_fee = fund_me.getEntranceFee()
    print(entracne_fee)
    fund_me.fund({"from": account, "value": entracne_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
