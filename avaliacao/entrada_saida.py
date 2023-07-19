import testes_fisicos
import avaliacao_main

print("******************************")
print("***** RELATÓRIO FINAL ********")
print("******************************\n")
print("Mobilidade glenoumeral")
print("Direito: {} ({})  Esquerdo: {} ({})".format(avaliacao_main.glenoumeral_lado_direito,
                                                   avaliacao_main.mobilidade_ombro_direito,
                                                   avaliacao_main.glenoumeral_lado_esquerdo,
                                                   avaliacao_main.mobilidade_ombro_esquerdo))
print("Percentual de assimetria: {:.2f}% ({})".format(avaliacao_main.percentual_assimetria_ombro,
                                                      avaliacao_main.nivel_assimetria_ombro))
print("Referência: distância entre as mãos > {} = mobilidade reduzida".format(avaliacao_main.tamanho_mao * 1.5))
print("\n")
print("Mobilidade quadril")
print("Direito: {} ({})  Esquerdo: {} ({})".format(avaliacao_main.quadril_lado_direito,
                                                   avaliacao_main.mobilidade_quadril_direito,
                                                   avaliacao_main.quadril_lado_esquerdo,
                                                   avaliacao_main.mobilidade_quadril_esquerdo))
print("Percentual de assimetria: {:.2f}% ({})".format(avaliacao_main.percentual_assimetria_quadril,
                                                      avaliacao_main.nivel_assimetria_quadril))
print("Referência: amplitude < 65 graus = mobilidade reduzida.")
print("\n")
print("Mobilidade tornozelo")
print("Direito: {} ({})  Esquerdo: {} ({})".format(avaliacao_main.tornozelo_lado_direito,
                                                   avaliacao_main.mobilidade_tornozelo_direito,
                                                   avaliacao_main.tornozelo_lado_esquerdo,
                                                   avaliacao_main.mobilidade_tornozelo_esquerdo))
print("Percentual de assimetria: {:.2f}% ({})".format(avaliacao_main.percentual_assimetria_tornozelo,
                                                      avaliacao_main.nivel_assimetria_tornozelo))
print("Referência: amplitude < 45 graus = mobilidade reduzida.")
print("\n")
print("Core")
print("Prancha ventral: {}            | score: {}".format(avaliacao_main.tempo_prancha_ventral,
                                                          avaliacao_main.resistencia_prancha_ventral))
print("Extensão da coluna: {}         | score: {}".format(avaliacao_main.tempo_extensao_coluna,
                                                          avaliacao_main.resistencia_extensao_coluna))
print("Prancha lateral (direito): {}  | score: {}".format(avaliacao_main.tempo_prancha_lateral_direita,
                                                          avaliacao_main.resistencia_prancha_lateral_direita))
print("Prancha lateral (esquerdo): {} | score: {}".format(avaliacao_main.tempo_prancha_lateral_esquerda,
                                                          avaliacao_main.resistencia_prancha_lateral_esquerda))
print("Referência: tempo < 20s = fraco | tempo < 40s = regular | tempo < 60 = bom | \ntempo < 80 = muito bom | tempo > 80s = excelente.")
print("\n")
print("Força muscular")
#print("Status de força geral: {:.2f}".format(status_geral_treinamento_forca))
print("\nStatus por padrão de movimento.")
print("Agachamento")
print("RM: {}  Força relativa: {:.2f}  Status: {}".format(avaliacao_main.rm_agachamento,
                                                          avaliacao_main.forca_relativa_agachamento,
                                                          avaliacao_main.status_agachamento))
print("Supino")
print("RM: {}  Força relativa: {:.2f}  Status: {}".format(avaliacao_main.rm_supino,
                                                          avaliacao_main.forca_relativa_supino,
                                                          avaliacao_main.status_supino))
print("Levantamento terra")
print("RM: {}  Força relativa: {:.2f}  Status: {}".format(avaliacao_main.rm_terra,
                                                          avaliacao_main.forca_relativa_terra,
                                                          avaliacao_main.status_terra))
print("Barra fixa")
print("RM: {}  Força relativa: {:.2f}  Status: {}".format(avaliacao_main.rm_barra_fixa,
                                                          avaliacao_main.forca_relativa_barra,
                                                          avaliacao_main.status_barra))
