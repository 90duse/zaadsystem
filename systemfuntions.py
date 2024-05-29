



#lacag dirid function

def lacagdiridfunction():
    
   
    try:
        lambarka = 633564453
        hadhaaga = 100
        hubi = "Ma hubtaa in aad u dirayso lambarka "
        haa = 1
        biin_numberka = 1111
        # mid_dooro = int(input('Hadii aad hubto taabo 1 hadii kale taabo 2: '))
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
                        print('Waxaad u dirtay ' + str(lacagta) + ' numberka ' + str(lambarka ) + 'hadhaagaagu hada waa ' + str(hadhaaga_rasmiga_ah) + '$')   
                    else:
                        print('biinka waa kaa qaldan yahay ee inagu kala wad')
                else:
                    print('mid ma dooran')
            else:
                print('lacagta lama hayo')
        
        else:
            print('lambarka waa qaldan yahay')
        

       
            

       
        #     exit
    except:
        print('unknwon error is accour in the function ... ')