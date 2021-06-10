import pandas as pd
def logwrite(content):
    with open('data.log', 'a') as file:
        file.write(f'{content}\n')
# def median()

def meanmedianmode(fsum, fx, frequency, cmas, cf, classSize):
    classInterlist = [(k, v) for k, v in classInter.items()]
    sumn = sum(fx)
    n = fsum/2
    for i in cf:
        if i >= n:
            mc = i
            break
        elif i<n:
            continue
    ind = cf.index(mc)
    fr = frequency[ind]
    cfe = cf[ind-1]
    h = classSize
    firste = []
    for i in classInterlist:
        firste.append(i[0])
    l = firste[ind]
    print(l)
    p = (n-cfe)/fr
    pm = p*h
    mead = pm+l
    mea = sumn/fsum
    mode1 = 3*mead
    mode2 = 2*mea
    mode = mode1-mode2
    print(mea)
    result = {
        "Class Interval": classInterlist,
        "Frequency" : frequency,
        "x": cmas,
        "fx" : fx,
        "cf" : cf
    }
    print(pd.DataFrame(result))
    print("Mean:")
    print(f'Frequency total = {fsum}')
    print(f'Fx total = {sumn}')
    meannn = f"Mean= {sumn}/{fsum} = {mea}"
    print(meannn)
    print('Median:')
    print(f'Meadian Class = {mc}')
    print(f'l = {l}')
    print(f'n/2 = {n}')
    print(f'cf = {cfe}')
    print(f'Frequency = {fr}')
    print(f'Class Size = {h}')
    print(f"Median = {l}+[({n}-{cfe})/{fr}]*{h} = {mead}\n")
    print('Mode:')
    print(f'Mode = 3 * {mead} - 2 * {mea} = {mode}')


type = int(input('Type of data(grouped-1/ungrouped-2): '))
if type == 1:
    logwrite('Grouped selected....')
    intervals = int(input('Enter total no of class intervals: '))
    classInter = {}
    frequency = []
    cf = []
    fx = []
    cmas = []
    x = float(input('Enter starting interval: '))
    y = int(input('Enter ending interval: '))
    classSize = int(input('Enter the class size: '))
    fsum = 0
    for q in range(1, intervals+1):
        fre = int(input('Enter the frequency: '))
        fsum = fsum + fre
        cf.append(fsum)
        frequency.append(fre)
        start = x 
        end  = x + classSize
        minus = end - start
        cmal = minus/2
        cma = cmal + start
        fxs = fre * cma
        cmas.append(cma)
        fx.append(fxs)
        classInter.update({start: end})
        x = end
    # for items, keys in classInter.items():
    #     print(f"{items} = {keys}")
    # print('Done')
    # for items, keys in frequency.items():
    #     print(f"{items} = {keys}")
    meanmedianmode(fsum, fx, frequency, cmas, cf, classSize)
    
elif type==2:
    logwrite('Ungropued selected....')