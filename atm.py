print("\n\nWELCOME TO ABC BANK " + "\n \n Insert your card")

# for i in range(1,9):
#      date= ""i +"" i
#      print ("DATE OF TRANSACTION -",date)

password=1802
choice = 0
balance= 24000
pin=int(input("enter the password - "))


if pin==password:

    while choice != 5:
          print("1-deposit")
          print("2-withdraw")
          print("3-Print receipt")
          print("4-Change password")
          print("5-Exit")

          choice=int(input("enter the choice - "))
          if choice==1:
              dep=int(input("enter the amount that is to be deposited"))
              balance= balance + dep #balance+=dep
              print("the total balance of the account is -",balance)
              print("\nthe amount is successfully is deposited")
    
          elif choice == 2:
                withdraw=int(input("Enter the amount that is to be withdrawn"))
                balance-=withdraw
                print("you have succesfully withdrawn",withdraw)
                print("\n\nthe total balance left is -",balance)
                print("\nthe amount is withdrawn")

     #      elif choice==3:
     #           for i in range(1,9)
     #           print("******ABC BANK*******")
     #           print("\n\ndate of receipt-",date)
     #    #  transactions

          elif choice==4:
                previous_password=int(input("\n\nEnter previous password -"))
                if previous_password==password:
                   new_password=int(input("\nEnter your new password -"))
                else:
                     print("\nPASSWORD NOT MATCHED|\nPlease try again!!!")
    
          else:
                print("THANKS FOR VISITING US")

else:
     print("You have entered wrong password \n \n Please try again")
         
     
