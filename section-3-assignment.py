names = ['Sumesh','Shalini','Dev']

for name in names:
    if len(name) > 5 and ("N" in name or "n" in name):
        print(name+' '+str(len(name)))



while True:
    if len(names) > 0:
        names.pop()
    else:
        break    


print('Names list size: '+str(len(names)))