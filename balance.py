from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=contract_address, abi=abi)


balance1 = w3.eth.get_balance("0xFC66b812D092db1B2F8308bdE5692e3db33146Ad")

balance2 = w3.eth.get_balance("0x642D563C322C1f6B54268e0b3C6a18c23e2Ef157")

balance3 = w3.eth.get_balance("0xd7eA8e946A73A5805713660a20D7Aeb963b0934D")

balance4 = w3.eth.get_balance("0xe953E4f6cFaECC25e465FEccB7066A995D6Dae8F")

balance5 = w3.eth.get_balance("0x2Ab46B948B826DCCd81664002c2b1E6bCf016768")

print(f'Баланс 1 аккаунта: {balance1}')
print(f'Баланс 2 аккаунта: {balance2}')
print(f'Баланс 3 аккаунта: {balance3}')
print(f'Баланс 4 аккаунта: {balance4}')
print(f'Баланс 5 аккаунта: {balance5}')