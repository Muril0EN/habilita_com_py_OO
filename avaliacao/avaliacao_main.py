import testes_fisicos

supino_homem = [0.6, 1.0, 1.2]
barra_homem = [0.5, 1.0, 1.15, 1.3]
agachamento_homem = [0.8, 1.2, 1.5]
terra_homem = [1.0, 1.5, 1.8]

supino_mulher = [0.4, 0.6, 0.8]
barra_mulher = [0.5, 1, 1.1]
agachamento_mulher = [0.6, 1, 1.3]
terra_mulher = [0.8, 1.2, 1.6]

peso_corporal = float(input("Peso corporal: "))

#experiencia (1/3)
print("Tempo ininterrupto de treinamento atual:")
print("1) até 2 meses; \n 2) entre 2 e 12 meses; \n 3) entre 1 e 3 anos; \n 4) + 3 anos.")
tempo_ininterrupto_treinamento_atual = int(input("-> "))

print("Experiência de treinamento: ")
print("1) até 2 meses \n2) entre 2 e 12; \n3)/ entre 1 e 3; \n4) + que 3 anos.")
experiencia_treinamento = int(input("-> "))

print("Tempo de destreinamento:")
print("1) até 8 meses; \n2)/ entre 4 e 8 meses; \n3) entre 1 e 4 meses; \n4) treinando atualmente.")
tempo_destreinamento = int(input("-> "))

print("Vamos descobrir seus níveis de mobilidade glenoumeral!")
tamanho_mao = float(input("Tamanho da mão: "))
glenoumeral_lado_direito = float(input("Mobilidade ombro direito: "))
glenoumeral_lado_esquerdo = float(input("Medida ombro esquerdo: "))

mobilidade_ombro_direito = testes_fisicos.mobilidade_ombro(glenoumeral_lado_direito, tamanho_mao)
mobilidade_ombro_esquerdo = testes_fisicos.mobilidade_ombro(glenoumeral_lado_esquerdo, tamanho_mao)
percentual_assimetria_ombro = testes_fisicos.calcula_assimetria(glenoumeral_lado_direito, glenoumeral_lado_esquerdo)
nivel_assimetria_ombro = testes_fisicos.classifica_assimetria(percentual_assimetria_ombro)
print("\n")
print("*** Mobilidade do quadril. ****")
quadril_lado_direito = float(input("Mobilidade quadril direito: "))
quadril_lado_esquerdo = float(input("Mobilidade quadril esquerdo: "))

mobilidade_quadril_direito = testes_fisicos.mobilidade_quadril(quadril_lado_direito)
mobilidade_quadril_esquerdo = testes_fisicos.mobilidade_quadril(quadril_lado_esquerdo)
percentual_assimetria_quadril = testes_fisicos.calcula_assimetria(quadril_lado_direito, quadril_lado_esquerdo)
nivel_assimetria_quadril = testes_fisicos.classifica_assimetria(percentual_assimetria_quadril)
print("\n")
print("***** Mobilidade do tornozelo. ****")
tornozelo_lado_direito = float(input("Mobilidade tornozelo direito: "))
tornozelo_lado_esquerdo = float(input("Mobilidade tornozelo esquerdo: "))

mobilidade_tornozelo_direito = testes_fisicos.mobilidade_tornozelo(tornozelo_lado_direito)
mobilidade_tornozelo_esquerdo = testes_fisicos.mobilidade_tornozelo(tornozelo_lado_esquerdo)
percentual_assimetria_tornozelo = testes_fisicos.calcula_assimetria(tornozelo_lado_direito, tornozelo_lado_esquerdo)
nivel_assimetria_tornozelo = testes_fisicos.classifica_assimetria(percentual_assimetria_tornozelo)
print("\n")
print("***** Resistência isométrica do core *********")
tempo_prancha_ventral = float(input("Tempo na prancha ventral: "))
tempo_extensao_coluna = float(input("Tempo na extensão da coluna: "))
tempo_prancha_lateral_direita = float(input("Tempo na prancha lateral (direita): "))
tempo_prancha_lateral_esquerda = float(input("Tempo na prancha lateral esquerda: "))

resistencia_prancha_ventral = testes_fisicos.resistencia_isometrica_core(tempo_prancha_ventral)
resistencia_extensao_coluna = testes_fisicos.resistencia_isometrica_core(tempo_extensao_coluna)
resistencia_prancha_lateral_direita = testes_fisicos.resistencia_isometrica_core(tempo_prancha_lateral_direita)
resistencia_prancha_lateral_esquerda = testes_fisicos.resistencia_isometrica_core(tempo_prancha_lateral_esquerda)

print("\n")
#nivel de força (2/3)
print("********** Status da força muscular ***********")
rm_agachamento = float(input("RM no agachamento: "))
rm_supino = float(input("RM no supino: "))
rm_terra = float(input("RM no terra: "))
rm_barra_fixa = float(input("RM na barra fixa: "))

#classifica niveis de força
forca_relativa_agachamento = testes_fisicos.calcula_forca_relativa(rm_agachamento, peso_corporal)
forca_relativa_supino = testes_fisicos.calcula_forca_relativa(rm_supino, peso_corporal)
forca_relativa_terra = testes_fisicos.calcula_forca_relativa(rm_terra, peso_corporal)
forca_relativa_barra = testes_fisicos.calcula_forca_relativa(rm_barra_fixa, peso_corporal)

#******************** teste força relativa ******************
status_agachamento = testes_fisicos.classifica_status_forca(forca_relativa_agachamento, agachamento_homem)
status_supino = testes_fisicos.classifica_status_forca(forca_relativa_supino, supino_homem)
status_terra = testes_fisicos.classifica_status_forca(forca_relativa_terra, terra_homem)
status_barra = testes_fisicos.classifica_status_forca(forca_relativa_barra, barra_homem)
#nivel de técnica (3/3) -> opcional (VAI ENTRAR NO FINAL)
#tecnica_agachamento = 2
#tecnica_supino = 2
#tecnica_terra = 4
#tecnica_barra = 1
#media_tecnica = (tecnica_agachamento + tecnica_supino + tecnica_terra + tecnica_barra) / 4
#print("Nível técnica: {}".format(media_tecnica)
print("\n\n")
#media_status_forca = (status_agachamento + status_supino + status_terra + status_barra) / 4
#status_geral_treinamento_forca = (tempo_ininterrupto_treinamento_atual, experiencia_treinamento, tempo_destreinamento, media_status_forca) / 4

#avaliacao_cardio = testes_fisicos.avalia_cardio()
