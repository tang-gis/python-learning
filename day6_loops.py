# 外业核查任务：逐个图斑点名，最后汇总（for 遍历列表）
plots=["GT-001","GT-002","GT-003","GT-004"]    # 图斑编号列表
for code in plots:                             # 对plots里面的每个编号依次取名为code
    print(f"正在核查图斑{code}:外业拍照→ 内页比对")
print(f"本轮巡查完成，共{len(plots)}个图斑")     # 循环结束后执行（顶格）

# 遥感影像某一行的 10 个 NDVI 像元值（-1~1，越高植被越好）
ndvi_row = [0.72, 0.45, 0.88, 0.31, 0.65, 0.52, 0.90, 0.38, 0.61, 0.77]
# 第一步：累加器求和、计数
total = 0        # 累加器先归零（必须写在循环外面）
count = 0        # 计数器同样归零
for v in ndvi_row:
    total += v   # 每圈把当前像元值加进累加器
    count += 1   # 每圈计 1 个
avg = total / count
print(f"该行共 {count} 个像元，NDVI 均值 {avg:.2f}")
# 第二步：循环套条件，数出植被稀疏的像元（NDVI < 0.4）
low=1   #归零只做一次：写在循环外 = 循环开始前归一次零
for v in ndvi_row:
    if v < 0.4:          # Day 5 的 if 搬进循环：逐个筛查
        low += 1
        print(f"发现稀疏像元：{v}")
print(f"植被稀疏像元（NDVI<0.4）共 {low} 个")

# 给 1~20 号监测桩自动生成编号牌，7 号之后每 3 个抽检一次
for i in range(1, 21):            # 含头不含尾：产生 1~20，没有 21
  tag = f"JC-{i:02d}"     
if i > 7 and i % 3 == 0:          # 编号大于 7 且能被 3 整除 → 抽检
     print(f"{tag} → 抽检桩")
else:
    print(f"{tag} → 常规桩")

# 某小流域年土壤侵蚀模数 50（t/km²·a，示例值），
# 每年治理后降为原来的 70%，降到 10 以下算达标——要几年？
erosion = 50.0
year = 0
while erosion > 10:              # 条件成立就一直转
    year += 1                    # 年数 +1
    erosion = erosion * 0.7      # 每年降 30%（这行改变条件，删掉就是死循环）
    print(f"第 {year} 年，侵蚀模数降至 {erosion:.1f}")
print(f"治理约 {year} 年后降到轻度以下")