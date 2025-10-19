import streamlit as st
import src.config as config
config.init_config()

from src.auth import init_app_state, login_view, menu, validate_login
from src.io_files import get_records_df
from src.ui_components import data_filters,player_block_dux
from src.util import grafico_zonas_lesionadas, grafico_tipo_mecanismo, grafico_evolucion_lesiones, grafico_tratamientos, grafico_dias_baja, grafico_recidivas

init_app_state()
validate_login()

# Authentication gate
if not st.session_state["auth"]["is_logged_in"]:
    login_view()
    st.stop()

st.header("Análisis :red[Individual]", divider=True)

menu()

jugadora_seleccionada, posicion, records = data_filters(modo=2)

st.divider()

player_block_dux(jugadora_seleccionada)

#st.dataframe(records)

col1, col2 = st.columns([1,1])
with col1:
    fig = grafico_evolucion_lesiones(records)
    if fig: st.plotly_chart(fig)

    fig = grafico_tipo_mecanismo(records)
    if fig: st.plotly_chart(fig)

    fig = grafico_dias_baja(records)
    if fig: st.plotly_chart(fig)

with col2:
    fig = grafico_zonas_lesionadas(records)
    if fig: st.plotly_chart(fig)

    fig = grafico_tratamientos(records)
    if fig: st.plotly_chart(fig)

    fig = grafico_recidivas(records)
    if fig: st.plotly_chart(fig)