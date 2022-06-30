def calculation(number_given):
    

    try:
        number_given = int(number_of_elements)

        if number_given > 0:
            number_calculated = number_given * 50
            print(f"Your result is {number_calculated}")
        
        elif number_given == 0 or number_given < 0:
            print("Invalid, number must be greater than 0")

    except ValueError:
        print("Invalid number!")

user_input_number = ""
while user_input_number != "exit":
    user_input_number = input("Please enter a number and I will multiply it by 50 : \n")
    for number_of_elements in user_input_number.split():
        calculation(user_input_number)