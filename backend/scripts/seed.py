from app.db.database import SessionLocal
from app.models.symbol import Symbol
SYMBOLS=[("SBER","Сбербанк","MOEX"),("GAZP","Газпром","MOEX"),("LKOH","Лукойл","MOEX"),("ROSN","Роснефть","MOEX"),("Si","USD/RUB Futures","MOEX FORTS"),("RTS","RTS Index Futures","MOEX FORTS")]
def run():
    db=SessionLocal()
    for ticker,name,market in SYMBOLS:
        if not db.query(Symbol).filter(Symbol.ticker==ticker).first():db.add(Symbol(ticker=ticker,name=name,market=market))
    db.commit(); db.close()
if __name__=="__main__":run()
