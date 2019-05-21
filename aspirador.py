import random

class Sala:
    def __init__(self, x, y):
        self.limpa = random.choice([True, False])
        self.x = x
        self.y = y
        self.aspirador_me_limpou = False

salas = []

for x in range(5):
    salas.append([])
    for y in range(5):
        sala = Sala(x, y)
        salas[x].append(sala)

class Aspirador:
    def __init__(self):
        global salas

        x_aleatorio = random.randint(0, 4)
        y_aleatorio = random.randint(0, 4)

        self.sala_atual = salas[x_aleatorio][y_aleatorio]
    
    def limpar_sala(self, sala):
        if sala.limpa == False:
            sala.limpa = True
        self.sala_atual = sala
        self.sala_atual.aspirador_me_limpou = True

    def proxima_sala(self):
        global salas

        x_atual = self.sala_atual.x
        y_atual = self.sala_atual.y

        opcoes = []

        if y_atual-1 >= 0:
            opcoes.append(salas[x_atual][y_atual-1]) # cima
        
        if x_atual+1 <= 4:
            opcoes.append(salas[x_atual+1][y_atual]) # direita

        if y_atual+1 <= 4:
            opcoes.append(salas[x_atual][y_atual+1]) # baixo

        if x_atual-1 >= 0:
            opcoes.append(salas[x_atual-1][y_atual]) # esquerda

        random.shuffle(opcoes)

        for sala in opcoes:
            if sala.aspirador_me_limpou == False:
                return sala
        
        # Neste ponto, o aspirador limpou todas as opcoes de salas
        return random.choice(opcoes)

    def limpou_tudinho(self):
        global salas

        for linha in salas:
            for sala in linha:
                if sala.limpa == False:
                    return False

        # Neste ponto, todas as salas estão limpas
        return True

    def mostrar_salas(self):
        global salas

        # Linha superior
        for i in range(5):
            print('--', end='')
        
        # Quebra de linha
        print()

        for linha in salas:
            print('|', end='')
            
            for sala in linha:
                if sala.limpa == True:
                    print(' |', end='')
                else:
                    print('X|', end='')

            # Quebra de linha
            print()

            # Linhas do meio
            for i in range(5):
                print('--', end='')

            # Quebra de linha
            print()


aspirador = Aspirador()

while aspirador.limpou_tudinho() == False:
    sala_que_vou_limpar = aspirador.proxima_sala()

    print('A sala', sala_que_vou_limpar.x, sala_que_vou_limpar.y, 'será limpa!')

    aspirador.limpar_sala(sala_que_vou_limpar)

    print()
    aspirador.mostrar_salas()
    print()




input()