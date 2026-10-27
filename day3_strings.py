s = "水土保持监测报告"
print(s[0])      # 水      ← 第0个
print(s[3])      # 保      ← 第3个
print(s[-1])     # 告      ← 倒数第1个（负号=从后往前数）
print(s[0:4])    # 水土保持  ← 切片：从第0个切到第4个（不含4）
print(len(s))    # 8       ← len()数长度

a = "  SPD-2026-003  "
print(a.strip())                              # 去掉首尾空格：SPD-2026-003
print(a.strip().split("-"))                     # 按横线拆开：['SPD', '2026', '003'] 
print("SPD".lower())                          # 转小写
print("坡耕地".replace("坡","梯"))             # 替换：梯耕地
print("监测报告中监测点共3处".count("监测"))    # 数出现次数：2
      
plot_id=7
coverage=83.3695
level="良好"
print(f"第{plot_id}地块植被覆盖度为{coverage:.1f}%，评价等级为{level}")