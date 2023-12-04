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

def do_plus():
    "+ キーが押されたときの計算動作、第一項の設定と入力中の数字のクリア"
    global current_number
    global first_term
    
    first_term = current_number
    current_number = 0

def do_eq():
    "= キーが押された時の計算動作、第二項の設定、加算の実施、入力中の数字のクリア"
    global second_term
    global result
    global current_number
    second_term = current_number
    result = first_term + second_term
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

def eq():
    do_eq()
    show_number(result)

def show_number(num):
    e.delete(0,tk.END)
    e.insert(0,str(num))

# tkinter での画面の構成

root = tk.Tk()
f = tk.Frame(root)
f.grid()

#ウィジェットの作成
Buttons = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
]

for i, j in enumerate(Buttons):
    for k, t in enumerate(j):
        tk.Button(f,text=t,command=lambda x = t:key(x)).grid(row=i+1,column=k)

tk.Button(f,text='0', command=lambda:key(0)).grid(row=4,column=0)
tk.Button(f,text='C', command=clear).grid(row=1,column=3)
tk.Button(f,text='+', command=plus).grid(row=2,column=3)
tk.Button(f,text='=', command=eq).grid(row=4,column=3)

# 数値を表示するウィジェット
e = tk.Entry(f)
e.grid(row=0,column=0,columnspan=4)
clear()

# ここから GUI がスタート
root.mainloop()