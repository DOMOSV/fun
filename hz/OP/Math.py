import random
from threading import Timer
import time
import datetime
def tablo(_x,_offset=0):
    """PERVAYA STROKA"""
    stroka = ""
    for i in str(_x):
        i = int(i)
        if i == 0:
            stroka +=" ***  "
        elif i == 1:
            stroka +="    * "
        elif i == 2:
            stroka +=" ***  "
        elif i == 3:
            stroka +="****  "
        elif i == 4:
            stroka +="*   * "
        elif i == 5:
            stroka +=" ***  "
        elif i == 6:
            stroka +=" ***  "
        elif i == 7:
            stroka +="***** "
        elif i == 8:
            stroka +=" ***  "
        elif i == 9:
            stroka +=" ***  "
    if _offset>0:
        print(6*" "*_offset + stroka)
    else:
        print(stroka)
    """VTORAYA STROKA"""
    stroka = ""
    for i in str(_x):
        i = int(i)
        if i == 0:
            stroka +="*   * "
        elif i == 1:
            stroka +="  * * "
        elif i == 2:
            stroka +="    | "
        elif i == 3:
            stroka +="    | "
        elif i == 4:
            stroka +="*   * "
        elif i == 5:
            stroka +="|     "
        elif i == 6:
            stroka +="|     "
        elif i == 7:
            stroka +="    * "
        elif i == 8:
            stroka +="|   | "
        elif i == 9:
            stroka +="|   | "
    if _offset > 0:
        print(6*" "*_offset + stroka)
    else:
        print(stroka)
    """TRETYA STROKA"""
    stroka = ""
    for i in str(_x):
        i = int(i)
        if i == 0:
            stroka +="*   * "
        elif i == 1:
            stroka +="*   * "
        elif i == 2:
            stroka +=" ***  "
        elif i == 3:
            stroka +="****  "
        elif i == 4:
            stroka +=" **** "
        elif i == 5:
            stroka +=" ***  "
        elif i == 6:
            stroka +=" ***  "
        elif i == 7:
            stroka +="   *  "
        elif i == 8:
            stroka +=" ***  "
        elif i == 9:
            stroka +=" ***  "
    if _offset > 0:
        print(6*" "*_offset + stroka)
    else:
        print(stroka)
    """CHETVERTAYA STROKA"""
    stroka = ""
    for i in str(_x):
        i = int(i)
        if i == 0:
            stroka += "*   * "
        elif i == 1:
            stroka += "    * "
        elif i == 2:
            stroka += "|     "
        elif i == 3:
            stroka += "    | "
        elif i == 4:
            stroka += "    * "
        elif i == 5:
            stroka += "    | "
        elif i == 6:
            stroka += "|   | "
        elif i == 7:
            stroka += "  *   "
        elif i == 8:
            stroka += "|   | "
        elif i == 9:
            stroka += "    | "
    if _offset > 0:
        print(6*" "*_offset + stroka)
    else:
        print(stroka)
    """PYATAYA STROKA"""
    stroka = ""
    for i in str(_x):
        i = int(i)
        if i == 0:
            stroka += " ***  "
        elif i == 1:
            stroka += "    * "
        elif i == 2:
            stroka += " ***  "
        elif i == 3:
            stroka += "****  "
        elif i == 4:
            stroka += "    * "
        elif i == 5:
            stroka += " ***  "
        elif i == 6:
            stroka += " ***  "
        elif i == 7:
            stroka += "  *   "
        elif i == 8:
            stroka += " ***  "
        elif i == 9:
            stroka += "****  "
    if _offset > 0:
        print(6*" "*_offset + stroka)
    else:
        print(stroka)
def sand_clock(x):
    x = int(x)
    if (x%2==0):
        return "You should use odd digits!"
    s=0
    print()
    for i in range(x,0,-2):
        print(s * " ",end="")
        print(i*"*")
        s+=1
    s=int(x/2)-1
    for i in range(3,x+1,2):
        print(s * " ",end="")
        print(i*"*")
        s-=1
    print(f"\nSand clock of {x} characters has been built!")
    return ""
