from datetime import datetime
import services
from users import User

now = datetime.now() # current date and time



class Lacaglabixid(User):
    #lacag dhigashto function
    def lacaglabixidfuntion(self):
        try:
            tariikhda = now.strftime('%Y')
            laanta = int(input('Fadlan geli lambarka laanta: '))
            if laanta:
               lacagtalalabaxayo = int(input('Geli lacagta aad la baxay: '))
               if lacagtalalabaxayo:
                    biinka = int(input('Geli biinkaaga: '))
                    if biinka == self.biinka:
                        print('------------------------')
                        print('Waxaaad laanta dhexe ee Telesom kala baxaday ' + str(lacagtalalabaxayo) + '$')
                        print('Taariikhda: ' + tariikhda  + ' Tixraaca: 10213Tls2024')
                        hadhaagarasmiga_ah = self.hadhaaga - lacagtalalabaxayo
                        print('Hadhaagu waa ' + str(hadhaagarasmiga_ah) + '$')
                        print('fadlan sug inta la xaqiijinayo Mahadsanid')
                        print('Hadii aad wax caawimaad ah u baahato waydii shaqaalaha tellerka fadha')
                        print('------------------------')
                    else:
                        print('Biinka aad gelisay waa qalad ee inagu kala wad')
               else:
                    print('Waanu ka xunahay lacagta aad gelisay way ka badan tahay inta kuugu jirta')
                    
               
            else:
                print('Numberka Laantu wuu qaldan yahay')
            

        except:
            print('unknwon error is accour in the function ... ')

    





