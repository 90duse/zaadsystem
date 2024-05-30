# Simple Zaad System 

import service 
import systemfuntions
service = service.Service
#lacagdiridfunction = systemfuntions.lacagdiridfunction

try:
    code = 222
    shortcode = int(input('Enter short code: '))
    if shortcode == code:
        print('1: Itus Hadhaaga')
        print('2: Lacag Dirid')
        print('3: Lacag la bixid')
        print('4: Ku iibso')
        print('5: itus dhaqdhaqaaq')
        print('6: E-Voucher')
        print('7: Dara-Salaam Bank')
        print('10: Ka bax')
        Dooro = int(input('Dooro Adeega: '))
        if Dooro == service.hadhaaga:
           print('Hadhaagaagu waa: 100$')
           exit
        elif Dooro == service.lacagdirid:
           systemfuntions.lacagdiridfunction()
        elif Dooro == service.lacaglabixid:
            systemfuntions.lacaglabixidfuntion()
        else:
            print('by')
        
        
       
    else:
        print('short code is not valid')


except:
    print('unkwone error occur ...')
    