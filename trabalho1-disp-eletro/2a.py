import math
vm = 18
res = 9.565
period = 1/60
w = (2*math.pi) / period
vd = [0.698, 0.781]
rd = [0.0505, 0.0428]

for i in (0,1):
    print(f"Dados da saída do diodo{i+1}")
    #Vomax
    vomax = res * ((vm - vd[i-1])/(res + rd[i-1]))
    
    #t1, T1 e T2
    t11 = (1/w) * math.asin((vd[i-1]/vm))
    periodCondT1 = ((period/2) - (2*t11)) * 1000
    periodNCondT2 = ((period/2) + (2*t11)) * 1000
    print(f"T1{i+1} = {periodCondT1}ms e T2{i+1} = {periodNCondT2}ms")

    #Vdmax e Vdmin
    Vdmax = vm - vomax
    Vdmin = -vm
    if i == 0: 
        print(f"Vdmax = {Vdmax}V e Vdmin = {Vdmin}V")
        print(f"Vomax{i+1} = {vomax}V")

    else: 
        print(f"Vdmax = {Vdmin}V e Vdmin = {Vdmax}V")
        print(f"Vomax{i+1} = {-vomax}V")


    