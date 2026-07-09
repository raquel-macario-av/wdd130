import math
import datetime
import os

diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_txt = os.path.join(diretorio_script, "volume_de_pneus.txt")

with open(caminho_txt, "at", encoding="utf-8") as arquivo_txt:
    data_e_hora_atuais = datetime.datetime.now()
    linha_cabecalho = f"{data_e_hora_atuais:%Y-%m-%d}\n"
    print(linha_cabecalho)
    arquivo_txt.write(linha_cabecalho)
   

    largura = float(input("Qual a largura do pnel?"))

    perfil = float(input("Qual perfil do pnel?"))

    diametro = float(input("Qual diametro do pnel?"))

    print (f"A largura do pnel é {largura} mm")
    print (f"O perfil do pnel é {perfil} %")
    print (f"O diametro do pnel é {diametro}")

    volume = (math.pi * (largura**2) * perfil * (largura * perfil + 2540 * diametro)) / (10**10)

    print(f"\nO volume aproximado é {volume:.2f} litros.")

    arquivo_txt.write(
    f"{data_e_hora_atuais:%Y-%m-%d}, {largura:.0f}, {perfil:.0f}, {diametro:.0f}, {volume:.2f}\n"
)