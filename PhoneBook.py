names = []phone_numbers = []num = int(input("Enter the no. of contact you want to save: "))for i in range(num):  names.append(input("Name: "))  phone_numbers.append(input("Phone_number: "))print("\nName\t\t\tPhone Number\n")print(num)for i in range(num):  print("{}\t\t\t{}".format(names[i], phone_numbers[i]))search_term = input("\nEnter search term: ")print("Search result: ")if search_term in names:  index = names.index(search_term)  phone_number = phone_numbers[index]  print("Name: {}, Phone Number: {}".format(search_term, phone_number))else:  print("No results found")