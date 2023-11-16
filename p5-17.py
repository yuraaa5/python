while True:
    x = input("平方根を求める数値を入力")
    try:
        x = float(x)
    except ValueError:
        if x == "end":
            exit()
        print(x, "は数値に変換できない")
        continue
    except:
        print("予期していないエラー")
        exit()
    if x <= 0:
        print(x, "は正の数値ではない")
        continue

    rnew = x
    diff = rnew - x/rnew
    if diff < 0:
        diff = abs(diff)
    while (diff > 1.0E-6):
        r1 = rnew
        r2 = x/r1
        rnew =  (r1 + r2)/2
        print(r1, rnew, r2)
        diff = r1 - r2
        if diff < 0:
            diff = abs(diff)
