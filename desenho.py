import os
import time

def desenho_forca(index):
        forca = """
         ____
        |
        |         
        |        
       _|_       
        """
        vazio = """ 


        """
        morreu ="""
        ################################################
         ____
        |   O      
        |  /|\\
        |  / \     
       _|_ 
       ################### Morreu #####################
        """
        cabeca ="""
         ____
        |    O      
        |
        |        
       _|_ 
        """
        tronco = """
         ____
        |    O     
        |    |
        |        
       _|_   
        """
        braco_esquerdo = """
         ____
        |   O      
        |  /|
        |       
       _|_                      
        """
        braco_direito = """
         ___
        |   O      
        |  /|\\
        |       
       _|_                  
        """
        perna_esquerda = """
         ___
        |   O      
        |  /|\\
        |  /    
       _|_ 
        """
        perna_direita = """
         ___
        |   O      
        |  /|\\
        |  / \     
       _|_ 
        """
        chances_boneco = [forca , cabeca,tronco, braco_esquerdo,braco_direito,perna_esquerda,perna_direita,morreu]
        # [ morreu, perna_direita, perna_esquerda, braco_direito, braco_esquerdo, tronco, cabeca, vazio]

        print(chances_boneco[index])

## Mostra a mensagem de vencedor
def venceu(jogador_jogando):
        os.system("cls")
        venceu =f"""
            ############# PARÁBENS {jogador_jogando["nome"].upper()} #############
        ################### VOCÊ ACERTOU A PALAVRA ############################# 

          \O/      
           |
          / \     
        
        """
        print(venceu)
        time.sleep(5)
        # os.system("cls")