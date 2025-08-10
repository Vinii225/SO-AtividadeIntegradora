#
# INFO: Simulação de dois processos concorrentes (produtor, consumidor) com sincronização Mutex
#

import threading
import time
import random

buffer = []
tamanho_max = 5
mutex = threading.Lock() 

def produtor():
    for _ in range(10):
        time.sleep(random.uniform(0.1, 0.4))
        with mutex: 
            if len(buffer) < tamanho_max:
                item = random.randint(1, 100)
                buffer.append(item)
                print(f"\n[PRODUTOR] produziu {item} | Buffer: {buffer}")


def consumidor():
    for _ in range(10):
        time.sleep(random.uniform(0.1, 0.4))
        with mutex: 
            if buffer:
                item = buffer.pop(0)
                print(f"\n[CONSUMIDOR] consumiu {item} | Buffer: {buffer}")



t1 = threading.Thread(target=produtor)
t2 = threading.Thread(target=consumidor)

t1.start()
t2.start()

t1.join()
t2.join()