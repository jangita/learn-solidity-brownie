from brownie import HelloWorld, accounts

def main():
    acct = accounts.load('chris')
    HelloWorld.deploy(,{'from': acct'})