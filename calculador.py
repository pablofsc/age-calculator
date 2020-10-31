# 07/03/2019
# Recriação da primeira versão do programa (02/11/2018)

import datetime

m31 = str('01 03 05 07 08 10 12')
m30 = str('04 06 09 11')
fev = str('02')

while True:
    # Mostrar data atual:
    now = datetime.datetime.now()
    print('Data atual: ' + str(now.strftime("%Y/%m/%d %H:%M:%S\n")))

    if now.year % 4 == 0: # Ano atual bissexto?
        bsxta = True
    else:
        bsxta = False

    qmesa = int # Define quantos dias o mês atualdeve ter:

    if str(now.month) in m31:
        qmesa = 31
    elif str(now.month) in m30:
        qmesa = 30
    elif str(now.month) in fev:
        if bissextoa:
            qmesa = 29
        if not bissextoa:
            qmesa = 28

    diab = int(input('Dia do nascimento: '))
    mesb = int(input('Mês do nascimento: '))
    anob = int(input('Ano do nascimento: '))
    print()

    if anob > now.year: # Ano de nascimento no inválido?
        print('O ano inserido está no futuro.\nReiniciando programa\n')
        continue

    if anob % 4 == 0: # Ano de nascimento bissexto?
        bsxtb = True
    else:
        bsxtb = False

    if mesb > 12 or mesb < 1: # Mês de nascimento inválido?
        print('O mês inserido é inválido.\nReiniciando programa\n')
        continue

    if str(mesb) in m31: # Quantos dias no mês de nascimento?
        qmesb = 31
    elif str(mesb) in m30:
        qmesb = 30
    elif str(mesb) in fev:
        if bsxtb:
            qdiasmesb = 29
        if not bsxtb:
            qmesb = 28

    if diab > qmesb or diab < 1: # Dia de nascimento inválido?
        print('O dia inserido é inválido.\nReiniciando programa\n')
        continue

    print('Data de nascimento: ' + str(anob) + '/' + str(mesb) + '/' + str(diab) + '\n')

    diav = int(0) # vividos
    mesv = float(0)

    diaan = int(0) # Quantos dias já se passaram nesse ano?
    for mes in range(1, now.month):
        mesv += 1
        if str(now.month) in m31:
            diaan += 31
        elif str(now.month) in m30:
            diaan += 30
        elif str(now.month) in fev:
            if bsxta:
                diaan += 29
            if not bsxta:
                diaan += 28

    diaan += now.day -1
    mesv -= 1

    diasentre = int(0)
    for ano in range(anob + 1, now.year):
        mesv += 12
        if ano % 4 == 0: # Ano avaliado bissexto?
            diasentre += 366
        else:
            diasentre += 365

    diabna = int(0)
    diabnd = int(0)
    for mes in range(1, mesb): # Quantos dias antes do nasc?
        mesv += 1
        if str(mes) in m31:
            diabna += 31
        elif str(mes) in m30:
            diabna += 30
        elif str(mes) in fev:
            if bsxtb:
                diabna += 29
            if not bsxtb:
                diabna += 28

    diabna += diab

    if bsxtb: # Quantos dias após nasc no ano de nasc?
        diabnd = 366 - diabna
    if not bsxtb:
        diabnd = 365 - diabna

    diav = diabnd + diasentre + diaan # Dias vividos
    mesv = mesv + (qmesb - diab)/qmesb + now.day/qmesa

    # Sáida
    print(round(diav/365, 1), 'anos vividos;')
    print(round(mesv, 1), 'meses vividos;')
    print(round(diav/7, 1), 'semanas vividas;')
    print(diav, 'dias vividos')

    input('\nConcluído\nPressione enter para reiniciar\n')
