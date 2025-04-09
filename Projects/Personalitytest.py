# Beginning: create variables
waffle_points = 0
pancake_points = 0

# Middle: Ask questions
answer = input("for breakfast would you rather A) waffle, or B) pancake")
if answer == "A":
    waffle_points += 1
elif answer == "B":
    pancake_points += 1


answer = input ("Would you rather eat A) Crepe, or B) Belgian waffle")
if answer == "A":
    pancake_points += 1
elif answer == "B":
    waffle_points += 1


answer = input("For a topping would you rather have A) Chocolate sauce, or B) Powdered sugar")
if answer == "A":
    waffle_points += 1
elif answer == "B":
    pancake_points += 1


answer = input("for a fruit would you want A) strawberries, or B) Blueberries")
if answer == "A":
    pancake_points += 1
elif answer == "B":
    waffle_points += 1

answer = input("would you rather have A) Butter,or B) Maple syrup")
if answer == "A":
    waffle_points += 1
elif answer == "B":
    pancake_points += 1

    # end of quiz:
if waffle_points > pancake_points:
    print("You prefer waffles")
elif pancake_points > waffle_points:
    print("You prefer pancakes")