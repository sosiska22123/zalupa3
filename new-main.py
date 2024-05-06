import requests
import time

symbols = ['bitcoin', 'ethereum', 'tether', 'bnb', 'solana', 'xrp', 'dogecoin', 'toncoin', 'cardano', 'shiba-inu', 'avalanche', 'tron', 'polkadot-new', 'bitcoin-cash', 'chainlink', 'near-protocol', 'polygon', 'internet-computer', 'litecoin',
           'multi-collateral-dai', 'uniswap', 'aptos', 'hedera', 'ethereum-classic', 'cronos', 'cosmos', 'stellar', 'filecoin', 'mantle', 'render', 'okb', 'immutable-x', 'renzo', 'pepe', 'arbitrum', 'optimism-ethereum', 'sui', 'dogwifhat', 'kaspa', 'vethor-token', 'bittensor','maker',
           'the-graph', 'monero', 'injective', 'fetch', 'theta', 'arweave', 'fantom', 'celestia', 'lido-dao','core-dao', 
           'bonk1', 'floki', 'algorand', 'quant', 'sei',
           'gala', 'jupiter-ag', 'flow', 'onbeam', 'wormhole', 'voyager-token','aave', 'bitcoin-sv', 'neo', 'ethena', 'flare', 'bittorrent-new',
           'ondo-finance', 'ribbon-finance', 'singularitynet', 'multiversx-egld', 'dydx-chain', 'chiliz', 'axie-infinity', 'gatetoken', 'the-sandbox',
           'starknet-token', 'akash-network', 'kucoin-tocken', 'tezos', 'ecash', 'eos', 'mina', 
           'synthetix', 'conflux-network', 'ronin', 'helium', 'safe','decentraland', 'jasmy', 'pyth-network','axelar', 'sats-ordinals', 'nervos-network', 'iota', 'kava',  
           'pancakeswap', 'tether-gold', 'terra-luna-v2', 'osmosis', 'wemix', 'venom', 'dymension', 'mantra', 'sats-ordinals', 'astar', 'wootrade','ocean-protocol', 'curve-dao-token', 'iotex', 'radix-protocol', 'altlayer', 
           'ethereum-name-service', 'ankr-network', '1inch', 'aerodrome-finance', 'amp', 'pax-gold', 'trust-wallet-token', 'zilliqa', 'enjin-coin', 'manta-network', 'green-metaverse-token', 'pendle', 'holo', 'arkham', 'memecoin', 'superfarm',  'livepeer', 
           'siacoin', 'celo', 'ravencoin', 'ethereum-pow', 'rocket-pool', 'terra-luna-v2', 'project-galaxy',
           'safepal', 'qtum', 'raydium', 'compound', 'zetachain', 'polymesh', 'casper', 'basic-attention-token', 'jito', 'binaryx-new']


for symbol in symbols:
        url = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug={symbol}&start=1&quoteCurrencyId=825&limit=100&category=perpetual&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true'

        print(symbol)
        response = requests.get(url).json()

        comission_dict = {'Binance': 0.07, 'Bybit': 0.05, 'MEXC': 0.05, 'KuCoin': 0.07}

        if "data" in response:
            market_pairs = response["data"]["marketPairs"]
            filtered_pairs = [pair for pair in market_pairs if pair["exchangeName"] in ["Binance", "Bybit", "MEXC", "KuCoin"]]

            funding_rates = {}

            for pair in filtered_pairs:
                exchange_name = pair.get('exchangeName', 'N/A')
                funding_rate = pair.get('fundingRate', 'N/A') * 100
                spot_price = pair.get('indexPrice', 'N/A')
                futures_price = pair.get('price', 'N/A')
                futures_url = pair.get('marketUrl', 'N/A')

                funding_rates[exchange_name] = (funding_rate, spot_price, futures_price, futures_url)

            for exchange1, (rate1, spot1, futures1, url1) in funding_rates.items():
                for exchange2, (rate2, spot2, futures2, url2) in funding_rates.items():
                    if exchange1 != exchange2:
                        diff = rate1 - rate2
                        if diff < -0.1 or diff > 0.1:
                            curse_spread = round(((futures1 - futures2) / futures2) * 100 , 3)

                            last_res = (f"{symbol} \n\n{url1} \n{exchange1} : {rate1} \nSpot : {spot1} \nFut : {futures1}\nCommission : {comission_dict[exchange1]}\n\n{url2} \n{exchange2} : {rate2} \nSpot : {spot2} \nFut : {futures2}\nCommission : {comission_dict[exchange2]}\n\nDifference : {diff:.4f}%\nTime : 8H \nCurse spread : {curse_spread}%")  
    
                            bot_token = '6346370947:AAFpePtGV60tX2PEv0rV0RK45h_VZcybx94'
                            chat_id = '-1001795323643'
                            url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={last_res}"
                            
                            response = requests.get(url)
                            data = response.json()
                            #print(data)

        else:
            #print(f"No data found for symbol {symbol}.")
            pass


