export type Candle={time:string;open:number;high:number;low:number;close:number;volume?:number};
export type OpenInterest={symbol:string;value:number;change:number};
export type Delta={symbol:string;delta:number};
export type OrderBookLevel={price:number;volume:number};
export type OrderBook={symbol:string;bids:OrderBookLevel[];asks:OrderBookLevel[]};
export type QuoteMessage={type:"quote";data:{symbol:string;price:number;volume:number;ts:string}};
