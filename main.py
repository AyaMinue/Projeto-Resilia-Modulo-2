from utilidades import corpo, palavras
from random import randint

def getPalavras(pLista):
    pIndex = randint(0, len(pLista) - 1)
    return pLista[pIndex]


def tela(corpo, letraErrada, letraCorreta, palavraSecreta):
    print(corpo[len(letraErrada)])
    print()

    print('Letras erradas ->  ', end='')

    for letra in letraErrada:
        print(letra, end=' ')
    print()

    lacuna = '_ ' * len(palavraSecreta)

    # substituindo os espaços em branco pelas letras corretas.
    for cont in range(len(palavraSecreta)):
        if palavraSecreta[cont] in letraCorreta:
            lacuna = lacuna[:cont] + palavraSecreta[cont] + lacuna[cont + 1:]

    # mostrar a palavra secreta com espaços entre cada letra
    for letra in lacuna:
        print(letra, end=' ')
    print()


def get_chute(letraChute):
    """
    :param letraChute:
    :return: Letra escolhida pelo usuário
    """

    while True:
        chute = str(input('Chute: ')).lower().strip()

        if len(chute) != 1:
            print(f'Por favor, digite apenas uma letra!')
        elif chute in letraChute:
            print(f'Ahh, essa você já chutou! Tente outra...')
        elif chute not in 'abcdefghijklmnopqrstuvwxyz':
            print(f'Por favor, digite uma letra!')
        else:
            return chute


def jogarNovamente():
    return input('Jogar mais uma? Tecle S para sim ou [N] para não: ').lower().startswith('s')
    print('')


print('-- C A R R A S C O --')
letraErrada = ''
letraCorreta = ''
palavraSecreta = getPalavras(palavras)
jogoFim = False

while True:
    tela(corpo, letraErrada, letraCorreta, palavraSecreta)

    chute = get_chute(letraErrada + letraCorreta)

    if chute in palavraSecreta:
        letraCorreta = letraCorreta + chute
        pCompleta = True

        for i in range(len(palavraSecreta)):
            if palavraSecreta[i] not in letraCorreta:
                pCompleta = False
                break

        if pCompleta:
            print(f'Legal, a palavra secreta é: {palavraSecreta}')
            jogoFim = True

    else:
        letraErrada = letraErrada + chute

        if len(letraErrada) == len(corpo) - 1:
            tela(corpo, letraErrada, letraCorreta, palavraSecreta)

            print(f'\nQue pena, suas chances acabaram...\n\n'
                  f'Total de chutes errados: {len(letraErrada)}\n\n'
                  f'Total de chutes corretos: {len(letraCorreta)}\n\n'
                  f'Ahh, a palavra secreta era: {palavraSecreta}\n\n')
            jogoFim = True

    # verificar se o jogador que jogar novamente...
    if jogoFim:
        if jogarNovamente():
            letraErrada = ''
            letraCorreta = ''
            jogoFim = False
            palavraSecreta = getPalavras(palavras)
        else:
            break