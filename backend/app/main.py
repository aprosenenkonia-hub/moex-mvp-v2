import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.symbols import router as symbols_router
from app.routers.watchlist import router as watchlist_router
from app.routers.candles import router as candles_router
from app.routers.market import router as market_router
from app.websocket.router import router as websocket_router
from app.services.redis_subscriber import subscribe_quotes
app=FastAPI(title="MOEX Analytics API",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
for r in [auth_router,users_router,symbols_router,watchlist_router,candles_router,market_router,websocket_router]: app.include_router(r)
@app.on_event("startup")
async def startup(): asyncio.create_task(subscribe_quotes())
@app.get("/")
async def root(): return {"status":"ok","service":"MOEX Analytics API"}
