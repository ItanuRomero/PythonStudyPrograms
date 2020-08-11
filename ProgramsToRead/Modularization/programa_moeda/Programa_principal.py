from programa_moeda import moeda
from programa_moeda import dados

valor = dados.validador_numerico('Digite um valor: R$ ')
moeda.resumo(valor, 15, 30)
