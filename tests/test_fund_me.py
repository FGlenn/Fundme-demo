from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest

# to test whether the "fund" and "withdraw" function works correctly
# 1 arrange necessary components to execute test
# 2 act on functions
# 3 assert whether the results are correct
# the first assert is to check whether the "fund" function works correctly, the second for the "withdraw" function


def test_can_fund_and_withdraw():
    # 1
    account = get_account()
    fund_me = deploy_fund_me()
    # 2
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    # 3
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    # 2
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    # 3
    assert fund_me.addressToAmountFunded(account.address) == 0


# To test if only the owner can withdraw funds
# install pytest with - pip install pytest
# import pytest and import exceptions through brownie
# if     "fund_me.withdraw({"from": bad_actor})"    reverts with VirtualMachineError    then that's good
def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
