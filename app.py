import streamlit as st
import yfinance as yf
from datetime import date

st.set_page_config(page_title="GalaxyPilot", layout="wide")

# 🔷 Branding
st.markdown("## 🚀 GalaxyPilot – La Opción Inteligente")
st.markdown("#### 📈🧠 Trading de Opciones | ETFs | Acciones")

# 🔹 Ticker Selector
ticker = st.selectbox("Selecciona un ticker:", ["SPY", "AAPL", "NVDA"])

# 🔹 Descargar datos
data = yf.download(ticker, period="1mo")

# 🔹 Manejo de errores al cargar datos
if data.empty:
    st.warning("⚠️ No se pudieron cargar los datos porque el DataFrame está vacío.")
    last_close = 666.00
elif "Close" not in data.columns:
    st.warning("⚠️ No se encontró la columna 'Close' en los datos descargados.")
    last_close = 666.00
else:
    last_close = round(data["Close"].iloc[-1], 2)

# 🔹 Mostrar gráfico solo si hay datos reales
if not data.empty and "Close" in data.columns:
    st.subheader(f"📉 Precio de cierre – ({ticker})")
    st.line_chart(data["Close"])
else:
    st.info("📭 Gráfico no disponible por falta de datos.")

# 🔹 Estrategia
st.markdown("## 📊 Estrategia Cardona Seleccionada")
estrategia = st.radio("Estrategia:", ["🟢 Bajo pista al alza", "CALL en canal", "PUT en consolidación"])
st.write(f"Estrategia seleccionada: **{estrategia}**")

# 🔹 Simulación básica con fallback en strike
strike = st.number_input("Strike Price", value=last_close)
vencimiento = st.date_input("Vencimiento", value=date.today())
prima = st.slider("Prima estimada ($)", 0.5, 10.0, 1.5)

st.markdown(f"🔥 Posible resultado al vencer: **{round(prima * 100, 2)} USD**")

# 🔹 Exportación manual
st.markdown("### 📋 Copia manualmente esta info para tu bitácora Notion:")
st.code(f"Ticker: {ticker} | Estrategia: {estrategia} | Strike: {strike} | Prima: {prima} | Vencimiento: {vencimiento}")
