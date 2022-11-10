from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    FORKED_LOCAL_ENVIRONMENTS,
)

# Since the account we want to use depends on the network we will deploy on, we need to use the get_account() function from helpful_scripts.py
# in order to find out which price feed address needs to be used to deploy the contract we have this if/else statement
# if the current network is not LOCAL_BLOCKCHAIN_ENVIRONMENTS (if it's not a development network), then use the pricefeed from config.yaml
# if the current network is a development network, then deploy mocks and use the pricefeed from the MockV3Aggregator
# import "from brownie import MockV3Aggregator"
def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    # After "from brownie import FundMe" the contract can be deployed by adding ".deploy".
    # When deploying we need 3 parameters, depending on the network: price_feed_address, {"from": account}, publish_source=
    # The price_feed_address will be used in the FundMe.sol constructor to set up the right AggregatorV3Interface
    # the "publish_source" True/False it determined by the "config.yaml" file
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
