from users import User
from businessUsers import Busines_users
from ku_iibso import Ku_iibso




class Tusdhaqdhaqaaq(Ku_iibso):
    
    def tusdhaqdhaqaaqfunction(self):
        # kuiibso = Ku_iibso.kuiibsofunction
        try:

          
            print('-------------------')
            print('Itus Dhaqdhaqaaqa: ')
            print('1: Dhaqdhaqaaqa kaliya')
            print('2: Warbixin kooban')
            print('0: dib u noqo')
            print('10: Ka bax')
            print('-------------------')
            dooro = int(input('Dooro Adeega: '))
            dhaqdhaqaaqa_kaliya = 1
            if dooro == dhaqdhaqaaqa_kaliya:
                print('-------------------')
                # print('Waxaa laguu soo diri doonaa fariin')
                print('Waxaad lacag u dirtay ' + str(self.businessnumber ) + ' cadadkeedu yahay ' + str(self.kuiibsofunction()))
                print('-------------------')
            else:
                print('Fadlan mid lanbarada meesha ku qoran kaliya dooro')

            
        except:
            print('Cilad ayaa ka jirta function tusdhaqdhaqaaq si guud fadlan xali')