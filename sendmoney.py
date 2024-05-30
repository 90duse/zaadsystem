from users import User

class Sendmoney(User): #send money class inheritance user class in users file
    
    def lacagdiridfunction(self):
        try:
            #hadhaaga_rasmiga_ah = self.hadhaaga - lacagta
            hubi = "Ma hubtaa in aad u dirayso lambarka "
            haa = 1
        
            gelinumberka = int(input('Geli Numberka: '))
            if gelinumberka == self.numberka:
                lacagta_ladirayo = int(input('Geli Lacagta aad dirayso: '))
                if lacagta_ladirayo:
                    print(hubi + str(self.numberka ) + " lacag cadadkeedu yahay: " + str(lacagta_ladirayo) + '$' )
                    print('1: HAA')
                    print('2: MAYA')
                    mid_dooro = int(input('Hadii aad hubto taabo 1 hadii kale taabo 2: '))
                    if mid_dooro == haa:
                        gelibiinka = int(input('geil biin numberkaaga: '))
                        if gelibiinka == self.biinka:
                            hadhaaga_rasmiga_ah = self.hadhaaga - lacagta_ladirayo
                            print('Waxaad u dirtay ' + str(lacagta_ladirayo) + ' numberka ' + str(self.numberka ) + ' hadhaagaagu hada waa ' + str(hadhaaga_rasmiga_ah) + '$')   
                        else:
                            print('biinka waa kaa qaldan yahay ee inagu kala wad')
                    else:
                        print('mid ma dooran')
                else:
                    print('lacagta lama hayo')
            else:
                print('lambarka waa qaldan yahay')
        except:
            print('unknwon error is accour in the lacagdirid function ... ' )


send = Sendmoney()



