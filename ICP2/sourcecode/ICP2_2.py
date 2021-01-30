
Number = int(input("Enter a non negative integer number "))  # Taking user input as a integer number
Num = Number
step_count = 0

while Num != 0:
    if Num % 2 == 0:                                           # Dividing by 2 if number is even
        print("step", step_count)
        print(Num, "is even; divide by 2 and obtain", Num/2)
        Num = Num/2

    else:
        print("step", step_count)
        print(Num, "is odd; subtract 1 and obtain", Num-1)
        Num = Num-1                                            # Subtracting by 2 if number is odd
    step_count = step_count+1

print("\nEntered Number = ", Number)
print("Number of Step = ", step_count)