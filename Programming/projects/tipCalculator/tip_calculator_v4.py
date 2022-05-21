while True:
    try:
        starter = int(input(f'how much was your starter?'))
    except ValueError:
        print ("that isn't a number, try again")
        continue
    else:
        print (f'starter price: £{starter}')
        break
while True:    
    try:
        main = int(input(f'how much was your main?'))
    except ValueError:
        print ("that isn't a number, try again")
        continue
    else:
        sub_total = starter + main
        print (f'main price: £{main}')
        print(f'your total so far is £{sub_total}')
        break            
while True:
    ask_tip = str(input(f'would you like to leave a tip?'))
    if ask_tip == "yes":
        tip_amount =(int(input("how much?")))
    
        print(f'your new total is £{tip_amount + sub_total}, please pay now')
        break
    elif ask_tip == "no":
        print(f'you broke bitch. your total is £{sub_total}')
        break
    else:
        print(f'sorry, this is a yes or no question.')
    
  