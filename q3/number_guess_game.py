import random 
def number_guessing_game():
    secret_number=random.randint(1,100)
    attempts=0
    print("=================")
    print("welcome to number guess game!")
    print("=================")
    print("i picked a number between 1-100")
    print("can you guess it !")
    print("")
    while True:
        guess =int(input("enter your guess"))
        attempts +=1
        if guess < secret_number:
            print("too low !Try higher")
        elif guess > secret_number:
             print("too high !Try lowerer")
        else :
            print("")   
            print("congratulation you  get it !")
            print(f"the number was {secret_number}")
            print(f"you took {attempts} attempts")
            break
number_guessing_game()


                        


            
            
