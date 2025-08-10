#
# INFO: Simulação de dois processos concorrentes (produtor, consumidor) sem sincronização
#

import threading
import time
import random

buffer =[]
tamanho_max=5

def produtor():
    for i in range(10):
        time.sleep(random.uniform(0.1, 0.4))
        if len(buffer) < tamanho_max:
            item=random.randint
            buffer.append(item)
            print(f"\n[PRODUTOR] produziu {item} | BUFFER: {buffer}")


def consumidor():
    for i in range(10):
        time.sleep(random.uniform(0.1, 0.4))
        if buffer:
            item=buffer.pop(0)
            print(f"\n[CONSUMIDOR] consumiu {item} | BUFFER: {buffer}")


t1=threading.Thread(target=produtor)
t2=threading.Thread(target=consumidor)

t1.start()
t2.start()

t1.join()
t2.join()