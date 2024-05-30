from datetime import datetime
import services
import users

now = datetime.now() # current date and time
user = users.User


#lacag dhigashto function

def lacaglabixidfuntion():
    try:
        hadhaaga = 100
        tariikhda = now.strftime('%Y')
        laanta = int(input('Fadlan geli lambarka laanta: '))
        if laanta == 200021:
           lacagtalalabaxayo = int(input('Geli lacagta aad la baxay: '))
           if lacagtalalabaxayo > hadhaaga:
               print('Waanu ka xunahay lacagta aad gelisay way ka badan tahay inta kuugu jirta')
           else:
               biinka = int(input('Geli biinkaaga: '))
               if biinka == 1111:
                   print('------------------------')
                   print('Waxaaad laanta dhexe ee Telesom kala baxaday ' + str(lacagtalalabaxayo) + '$')
                   print('Taariikhda: ' + tariikhda  + ' Tixraaca: 10213Tls2024')
                   hadhaagarasmiga_ah = hadhaaga - lacagtalalabaxayo
                   print('Hadhaagu waa ' + str(hadhaagarasmiga_ah) + '$')
                   print('fadlan sug inta la xaqiijinayo Mahadsanid')
                   print('Hadii aad wax caawimaad ah u baahato waydii shaqaalaha tellerka fadha')
                   print('------------------------')
               else:
                   print('Biinka aad gelisay waa qalad ee inagu kala wad')
               
        else:
            print('Lambarka laanta aad gelisay waa qalad ')

    except:
        print('unknwon error is accour in the function ... ')

def ku_iibsofunction():
    try:
        print('fadlan geli lambarka qaansheegta')
    except:
        print('unknwon error is accour in the function ... ')
