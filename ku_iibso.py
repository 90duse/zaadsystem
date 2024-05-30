from datetime import datetime
from users import User
from businessUsers import Busines_users


#

now = datetime.now() # current date and time

class Ku_iibso(User, Busines_users):
    def kuiibsofunction(self):
        try:
            tariikhda = now.strftime('%Y')
            Haa = 1
            aqoonsiga_ganacsiga = int(input('Fadlan Geli numberka ganacsiga: '))
            if aqoonsiga_ganacsiga  and aqoonsiga_ganacsiga == self.businessnumber:
                magacaganacsahada = self.businesname
                qaansheegta = int(input('Geli qaansheegta: '))
                if qaansheegta:
                    faahfaahin = input('Fadlan geli faahfaahin ku saabsan qaansheegta aad bixinayso: ')
                    if faahfaahin:
                        print('Ma hubtaa in aad ' + str(qaansheegta) + '$ u dirayso' + str(magacaganacsahada) +
                                         'oo ah ' + str(faahfaahin))
                        print('1: HAA')
                        print('2: MAYA')
                        mid_dooro = int(input('Hadii aad hubto taabo 1 hadii kale taabo 2: '))
                        if mid_dooro ==  Haa:
                             gelibiinka = int(input('Fadlan geli number sireedkaaga si aad u fuliso codsigan: '))
                             if gelibiinka == self.biinka:
                                print('------------------------')
                                print('Waxaaad wax kaga iibsatay' + str(qaansheegta) + '$')
                                print('ganacsadaha sumadiisu tahay ' + str(aqoonsiga_ganacsiga))
                                print('Taariikhda: ' + tariikhda  + ' Tixraaca: ' + str(self.businessnumber+self.numberka) )
                                hadhaagarasmiga_ah = self.hadhaaga - qaansheegta
                                print('Hadhaagu waa ' + str(hadhaagarasmiga_ah) + '$')
                                print('Hadii aad wax caawimaad ah u baahato waydii shaqaalaha tellerka fadha')
                                print('------------------------')
                                 
                             else:
                                  print('Biinka aad gelisay waa qalad ee inagu kala wada')

                        else:
                            print('Haye Nabadeey')

                        
                    else:
                        print('Faahfaahinta aad gelisay ayaa wax ka qaldan yihiin ')
                else:
                    print('qaansheegtu waa tiro wax aan tiro ahayn ayaad gelisay')

            else:
                print('Lambarka qaansheegta waa qalad')
        except:
            print('unknwon error is accour in the ku iibso function ... please solve it ')




            if hubi:

                            print('------------------------')
                            print('Waxaaad wax kaga iibsatay' + str(qaansheegta) + '$')
                            print('ganacsadaha sumadiisu tahay ' + str(aqoonsiga_ganacsiga))
                            print('Taariikhda: ' + tariikhda  + ' Tixraaca: ' + str(self.businessnumber+self.numberka) )
                            hadhaagarasmiga_ah = self.hadhaaga - qaansheegta
                            print('Hadhaagu waa ' + str(hadhaagarasmiga_ah) + '$')
                            print('Hadii aad wax caawimaad ah u baahato waydii shaqaalaha tellerka fadha')
                            print('------------------------')