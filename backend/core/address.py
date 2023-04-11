from bitcoinaddress import Wallet
from mnemonic import Mnemonic
from web3 import Web3
from tronpy.keys import PrivateKey as TronPrivateKey


def GenerateAddress(currency="BTC", network="mainnet", seed=None):
    private_key = ""
    public_key = ""
    if currency == 'BTC':

        if network == "mainnet":
            testnet = False
        else:
            network = "testnet"
            testnet = True

        wallet = Wallet(seed, testnet=testnet)
        private_key = wallet.key.__dict__['hex']
        public_key = wallet.address.__dict__[network].__dict__["pubaddr1"]
    elif currency == 'ETH':

        mnemo = Mnemonic("english")
        words = seed
        if words is None:
            words = mnemo.generate(strength=256)
        seedgenerated = mnemo.to_seed(words, passphrase="")
        NETWORK_HTTP_ENDPOINT = ""
        if network == "mainnet":
            NETWORK_HTTP_ENDPOINT = "https://eth‑mainnet.public.blastapi.io"
        else:
            NETWORK_HTTP_ENDPOINT = "https://ropsten.infura.io/v3/"

        w3 = Web3(Web3.HTTPProvider(NETWORK_HTTP_ENDPOINT))
        account = w3.eth.account.from_key(seedgenerated[:32])
        private_key = account._private_key.hex()
        public_key = account.address
    elif currency == 'TRX':

        priv_key = TronPrivateKey.random()
        account = priv_key.public_key.to_base58check_address()
        private_key = priv_key
        public_key = account

    return {"private_address": str(private_key), "public_address": str(public_key)}
