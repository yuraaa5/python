'''
#p5-1
# x の平方根を求める
x = 2
#
rnew = x
#
for i in range(10):
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
'''
'''
#p5-2
# x の平方根を求める
x = 2
#
rnew = x
#
for i in range(1000):
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
print(r1, rnew, r2)
'''
'''
#p5-3
for i in range(10):
    if i == 1:
        continue
    if i == 8:
        break
    print(i)
'''
'''
#p5-4
sum = 0
for i in range(10):
    sum+=i
    print(sum)
'''
'''
#p5-5
for i in range(3):
    for j in range(3):
        print(i, j)
'''
'''
#p5-6
x = 2
rnew = x
diff = rnew - x/rnew
if diff < 0:
    diff = -diff
while (diff > 1.0E-6):
    r1 = rnew
    r2 = x/r1
    rnew =  (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 - r2
    if diff < 0:
        diff = -diff
'''
'''
#p5-7
x = 2
rnew = x
while True:
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 - r2
    if diff < 0:
        diff = -diff
    if diff <= 1.0E-6:
        break
'''
'''
#p5-8
a = 1
b = 0
if (a == 1) and (b == 0):
    print("YES a==1 and b == 0")
'''
'''
#p5-9
a = 1
b = 0
if a ==1:
    if b == 0:
        print("YES a==1 and b == 0")
'''
#p5-10
while True:
    x = input("正の数値を入力")
    try:
        x = float(x)
    except ValueError:
        print(x, "は数値に変換できない")
        continue
    except:
        print("予期していないエラー")
        exit()
    if x <= 0:
        print(x, "は正の数値ではない")
        continue
#以下は正しい入力の場合の処理
    print(x)