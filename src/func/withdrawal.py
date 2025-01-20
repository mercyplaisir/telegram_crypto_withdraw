import ccxt	
import os
bin_obj = ccxt.binance(
    {
        "apiKey":os.getenv("BINANCEPUBLICKEY"),
        "secret":os.getenv("BINANCEPRIVATEKEY")
    }
)
def binance_withdraw(amount:float,address:str,coin:str="TRX",network:str="TRC20")->object:
    print("withdrawing ...")
    return bin_obj.withdraw(coin,amount,address,tag="",params={"network":network})