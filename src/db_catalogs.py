import pandas as pd
from src.db_connection import get_connection
import streamlit as st

@st.cache_data(ttl=3600)  # cachea por 1 hora (ajústalo según tu frecuencia de actualización)
def load_catalog_list_db(table_name, as_df=False):
    """
    Carga un catálogo desde la base de datos y lo cachea.
    - table_name: nombre de la tabla a leer.
    - as_df: True para devolver DataFrame, False para lista de dicts.
    """
    conn = get_connection()
    if not conn:
        st.error("⚠️ No se pudo establecer conexión con la base de datos.")
        return pd.DataFrame() if as_df else []

    try:
        query = f"SELECT * FROM {table_name} ORDER BY id;"
        df = pd.read_sql(query, conn)
        if as_df:
            return df
        else:
            return df.to_dict(orient="records")
    except Exception as e:
        st.error(f"⚠️ Error al cargar datos de {table_name}: {e}")
        return pd.DataFrame() if as_df else []
    finally:
        conn.close()
