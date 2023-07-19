def calcula_forca_relativa(rm, peso_corporal):
    forca_relativa = rm / peso_corporal
    return forca_relativa

def calcula_assimetria(lado_direito, lado_esquerdo):
    if (lado_esquerdo < lado_direito):
        percentual_assimetria = (((lado_direito - lado_esquerdo) / lado_esquerdo) * 100)
    else:
        percentual_assimetria = (((lado_esquerdo - lado_direito) / lado_direito) * 100)
    return percentual_assimetria

def classifica_assimetria (percentual_assimetria):
    if (percentual_assimetria > 10):
        assimetria = "acima do normal"
    else:
        assimetria = "normal"
    return assimetria

def mobilidade_ombro(distancia_entre_maos, tamanho_mao):
    referencia_ombro = tamanho_mao * 1.5
    if (distancia_entre_maos <= referencia_ombro):
        mobilidade = "normal"
    else:
        mobilidade = "reduzida"
    return mobilidade, referencia_ombro

def mobilidade_quadril(graus_flexão):
    referencia_quadril = 65
    if (graus_flexão > referencia_quadril):
        mobilidade = "normal"
    else:
        mobilidade = "reduzida"
    return mobilidade

def mobilidade_tornozelo(graus_dorsiflexao):
    referencia_tornozelo = 45
    if (graus_dorsiflexao >= referencia_tornozelo):
        mobilidade = "normal"
    else:
        mobilidade = "reduzida"
    return mobilidade

def resistencia_isometrica_core (tempo):
    if (tempo <= 20):
        score = "fraco"
    elif (tempo < 40):
        score = "regular"
    elif (tempo < 60):
        score = "bom"
    elif (tempo < 80):
        score = "muito bom"
    else:
        score = "excelente"
    return score

def classifica_status_forca(forca_relativa, lista_score):
    score_final = "nada"
    def converte_status_forca(score_parcial):
            score_final = "nada"
            if (score_parcial == 0):
                score_final = "Iniciante."
            elif (score_parcial == 1):
                score_final = "Antermediário."
            elif (score_parcial == 2):
                score_final = "Avançado."
            else:
                score_final = "Altamente avançado."
            return score_final

    index = 0
    score_parcial = 0
    for score in lista_score:
        if (forca_relativa >= score):
            score_parcial = index
        index = index + 1
    return converte_status_forca(score_parcial)

def avalia_cardio ():
    velocidade_estagio = 5
    estagio = 1
    lista_frequencia_cardiaca = []
    lista_velocidade = []
    indice = 0
    frequencia_cardiaca_estagio = 1

    while frequencia_cardiaca_estagio != 0:
        print("Digite 0 (zero) para encerrar o teste.")
        frequencia_cardiaca_estagio  = int(input("Frequência cardíaca do estágio {}: ".format(estagio)))
        estagio = estagio + 1
        lista_frequencia_cardiaca[indice] = frequencia_cardiaca_estagio
        lista_velocidade[indice] = velocidade_estagio + 1
        indice = indice + 1

    for indice in lista_velocidade:
        print(lista_velocidade)
    #return lista_velocidade, lista_frequencia_cardiaca

#PSE_do_estagio = int(input("PSE do estágio {}: ".format(estagio)))
#lista_PSE = []
#lista_PSE[item] = PSE_do_estagio
