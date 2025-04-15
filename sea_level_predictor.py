import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Importar dados
    df = pd.read_csv("epa-sea-level.csv")

    # Criar scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Ajuste de linha para todos os dados
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_all = pd.Series(range(1880, 2051))
    y_pred_all = res_all.slope * x_pred_all + res_all.intercept
    ax.plot(x_pred_all, y_pred_all, 'r', label='Fit: All data')

    # Ajuste de linha apenas para dados a partir de 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    ax.plot(x_pred_recent, y_pred_recent, 'g', label='Fit: 2000 onwards')

    # Personalizações do gráfico
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()

    # Salvar imagem
    plt.tight_layout()
    plt.savefig('sea_level_plot.png')
    return fig