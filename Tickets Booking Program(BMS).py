Budget_Price = 150
Economy_Price = 300

print("*** Welcome to EZtickets ***")
print()
input("Enter your Login ID: ")
input("Enter your Password: ")
print()

while True:
    
    user = input("Select to proceed - EVENTS or MOVIES or SPORTS: ").capitalize()

    if user == "Events":
        print()
        slct_evnt = input("Select to proceed - Concert or Comedy: ").capitalize()
        print()
        
        if slct_evnt == "Concert" or slct_evnt == "Comedy":
            slct_tckte = input("Select Ticket Type - Budget or Economy: ").capitalize()
            print()

            if slct_tckte == "Budget":
                Num_of_Tckts = int(input("Select Number of Tickets: ").capitalize())
                print()
                print("Total Price of Ticket: ₹", Num_of_Tckts * Budget_Price)
                print()
                confirm = input("Please Confirm - Yes or No: ").capitalize()
                
                if confirm == "Yes":
                    print("Your Payment is Done")
                    print("Thanks for booking")
                    print("Your Ticket is confirmed and sent to yout Email...")

                elif confirm == "No":
                    print("Your Payment is Failed")
                    print("Please Retry...")

                else:
                    print("Enter the Valid Keys...")

            elif slct_tckte == "Economy":
                Num_of_Tckts = int(input("Select Number of Tickets: ").capitalize())
                print()
                print("Total Price of Ticket: ₹", Num_of_Tckts * Economy_Price)
                print()
                confirm = input("Please Confirm - Yes or No: ").capitalize()

                if confirm == "Yes":
                    print("Your Payment is Done")
                    print("Thanks for booking")
                    print("Your Ticket is confirmed and sent to yout Email...")

                elif confirm == "No":
                    print("Your Payment is Failed")
                    print("Please Retry...")

                else:
                    print("Enter the Valid Keys...")

            else:
                print("Enter valid keys...")

        else:
            print("Enter valid keys...")

    elif user == "Movies":
        print()
        slct_mve = input("Select to proceed - Vikram or Don or Jurassic World: ").capitalize()
        print()

        if slct_mve == "Vikram" or slct_mve == "Don" or slct_mve == "Jurassic world":
            slct_tcktm = input("Select Ticket Type - Budget or Economy: ").capitalize()
            print()

            if slct_tcktm == "Budget":
                Num_of_Tckts = int(input("Select Number of Tickets: ").capitalize())
                print()
                print("Total Price of Ticket: ₹", Num_of_Tckts * Budget_Price)
                print()
                confirm = input("Please Confirm - Yes or No: ").capitalize()

                if confirm == "Yes":
                    print("Your Payment is Done")
                    print("Thanks for booking")
                    print("Your Ticket is confirmed and sent to yout Email...")

                elif confirm == "No":
                    print("Your Payment is Failed")
                    print("Please Retry...")

                else:
                    print("Enter the Valid Keys...")

            elif slct_tcktm == "Economy":
                Num_of_Tckts = int(input("Select Number of Tickets: ").capitalize())
                print()
                print("Total Price of Ticket: ₹", Num_of_Tckts * Economy_Price)
                print()
                confirm = input("Please Confirm - Yes or No: ").capitalize()

                if confirm == "Yes":
                    print("Your Payment is Done")
                    print("Thanks for booking")
                    print("Your Ticket is confirmed and sent to yout Email...")

                elif confirm == "No":
                    print("Your Payment is Failed")
                    print("Please Retry...")

                else:
                    print("Enter the Valid Keys...")

            else:
                print("Enter valid keys...")

        else:
            print("Enter valid keys...")

    elif user == "Sports":
        print()
        slct_sprt = input("Select to proceed - IPL or Kabaddi: ").capitalize()
        print()

        if slct_sprt == "IPL" or slct_sprt == "Kabaddi":
            slct_tckts = input("Select Ticket Type - Budget or Economy: ").capitalize()
            print()

            if slct_tckts == "Budget":
                Num_of_Tckts = int(input("Select Number of Tickets: ").capitalize())
                print()
                print("Total Price of Ticket: ₹", Num_of_Tckts * Budget_Price)
                print()
                confirm = input("Please Confirm - Yes or No: ").capitalize()

                if confirm == "Yes":
                    print("Your Payment is Done")
                    print("Thanks for booking")
                    print("Your Ticket is confirmed and sent to yout Email...")

                elif confirm == "No":
                    print("Your Payment is Failed")
                    print("Please Retry...")

                else:
                    print("Enter the Valid Keys...")

            elif slct_tckts == "Economy":
                Num_of_Tckts = int(input("Select Number of Tickets: ").capitalize())
                print()
                print("Total Price of Ticket: ₹", Num_of_Tckts * Economy_Price)
                print()
                confirm = input("Please Confirm - Yes or No: ").capitalize()

                if confirm == "Yes":
                    print("Your Payment is Done")
                    print("Thanks for booking")
                    print("Your Ticket is confirmed and sent to yout Email...")

                elif confirm == "No":
                    print("Your Payment is Failed")
                    print("Please Retry...")

                else:
                    print("Enter the Valid Keys...")

            else:
                print("Enter valid keys...")

        else:
            print("Enter valid keys...")
          
    else:
        print("Enter valid keys...")

    break
