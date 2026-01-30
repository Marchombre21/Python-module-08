# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    loading.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/30 16:38:38 by bfitte            #+#    #+#             #
#    Updated: 2026/01/30 17:28:50 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

import importlib as imp

try:
    pd = imp.import_module("pandas")
except ImportError:
    print("\nYou don't have download pandas library. To download all requested"
          " dependancies type the command (make it in a virtual environment):")
    print("python3 -m pip install -r requirements.txt")
try:
    plt = imp.import_module("matplotlib.pyplot")
except ImportError as e:
    print(e)
    print("\nYou don't have download matplotlib library. To download all"
          " requested dependancies type the command (make it in a virtual"
          " environment): ")
    print("python3 -m pip install -r requirements.txt")
try:
    np = imp.import_module("numpy")
except ImportError:
    print("\nYou don't have download numpy library. To download all requested"
          " dependancies type the command (make it in a virtual environment):")
    print("python3 -m pip install -r requirements.txt")


def run_analysis():
    try:
        raw_data = np.random.randn(100, 2)
        df = pd.DataFrame(raw_data, columns=['Stabilité du Code',
                                             'Flux de Données'])
        df['Moyenne Lissée'] =\
            df['Stabilité du Code'].rolling(window=10).mean()
        print(f"Analyse de {len(df)} points de données effectuée.")
        plt.figure(figsize=(10, 6))
        plt.plot(df['Stabilité du Code'], label='Signal Brut', alpha=0.3)
        plt.plot(df['Moyenne Lissée'], label='Tendance (Analyse)', color='red')
        plt.title("Analyse de la Matrice")
        plt.xlabel("Temps (itérations)")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.savefig('matrix_analysis.png')
        print("Graphique sauvegardé sous : matrix_analysis.png")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    run_analysis()
