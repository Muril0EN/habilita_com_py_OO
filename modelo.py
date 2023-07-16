class Protocolo:
    def __init__(self, nivel, objetivo, zona_de_reps, series_por_exercicio, intervalo, velocidade_do_movimento, frequencia_semanal):
        self._nivel = nivel
        self._objetivo = objetivo
        self._zona_de_reps = zona_de_reps
        self._series_por_exercicio = series_por_exercicio
        self._intervalo = intervalo
        self._velocidade_do_movimento = velocidade_do_movimento
        self._frequencia_semanal = frequencia_semanal
    def __str__(self):
        return f'Nível: {self._nivel}\nObjetivo: {self._objetivo}\nZona de repetições: {self._zona_de_reps}\n' \
               f'Séries por exercício: {self._series_por_exercicio}\nIntervalo: {self._intervalo}\n' \
               f'Velocidade do movimento: {self._velocidade_do_movimento}\nFrequência semanal: {self._frequencia_semanal}'
class Sessao_de_treinamento:
    def __init__(self, nome, exercicios):
        self.nome = nome
        self._exercicios = exercicios
    def __getitem__(self, item):
        return self._exercicios[item]
    @property
    def lista(self):
        return self._exercicios
    def __len__(self):
        return len(self._exercicios)
class Exercicio:
    def __init__(self, nome):
        self._nome = nome
    def __str__(self):
        return f'{self._nome}'

#Área de testes
#criando exercícios
agachamento = Exercicio('Agachamento')
supino = Exercicio('Supino')
barra_fixa = Exercicio('Barra fixa')
terra = Exercicio('Levantamento terra')

#Criando lista de exercício para treino
lista_exercicios_A = [agachamento, supino, barra_fixa, terra]
treino_A = Sessao_de_treinamento('A', lista_exercicios_A)

iniciante_forca = Protocolo('iniciante', 'hipertrofia', '12 a 15', '3', '1 minuto', 'moderada', '3x na semana')

print(iniciante_forca)

#dinâmica de uma sessão:
print(f'Treino {treino_A.nome}')
for exercicio in treino_A:
    print(exercicio)
















