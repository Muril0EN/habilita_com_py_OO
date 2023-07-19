import time
import sys

lista_de_exercicios = [ 'agachamento', 'supino', 'mesa flexora', 'barra_fixa']
series_protocolo = 3

def calcula_tonelagem_por_serie():
    peso = float(input('Peso: '))
    repeticoes = int(input("repetições: "))
    tonelagem = repeticoes * peso
    print('Intervalo')
    return tonelagem

def contagem_regressiva(intervalo_em_segundos):
    while intervalo_em_segundos:
        mins, secs = divmod(intervalo_em_segundos, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        sys.stdout.write('\r' + timer)
        sys.stdout.flush()
        time.sleep(1)
        intervalo_em_segundos -= 1

    print('\nFinal do intervalo!')
def loop_series(series_por_exercicio_protocolo):
    series_feitas = 1
    while series_feitas <= series_protocolo:
        print(f'Série: {series_feitas}')
        calcula_tonelagem_por_serie()
        series_feitas += 1
        contagem_regressiva(int(5))
def sessao_de_treino(lista_de_exercicios, series_protocolo):
    indice = 0
    serie = 1
    for i in lista_de_exercicios:
        item = lista_de_exercicios[indice]
        print(f'Exercicio: {item}')
        loop_series(series_protocolo)
        indice += 1
    return

sessao_de_treino(lista_de_exercicios, series_protocolo)