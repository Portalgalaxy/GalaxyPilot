
import streamlit as st
import pandas as pd

st.set_page_config(page_title="GalaxyPilot – La Opción Inteligente")

st.title("🚀 GalaxyPilot – La Opción Inteligente")
st.subheader("📊 Simulación de datos sin conexión a Yahoo Finance")

# Cargar datos simulados
df = pd.DataFrame({
    "Date": ['2025-06-28', '2025-06-29', '2025-06-30', '2025-07-01', '2025-07-02', '2025-07-03', '2025-07-04', '2025-07-05', '2025-07-06', '2025-07-07', '2025-07-08', '2025-07-09', '2025-07-10', '2025-07-11', '2025-07-12', '2025-07-13', '2025-07-14', '2025-07-15', '2025-07-16', '2025-07-17', '2025-07-18', '2025-07-19', '2025-07-20', '2025-07-21', '2025-07-22', '2025-07-23', '2025-07-24', '2025-07-25', '2025-07-26', '2025-07-27'],
    "Close": [500, 511, 522, 503, 514, 525, 506, 517, 528, 509, 520, 531, 512, 523, 534, 515, 526, 537, 518, 529, 540, 521, 532, 543, 524, 535, 546, 527, 538, 549]
})

# Mostrar DataFrame
st.write("### Datos Simulados – SPY", df)

# Graficar
st.line_chart(df.set_index("Date"))
