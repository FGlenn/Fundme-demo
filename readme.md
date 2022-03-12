Tn order to run brownie you'll need to install the following:
# Terminal > python -m pip install --user pipx
# Terminal > python -m pipx ensurepath
Now, each time you want to install a Python package on your computer (outside of a virtual environment specific to a project), do pipx install my_package instead of pip install my_package.
# pipx install eth-brownie

To automatically generate all files/folders:
# brownie int

To automatically create and place the ABI+bytecode files in .json:
# brownie compile

To run a script in brownie:
# brownie run 'folder'/'file'.'py/sol/etc'


3 Ways to add accounts:
1. Built in local Ganache accounts
# from brownie import accounts
This imported accounts package natively understands how to work with accounts
# account = accounts[]
Takes the account created by Ganache at the zerowidth index [0]

2. Encrypter command line
# Terminal > brownie accounts new 'name brownie account'
# Terminal > 'enter private key'
# Terminal > 'enter password'
# Terminal > brownie accounts list
# Terminal > brownie accounts delete 'name brownie account'
# account = accounts.load("name brownie account")

3. Enviromental variable
# create a ".env" file
# in ".env" file > export PRIVATE_KEY=0x....
# create "brownie-config.yaml" file
# in "brownie-config.yaml" file > dotenv: .env
# Add ".env" to ".gitignore", so it won't be exported.
3.A
# import os
# account = accounts.add(os.getenv("PRIVATE_KEY"))
# in "brownie-config.yaml" file > wallets:   from_key: ${PRIVATE_KEY}
3.B
# from brownie import config
# account = accounts.add(config["wallets"]["from_key"])

To check for networks
# Terminal > brownie networks list

To add network to brownie
# Terminal >brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1:7545 fork=https://eth-mainnet.alchemyapi.io/v2/0LeLMok1alT8TVWbFlPjVsWITxtUD_1b accounts=10 mnemonic=brownie port=7545
# Terminal >brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=5777


Import project ID in enviroment variables
# in ".env" file > export WEB3_INFURA_PROJECT_ID=____Check INFURA's website___


To be able to import functions from different scripts in the same folder
# create a new empty file in the same folder called : '__init__.py'
# from "folder name"."file name" import  "function to import name"

Contract verification
# get an API-key from my profile in Etherscan
# in ".env" file > ETHERSCAN_TOKEN=_____

