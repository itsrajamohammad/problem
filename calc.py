#lib for spl split func
import re
#to get user input
user_input=input("Enter your values:")
num=re.split('(\+|/|-|\*)',user_input) 
    
#to separate operators 
oper=[] 
for i in range(len(num)):
    if num[i]=='+'or num[i]=='/'or num[i]=='*'or num[i]=='-':
        oper.append(num[i])
        
#to separate int values
value=[]
value=re.split('[+/\-\*]',user_input)
        
#define func to perfrom arthimetic operations using list of oper & val       
def arthmetic_func(sign):
    while sign in oper:
        for i in range(len(oper)):
            
            if oper[i]==sign:
                a=float(value[i])
                b=float(value[i+1])
                if sign=='/':
                    ans=a/b
                if sign=='*':
                    ans=a*b
                if sign=='+':
                    ans=a+b
                if sign=='-':
                    #assign sign and add elements to list for avoid precedence error
                    ans=a
                    value[i+1]=-b
                    value.insert(i,'dummy')
                    oper.insert(i+1,'+')
                oper.pop(i)
                oper.append('end')
                value.pop(i)
                value.pop(i)
                value.insert(i,ans)
    
while oper[0]!='end':
    arthmetic_func('/')
    arthmetic_func('*')
    arthmetic_func('-')
    arthmetic_func('+')
            
print(value[0])

                  