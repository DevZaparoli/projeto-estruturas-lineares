import os

os.system("cls")

votos = []
# Lista de candidatos em letras minúsculas para facilitar a comparação
candidatos_validos = [
    "lionel messi",
    "alexandre de moraes",
    "vinicius rafacho",
]

while True:
    print("Candidatos : Lionel Messi, Alexandre de Moraes, Vinicius Rafacho ")
    comeco_voto = (
        input(
            "Informe o nome do aluno(a) que voce escolheu\nou\nDigite [FIM] para sair e votar nulo: "
        )
        .strip()
        .lower()
    )  # Converte tudo para minúsculo

    if comeco_voto == "fim":
        os.system("cls")
        print("Programa encerrado")
        break

    # Verifica se o voto está na lista de candidatos
    if comeco_voto in candidatos_validos:
        # Armazena o voto com as letras corretas de acordo com a sua lista
        votos.append(comeco_voto.title().replace(" De ", " de "))
        os.system("cls")
        print("Voto Confirmado ")
        print("\n")

    else:
        os.system("cls")
        print("Candidato nao encontrado, tentar novamente!!!\n")

# Contação de votos (convertendo a lista para os nomes corretos)
Lionel_Messi = votos.count("Lionel Messi")
Alexandre_de_Moraes = votos.count("Alexandre de Moraes")
Vinicius_Rafacho = votos.count("Vinicius Rafacho")

maxvotos = max(Lionel_Messi, Alexandre_de_Moraes, Vinicius_Rafacho)

vencedores = []

if Lionel_Messi == maxvotos:
    vencedores.append("Lionel Messi")
if Alexandre_de_Moraes == maxvotos:
    vencedores.append("Alexandre de Moraes")
if Vinicius_Rafacho == maxvotos:
    vencedores.append("Vinicius Rafacho")

if len(vencedores) == 1:
    print(f"Vencedor: {vencedores[0]}")
else:
    print("\nEmpate entre:", ", ".join(vencedores))

print(
    f"\nResultado do embate Lionel= {Lionel_Messi} , Alexandre= {Alexandre_de_Moraes} e Vinicius= {Vinicius_Rafacho}\n"
)