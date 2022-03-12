from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000

# this function returns an account matching with the right network
# if the network is "development", "ganache-local", "mainnet-fork" or "mainnet-fork-dev",
# then return the local built-in ganache account
# otherwise, return the account from brownie-config under: ["wallets"]["from_key"]
def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


# this function deploys mocks, a fake version of a contract in order to interact with it
# in this case it's deploying a mock for a pricefeed
# to deploy a mock copy+paste into contracts>tests> the code from // from: "https://github.com/smartcontractkit/chainlink-mix/tree/master/contracts/test"
# the MockV3Aggregator's constructor needs 2 parameters: DECIMALS and STARTING_PRICE
# additionaly for deployment it needs a {"from": get_account()}
# # the "if len(MockV3Aggregator)" gets the length of a list. If the list is empty (<= 0), then execute.
def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!")
