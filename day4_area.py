line = "  地块面积：12.5 公顷  "
clean=line.strip()
num_str=clean.replace("地块面积：","").replace("公顷","").strip()
area=float(num_str)
mu=area*15
print(line)
print(f"地块面积是{area:.2f}，合算{mu:.1f}亩")