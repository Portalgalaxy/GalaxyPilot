import streamlit as st
import yfinance as yf
from datetime import date

st.set_page_config(page_title="GalaxyPilot", layout="wide")

# Branding
st.markdown("# 🚀 GalaxyPilot – La Opción Inteligente")
st.markdown("### 📊 Trading de Opciones | ETFs | Acciones")

# Ticker Selector
ticker = st.selectbox("Selecciona un ticker:", ["SPY", "AAPL", "NVDA"])

# Descargar datos
try:
    data = yf.download(ticker, period="1mo")
except Exception as e:
    data = None
    st.warning("⚠️ Error al intentar descargar los datos de Yahoo Finance.")

# Evaluar cierre
if data is None or data.empty or "Close" not in data.columns:
    st.warning("⚠ No se pudieron cargar los datos reales de precios. Se usará un valor estimado por defecto.")
    last_close = 640.00
    show_chart = False
else:
    last_close = round(data["Close"].iloc[-1], 2)
    show_chart = True

# Mostrar gráfico si hay datos
if show_chart:
    st.subheader(f"📈 Precio de cierre – {ticker}")
    st.line_chart(data["Close"])
else:
    st.info("📉 Gráfico no disponible por falta de datos.")

# Estrategia
st.markdown("### 🎯 Estrategia Cardona Seleccionada")
estrategia = st.radio("Estrategia:", ["Gap Bajista al Alza", "CALL en canal", "PUT en consolidación"])
st.write(f"Estrategia seleccionada: **{estrategia}**")

# Simulación básica
strike = st.number_input("Strike Price", value=last_close)
vencimiento = st.date_input("Vencimiento", value=date.today())
prima = st.slider("Prima estimada ($)", 0.5, 10.0, 1.5)

st.markdown(f"💰 Posible resultado al vencer: **{round(prima * 100, 2)} USD**")

# Exportación manual
st.markdown("💾 **Copia manualmente esta info para tu bitácora Notion:**")
st.code(f"Ticker: {ticker} | Estrategia: {estrategia} | Strike: {strike} | Prima: ${prima} | Vencimiento: {vencimiento}")

st.markdown("---")
st.caption("Versión MVP v0.1 • Colores: naranja, verde, azul • Marca: GalaxyPilot • Modo Fallback activado")