def calculate ():
    #Old version
    with open("settings.txt") as f:
        type = [a for a in f.read().split(",")][2]
    if type=="Old":
        firstDigit = _settings_user_Digit_Check("First digit:")
        secondDigit =_settings_user_Digit_Check("Second digit:")
        result = 0
        operation = _calc_check_operation("Enter operation: ")
    #New
    elif type == "New":
        expres = _calc_check_expression("Enter the expression: ")
        firstDigit,secondDigit,operation,result = int(expres[0]),int(expres[2]),expres[1],0
    if firstDigit < 0 or secondDigit < 0:
        return "Digits cant be negative!"
    try:
        if operation == "/":
            result = int(firstDigit/secondDigit)
    except ZeroDivisionError:
        return "Division on zero"
    if operation == "+":
        result = firstDigit+secondDigit
    elif operation == "-":
        result = firstDigit-secondDigit
    elif operation == "*":
        result = firstDigit * secondDigit
    if result<0:
        return "Negative result"
    if operation=="/" and firstDigit%secondDigit!=0:
        return "Not divided result"
    maxLen = max(len(str(result)), len(str(firstDigit)), len(str(secondDigit)))
    offset1 = maxLen-len(str(firstDigit))
    offset2 = maxLen - len(str(secondDigit))
    offsetRes = maxLen - len(str(result))
    if maxLen==1:
        print()
        tablo(firstDigit,offset1+1)
        print(operation)
        tablo(secondDigit,offset2+1)
        print("------"*(maxLen+1))
        tablo(result,offsetRes+1)
    else:
        print()
        tablo(firstDigit, offset1 )
        print(operation)
        tablo(secondDigit, offset2)
        print("------" * maxLen )
        tablo(result, offsetRes)
    return ""
def _calc_check_expression(promt=""):
    while True:
        try:
            user_input = input(promt)
            _list = [a for a in user_input.split(" ")]
            if (len(_list))!=3:
                print("Incorrect input")
                continue
            if user_input != "/" and user_input != "-" and user_input != "+"  and user_input != "*":
                print("Incorrect operation")
                continue
            fdig,secdig = int(_list[0]),int(_list[2])
            return _list
        except ValueError:
            print("Not a digit or incorrect syntax")
def _calc_check_operation(promt=""):
    while True:
        try:
            user_input = input(promt)
            if user_input.isdigit():
                print("Not operation")
                continue
            if user_input != "/" and user_input != "-" and user_input != "+"  and user_input != "*":
                print("Incorrect operation")
                continue
            return user_input
        except:
            pass
def example_solve(_mode,answers,_Timeout=10):
        #Default mode
        with open("settings.txt","r") as f:
            l = [a for a in f.read().split(",")]
            minDef,maxDef = int(l[4]),int(l[5])
        if _mode == "Def":
            if (is_permamently_using()):
                a,b = minDef,maxDef
            else:
                a,b = 2,20
            firstDigit = random.randint(a,b)
            secondDigit = random.randint(a,b)
            operations = ["+","-","*","/"]
            randOperation = operations[random.randint(0,3)]
            result = 0
            if randOperation == "+":
                result = firstDigit+secondDigit
            elif randOperation == "-":
                result=firstDigit-secondDigit
            elif randOperation == "*":
                firstDigit = random.randint(a, b)
                secondDigit = random.randint(a, b)
                result = firstDigit*secondDigit
            elif randOperation == "/":
                secondDigit = int(random.randint(a,b)/2)
                if secondDigit<a:
                    secondDigit=secondDigit*2
                firstDigit = (secondDigit * random.randint(2, int(b/secondDigit)))
                result = int(firstDigit/secondDigit)
            answers.append(result)
            maxLen = max(len(str(firstDigit)), len(str(secondDigit)))
            if len(str(firstDigit))==1 and len(str(secondDigit))==1 :
                print()
                tablo(firstDigit, 1 + max(len(str(firstDigit)), len(str(secondDigit))) - len(str(firstDigit)))
                print(randOperation)
                tablo(secondDigit, 1 + max(len(str(firstDigit)), len(str(secondDigit))) - len(str(secondDigit)))
                print("------" * (maxLen+1))
            else:
                print()
                tablo(firstDigit, max(len(str(firstDigit)), len(str(secondDigit))) - len(str(firstDigit)))
                print(randOperation)
                tablo(secondDigit, max(len(str(firstDigit)), len(str(secondDigit))) - len(str(secondDigit)))
                print("------" * maxLen)
            userResult = input()
            while True:
                try:
                    if int(userResult) == result:
                        return "Correct"
                    else:
                        return "Incorrect"
                except ValueError:
                    print("Incorrect input! Use Digits!")
                    userResult = input()



        #Time Limit Mode
        with open("settings.txt", "r") as f:
            l = [a for a in f.read().split(",")]
            minDef, maxDef = int(l[6]), int(l[7])
        if _mode == "TLim":
            if (is_permamently_using()):
                a, b = minDef, maxDef
            else:
                a, b = 1, 20
            firstDigit = random.randint(a, b)
            secondDigit = random.randint(a, b)
            operations = ["+", "-", "*","/"]
            randOperation = operations[random.randint(0, 3)]
            result = 0
            if randOperation == "+":
                result = firstDigit + secondDigit
            elif randOperation == "-":
                result = firstDigit - secondDigit
            elif randOperation == "*":
                firstDigit = random.randint(a, b)
                secondDigit = random.randint(a, b)
                result = firstDigit * secondDigit
            elif randOperation == "/":
                secondDigit = int(random.randint(a, b) / 2)
                if secondDigit < a:
                    secondDigit=secondDigit * 2
                firstDigit = (secondDigit * random.randint(2, int(b / secondDigit)))
                result = int(firstDigit / secondDigit)
            answers.append(result)
            maxLen = max(len(str(firstDigit)), len(str(secondDigit)))
            if len(str(firstDigit)) == 1 and len(str(secondDigit)) == 1:
                print()
                tablo(firstDigit, 1 + max(len(str(firstDigit)), len(str(secondDigit))) - len(str(firstDigit)))
                print(randOperation)
                tablo(secondDigit, 1 + max(len(str(firstDigit)), len(str(secondDigit))) - len(str(secondDigit)))
                print("------" * (maxLen+1))
            else:
                print()
                tablo(firstDigit, max(len(str(firstDigit)), len(str(secondDigit))) - len(str(firstDigit)))
                print(randOperation)
                tablo(secondDigit, max(len(str(firstDigit)), len(str(secondDigit))) - len(str(secondDigit)))
                print("------" * maxLen)

            print()
            t = Timer(_Timeout,print,"TimeOut, press Enter...")
            t.start()
            userResult = input()
            t.cancel()
            while True:
                try:
                    if userResult=="":
                        return "Incorrect"
                    if int(userResult) == result:
                        return "Correct"
                    else:
                        return "Incorrect"
                except ValueError:
                    print("Incorrect input! Use Digits!")
                    userResult = input()
