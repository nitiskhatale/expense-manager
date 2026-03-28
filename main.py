expenses = []

while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. Total spending")
    print("4. Filter by category")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("enter your amount: "))
        category = input("enter your category: ")
        note = input("enter your note: ")

        dict = {
            "amount": amount,
            "category": category,
            "note": note
        }

        expenses.append(dict)

    elif choice == "2":
        if expenses == []:
            print("No expenses available")
        else:
            number = 1
            for item in expenses:
                print(number, ". Amount:", item["amount"],
                      "| Category:", item["category"],
                      "| Note:", item["note"])
                number += 1
                
    elif choice == "3":
         if expenses ==[]:
             print("No expense")
         else:
             total = 0
             for item in expenses:
                 total= total+item["amount"]
                 
                 print("Total spending:", total)
    elif choice == "4":
        if expenses == []:
            print("no expense available")
        else:
            search=input("Enter category: ")
            for item in expenses:
                if item["category"]==  search:
                    print(item)
    elif choice=="5":
        print("Have a nice day")
        break
