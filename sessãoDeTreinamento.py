print("Nível de treinamento?")
print("Iniciante -> 1\nIntermediário -> 2\nAvançado -> 3\nAltamente avançado -> 4\n")
nivel_de_treinamento = int(input("Resposta: "))

def define_qtd_series (nivel_de_treinamento):
    if nivel_de_treinamento == 1:
       series_programadas = 10
    elif nivel_de_treinamento == 2:
        series_programadas = 15
    else:
        series_programadas = 20
    return series_programadas

series_executadas = 1
repeticoes_final = 0
tonelagem_final = 0

while(series_executadas <= define_qtd_series(nivel_de_treinamento)):

    print("\nSérie {} de {}.".format(series_executadas, define_qtd_series(nivel_de_treinamento)))
    peso = float(input("Peso: "))
    repeticoes = int(input("Repetições: "))
    tonelagem = peso * repeticoes

    repeticoes_final += repeticoes
    tonelagem_final += tonelagem

    print(" ** Resumo da série ** ")
    print("Repetições: {}".format(repeticoes))
    print("Tonelagem da série: {}".format(tonelagem))
    print("\n")
    print(" ** Resumo do treino ** ")
    print("Repetições final: {}".format(repeticoes_final))
    print("Tonelagem final: {}".format(tonelagem_final))

    series_executadas += 1

define_qtd_series(nivel_de_treinamento)
pse = int(input("PSE: "))

#if(__name__ == "__main__"):
#revisar esse comando...