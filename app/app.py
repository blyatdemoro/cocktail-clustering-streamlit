# app/app.py

import streamlit as st
import pandas as pd
import os
from collections import Counter

# Cargar datos preparados
@st.cache_data
def load_data():
    df = pd.read_csv("C:/Users/druiz/Documents/Proyectos data analyst/Proyecto Cocktails/data/merged_cocktails.csv", converters={"Ingredient": eval})
    return df

df = load_data()


# ---------- Inicializar session state ----------
if "ingredientes_seleccionados" not in st.session_state:
    st.session_state.ingredientes_seleccionados = []

# ---------- Paso 1: Ingrediente inicial ----------
st.title("🍹 Cocktail Selector")
st.markdown("### Paso 1: Elige un Ingrediente para comenzar")

ingredientes_planos = [ing for lista in df["Ingredient"] for ing in lista]
top_ingredientes = [i[0] for i in Counter(ingredientes_planos).most_common(30)]

with st.form("form_inicial"):
    ingrediente_inicial = st.selectbox("Ingredientes más usados:", top_ingredientes, key="selector_inicial")
    confirmacion = st.form_submit_button("Seleccionar ingrediente inicial")

if confirmacion:
    st.session_state.ingredientes_seleccionados = [ingrediente_inicial]  # Reinicia con solo este
    st.rerun()


# ---------- Ingredientes seleccionados ----------
st.markdown("---")
st.subheader("🥂 Ingredientes seleccionados:")
st.write(st.session_state.ingredientes_seleccionados)

# ---------- Paso 2: Sugerir ingredientes compatibles ----------
st.markdown("### Paso 2: Elige otro ingrediente compatible")

df_filtrado = df[df['Ingredient'].apply(lambda x: all(ing in x for ing in st.session_state.ingredientes_seleccionados))]

ingredientes_posibles = [
    ing for lista in df_filtrado["Ingredient"]
    for ing in lista if ing not in st.session_state.ingredientes_seleccionados
]
ingredientes_compatibles = [i[0] for i in Counter(ingredientes_posibles).most_common(10)]

if ingredientes_compatibles:
    with st.form("form_nuevo_ing"):
        nuevo_ing = st.selectbox("Ingredientes compatibles:", ingredientes_compatibles, key="selector_compatibles")
        submit = st.form_submit_button("Añadir ingrediente")
    
    if submit:
        if nuevo_ing and nuevo_ing not in st.session_state.ingredientes_seleccionados:
            st.session_state.ingredientes_seleccionados.append(nuevo_ing)
            st.rerun()

# ---------- Paso Final: Buscar cócteles compatibles ----------
st.markdown("### 🧾 Cócteles que puedes hacer con esta combinación")

df_resultado = df[df['Ingredient'].apply(lambda x: all(ing in x for ing in st.session_state.ingredientes_seleccionados))]



if not df_resultado.empty:
    for _, row in df_resultado.iterrows():
       # st.write(df_resultado.columns.tolist())
        st.markdown(f"#### 🍸 {row['strDrink']}")

         # Mostrar imagen si existe
        img_path = os.path.normpath(os.path.join("..", "data", row["image_path"]))  # ajusta si se llama diferente
        if os.path.exists(img_path):
            st.image(img_path, width=200)
    
        st.markdown(f"**Instrucciones:** {row['strInstructions']}")
        st.markdown(f"**Ingredientes:** {', '.join(row['Ingredient'])}")
        st.markdown("---")
else:
    st.info("No hay coincidencias aún. Añade más ingredientes o reinicia la búsqueda.")

# ---------- Reiniciar ----------
if st.button("🔁 Reiniciar selección"):
    st.session_state.ingredientes_seleccionados = []
    st.rerun()