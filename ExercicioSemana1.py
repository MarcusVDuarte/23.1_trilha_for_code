import random

jogadas=["pedra","papel","tesoura"]
rodadas=[]
vitoria1=[]
vitoria2=[]

i=0
while i<1:
    jogador1numero=random.randint(0,2)
    jogador1=jogadas[jogador1numero]
    print(jogador1)
    jogador2numero=random.randint(0,2)
    jogador2=jogadas[jogador2numero]
    print(jogador2)
    
    if jogador1numero==0:
        if jogador2numero==0:
            print('EMPATE')
            rodadas.append('empate')
    
        elif jogador2numero==1:
            print('JOGADOR 2 GANHOU')
            rodadas.append('jogador 2')
            vitoria2.append('ganhou')
            if len(vitoria2)==5:
                i=1
    
        elif jogador2numero==2:
            print('JOGADOR 1 GANHOU')
            rodadas.append('jogador 1')
            vitoria1.append('ganhou')
            if len(vitoria1)==5:
                i=1

    elif jogador1numero==1:
        if jogador2numero==0:
            print('JOGADOR 1 GANHOU')
            rodadas.append('jogador1')
            vitoria1.append('ganhou')
            if len(vitoria1)==5:
                i=1
    
        elif jogador2numero==1:
            print('EMPATE')
            rodadas.append('empate')
    
        elif jogador2numero==2:
            print('JOGADOR 2 GANHOU')
            rodadas.append('jogador 2')
            vitoria2.append('ganhou')
            if len(vitoria2)==5:
                i=1
    elif jogador1numero==2:
        if jogador2numero==0:
            print('JOGADOR 2 GANHOU')
            rodadas.append('jogador 2')
            vitoria2.append('ganhou')
            if len(vitoria2)==5:
                i=1

        elif jogador2numero==1:
            print('JOGADOR 1 GANHOU')
            rodadas.append('jogador 1')
            vitoria1.append('ganhou')
            if len(vitoria1)==5:
                i=1
        elif jogador2numero==2:
            print('EMPATE')
            rodadas.append('empate')
        
print(rodadas)
    
    


    