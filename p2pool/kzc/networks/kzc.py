import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'bd1b44ba'.decode('hex')
P2P_PORT = 8277
ADDRESS_VERSION = 46
SCRIPT_ADDRESS_VERSION = 16
RPC_PORT = 8276
RPC_CHECK = defer.inlineCallbacks(lambda kzcd: defer.returnValue(
            'kzcashaddress' in (yield kzcd.rpc_help()) and
            not (yield kzcd.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('dash_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('dash_hash').getPoWHash(data))
BLOCK_PERIOD = 150
SYMBOL = 'KZC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'kzcashcore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/kzcashcore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.kzcashcore'), 'kzcash.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://chain.kzcash.kz/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://chain.kzcash.kz/address/'
TX_EXPLORER_URL_PREFIX = 'http://chain.kzcash.kz/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
