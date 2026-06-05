import time
from fake_algopack import FakeAlgoPack
from publisher import publish_quote
from storage import save_candle
SYMBOLS=["SBER","GAZP","LKOH","Si","RTS"]
def main():
    api=FakeAlgoPack()
    while True:
        for s in SYMBOLS:
            q=api.get_quote(s); c=api.get_candle(s); publish_quote(q); save_candle(c); print(f"{s}: {q['price']}")
        time.sleep(1)
if __name__=="__main__":main()