def create_log():
    try:
        with open("Log.txt","x") as file:
            file.write(f"Start Log   {datetime.datetime.now()}\n")
            print("Log created!")
    except FileExistsError:
        pass
def show_log():
    my_file = open("Log.txt", "r")
    print(*my_file)
    my_file.close()
def write_log(_mode,_time,_Num_Of_Questions,_CorrectAnswers,_TimeToAnswer=""):
    my_file = open("Log.txt", "a+")
    my_file.write(f"\n{datetime.datetime.now()}\n"
                  f"Chosen mode: {_mode}\n"
                  f"Number of questions: {_Num_Of_Questions}\n"
                  f"Correct answers: {_CorrectAnswers}\n"
                  f"Your time: {_time:.2f}\n"
                  f"Overage time for each question: {int(_time)/int(_Num_Of_Questions)} \n")
    if _mode=="TLim":
        my_file.write(f"Time to answer: {_TimeToAnswer}\n")
    my_file.close()
def create_setting():
    default_setting = "10,10,Old,0,2,20,2,20"
    try:
        with open("settings.txt","x") as file:
            file.write(default_setting)
            print("Settings created!")
    except FileExistsError:
        with open("settings.txt","r+") as file:
            if len([a for a in file.read().split(",")])==1:
                file.write(default_setting)
                print("Program was closed incorrectly,settings switched to default")
