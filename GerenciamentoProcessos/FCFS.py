#
# INFO: FCFS - First Come First Served ou FIFO (Simulação)
#

from processos import processos 

tempo=0

for processo in processos:
    if tempo<processo["Chegada"]:
        tempo=processo["Chegada"]

    inicio = tempo
    fim = tempo + processo["Duração"]
    espera = inicio - processo["Chegada"]

    print(f"{processo['ID']}: Chegada={processo['Chegada']}, Início={inicio}, Fim={fim}, Espera={espera}")
    tempo = fim