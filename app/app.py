import pandas as pd
import streamlit as st
import folium 
from streamlit_folium import st_folium

## configuração da página 
st.set_page_config(
    page_title="Safe to Eat",
    layout="wide"
)

## título 
st.title("Safe to Eat")
st.subheader("Mapa de restaurantes seguros para celíacos")

## carregar dados 
df = pd.read_csv("data/raw/restaurantes_curitiba_rmc.csv")

## limpar espaços extras
df.columns = df.columns.str.strip()

## preencher valores vazios
df["nivel_seguranca"] = df["nivel_seguranca"].fillna("Desconhecido")
df["observacoes"] = df["observacoes"].fillna("Sem informações")

## criar mapa
mapa = folium.Map(
    location=[-25.23, -49.27],
    zoom_start=11
)

## função para cor dos marcadores
def cor_marcador(seguro):
    if seguro == "Sim":
        return "green"
    else:
        return "red"
    
## adicionar pontos no mapa
for _, row in df.iterrows():

    popup = f"""
    <b>{row['nome']}</b><br>
    Tipo: {row['tipo']}<br>
    Bairro: {row['bairro']}<br>
    Cidade: {row['cidade']}<br>
    Seguro para celíacos: {row['seguro_celiaco']}<br>
    Nível de segurança: {row['nivel_seguranca']}<br>
    Observações: {row['observacoes']}"""

    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=popup,
        icon=folium.Icon(
color=cor_marcador(row["seguro_celiaco"])
        )
    ).add_to(mapa)

## mostrar mapa no streamlit 
st_folium(mapa, width=1400, height=700)


