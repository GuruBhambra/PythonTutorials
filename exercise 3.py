# Guessing the number


chances = 0

original_Num = 33
while(chances<5):
    num = int(input("Enter a number to guess "))
    if num < original_Num:
        print("Enter a bigger number than " + str(num))
        chances = chances + 1
        chances_left = 5-chances
        print("Number of attempts left "+ str(chances_left))
        continue

    elif num > original_Num:
        print("Enter a number smaller than " + str(num))
        chances = chances + 1
        chances_left = 5 - chances
        print("Number of attempts left "+ str(chances_left))
        continue
    elif num==original_Num:
        chances = chances + 1
        print("congratulation! You have guessed the correct number!")
        break

if chances_left==0 and num!= original_Num:
    print("Game Over!")
