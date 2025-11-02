import pandas as pd
import matplotlib.pyplot as plt
from upsetplot import UpSet

def generar_grafico_upset():
    df = pd.read_csv('DataUpsetPEC2.csv', sep=';')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.dropna(axis=1, how='all')

    # 2. Se ignora la columna de fecha
    if 'Fecha' in df.columns:
        df = df.drop('Fecha', axis=1)

    # 3. Convierto a Dummies
    df_dummies = pd.get_dummies(df)

    # 4. Agrupo combinaciones
    upset_data = df_dummies.groupby(list(df_dummies.columns)).size()

    # 5. Gráfico
    fig = plt.figure(figsize=(10, 6))
    upset = UpSet(
        upset_data,
        sort_by='cardinality',
        min_subset_size=1,
        show_counts=True
    )
    upset.plot(fig=fig)
    plt.title("Gráfico UpSet: Precio y Generación Renovable")
    plt.tight_layout()
    plt.savefig("grafico_upset.png", dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    generar_grafico_upset()