import type { Config } from "tailwindcss";
const config: Config = { content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"], theme: { extend: { colors: { terminal: { bg: "#020617", panel: "#0f172a", border: "#1e293b" }}}}, plugins: [] };
export default config;
