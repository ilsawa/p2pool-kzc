from p2pool.kzc import networks

PARENT = networks.nets['kzc']
SHARE_PERIOD = 25
CHAIN_LENGTH = 24*60*60//25
REAL_CHAIN_LENGTH = 24*60*60//25
TARGET_LOOKBEHIND = 100
SPREAD = 10
IDENTIFIER = '1bfe3868e2b7a04f'.decode('hex')
PREFIX = '1bfe3868e64b2750'.decode('hex')
COINBASEEXT = '2f5032506f6f6c2d4b5a432f'.decode('hex')
P2P_PORT = 8278
MIN_TARGET = 4
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8279
BOOTSTRAP_ADDRS = 'crypto.mine.nu tomsk.mine.nu p2p-spb.xyz'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-kzc'
VERSION_CHECK = lambda v: v >= 10701
