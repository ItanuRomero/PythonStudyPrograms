"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import urllib.request
try:
    urllib.request.urlopen("http://pudim.com.br/")
except:
    print('The website is offline.')
else:
    print('The website is online.')