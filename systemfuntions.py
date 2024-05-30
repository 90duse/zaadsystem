

#lacag dirid function


from datetime import datetime

now = datetime.now() # current date and time


def lacagdiridfunction():
    try:
        lambarka = 633564453
        hadhaaga = 100
        hubi = "Ma hubtaa in aad u dirayso lambarka "
        haa = 1
        biin_numberka = 1111
        gelinumberka = int(input('Geli Numberka: '))
        if gelinumberka == lambarka:
            lacagta = int(input('Geli Lacagta aad dirayso: '))
            if lacagta:
                print(hubi + str(lambarka ) + " lacag cadadkeedu yahay: " + str(lacagta) + '$' )
                print('1: HAA')
                print('2: MAYA')
                mid_dooro = int(input('Hadii aad hubto taabo 1 hadii kale taabo 2: '))
                if mid_dooro == haa:
                    gelibiinka = int(input('geil biin numberkaaga: '))
                    if gelibiinka == biin_numberka:
                        hadhaaga_rasmiga_ah = hadhaaga - lacagta
                        print('Waxaad u dirtay ' + str(lacagta) + ' numberka ' + str(lambarka ) + ' hadhaagaagu hada waa ' + str(hadhaaga_rasmiga_ah) + '$')   
                    else:
                        print('biinka waa kaa qaldan yahay ee inagu kala wad')
                else:
                    print('mid ma dooran')
            else:
                print('lacagta lama hayo')
        else:
            print('lambarka waa qaldan yahay')
    except:
        print('unknwon error is accour in the function ... ')

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