def settings ():
    _file = open("settings.txt","r")
    _list = [a for a in _file.read().split(",")]
    setting_len = len(_list)
    if setting_len!=8:
        exit("The settings are entered incorrectly! Delete the file settings.txt and restart the program...")
    _NQ =_list[0]
    _Tlim=_list[1]
    _Calc = _list[2]
    _PermUsing = _list[3]
    _Min_Def,_Max_Def = _list[4],_list[5]
    _Min_TLim,_Max_TLim = _list[6],_list[7]
    _file.close()
    print(f"Current settings\n\n"
          f"Number of Questions: {_NQ}\n"
          f"TLimTime: {_Tlim}\n"
          f"Type of calculator: {_Calc}\n"
          f"Range of numbers for Def Exam?(min,max):{_Min_Def},{_Max_Def}\n"
          f"Range of numbers for TLim Exam?(min,max):{_Min_TLim},{_Max_TLim}\n"
          f"Is setting permamently using in Exam?:{_PermUsing}\n")
    _menu = input("Do you want change settings?(y/n):")
    print()
    if _menu == "y":
        try:
            with open("settings.txt","w") as file:
                user_Number_Questions = _settings_user_Digit_Check("Enter number of questions: ")
                user_TLim_Time = _settings_user_Digit_Check("Enter default time(for TLim mode): ")
                user_Calc_Enter = _settings_user_Calc_Enter("Type of calculator?(Old or New):")
                user_Min_Max_Def = _settings_user_min_max_check("Range of numbers for Def Exam?(min,max):")
                user_Min_Max_TLim = _settings_user_min_max_check("Range of numbers for Def Exam?(min,max):")
                user_Perm_Using = _setting_user_Perm_check("Permamently using(1 or 0):")
                file.write(f"{user_Number_Questions},{user_TLim_Time},{user_Calc_Enter},{user_Perm_Using},{user_Min_Max_Def},{user_Min_Max_TLim}")
                print("\nSettings updated!\n")
        except:
            pass
    _file = open("settings.txt", "r")
    _list = [a for a in _file.read().split(",")]
    if (len(_list)!=setting_len):
        exit("The settings are entered incorrectly! Delete the file settings.txt and restart the program...")
    _file.close()
def _settings_user_Digit_Check(promt=""):
    while True:
        try:
            user_input = int(input(promt))
            if user_input<0:
                print("Cant be less 0")
            else:
                return user_input
        except ValueError:
            print("Not a digit")
def _settings_user_Calc_Enter(promt=""):
    while True:
        user_input = input(promt)
        if user_input=="New":
            return "New"
        elif user_input=="Old":
            return "Old"
        else:
            print("Incorrect input")
def _settings_user_min_max_check(promt=""):
    while True:
        try:
            user_input = input(promt)
            l = [int(a) for a in user_input.split(",")]
            if len(l)!=2:
                print("Incorrect syntax")
                continue
            if l[0]<2 or l[1]<2:
                print("Digits cant be less 2")
                continue
            if l[0]>l[1]:
                print("min > max")
                continue
            else:
                return user_input
        except ValueError:
            print("Not a digits")
def _setting_user_Perm_check(promt=""):
    while True:
        try:
            user_input = int(input(promt))
            if user_input==1:
                return 1
            if user_input==0:
                return 0
            print("Can be only 1 or 0")
        except ValueError:
            print("Not a digit")
def is_permamently_using():
    with open("settings.txt") as f:
        l = int([a for a in f.read().split(",")][3])
    if l==1:
        return True
    if l==0:
        return False;
def help():
    print(f"\nAvailible commands\n"
          f"1.Tablo - 1/T\n"
          f"\tDisplaying digits\n"
          f"2.Sand Clock - 2/P\n"
          f"\tDisplaying sand clocks with user sizes\n"
          f"3.Calculate - 3/C:\n"
          f"\tAvailible operations: +,-,/,*\n"
          f"\tResult or digits CANT BE NEGATIVE\n"
          f"\tType of input in New Calculator: FirstDigit Operation SecondDigit\n"
          f"4.MathGame - 4/Ex/MG\n"
          f"\tAvailible operations: +,-,/,*\n"
          f"\tResult or digits CANT BE NEGATIVE\n"
          f"5.ShowLog - 5/SS\n"
          f"\tDisplaying information about previous MathGames\n"
          f"6.Settings - 6/Set\n"
          f"\tChanging different values for MathGame and Calc\n"
          f"7.Help - 7/H/Help\n"
          f"0.Exit - 0/Exit\n")

"""                 MAIN                 """

