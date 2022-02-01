# O projeto foi feito de forma coletiva por: Beatriz Laquini, Dayana Prado, Harão Tavares, Yuri Rodrigues, com ajuda adicional de Vitor Hugo, Raian Porto.

from random import choice
import random
import os
import desenho


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

lista_palavras = ['programar', 'computador', 'tecnologia', 'internet', 'input', 'output', 'analise', 'mouse', 'hardware',
                  'desenvolvedor', 'debugar', 'armazenamento', 'dados', 'hacker', 'projeto','java', 'python', 'linguagem', 'deadline', 'codar']

# função que sorteia as palavras de acordo com as palavaras existentes dentro da lista acima.
def sorteia_palavra(lista_palavras):
    palavra = random.choice(lista_palavras)
    return palavra


# print(sorteia_palavra(lista_palavras))


# parte de escolha do jogo, para escolher o multiplayer e definir jogadores.
total_jogadores = int(input("Quantos jogadores: "))
lista_de_jogadores=[]


# parte que sorteia a palavra para cada jogador, e vai adicionando os jogadores dentro da lista.
for i in range(total_jogadores):
    nome = input("qual o nome do jogador?")
    palavra = sorteia_palavra(lista_palavras)
    lista_de_jogadores.append(cria_jogador(nome,palavra))


# função chamada na hora de jogar, nela faz o processo de contagem de acertos e erros no jogo e caso alguém erre ele muda simultaneamente para o próximo jogador.
def jogo(lista_de_jogadores,id):
    jogador_jogando = lista_de_jogadores[id]
    if jogador_jogando["erros"]<7 :
        print(f"jogando com {jogador_jogando['nome']}")
        mensagem = ["_"]*len(jogador_jogando["palavra_secreta"])
        print(jogador_jogando["situacao_palavra"])
        tentativa = input("Chute uma letra ")
        indice=0
    # while indice<=len(lista_de_jogadores):
        
        while tentativa in jogador_jogando["palavra_secreta"]:
            
            # for letra in jogador_jogando["palavra_secreta"]:
                
            for posicao, letra in enumerate(jogador_jogando["palavra_secreta"]):
                if tentativa == jogador_jogando["palavra_secreta"][posicao]:
                    # print(jogador_jogando["palavra_secreta"][posicao])
                    mensagem[posicao] = letra         
            # print(forca+chances_do_boneco[erros])
            print(mensagem)
            jogador_jogando["situacao_palavra"] = mensagem 
            
            jogador_jogando["erros"] +=1
            palavrastring = "" 
            for l in jogador_jogando["situacao_palavra"]:
                palavrastring +=l
            print(palavrastring)
            
            
            if palavrastring == jogador_jogando["palavra_secreta"]:
                print(f"Parabens vc ganhou {jogador_jogando['nome']}")
                return False
            else:
                tentativa = input("Chute outra letra ")
        jogador_jogando["erros"] +=1
        desenho.desenho_forca(jogador_jogando["erros"])
        return True
        
                
        
        

# def verfica_perdedores(lista_de_jogadores):
#     jogadores_jogando = 0
#     for jogador  in lista_de_jogadores:
#         if jogador["erros"]==7:
#             jogadores_jogando+=1

#         if jogadores_jogando==1:
#             return False
#         else:
#             return True
    


# parte que escolhe se quer continuar jogando.
id = 0
continua = True
while continua:
    if id ==len(lista_de_jogadores):
        id=0
    continua = jogo(lista_de_jogadores,id)
    # continua = verfica_perdedores(lista_de_jogadores)
    id +=1

    
    
    
  






