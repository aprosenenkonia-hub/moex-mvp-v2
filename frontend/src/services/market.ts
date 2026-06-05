import { apiFetch } from "@/lib/api"; import type { Candle,Delta,OpenInterest,OrderBook } from "@/types/market";
export async function getCandles(symbol:string):Promise<Candle[]>{const r=await apiFetch(`/candles/${symbol}`);return r.json()}
export async function getOpenInterest(symbol:string):Promise<OpenInterest>{const r=await apiFetch(`/market/oi/${symbol}`);return r.json()}
export async function getDelta(symbol:string):Promise<Delta>{const r=await apiFetch(`/market/delta/${symbol}`);return r.json()}
export async function getOrderBook(symbol:string):Promise<OrderBook>{const r=await apiFetch(`/market/orderbook/${symbol}`);return r.json()}