def main():
    create_log()
    create_setting()
    isTrue = True
    print(f"Menu\n1.Tablo\n2.Sand Clock\n3.Calculate\n4.MathGame\n5.ShowLog\n6.Settings\n7.Help\n0.Exit\n")
    while isTrue:
        menu = input("Enter command: ")
        if menu=='T' or menu=="1":
            x = input("Write any digit: ")
            if x.isdigit():
                print()
                tablo(x)
            else:
                print("Not digit!")
        elif menu == "P" or menu=="2":
            x = input("Write any odd digit: ")
            if x.isdigit():
                print(sand_clock(x))
            else:
                print("Not digit!")
        elif menu == "C" or menu=="3":
            print(calculate())
        elif menu == "Ex" or menu=="4" or menu=="MG":
            answers = []
            incAnsw = []
            CorAnsw = 0
            mode = input("Which mode of exam?(TLim/Def): ")
            if is_permamently_using()==False:# Если мы не используем настройки по умолчанию
                Setting = input("Do you want to use setting?(y/n): ")
                if Setting == "y":
                    file = open("settings.txt","r")
                    NumOfQuest = [a for a in file.read().split(",")][0]
                    file.close()
                else:
                    NumOfQuest = _settings_user_Digit_Check("Number of questions?: ")
            else: # Если мы Используем настройки по умолчанию
                file = open("settings.txt","r")
                NumOfQuest = [a for a in file.read().split(",")][0]
                file.close()
            if mode == "Def":
                print()
                start_time = time.time()
                for i in range(0, int(NumOfQuest)):
                    if (example_solve(mode,answers) == "Correct"):
                        CorAnsw += 1
                    else:
                        incAnsw.append(i + 1)
                total_time = time.time()-start_time
                write_log(_mode=mode,_time=total_time,_Num_Of_Questions=NumOfQuest,_CorrectAnswers=CorAnsw)
                print(f"Your time is {total_time:.2f}")
                print(f"You answered correctly on: {CorAnsw}/{NumOfQuest}!",end="")
                tempMenu = input(" Show correct answers?(Y/y to show): ")
                if (tempMenu.lower() == 'y'):
                    print("Correct answers: ",end="")
                    print(", ".join(map(str,answers)))
                    if len(incAnsw)>0:
                        print(f"Numbers of incorrect answers: {", ".join(map(str,incAnsw))}")
                    else:
                        print(f"Good work!")
                    answers.clear()
            elif mode == "TLim":
                if is_permamently_using() == False:
                    if Setting == "y":
                        file = open("settings.txt", "r")
                        TimeToAnswer = [a for a in file.read().split(",")][1]
                        file.close()
                    else:
                        TimeToAnswer = input("Time to answer?: ")
                        print()
                else:
                    file = open("settings.txt", "r")
                    TimeToAnswer = [a for a in file.read().split(",")][1]
                    file.close()
                """if TimeToAnswer=="":
                    start_time = time.time()
                    for i in range(0, int(NumOfQuest)):
                        if (example_solve(mode) == "Correct"):
                            CorAnsw += 1
                        else:
                            incAnsw.append(i+1)
                    total_time = time.time()-start_time
                    write_log(_mode=mode, _time=total_time, _Num_Of_Questions=NumOfQuest, _CorrectAnswers=CorAnsw,_TimeToAnswer=TimeToAnswer)
                    print(f"You answered correctly on: {CorAnsw}/{NumOfQuest}! ",end="")
                    tempMenu = input("Show correct answers?(Y/y to show) ")
                    if (tempMenu.lower() == 'y'):
                        print("Correct answers: ", end="")
                        print(", ".join(map(str,answers)))
                        if len(incAnsw) > 0:
                            print(f"Numbers of incorrect answers: {", ".join(map(str,incAnsw))}")
                        else:
                            print(f"Good work!")
                        answers.clear()"""
                #else:
                start_time = time.time()
                for i in range(0,int(NumOfQuest)):
                    if(example_solve(mode,answers,int(TimeToAnswer))=="Correct"):
                        CorAnsw+=1
                    else:
                        incAnsw.append(i+1)
                total_time = time.time() - start_time
                write_log(_mode=mode, _time=total_time, _Num_Of_Questions=NumOfQuest, _CorrectAnswers=CorAnsw,_TimeToAnswer=TimeToAnswer)
                print(f"Your time is {total_time:.2f}")
                print(f"You answered correctly on: {CorAnsw}/{NumOfQuest}!",end="")
                tempMenu = input(" Show correct answers?(Y/y to show) ")
                if (tempMenu.lower() == 'y'):
                    print("Correct answers: ", end="")
                    print(", ".join(map(str,answers)))
                    if len(incAnsw) > 0:
                        print(f"Numbers of incorrect answers: {", ".join(map(str,incAnsw))}")
                    else:
                        print(f"Good work!")
                    answers.clear()
            else:
                print(f"Wrong mode or number!")
        elif menu=="SS" or menu=="5":
            show_log()
        elif menu=="Set" or menu== "6":
            settings()
        elif menu == "H" or menu=="7" or menu=="Help":
            help()
        elif menu=="0" or menu=="Exit":
            menu = input("You sure you want to close program?(Y/y to close): ")
            if (menu.lower() == 'y'):
                isTrue = False
        else:
            print(f"No such command: '{menu}'! To check commands enter 'Help'")
            """menu = input("Do you want to continue?(Y/y to continue): ")
            if (menu.lower()!='y'):
                isTrue=False"""

main()
input ("Press Enter to close...")
