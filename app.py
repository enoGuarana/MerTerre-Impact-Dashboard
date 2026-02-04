import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="MerTerre Impact Dashboard", layout="wide")

st.title("🌊 MerTerre: Dashboard de Impacto")
st.markdown("### 📍 Mapeamento: Projeto Adopt'1 Spot")

# --- DADOS ---
# Simulando a estrutura de dados que você tem no seu projeto
data = {
    'Local': ["Calanque de Sormiou", "Plage du Prado", "Vieux Port", "Calanque de Morgiou", "L'Estaque"],
    'Lat': [43.2104, 43.2556, 43.2951, 43.2125, 43.3630],
    'Lon': [5.4194, 5.3730, 5.3744, 5.4428, 5.3190],
    'Status': ["Adotado ✅", "Precisa de Ação ⚠️", "Ação Agendada 📅", "Adotado ✅", "Precisa de Ação ⚠️"],
    'Lixo_kg': [120, 350, 410, 95, 210],
    'Tipo_Principal': ["Plástico", "Bitucas", "Plástico", "Vidro", "Metal"]
}
df = pd.DataFrame(data)

# --- MAPA INTERATIVO ---
m = folium.Map(location=[43.2965, 5.3698], zoom_start=11)

for i, row in df.iterrows():
    color = "green" if "Adotado" in row['Status'] else "red" if "Ação" in row['Status'] else "orange"
    folium.Marker(
        [row['Lat'], row['Lon']],
        popup=f"<b>{row['Local']}</b><br>Status: {row['Status']}<br>Lixo: {row['Lixo_kg']}kg",
        icon=folium.Icon(color=color, icon="info-sign")
    ).add_to(m)

# Exibir mapa no Streamlit
st_folium(m, width=1200, height=500)

# --- ANÁLISE GRÁFICA ---
st.markdown("### 📊 Análise de Resíduos: Zéro Déchet Sauvage")

fig = px.bar(df, x='Local', y='Lixo_kg', color='Tipo_Principal',
             title="Total de Lixo Coletado por Local e Tipo",
             text_auto=True,
             labels={'Lixo_kg': 'Kg de Lixo', 'Local': 'Localização'})

st.plotly_chart(fig, use_container_width=True)

st.info("💡 Este dashboard é um protótipo para auxiliar a ONG MerTerre na visualização de dados de preservação marinha.")
