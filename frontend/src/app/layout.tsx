import "./globals.css";
import QueryProvider from "@/providers/QueryProvider";
export const metadata={title:"MOEX Analytics Platform",description:"Order Flow, Open Interest, Delta and MOEX market analytics."};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="ru"><body><QueryProvider>{children}</QueryProvider></body></html>}
