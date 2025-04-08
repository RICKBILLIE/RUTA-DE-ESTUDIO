def print_numbers(text_1,text_2) -> int :

    count = 0 
    for number in range ( 1, 101):
        if number % 3 == 0:
           print(text_1)
        elif number % 5 == 0:
           print(text_2)
        elif  number % 3 == 0 and number % 5 == 0:
           print(text_1+text_2)
        else:
           print(number)
           count += 1
    return count 


print(print_numbers("TEXTO 1","TEXTO 2"))