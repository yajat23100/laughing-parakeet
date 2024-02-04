from web3 import Web3
from web3.middleware import geth_poa_middleware

API_url = 'https://mainnet.infura.io/v3/a36a08419aeb437ca8c79973e97b5868'
web3 = Web3(Web3.HTTPProvider(API_url))

Block_data = web3.geth.getBlock(19154560)

print('transaction data :', Block_data ['transactions'])
transaction = web3.eth.get_transaction('0x2ce85b9aabddbf910f44c41b47be60d126d3065c19f2cd3fb5c8aba8ff478f04')

print('blockHash:', transaction['blockHash'].hex())
print('blockNumber:', transaction['blockNumber'])
print('from:', transaction['from'])
print('gas:', transaction['gas'])
print('gasPrice in ether:', transaction['gasPrice'])
print('hash:', transaction['hash'].hex())
print('input:', transaction['input'])
print('nonce:', transaction['nonce'])
print('signature:', transaction['s'].hex())
print('to:', transaction['to'])
print('value:', transaction['value'])