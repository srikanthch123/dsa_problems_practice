## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)


# https://www.codingninjas.com/studio/problems/sum-of-even-odd_624650?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

def even_odd(n):
    str_num=str(n)
    even_sum=0
    odd_sum =0
    for i in str_num:
        int_num=int(i)
        if int_num %2 ==0:
            even_sum += int_num
        else:
            odd_sum += int_num
    return even_sum,odd_sum

num=int(input())
a,b=even_odd(num)  
print(a,b)