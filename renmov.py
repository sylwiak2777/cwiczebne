#Skrypt tworzacy katalogi na bazie nazw plików i przesuwający do nich pliki
#wykorzystanie importu i pętli, praca na listach składających się z stringów

import os
import shutil

#listaPlikow = os.listdir('.' )
#print(listaPlikow)
#nazwa pliku
#print(os.path.basename(__file__))
areYouSure = ''
areYouSure = input('Ropocząć przesuwanie? (Tak/Nie)')
#print(areYouSure)
#upewniamy się, że operator wie co robi
if areYouSure == 'Tak' or areYouSure == 'tak':
    print ('Rozpoczynam: ')
    for plik in os.listdir('.' ):
        #intersują nas nazwy tylko plików (bez katalogów), bez nazwy naszego pliku i konczacych sie na .jpg 
        if plik != os.path.basename(__file__) and ( os.path.isfile(plik) and plik.endswith('.jpg') ):
            #print ( plik , ' ', plik[:-4], ' ', plik[:-2])
            #tworzenie katalogu usera / brak reakcji jesli istnieje
            os.makedirs (plik[:-14], exist_ok = True)
            #próba "przesunięcia" pliku
            try:
                #przesuniecie
                #print('OK')
                shutil.move( plik , plik[:-14])
                #\r do drukowania w tej samej linii
                print('Plik: ', plik, 'do: ', plik[:-14], end='\r')
            except:
                #jesli przesuniecie zwraca błąd plik prawdopodobnie istnieje
                print ('UWAGA: ', plik, ' istnieje!')
                #przerwanie działania
                break
else:
    print('Nic nie robie!')
print('\nZakończono działanie...', end='\n')
