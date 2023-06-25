#Aqui esta la func para calcular el avg de la lista de nums
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

#Le pedimos con un input el numero al usuario
def get_numbers():
    numbers = []
    while True:
        try:
            num = input("Enter a number (or 'done' to finish): ")
            if num.lower() == "done":
                break           #Cuando escriban 'done' se acaba la cadena
            else:
                num = float(num)
                numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")  #No pueden escribir letras, solo num
    return numbers

#Funcion principal para ejecutar el script
def main():
    print("Welcome to the Average Calculator!")
    numbers = get_numbers()
    if numbers:
        average = calculate_average(numbers)
        print("The average is:", average)
    else:
        print("No numbers entered. Exiting...")

if __name__== "__main__":
    main()
