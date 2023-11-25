import tkinter as tk

#計算機能のための変数とイベント用の関数定義

# 2項演算のモデル
# 入力中の数字
current_number = 0
# 第一項
first_term = 0
# 第二項
second_term = 0
# 結果
result = 0

operation = 0

def do_plus():
    "+ キーが押されたときの計算動作、第一項の設定と入力中の数字のクリア"
    global current_number
    global first_term
    global operation

    first_term = current_number
    current_number = 0
    operation = 1

def do_minus():
    global current_number
    global first_term
    global operation

    first_term = current_number
    current_number = 0
    operation = 2

def do_times():
    global current_number
    global first_term
    global operation

    first_term = current_number
    current_number = 0
    operation = 3

def do_divided():
    global current_number
    global first_term
    global operation

    first_term = current_number
    current_number = 0
    operation = 4

def do_eq():
    "= キーが押された時の計算動作、第二項の設定、加算の実施、入力中の数字のクリア"
    global second_term
    global result
    global current_number
    second_term = current_number
    if operation == 1:
        result = first_term + second_term
    elif operation == 2:
        result = first_term - second_term
    elif operation == 3:
        result = first_term * second_term
    else:
        if second_term != 0:
                result = first_term / second_term
        else:
            result = 'error'
    current_number = 0

# 数字キーを一括処理する関数
def key(n):
    global current_number
    current_number = current_number * 10 + n
    show_number(current_number)

def clear():
    global current_number
    current_number = 0
    show_number(current_number)

def plus():
    do_plus()
    show_number(current_number)

def minus():
    do_minus()
    show_number(current_number)

def times():
    do_times()
    show_number(current_number)

def divided():
    do_divided()
    show_number(current_number)

def eq():
    do_eq()
    show_number(result)

def show_number(num):
    e.delete(0,tk.END)
    e.insert(0,str(num))

# tkinter での画面の構成

root = tk.Tk()
f = tk.Frame(root)
f.configure(bg = '#ffffc0')
f.grid()

#ウィジェットの作成

b1 = tk.Button(f,text='1', command=lambda:key(1))
b1.configure(width=2)
b1.configure(bg = '#ffffff')
b1.configure(font=('Helvetica', 14))

b2 = tk.Button(f,text='2', command=lambda:key(2))
b2.configure(width=2)
b2.configure(bg = '#ffffff')
b2.configure(font=('Helvetica', 14))

b3 = tk.Button(f,text='3', command=lambda:key(3))
b3.configure(width=2)
b3.configure(bg = '#ffffff')
b3.configure(font=('Helvetica', 14))

b4 = tk.Button(f,text='4', command=lambda:key(4))
b4.configure(width=2)
b4.configure(bg = '#ffffff')
b4.configure(font=('Helvetica', 14))

b5 = tk.Button(f,text='5', command=lambda:key(5))
b5.configure(width=2)
b5.configure(bg = '#ffffff')
b5.configure(font=('Helvetica', 14))

b6 = tk.Button(f,text='6', command=lambda:key(6))
b6.configure(width=2)
b6.configure(bg = '#ffffff')
b6.configure(font=('Helvetica', 14))

b7 = tk.Button(f,text='7', command=lambda:key(7))
b7.configure(width=2)
b7.configure(bg = '#ffffff')
b7.configure(font=('Helvetica', 14))

b8 = tk.Button(f,text='8', command=lambda:key(8))
b8.configure(width=2)
b8.configure(bg = '#ffffff')
b8.configure(font=('Helvetica', 14))

b9 = tk.Button(f,text='9', command=lambda:key(9))
b9.configure(width=2)
b9.configure(bg = '#ffffff')
b9.configure(font=('Helvetica', 14))

b0 = tk.Button(f,text='0', command=lambda:key(0))
b0.configure(width=2)
b0.configure(bg = '#ffffff')
b0.configure(font=('Helvetica', 14))

bc = tk.Button(f,text='C', command=clear)
bc.configure(width=2)
bc.configure(bg = '#ff0000')
bc.configure(font=('Helvetica', 14))

bp = tk.Button(f,text='+', command=plus)
bp.configure(width=2)
bp.configure(bg = '#00ff00')
bp.configure(font=('Helvetica', 14))

bm = tk.Button(f,text='-', command=minus)
bm.configure(width=2)
bm.configure(bg = '#00ff00')
bm.configure(font=('Helvetica', 14))

bt = tk.Button(f,text='×', command=times)
bt.configure(width=2)
bt.configure(bg = '#00ff00')
bt.configure(font=('Helvetica', 14))

bd = tk.Button(f,text='÷', command=divided)
bd.configure(width=2)
bd.configure(bg = '#00ff00')
bd.configure(font=('Helvetica', 14))

be = tk.Button(f,text='=', command=eq)
be.configure(width=2)
be.configure(bg = '#00ff00')
be.configure(font=('Helvetica', 14))

#Grid 型ジオメトリマネージャによるウィジェットの割付

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
bc.grid(row=1,column=3)
be.grid(row=4,column=3)
bp.grid(row=2,column=3)
bm.grid(row=3,column=3)
bt.grid(row=4,column=1)
bd.grid(row=4,column=2)

# 数値を表示するウィジェット
e = tk.Entry(f)
e.grid(row=0,column=0,columnspan=4)
clear()

# ここから GUI がスタート
root.mainloop()