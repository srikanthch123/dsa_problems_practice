#https://www.codingninjas.com/studio/problems/find-character-case_58513?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
def check_alphabet(char):
    if char.isupper():
        output=1 
    elif char.islower():
        output=0
    else:
        output=-1
    return output   
    
char=input()
res=check_alphabet(char)
print(res)    