import tkinter as tk

class Dentaku():
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.current_number = 0
        self.operation = "+"

    def do_eq(self):
        "= キーが押された時の計算動作、第二項の設定、四則演算の実施、入力中の数字のクリア"
        self.second_term = self.current_number
        if self.operation == "+":
            self.result = self.first_term + self.second_term
        elif self.operation == "-":
            self.result = self.first_term - self.second_term
        elif self.operation == "×":
            self.result = self.first_term * self.second_term
        elif self.operation =="÷":
            self.result = self.first_term // self.second_term

dentaku = Dentaku()

# 数字キーを一括処理する関数
def key(n):
    dentaku.current_number = dentaku.current_number * 10 + n
    show_number(dentaku.current_number)

def clear():
    dentaku.current_number = 0
    show_number(dentaku.current_number)

def plus():
    dentaku.operation = "+"
    dentaku.first_term = dentaku.current_number
    dentaku.current_number = 0
    show_number(dentaku.current_number)

def minus():
    dentaku.operation = "-"
    dentaku.first_term = dentaku.current_number
    dentaku.current_number = 0
    show_number(dentaku.current_number)

def times():
    dentaku.operation = "×"
    dentaku.first_term = dentaku.current_number
    dentaku.current_number = 0
    show_number(dentaku.current_number)

def divided():
    dentaku.operation = "÷"
    dentaku.first_term = dentaku.current_number
    dentaku.current_number = 0
    show_number(dentaku.current_number)

def eq():
    dentaku.do_eq()
    show_number(dentaku.result)

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
b1.configure(width=2,bg = '#ffffff',font=('Helvetica', 14))

b2 = tk.Button(f,text='2', command=lambda:key(2))
b2.configure(width=2,bg = '#ffffff',font=('Helvetica', 14))

b3 = tk.Button(f,text='3', command=lambda:key(3))
b3.configure(width=2,bg = '#ffffff',font=('Helvetica', 14))

b4 = tk.Button(f,text='4', command=lambda:key(4))
b4.configure(width=2,bg = '#ffffff',font=('Helvetica', 14))

b5 = tk.Button(f,text='5', command=lambda:key(5))
b5.configure(width=2,bg = '#ffffff',font=('Helvetica', 14))

b6 = tk.Button(f,text='6', command=lambda:key(6))
b6.configure(width=2,bg = '#ffffff',font=('Helvetica', 14))

b7 = tk.Button(f,text='7', command=lambda:key(7))
b7.configure(width=2,bg = '#ffffff',font=('Helvetica', 14))

b8 = tk.Button(f,text='8', command=lambda:key(8))
b8.configure(width=2,bg = '#ffffff',font=('Helvetica', 14))

b9 = tk.Button(f,text='9', command=lambda:key(9))
b9.configure(width=2,bg = '#ffffff',font=('Helvetica', 14))

b0 = tk.Button(f,text='0', command=lambda:key(0))
b0.configure(width=2,bg = '#ffffff',font=('Helvetica', 14))

bc = tk.Button(f,text='C', command=clear)
bc.configure(width=2,bg = '#ff0000',font=('Helvetica', 14))

bp = tk.Button(f,text='+', command=plus)
bp.configure(width=2,bg = '#00ff00',font=('Helvetica', 14))

bm = tk.Button(f,text='-', command=minus)
bm.configure(width=2,bg = '#00ff00',font=('Helvetica', 14))

bt = tk.Button(f,text='×', command=times)
bt.configure(width=2,bg = '#00ff00',font=('Helvetica', 14))

bd = tk.Button(f,text='÷', command=divided)
bd.configure(width=2,bg = '#00ff00',font=('Helvetica', 14))

be = tk.Button(f,text='=', command=eq)
be.configure(width=2,bg = '#00ff00',font=('Helvetica', 14))

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
e.configure(font=('Helvetica', 14))
e.grid(row=0,column=0,columnspan=4)
clear()

# ここから GUI がスタート
root.mainloop()