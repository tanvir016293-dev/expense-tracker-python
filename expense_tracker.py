print(" Welcome to Expense Tracker 💸 ")
expense = {}

while True:
    print("======= MENU ======= ")
    print("1.Add Expense ")
    print("2.View All Expenses ")
    print("3.View Total Spending ")
    print("4.Exit ")

    print("===================== ")

    choice = int(input("Enter your choice (1-4) :"))

    if (choice==1):
        date = input("Enter date (DD-MM-YYYY):\n")
        category  = input("Enter category (Food, Travel, Shopping, etc) :\n")
        description = input("Enter short description :\n") 
        amount = float(input("Enter amount (₹) :\n"))

        if date not in expense:
           expense[date] =[]
           
        new_expense = {
                
                "category" : category,
                "description" : description,
                "amount" : amount
        }
        expense[date].append(new_expense)
        print("✅ Expense added successfully! ")
        
    elif(choice==2): 
      print("\n All Expenses...")
      for date,items in expense.items():
         print(f"\nDate : {date}")
         for exp in items:
            print(f" -=>\ncategory = {exp['category']}\ndescription = {exp['description']}\namount = {exp['amount']}")

    elif(choice==3):
       total = 0
       for items in expense.values():
          for exp in items:
             total +=exp["amount"]
       print(f"\nTotal spending : {total}") 
            
    elif(choice==4):
       print("-----Exit-----")
       break
    else:
       print("Invalid choice ! Please enter 1-4.")

       


        
