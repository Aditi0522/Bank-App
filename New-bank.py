
class Bank_account:
   def __init__(self):
      self.w =[]
         
   def create_account(self,name,phone,pw,amt):
      try:
        acc_id=self.w[-1][0]+1
      except:
         acc_id=1  
         
      self.w.append([acc_id,name,phone,pw,amt])
      print(self.w)
      print("Account Succesfully created!!")
      print(f"Don't forget that your Account id is {self.w[-1][0]}, note it somewhere if you have to 😉")
      
   def use_account(self):
      while True:
        opened_acc=int(input("Please enter your account id: "))
        if self.w[opened_acc-1]==0:
           print("This account does not exist, please try again.")
           print(self.w)
           break
        if opened_acc> self.w[opened_acc-1][0]:
           print("This account does not exist, please check your credential again.")
           opened_acc=int(input("Please enter your account id: ")) 
      
        pwcheck=input("Please enter your password: ")
       
        if pwcheck != self.w[opened_acc-1][3]:
           print("The password you have entered is incorrect, please try again.")
           break         
        else:
           while True:
             print("\t\t\t\t\tCHOICE\t\t\t\t\t")
             print("1) Transfer money\n2) Deposit money\n3) Withdraw money\n4) Show current balance\n5)Exit")
             ind=int(input("Enter the index to execute the function: "))

             if ind == 1:
                transf_acc=int(input("Enter the account id of the bank account in which you would like try tranfer money: "))
                if transf_acc > self.w[-1][0]:
                   print("This account does not exist, please try again.")
                   transf_acc=int(input("Enter the account id to which you would like to tranfer money: "))
                money_t=int(input("How much money would you like to tranfer? "))
                if money_t> self.w[opened_acc-1][4]:
                   print("aww looks like you are short on cash.Please enter suitable amount of money to transfer")
                   money_t=int(input("How much money would you like to tranfer?"))
                self.w[transf_acc-1][4]+=money_t
                self.w[opened_acc-1][4]-=money_t
                print("The money was succesfully transferred!!! ")
                              
             elif ind == 2:
                money_d=int(input("How much money would you like to deposit? "))
                self.w[opened_acc-1][4]+=money_d
                print("Your money has been successfully deposited!!")
             elif ind == 3:
                money_w=int(input("How much money would you like to withdraw? "))
                if money_w > self.w[opened_acc-1][4]:
                   print("Sorry, but you don't have that much money in your account. Please try again.")
                   money_w=int(input("How much money would you like to withdraw? "))
                self.w[opened_acc-1][4]-=money_w
                print(f"You have withdrawn {money_w} from your bank account")   
             elif ind ==4:
                print(f"The current balance of your account is {self.w[opened_acc-1][4]}")
             elif ind ==5:
                break
             else:
                print("This choice does not exist, please try again")
                break
           break 
        
             
   def update_account(self):
      while True:
        print(self.w)
        up_acc=int(input("Please enter your account id: "))
        if self.w[up_acc-1]==0:
           print("This account does not exist, please try again.")
           break
        if up_acc> self.w[up_acc-1][0]:
           print("This account does not exist, please check your credential again.")
           up_acc=int(input("Please enter your account id: ")) 
      
        pwcheck1=input("Please enter your password: ")
       
        if pwcheck1 != self.w[up_acc-1][3]:
           print("The password you have entered is incorrect, please try again.")
         
        else:
           while True:
              print("\t\tWhich of the following criteria would you like to update?\t\t")
              print("1) Name\n2) phone number\n3) password\n4) exit")
              choice = int(input("Enter the index of the required criteria"))
              if choice == 1:
                 new_name=input("Enter your updated name: ").strip().lower()
                 self.w[up_acc-1][1]=new_name
                 print("Your name has been updated!!")
                 print(f"These are your updated account details {self.w[up_acc-1]}")
              elif choice == 2:
                 new_phone=int(input("Enter your updated mobile number: ").strip())
                 self.w[up_acc-1][2]=new_phone
                 print("Your mobile number has been updated!!")
                 print(f"These are your updated account details {self.w[up_acc-1]}")
              elif choice == 3:
                 new_pw=input("Enter your updated password: ").strip()
                 self.w[up_acc-1][3]=new_pw
                 print("Your password has been updated!!")
                 print(f"These are your updated account details {self.w[up_acc-1]}")
              elif choice == 4:
                 break

              else:
                 print("This choice does not exist, please try again")
                 break
           break 
        break

   def delete_account(self):
      del_acc=int(input("Please enter your account id: "))
      if del_acc> self.w[del_acc-1][0]:
         print("This account does not exist, please check your credential again.")
         del_acc=int(input("Please enter your account id: ")) 
      
      pwcheck2=input("Please enter your password: ")
       
      if pwcheck2 != self.w[del_acc-1][3]:
         print("The password you have entered is incorrect, please try again.")
         
      else:
         while True:
            del self.w[del_acc]
            self.w.insert(del_acc-1,0)
            print("Your account has been succesfully deleted!!")
            print(self.w)
            break
            
def main_menu():
   bank = Bank_account()
   while True:
      print("BANK✔")
      print("Choice:\n 1) Create account\n 2) Use account\n 3) Update account\n 4) Delete account\n 5) Exit Application")
      print("\n What would you like to do?\n ")
      choice = input("Kindly enter the index to execute the function:\n")

      if choice == "1":
         name = input("Enter the account holder's name: ").strip().lower()
         phone = int(input("Enter you phone number: ").strip())
         if phone in z:
            print("This account already exists, please try again")
            main_menu()

         pw = input("Create a password: ").strip()
         if pw in z:
            print("This password is already in use, please create a new password")
            pw = input("Create a new password: ").strip() 
         z.append(phone)
         z.append(pw) 
         amt = float(input("Enter the amount of money you want deposit in account: "))
         bank.create_account(name, phone, pw, amt)
           
      elif choice == "2": 
         bank.use_account()
      elif choice == "3":
         bank.update_account()
      elif choice == "4":
         bank.delete_account()
      elif choice == "5":
         print("Thank You for choosing our services, We hope to see you again. Until next time.")
         quit()

      else:
         print("Invalid choice. Please try again.")
         main_menu()

mm = Bank_account()
z=[]
acc_id = 0
if __name__ == "__main__":
   main_menu()
