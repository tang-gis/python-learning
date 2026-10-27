weight=float(input("请输入体重（公斤）："))
height=float(input("请输入身高（米）："))
name="黎明"
age=21
is_adult=age>=18
bmi=weight/(height*height)
print(f"{name}的年龄是{age}，bmi是{bmi:.1f}，是否成年：{is_adult}")