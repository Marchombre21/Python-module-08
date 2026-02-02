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
import importlib.metadata


def import_function() -> list:
    libraries: str = ["pandas", "matplotlib.pyplot", "numpy"]
    purposes: dict = {"pandas": "Data manipulation ready",
                      "matplotlib.pyplot": "Visualization ready",
                      "numpy": "Generation data ready"}
    modules: list = []
    for library in libraries:
        try:
            modules.append(imp.import_module(library))
            lib: str = library.split(".")[0]
            version: str = importlib.metadata.version(lib)
            print(f"[OK] {library} ({version}) - {purposes.get(library)}")
        except ImportError:
            print(f"\nYou don't have download {library} library. To download"
                  " all requested dependencies via pip type the command (make"
                  " it in a virtual environment):")
            print("python3 -m pip install -r requirements.txt")
            print("If you prefer doing that via poetry you have to install it"
                  " with:")
            print("python3 -m pip install pipx\npython3 -m pipx ensurepath")
            print("It will install pipx which is necessary for poetry"
                  " installation")
            print("Then you can type 'pipx install poetry'. After that all"
                  " you have to do is:")
            print("poetry install --no-root (install all dependencies)")
            print("poetry run python3 loading.py")
            raise ImportError("Missing at least one dependency")
    return modules


def main():
    try:
        print("\nLOADING STATUS: Loading programs...")
        print("\nChecking dependencies:")
        pd, plt, np = import_function()
        raw_data = np.random.randn(100, 2)
        df = pd.DataFrame(raw_data, columns=['Stabilité du Code',
                                             'Flux de Données'])
        df['Moyenne Lissée'] =\
            df['Stabilité du Code'].rolling(window=10).mean()
        print("\nAnalyzing Matrix data...")
        print(f"Analyse de {len(df)} points de données effectuée.")
        plt.figure(figsize=(10, 6))
        plt.plot(df['Stabilité du Code'], label='Signal Brut', alpha=0.3)
        plt.plot(df['Moyenne Lissée'], label='Tendance (Analyse)', color='red')
        plt.title("Analyse de la Matrice")
        plt.xlabel("Temps (itérations)")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.savefig('matrix_analysis.png')
        print("\nAnalysis complete")
        print("Results saved to: matrix_analysis.png")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
