
def desenho_forca(index):
        forca = """
        ______
                | 
                |
                _
        """
        vazio = """ 


        """
        morreu ="""
        morreu
        """
        cabeca ="""
                O
        """
        tronco = """
                O
                |
        """
        braco_esquerdo = """
                O
                /|
        """
        braco_direito = """
                O
                /|\\
        """
        perna_esquerda = """
                O
                /|\\
                /
        """
        perna_direita = """
                O
                /|\\
                / \\
        """
        chances_boneco = [vazio , cabeca,tronco, braco_esquerdo,braco_direito,perna_esquerda,perna_direita,morreu]
        # [ morreu, perna_direita, perna_esquerda, braco_direito, braco_esquerdo, tronco, cabeca, vazio]

        print(chances_boneco[index])