# O projeto foi feito de forma coletiva por: Beatriz Laquini, Dayana Prado, Harão Tavares, Yuri Rodrigues, com ajuda adicional de Vitor Hugo, Raian Porto.

from random import choice
import random
import os
import desenho
import time

print ('Bem Vindo ao Jogo da forca\n\n')

# Função feita para criar jogador,  pede para que o usuario crie seu próprio login.
os.system("cls")
def cria_jogador(nome,palavra):
    return{
        "nome":nome,
        "palavra_secreta":palavra,
        "acertos":len(palavra),
        "situacao_palavra":"",
        "erros":0,
        "ganhou":False,      
    }


# função que sorteia as palavras de acordo com as palavaras existentes dentro da lista acima.
def sorteia_palavra(lista_palavras):
    palavra = random.choice(lista_palavras)
    return palavra

# função chamada na hora de jogar, nela faz o processo de contagem de acertos e erros no jogo e caso alguém erre ele muda simultaneamente para o próximo jogador.
def jogo(lista_de_jogadores,id):
    jogador_jogando = lista_de_jogadores[id]
    if jogador_jogando["erros"]<7 and not jogador_jogando['ganhou'] :
        
        informacoes_jogador(jogador_jogando)
        
        if len(jogador_jogando["situacao_palavra"])==0:
            print(f'{["_"]*len(jogador_jogando["palavra_secreta"])}')
            mensagem = ["_"]*len(jogador_jogando["palavra_secreta"])
        else:
            print(jogador_jogando["situacao_palavra"])
            mensagem = jogador_jogando["situacao_palavra"]
        
        tentativa = input("Chute uma letra ").lower()
        while tentativa.isdigit() == True:
            print('\nSomente letras por favor!\n')
            tentativa = input("Chute uma letra \n").lower()                                          
        indice=0
    
        while tentativa in jogador_jogando["palavra_secreta"]:
            
                
            for posicao, letra in enumerate(jogador_jogando["palavra_secreta"]):
                if tentativa == jogador_jogando["palavra_secreta"][posicao]:
                    mensagem[posicao] = letra
                         
            print(f'{mensagem}')
            jogador_jogando["situacao_palavra"] = mensagem 
            
            palavrastring = "" 
            for l in jogador_jogando["situacao_palavra"]:
                palavrastring +=l
            
            if palavrastring == jogador_jogando["palavra_secreta"]:
                
                desenho.venceu(jogador_jogando)
                jogador_jogando["ganhou"]=True
                return False
            else:
                tentativa = input("Chute outra letra ").lower()
                while tentativa.isdigit() == True:
                    print('\nSomente letras por favor!\n')
                    tentativa = input("Chute uma letra \n").lower()    
        
        errou_chute(jogador_jogando)          
        
        
        
# Essa função verifica se ainda há jogadores jogando o jogo
def verifica_perdedores(lista_de_jogadores):
    jogando = 0
    # total_jogadores = len(lista_jogadores)
    for jogador in lista_de_jogadores:
        if  not jogador["erros"]>=7 and not jogador["ganhou"]:
            jogando =+1
    if jogando == 0:
        return False
    else: return True

# Printa mensagens na tela, e incrementa mais um aos erros do jogador
def errou_chute(jogador_jogando):
    jogador_jogando["erros"] +=1
    os.system("cls")
    print(f'{jogador_jogando["nome"].capitalize()} você errou a letra')
    desenho.desenho_forca(jogador_jogando["erros"])
    print(f'ERROS: {jogador_jogando["erros"]}')
    time.sleep(1)
    os.system("cls")

# Mostra as informações do jogador atual
def informacoes_jogador(jogador_jogando):
    print(f"Jogando com {jogador_jogando['nome'].capitalize()}")
    desenho.desenho_forca(jogador_jogando["erros"])
    print(f'ERROS: {jogador_jogando["erros"]}')
    
# Inicializa o jogo
def inicializacao():
    os.system("cls") # Limpa a tela inicial
    print ('Bem Vindo ao Jogo da forca\n\n')
    time.sleep(1)

    # Palavras a serem sorteadas
    lista_palavras = [
        'programar', 'computador', 'tecnologia', 'internet', 'input', 'output', 'analise', 'mouse', 'hardware',
        'desenvolvedor', 'debugar', 'armazenamento', 'dados', 'hacker', 'projeto','java', 'python', 'linguagem', 'deadline', 'codar',
    ]


    # Define quantos jogadores o jogo terá
    total_jogadores = input("Quantos jogadores: ")
    while total_jogadores.isdigit() == False:
        print('\nSomente numeros por favor!\n')
        total_jogadores = input("Quantos jogadores: \n")
    total_jogadores = int(total_jogadores)
    print('\n')


    # Cria os jogadores, define seus atributos e sorteia a palavra de cada um.
    lista_de_jogadores=[]
    for i in range(total_jogadores):
        nome = input(f"Qual o nome do jogador {i+1}? \n")
        palavra = sorteia_palavra(lista_palavras)
        lista_de_jogadores.append(cria_jogador(nome,palavra))
    os.system("cls")


    # Execução do multiplayer atravez do ID ele alterna entre os jogadores.O while verifica se continua o jogo(se há jogadores jogando)
    id = 0
    continua = True
    while continua:
        if id ==len(lista_de_jogadores):
            id=0
        continua = verifica_perdedores(lista_de_jogadores)
        if continua ==True:
            jogo(lista_de_jogadores,id)
        
        id +=1