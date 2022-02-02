# break 範例
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n)
#     n+=1
# print("最後的N: ",n)    

# continue 範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     n+=1
#     print(n)

# else範例    
# while + else範例    
# while 跑完後 會再跑else一次
# n=0
# while n<5:
#     print(n)
#     n+=1
# else:    
#     print("最後的N: ",n)   

# for + else範例    
# for 跑完後 會再跑else一次
# sum=0
# for x in range(11):
#     sum += x
# else:    
#     print("最後的sum: ",sum)   

#綜合範例: 找出整數平方根 
n1 = int(input("請輸入要找平方根的整數: "))

for x in range(n1):
    if (x*x==n1):
        print("有整數平方根:",x)
        break
else:
    print("沒有整數平方根")