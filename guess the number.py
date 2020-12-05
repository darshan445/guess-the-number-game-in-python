print("this is guessing numbers game")
print("guess numbers between 1 to 100")
ans=10
guess=1
left = 9
print("Guess the number")
while guess<=9:
    user_input = int(input())
    if ans==user_input:
        print("your guess is right you won this game!!")
        print("your guess attempt is",guess)
        break
    elif user_input>10:
        if left<=1:
            print("sorry you loose this game")
        else:
            print("your guess number is high")
    elif user_input<10:
        print("your guess number is low")
    guess = guess + 1
    left=left-1
    if left<1:
        break
    else:
        print("you left:",left)





