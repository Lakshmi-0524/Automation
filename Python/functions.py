from itertools import combinations

def func_01(name="friend"):
    print("Hello "+name)

func_01("Lakshmi") #Hello Lakshmi
func_01() #Hello friend

def add_num():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=int(input("Enter c: "))
    sum=a + b + c
    print("Sum=", sum)
add_num()

def mul_num(a,b):
    prod1=int(a)*int(b)  
    prod2=a*b
    print("product_int=",prod1) #product= 6
    print("product=",prod2) #product= 7.0

mul_num(2,3.5) 
mul_num(4,"Hi") #ValueError

#python code to append list items separately that make equal sum from input list [1,2,3,4]
def split_equal_sum(in_lst):
    n=len(in_lst)

    result=[]
    total_sum=sum(in_lst)
    target=total_sum//2

    if total_sum%2 !=0:
        print("equal partitioning is not possible")
    
    else:
        for i in range(1,n):
            for subset in combinations(in_lst,i):
                if sum(subset)==target:
                    subset_01=list(subset)
                    subset_02=in_lst.copy()
                    for i in subset_01:
                        subset_02.remove(i)
                    result.append(subset_01)
                    result.append(subset_02)
                    return result
        
in_lst=[2,4,6,8]
subsets=split_equal_sum(in_lst)
print(subsets) #output:[[2, 8], [4, 6]]
