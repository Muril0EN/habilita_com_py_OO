class Protocolo:
    def __init__(self, objetivo, series, repeticoes, intervalo):
        self._objetivo = objetivo
        self._series = series
        self._repeticoes = repeticoes
        self._intervalo = intervalo
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

#criando exercícios
agachamento = Exercicio('Agachamento')
supino = Exercicio('Supino')
barra_fixa = Exercicio('Barra fixa')
terra = Exercicio('Levantamento terra')

#Criando lista de exercício para treino
lista_exercicios_A = [agachamento, supino, barra_fixa, terra]
treino_A = Sessao_de_treinamento('A', lista_exercicios_A)

print(f'Treino {treino_A.nome}')
for exercicio in treino_A:
    print(exercicio)
















