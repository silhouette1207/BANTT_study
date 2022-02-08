from colorsys import TWO_THIRD
from numpy import ones

number = {
        0 : "zero",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine"
    }
def solution(s):
    
    answer = 0
    
    print(len(s))
    while len(s)>0:

        if s[0].isdigit() == True:
            answer = answer*10 + int(s[0])
            s= s[1:]
            
        else:
            if s[0] == "z":
                answer = answer*10
                s = s[4:]
            elif s[0] == "o":
                answer = answer*10 + 1
                s= s[3:]
            elif s[0] == "t":
                if s[1] == "w":
                    answer = answer* 10 +2
                    s= s[3:]
                elif s[1] == "h":
                    answer = answer * 10 +3
                    s= s[5:]
            elif s[0] == "f":
                if s[1]== "o":
                    answer = answer *10 +4
                    s = s[4:]
                elif s[1] == "i":
                    answer = answer * 10 +5
                    s = s[4:]
            elif s[0] == "s":
                if s[1]=="i":
                    answer = answer *10 +6
                    s= s[3:]
                elif s[1] == "e":
                    answer = answer * 10 +7
                    s= s[5:]
            elif s[0]== "e":
                answer = answer *10 +8
                s= s[5:]
            elif s[0] == "n":
                answer = answer * 10 +9
                s = s[4:]
    
    return answer


s = "one4seveneight"

print(solution(s))