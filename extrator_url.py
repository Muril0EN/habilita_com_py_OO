import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    def valida_url(self):
        if not self.url:
            raise ValueError("A url está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError('A url não é válida.')
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor: indice_e_comercial]
        return valor
    def __len__(self): #tornar 'contável'
        return len(self.url)

    def __str__(self): #tornar 'imprimível'
        return self.url + '\n' "Parâramento: " + self.get_url_parametros() + '\n' + "URL base: " + self.get_url_base()

    def __eq__(self, other):#tornar 'comparável', ignorando o fato de estarem em endereços de memória diferente
        return self.url == other.url #iguais (valor) mas não idênticos(endereços de memória)

url = ('https://www.bytebank.com.br/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar')
extrator_url = ExtratorURL(url)

valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

#VER O ENDEREÇO DE MEMÓRIA
#id(objeto)
#x is True

#https://docs.google.com/spreadsheets/d/15MIKsiaxz2OgAT3Y7SSsvZROuCrT_NqkHqazVvNBE6I/edit?usp=sharing

sheet_id_andre = '15MIKsiaxz2OgAT3Y7SSsvZROuCrT_NqkHqazVvNBE6I'
sheet_pagina_name = 'controle_de_carga'
url_controle_de_carga = f'https://docs.google.com/spreadsheets/d/{sheet_id_andre}/gviz/tq?tqx=out:csv&sheet={sheet_pagina_name}'
#andre = pd.read_csv(url_controle_de_carga)