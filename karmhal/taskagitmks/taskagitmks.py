# rock scissors paper game
import random

def main():
    rsp()

def rsp():
    i = 0
    user_score = 0
    robot_score = 0

    while user_score < 3 and robot_score < 3:
        robot = random.choice(("Tas", "Kagit", "Makas"))
        robot = robot.lower()
        user = input("Tas-Kagit-Makas: ")
        print(f"Robot: {robot}")
        # robot wins
        if user == "tas" and robot == "kagit":
            robot_score +=1
            i +=1
        # user wins
        elif user == "tas" and robot == "makas":
            user_score +=1
            i +=1
        # user wins
        elif user == "kagit" and robot == "tas":
            user_score +=1
            i +=1
        # robot wins
        elif user == "kagit" and robot == "makas":
            robot_score +=1
            i +=1
        # user wins
        elif user == "makas" and robot == "kagit":
            user_score +=1
            i +=1
        # robot wins
        elif user == "makas" and robot == "tas":
            robot_score +=1
            i +=1
    
    if user_score == 3:
        print("Kazandiniz!")
    else:
        print("Kaybettiniz!")
        

if __name__=="__main__":
    main()
