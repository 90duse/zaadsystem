# Simple Zaad System
import services 
import lacaglabixid
from sendmoney import Sendmoney
from lacaglabixid import Lacaglabixid
from ku_iibso import Ku_iibso


services = services.Service
sendmoney = Sendmoney()
lacaglabixid = Lacaglabixid()
kuiibso = Ku_iibso()



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
        if Dooro == services.hadhaaga:
           print('Hadhaagaagu waa: 100$')
           exit
        elif Dooro == services.lacagdirid:
            #sendmoney.lacagdiridfunction()
            sendmoney.lacagdiridfunction()
        elif Dooro == services.lacaglabixid:
           lacaglabixid.lacaglabixidfuntion()
        elif Dooro == services.ku_iibso:
            kuiibso.kuiibsofunction()
        else:
            print('by')
        
        
       
    else:
        print('short code is not valid')


except:
    print('code ka main ka ayaa error ku jiraa ...')
    