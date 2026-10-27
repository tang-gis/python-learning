coverage=float(input("请输入植被覆盖度(%)："))
if coverage>=80:
    level="优"
elif coverage>=60:
    level="良"
elif coverage>=40:
    level="中"
else:
    level="差"
print(f"植被覆盖度{coverage:.1f}%，水平等级:{level}")