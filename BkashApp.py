# Make Bkash App
print("""
===============================
      Welcome To Bkash App
           Dial *247#
===============================
      """)
user_dial = input("Dial Bkash: ")
if user_dial == "*247#":
    print("""
          Login Successfully...
          Now You Can Choose Option
          1. Main Menu
          2. Logout
          """)
    user_option = input("Enter Option: ")
    if user_option == '1':
        print("""
              Welcome to main menu
              Now You Can Choose Option
              1. Send Money
              2. Mobile Recharge
              3. CashOut
              """)
        main_menu_option = input("Enter Main Menu Option: ")
        if main_menu_option == '1':
            print("You Choose Send Money Option")
            send_number = input("Enter Receiver Account Number: ")
            if send_number.isdecimal() == True:
                send_amount = input("Enter Amount: ")
                if send_amount.isdecimal() == True:
                    send_pin = input("Enter Your Pin Number: ")
                    if send_pin.isdecimal() == True:
                        print(f"{send_number} This Number Successfully Send {send_amount} Taka")
                    else:
                        print("Invalid Pin")
                else:
                    print("Invalid Amount")
            else:
                print("Invalid Number")  
        elif main_menu_option == '2':
            print("You Choose Mobile Recharge Option")
            recharge_number = input("Enter Recharge Number: ")
            operator_code = recharge_number[:3]
            if recharge_number:
                print("""
                  Recharge Oparator
                  1. Banglalink
                  2. GrameenPhone
                  3. Teletalk
                  """)
                oparator = int(input("Enter Oparator: "))
                if oparator == 1 and '019' in operator_code:
                    amount = int(input("Enter Amount: "))
                    if amount:
                        bkash_pin = int(input("Enter Pin: "))
                        if bkash_pin:
                            print(f"{amount} Recharge Successfully This Number {recharge_number}")
                        else:
                            print("Invalid Pin")    
                    else:
                        print("Invalid Amount")  
                
                elif oparator == 2 and '017' in operator_code:
                    amount = int(input("Enter Amount: "))
                    if amount:
                        bkash_pin = int(input("Enter Pin: "))
                        if bkash_pin:
                            print(f"{amount} Recharge Successfully This Number {recharge_number}")
                        else:
                            print("Invalid Pin")    
                    else:
                        print("Invalid Amount")
                        
                elif oparator == 3 and '015' in operator_code:
                    amount = int(input("Enter Amount: "))
                    if amount:
                        bkash_pin = int(input("Enter Pin: "))
                        if bkash_pin:
                            print(f"{amount} Recharge Successfully This Number {recharge_number}")
                        else:
                            print("Invalid Pin")    
                    else:
                        print("Invalid Amount")
                else:
                    print("Invalid Oparator")        
                   
        elif main_menu_option == '3':
            print("You Choose CashOut Option")
            cash_number = input("Enter CashOut Number: ")
            cash_oparator = cash_number[:3]
            if cash_number:
                print("""
                  Recharge Oparator
                  1. Banglalink
                  2. GrameenPhone
                  3. Teletalk
                  """)
                cash_opa = int(input("Enter CashOut Oparator: "))
                
                if cash_opa == 1 and '019' in cash_oparator:
                    cash_amount = int(input("Enter Amount: "))
                    if cash_amount:
                        cash_pin = int(input("Enter Pin: "))
                        if cash_pin:
                            print(f"{cash_amount} CashOut Successfully This Number {cash_number}")
                        else:
                            print("Invalid Pin")
                    else:
                        print("Invalid Amount") 
                    
                elif cash_opa == 2 and '017' in cash_oparator:
                    cash_amount = int(input("Enter Amount: "))
                    if cash_amount:
                        cash_pin = int(input("Enter Pin: "))
                        if cash_pin:
                            print(f"{cash_amount} CashOut Successfully This Number {cash_number}")
                        else:
                            print("Invalid Pin")
                    else:
                        print("Invalid Amount") 
                    
                elif cash_opa == 3 and '015' in cash_oparator:
                    cash_amount = int(input("Enter Amount: "))
                    if cash_amount:
                        cash_pin = int(input("Enter Pin: "))
                        if cash_pin:
                            print(f"{cash_amount} CashOut Successfully This Number {cash_number}")
                        else:
                            print("Invalid Pin")
                    else:
                        print("Invalid Amount")    
                else:
                    print("Invalid Oparator") 
                    
            else:
                print("Invalid CashOut Number Input")
        elif main_menu_option.isdecimal() == False:
            print("Main Menu Option Empty")
        else:
            print("Invalid Input")
    elif user_option == '2':
        print("Bkash App Successfully Logout")
    elif user_option.isdecimal() == False:
        print("User Option Empty")
    else:
        print("Invalid Input")
elif user_dial == "":
    print("Dial Empty")
else:
    print("Dial Invalid")