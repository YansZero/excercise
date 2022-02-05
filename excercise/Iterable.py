# 下列稱為Iterable 可疊代的資料型態
# 意指 可以將內部資料 逐一取出
# string   
# List    []
# Set     {}
# dictionary [key:value,key2:value2]

# 方式會使用 
# for 迴圈
# for 變數名稱 in 可疊代的資料:
# for x in 'abc':
#     print(x)

# for y in [3,5,2]:
#     print(y)


# for z in {1,"2t","5",3,4,"我我我"}:
#     print(z)

# 用在dictionary 則是取KEY出來
# 要取值要額外處理一下
# dic={"a":3,"b":5}
# for aa in dic:
#     print(aa)
#     print(dic[aa])

# 內建函式
# 回傳最大值: max(可疊代的資料)
# result=max([1,8,30,5,99,0])
# print(result)

# result=max("azbX") #照ASCII CODE去排
# print(result)

# result=max({10,30,300,1})
# print(result)

# result=max({"x":10,"a":50}) # 用在dictionary 則是取KEY出來 KEY找最大
# print(result)

# 進行資料排序:sorted(可疊代的資料) 小排前 大排後
#回傳一定是一個LIST形式
result=sorted("azbX") #照ASCII CODE去排
print(result)  #結果['X', 'a', 'b', 'z']

result=sorted([1,8,30,5,99,-2])
print(result)  #結果[-2, 1, 5, 8, 30, 99]

result=sorted({10,-30,200,99})
print(result) #結果[-30, 10, 99, 200]

result=sorted({"x":10,"a":50}) # 用在dictionary 則是取KEY出來 再排序
print(result) #結果['a', 'x']
