zasieg=200000
for i in range(1,zasieg):
    liczba=round(i/zasieg*100)
    print(liczba, '%', sep='', end='\r')
    liczba+=1
print('100% - done...                       ')
print(' ')
