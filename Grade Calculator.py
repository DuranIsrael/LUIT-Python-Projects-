percent = int(input("What is your score percentage: "))

if percent >= 90 and percent <= 100:
    print("Your Grade is A")
elif percent >= 80 and percent <= 89:
    print("Your Grade is B")
elif percent >= 70 and percent <= 79:
    print("Your Grade is C")
elif percent >= 60 and percent <= 69:
    print("Your Grade is D")
else:
    print("You failed!")


