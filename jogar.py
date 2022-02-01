#imports necessários pra jogar o jogo
### Aqui so precisa rodar esta pagina pois devido aos imports ela se comunica com as demais###
from random import choice
import time
from funcoes import jogo
from funcoes import sorteia_palavra
from funcoes import cria_jogador
import random
import os
import desenho
import funcoes


#Este while é pra tomada de decisão do usuário se que continuar jogando.
decisao = True
while decisao:
    funcoes.inicializacao()
    decisao = input("Deseja jogar novamente?").upper()
    
    while decisao!= "S" and decisao!= "N":
        decisao = input("Digite S ou N:").upper()
    if decisao == 'S':
        funcoes.inicializacao()
    else:
        print("Fim de Jogo")
         