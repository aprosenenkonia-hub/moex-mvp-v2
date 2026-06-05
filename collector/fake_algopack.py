import random
from datetime import datetime
class FakeAlgoPack:
    def __init__(self):self.prices={"SBER":285.0,"GAZP":165.0,"LKOH":7200.0,"Si":90000.0,"RTS":112000.0}
    def get_quote(self,symbol):
        price=self.prices.get(symbol,100.0)+random.uniform(-1.5,1.5); self.prices[symbol]=price; return {"symbol":symbol,"price":round(price,2),"volume":random.randint(100,5000),"ts":datetime.utcnow().isoformat()}
    def get_candle(self,symbol):
        op=self.prices.get(symbol,100.0); cl=op+random.uniform(-1.2,1.2); hi=max(op,cl)+random.uniform(0,1); lo=min(op,cl)-random.uniform(0,1); self.prices[symbol]=cl; return {"symbol":symbol,"timeframe":"1m","ts":datetime.utcnow(),"open":round(op,2),"high":round(hi,2),"low":round(lo,2),"close":round(cl,2),"volume":random.randint(1000,20000)}
