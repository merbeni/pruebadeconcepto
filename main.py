import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')
import nltk
from textblob import TextBlob
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Referencias y variables
df = pd.read_csv('Reporte.csv')


# FUNCIONES

# Gráfico de barras de acuerdo a la cantidad de comentarios por cantidad de estrellas
def starsBarChart():
    barChart = df['Satisfaccion general'].value_counts().sort_index() \
        .plot(kind='bar',
              title='Cantidad de comentarios por estrellas',
              figsize=(10, 5))
    barChart.set_xlabel('Estrellas de comentarios')
    plt.show()


# Gráfico de torta de acuerdo a la cantidad de comentarios por cantidad de estrellas
def startsPieChart():
    pie = df['Satisfaccion general'].value_counts().sort_index() \
        .plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(8, 8))
    pie.set_xlabel('Estrellas de comentarios')
    plt.show()


# Convertir el grado de satisfacción en categorías
def categoryChart():
    df['categoria'] = df['Satisfaccion general'] \
        .apply(lambda x: 'bueno' if x >= 4 else 'neutro' if x == 3 else 'malo')
    pie = df['categoria'].value_counts().sort_index() \
        .plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(8, 8))
    pie.set_xlabel('categorias graficadas')
    plt.show()


# Initializer
starsBarChart()
startsPieChart()
categoryChart()

# Dividir los datos en conjuntos de entrenamiento y prueba
 function = X_train, X_test, y_train, y_test = train_test_split(data['polaridad'], data['categoria'], test_size=0.2, random_state=42)
# opinion1 = TextBlob(df['Texto de comentario'][1])
# print(opinion1)
# print(opinion1.sentiment)
