import random

first_reward = "100r"
second_reward = "60r"
thrid_reward = "40r"
fourth_reward = "20r"
fifth_reward = "10r"
sixth_reward = "5r"


final_red = random.sample(range(1,34,1),6)#生成最终中奖红球号码
final_blue = random.sample(range(1,17,1),1)#生成最终中奖蓝球号码
final_ball = final_red + final_blue#生成最终中奖号码


while True:
    r=input("请输入你要选择的红球号码(1-33不重复且用空格隔开）:")
    # 检查是否是6个数字
    numbers = r.split()
    if len(numbers) != 6:
        print("请输入6个数字！")
        continue
    # 检查是否都是数字
    all_digits = True
    for num in numbers:
        if not num.isdigit():
            print("请输入数字！")
            all_digits = False
            break
        int_num = int(num)
        if int_num <1 or int_num>33:
            print("请注意范围")
            all_digits = False
            break
    if not all_digits:
        continue
    num_list = [int(num) for num in numbers]  # 先转换成数字
    if len(num_list) != len(set(num_list)):
        print("数字不能重复！")
        continue
    else:
        break

while True:
    b=input("请输入你要选择的蓝球号码（1-16）:")
    if not b.isdigit():
        print("请输入数字！")
        continue
    if int(b) < 1 or int(b) >16:
        print("请输入1-16之间的数字！")
        continue
    else:
        break

R=[int(num) for num in r.split()]#把r中数字按空格划分形成一个字符串的列表并把列表中的数字从字符串转化成整数形式
B=int(b)#把b中数字化为整形
A=R+[B]#赋值最终中奖号码


print("你选择的号码为：",A)

print("中奖号码是：",final_ball)#打印最终中奖号码


#打印各色球匹配个数
s_final_red=set(final_red)
s_final_blue=set(final_blue)
s_R=set(R)
s_B={B}
print("红球匹配个数:",len(s_final_red & s_R))
print("蓝球匹配个数:",len(s_final_blue & s_B))
m = len(s_final_red & s_R)
n = len(s_final_blue & s_B)
if m==6 and n==1 :
    print("恭喜您中了一等奖！奖金为：",first_reward)
elif m==6 and n==0 :
    print("恭喜您中了二等奖！奖金为：",second_reward)
elif m==5 and n==1 :
    print("恭喜您中了三等奖！奖金为：",thrid_reward)
elif m==5 and n==0 or m==4 and n==1 :
    print("恭喜您中了四等奖！奖金为：",fourth_reward)
elif m==4 and n==0 or m==3 and n==1 :
    print("恭喜您中了五等奖！奖金为：",fifth_reward)
elif m==2 and n==1 or m==1 and n==1 or m==0 and n==1 :
    print("恭喜您中了六等奖！奖金为：",sixth_reward)
else:
    print("很遗憾您未中奖，继续加油！")
            
                
                









        
