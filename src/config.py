"""Configuracion central del proyecto: tickers monitoreados y umbrales de negocio."""
import os
from dotenv import load_dotenv

load_dotenv()

# Definicion de negocio: "penny stock" = precio de cierre menor a este umbral (USD).
PENNY_STOCK_PRICE_THRESHOLD = 5.0

# MVP: tickers reales, liquidos, conocidos como penny stocks al momento de escribir esto.
DEFAULT_TICKERS = ["SNDL", "CTRM", "PDSB", "RETO", "BNGO"]

# Credenciales y Base de Datos (Fase 1)
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/penny_stocks.db")