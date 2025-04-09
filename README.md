# 🍸 Cocktail Ingredient Clustering & Recommender App

Este proyecto explora patrones en recetas de cócteles usando técnicas de análisis de datos y clustering no supervisado. Como parte final, se desarrolló una app interactiva en Streamlit para recomendar recetas según los ingredientes disponibles.

## 📌 Objetivo

- Analizar combinaciones de ingredientes en recetas de cócteles.
- Identificar "familias" de cócteles mediante clustering.
- Desarrollar una app que sugiera cócteles posibles con lo que tienes en casa.

## 📁 Estructura del repositorio

- `data/`: Dataset original descargado de Kaggle.
- `notebooks/`: Exploración de datos, visualizaciones y clustering.
- `outputs/`: Imágenes generadas (PCA, t-SNE, capturas de la app).
- `app/`: Código de la aplicación Streamlit.
- `README.md`: Documentación del proyecto.
- `requirements.txt`: Paquetes necesarios para ejecutar el entorno.

## ⚙️ Cómo ejecutar el proyecto

1. Clona el repositorio:
```bash
git clone https://github.com/blyatdemoro/cocktail-clustering-streamlit.git
cd cocktail-clustering-app
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la app:
```bash
streamlit run app/app.py
```

## 🧪 Técnicas utilizadas

- Análisis exploratorio (EDA) con pandas y seaborn
- Ingeniería de características (one-hot encoding de ingredientes)
- Clustering con KMeans
- Visualización 2D con PCA y t-SNE
- Interpretación temática de los clústeres
- Desarrollo de app interactiva con Streamlit

## 🧠 Resultados destacados

- Se identificaron 6 clústeres representando diferentes estilos de cócteles.
- Las visualizaciones muestran agrupaciones claras en el espacio de ingredientes.
- La app permite construir combinaciones progresivas de ingredientes y ver los cócteles compatibles.
- Se incluyen imágenes e instrucciones detalladas por cóctel.

## 📚 Dataset

Los datos provienen del dataset **Cocktails and Ingredients** publicado en Kaggle por [the_hedgehog](https://www.kaggle.com/datasets/thehedgehog/cocktails-hotal).  
Se utilizaron tres archivos: recetas, ingredientes e imágenes.

## 👤 Autor

Desarrollado por David Ruiz Sola como parte de su portfolio de análisis de datos.  
📫 Contacto: [LinkedIn](https://linkedin.com/in/tuusuario) | [GitHub](https://github.com/blyatdemoro)

---

Proyecto desarrollado con fines educativos para portfolio profesional.
