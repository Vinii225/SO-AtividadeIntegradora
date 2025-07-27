#
# INFO: SJF - Shortest Job First (Simulação)
#

from processos import processos

tempo=0
executados=[]

while len(executados) < len(processos):
    disponiveis = []


    for processo in processos:
        if processo["Chegada"] <= tempo and processo not in executados:
            disponiveis.append(processo)

    if len(disponiveis)==0:
        menor_chegada=999
        for processo in processos:
            if processo not in executados and processo["Chegada"] < menor_chegada:
                menor_chegada=processo["Chegada"]
        tempo=menor_chegada
        continue

    menor_duracao=999
    escolhido=None
    for processo in disponiveis:
        if processo["Duração"] < menor_duracao:
            menor_duracao=processo["Duração"]
            escolhido=processo
    
    executados.append(escolhido)

    inicio = tempo
    fim = tempo + escolhido["Duração"]
    espera = inicio - escolhido["Chegada"]
    
    print(f"{escolhido['ID']}: Chegada={escolhido['Chegada']}, Início={inicio}, Fim={fim}, Espera={espera}")
    tempo = fim