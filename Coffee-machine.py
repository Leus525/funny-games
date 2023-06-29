Tea = ['Tea' , 0.50]
Water = ['Water' , 0.15]
Wc = ['White_coffee' , 0.8]
Co = ['Coffee_origenal' , 0.70]
#Функция отказа
def Refusing():
    print('Bye Bye!')
#функция налив напитка
def Pour_drink_and_offer_another():
    print('Your drink : ' , x_2 , ' is ready with ' , sugar , ' spoons of sugar')
#функция вычесления здачи
def Calculate_money_dipozite():
    change = received_money - x
    print('Your change is : ' , round(change, 2) , ' euro')
#функция выбор напитка
def choice_drink(x, x_2):
     print(x_2 , ' = ' , x , ' euro')
print('             Welcome!!!')
while True:
    print('We have:' , '\n' , 'Index - Name - Price' , '\n' , '0 = End' , '\n' , '1 = ' , Tea[0] , Tea[1] , '\n' , '2 = ' , Water[0] , Water[1] , '\n' \
          , '3 = ' , Wc[0] , Wc[1] , '\n' , '4 = ' , Co[0] , Co[1])
    choice = input('Enter index: ')
    sugar = int(input('Enter quantity of shugar from 0 to 5 : '))
#условиe функции отказа
    if choice == '0':
        Refusing()
        break
# условия выбора напитка
    elif choice == '1':
        x = Tea[1]
        x_2 = Tea[0]
        choice_drink(x, x_2)
    elif choice == '2':
        x = Water[1]
        x_2 = Water[0]
        choice_drink(x, x_2)
    elif choice == '3':
        x = Wc[1]
        x_2 = Wc[0]
        choice_drink(x, x_2)
    elif choice == '4':
        x = Co[1]
        x_2 = Co[0]
        choice_drink(x, x_2)
    else:
        continue
# условие выдачи сдачи
    received_money = float(input('Please put the ^^^money : '))
    if received_money > x:
        Calculate_money_dipozite()
        Pour_drink_and_offer_another()
        con_bye = input('Do you want another drink? Yes/No : ')
        if con_bye == 'Yes':
            continue
        else:
            Refusing()
            break
# условие без сдачи
    elif received_money == x:
        Pour_drink_and_offer_another()
        con_bye = input('Do you want another drink? Yes/No : ')
        if con_bye == 'Yes':
            continue
        else:
            Refusing()
            break
# условие если денег мало
    elif received_money < x:
        money_less = x - received_money
        print('Please add ' , round(money_less, 2) , ' money') 
        received_money = float(input('Please add the ^^^ money : '))
        while received_money < money_less:
            money_less = money_less - received_money
            print('Please add ' , round(money_less, 2) , ' money') 
            received_money = float(input('Add the ^^^ money : '))
        if received_money > money_less:
            x = money_less
            Calculate_money_dipozite()
            Pour_drink_and_offer_another()
            con_bye = input('Do you want another drink? Yes/No : ')
            if con_bye == 'Yes':
                continue
            else:
                Refusing()
                break
        else:
            Pour_drink_and_offer_another()
            con_bye = input('Do you want another drink? Yes/No : ')
            if con_bye == 'Yes':
                continue
            else:
                Refusing()
                break
            
    else:
        Refusing()
        break
