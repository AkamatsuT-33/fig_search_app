#### インポート ####
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as f
from tkinter import filedialog
from os.path import expanduser
from os import makedirs
import random
from tkinter import messagebox
import sqlite3
import datetime as dt

#### 関数
# 難易度選択画面を表示させる
def up_frame_select():
    frame_select.tkraise()

# トップ画面を表示させる
def up_frame_top():
    frame_top.tkraise()

# 難易度イージーの画面を表示させる
def up_frame_difficlt_check_easy():
    global c_fig, game_btn1
    game_btn1 = ttk.Button(frame_game, text='submit', command= lambda:win_or_lose_easy(game_entry1, c_fig))
    game_btn1.grid(row=3, column=0, pady=5)
    c_fig = int(random.randint(0,9))
    frame_game.tkraise()

# 難易度ノーマルの画面を表示させる
def up_frame_difficlt_check_normal():
    global c_fig, game_btn1
    game_btn1 = ttk.Button(frame_game, text='submit', command= lambda:win_or_lose_normal(game_entry1, c_fig))
    game_btn1.grid(row=3, column=0, pady=5)
    c_fig = int(random.randint(0,9))
    frame_game.tkraise()

# 難易度ハードの画面を表示させる
def up_frame_difficlt_check_hard():
    global game_btn1
    game_btn1 = ttk.Button(frame_game, text='submit', command= lambda:win_or_lose_hard(game_entry1, c_fig))
    game_btn1.grid(row=3, column=0, pady=5)
    frame_game.tkraise()

# ルール選択画面を表示させる
def up_frame_rule():
    frame_rule.tkraise()

# 難易度イージーのルール画面を表示させる
def up_frame_rule_easy():
    frame_rule_easy.tkraise()

# 難易度ノーマルのルール画面を表示させる
def up_frame_rule_normal():
    frame_rule_normal.tkraise()

# 難易度ハードのルール画面を表示させる
def up_frame_rule_hard():
    frame_rule_hard.tkraise()

# エラー画面表示
def up_frame_error():
    frame_error.tkraise()

# 難易度イージーの勝敗をチェック
def win_or_lose_easy(game_entry1, c_fig):
    global repeat_check, memories_check
    try:
        p_fig = int(game_entry1.get())

        if p_fig in [1,2,3,4,5,6,7,8,9,0]:
            if c_fig == p_fig:
                repeat_check[0] += 1
                if (memories_check[0] > repeat_check[0]) or (memories_check[0] == 0):
                    memories_check[0] = repeat_check[0]
                else:
                    pass
                messagebox.showinfo('当たり', 'あたりです。おめでとう!あなたは' + str(repeat_check[0]) + '回で当たりました。')
                print(repeat_check, memories_check)
                repeat_check[0] = 0
                up_frame_top()
            else:
                if c_fig > p_fig:
                    repeat_check[0] += 1
                    messagebox.showinfo('はずれ', "ヒント\nコンピュータの数字の方が大きいです。")
                elif c_fig < p_fig:
                    repeat_check[0] += 1
                    messagebox.showinfo('はずれ', "ヒント\nコンピュータの数字の方が小さいです。")
                else:
                    pass
        else:
            up_frame_error()
    except:
        up_frame_error()
    
    #p_fig = int(game_entry1.get())
    print(p_fig, c_fig)



# 難易度ノーマルの勝敗をチェック
def win_or_lose_normal(game_entry1, c_fig):
    global repeat_check, memories_check

    try:
        p_fig = int(game_entry1.get())

        if p_fig in [1,2,3,4,5,6,7,8,9,0]:
            if c_fig == p_fig:
                repeat_check[1] += 1
                if (memories_check[1] > repeat_check[1]) or (memories_check[1] == 0):
                    memories_check[1] = repeat_check[1]
                else:
                    pass
                messagebox.showinfo('当たり', 'あたりです。おめでとう! あなたは' + str(repeat_check[1]) + '回で当たりました。')
                repeat_check[1] = 0
                up_frame_top()
            else:
                if c_fig > p_fig:
                    repeat_check[1] += 1
                    messagebox.showinfo('はずれ', "はずれです。")
                elif c_fig < p_fig:
                    repeat_check[1] += 1
                    messagebox.showinfo('はずれ', "はずれです。")
                else:
                    pass
        else:
            up_frame_error()
    except:
        up_frame_error()

    #p_fig = int(game_entry1.get())
    print(p_fig, c_fig)

# 難易度ハードの勝敗をチェック
def win_or_lose_hard(game_entry1, c_fig):
    global repeat_check, memories_check
    c_fig = int(random.randint(0,9))
    try:
        p_fig = int(game_entry1.get())

        if p_fig in [1,2,3,4,5,6,7,8,9,0]:
            if c_fig == p_fig:
                repeat_check[2] += 1
                if (memories_check[2] > repeat_check[2]) or (memories_check[2] == 0):
                    memories_check[2] = repeat_check[2]
                else:
                    pass
                messagebox.showinfo('当たり', 'おめでとう! あなたは' + str(repeat_check[2]) + '回で当たりました。')
                repeat_check[2] = 0
                up_frame_top()
            else:
                if c_fig > p_fig:
                    repeat_check[2] += 1
                    messagebox.showinfo('はずれ', "はずれです。")
                elif c_fig < p_fig:
                    repeat_check[2] += 1
                    messagebox.showinfo('はずれ', "はずれです。")
                else:
                    pass
        else:
            up_frame_error()
    except:
        up_frame_error()
    #p_fig = int(game_entry1.get())
    print(p_fig, c_fig)


# 数字を受け取る
def get_fig():
    global p_fig, game_entry1
    try:
        p_fig = int(game_entry1.get())

        if p_fig in [1,2,3,4,5,6,7,8,9,0]:
            pass
        else:
            up_frame_error()
    except:
        up_frame_error()

# 今回の最高記録の表示
def up_frame_memories():
    global memories_check, memories_now_label4, memories_now_label5, memories_now_label6
    memories_now_label4 = ttk.Label(frame_memories_now, text='Easy  : ' + str(memories_check[0]) + '回')
    memories_now_label5 = ttk.Label(frame_memories_now, text='Normal: ' + str(memories_check[1]) + '回')
    memories_now_label6 = ttk.Label(frame_memories_now, text='Hard  : ' + str(memories_check[2]) + '回')

    memories_now_label4.grid(row=3, column=0, pady=5)
    memories_now_label5.grid(row=4, column=0, pady=5)
    memories_now_label6.grid(row=5, column=0, pady=5)

    frame_memories.tkraise()

# データベースからのデータを受け取り、表示
def memories_check_display():
    global memories_before_label4, memories_before_label5, memories_before_label6, frame_memories_berore
    try:
        dir_path = expanduser("~\Figure_search_game_app") 
        data_path = str(dir_path) + '\Figure_search_game_data.db'
        file_connect = sqlite3.connect(data_path)
        cur = file_connect.cursor()
        cur.execute("SELECT id, date,easy, normal, hard FROM data")
        item_list = cur.fetchall()
        
        cur.close

        for i in sorted(item_list, reverse=True):
            print(i)

        num = sorted(item_list, reverse=True)

        try:
            memories_before_label4 = ttk.Label(frame_memories_berore, text=str(num[0][1]) + "   Easy：" +  str(num[0][2]) + "回" + "   Normal：" + str(num[0][3]) + "回" + "   Hard：" + str(num[0][4]) + "回    " + "最新")
            memories_before_label4.grid(row=3, column=0)
        except:
            pass
        try:
            memories_before_label5 = ttk.Label(frame_memories_berore, text=str(num[1][1]) + "   Easy：" +  str(num[1][2]) + "回" + "   Normal：" + str(num[1][3]) + "回" + "   Hard：" + str(num[1][4]) + "回    " + "　　")
            memories_before_label5.grid(row=4, column=0)
        except:
            pass
        try:
            memories_before_label6 = ttk.Label(frame_memories_berore, text=str(num[2][1]) + "   Easy：" +  str(num[2][2]) + "回" + "   Normal：" + str(num[2][3]) + "回" + "   Hard：" + str(num[2][4]) + "回    " + "　　")
            memories_before_label6.grid(row=5, column=0)
        except:
            pass
        try:
            memories_before_label7 = ttk.Label(frame_memories_berore, text=str(num[3][1]) + "   Easy：" +  str(num[3][2]) + "回" + "   Normal：" + str(num[3][3]) + "回" + "   Hard：" + str(num[3][4]) + "回    " + "　　")
            memories_before_label7.grid(row=6, column=0)
        except:
            pass
        try:
            memories_before_label8 = ttk.Label(frame_memories_berore, text=str(num[4][1]) + "   Easy：" +  str(num[4][2]) + "回" + "   Normal：" + str(num[4][3]) + "回" + "   Hard：" + str(num[4][4]) + "回    " + "　　")
            memories_before_label8.grid(row=7, column=0)
        except:
            pass    

        frame_memories_berore.tkraise()
    except:
        messagebox.showinfo('Info', 'まだ記録がありません。')

# 記録を表示する
def up_frame_memories_now():
    frame_memories_now.tkraise()

# 閉じる操作をした時、データベースに記録を保存
def click_close():
    global memories_check
    print('閉じる')

    p = 0
    for i in memories_check:
        p += i
    
    if p != 0:
        dir_path = expanduser("~\Figure_search_game_app")
        try:
            makedirs(dir_path)
        except:
            pass
        data_path = str(dir_path) + '\Figure_search_game_data.db'
        print(data_path)
        file_connect = sqlite3.connect(data_path)
        cur = file_connect.cursor()

        try:
            cur.execute("DROP TABLE IF EXISTS items")
            cur.execute('CREATE TABLE data(id INTEGER PRIMARY KEY, date, easy INTEGER, normal INTEGER, hard INTEGER)')
            cur.execute('INSERT INTO data(date, easy, normal, hard) VALUES (datetime("now", "+9 hours"),' + str(memories_check[0]) + ',' + str(memories_check[1]) + ',' + str(memories_check[2]) + ')')
        except:
            cur.execute('INSERT INTO data(date, easy, normal, hard) VALUES (datetime("now", "+9 hours"),' + str(memories_check[0]) + ',' + str(memories_check[1]) + ',' + str(memories_check[2]) + ')')

        cur.execute('SELECT * FROM data WHERE id == 6')
        d = cur.fetchone()
        
        if d == None:
            pass
        else: 
            cur.execute('delete from data where id = 1')
            cur.execute('update data set id = 1 where id = 2')
            cur.execute('update data set id = 2 where id = 3')
            cur.execute('update data set id = 3 where id = 4')
            cur.execute('update data set id = 4 where id = 5')
            cur.execute('update data set id = 5 where id = 6')
        
        file_connect.commit()
        
        cur.close
    else:
        pass
    
    root.destroy()

# 変数の初期化
c_fig = -1
repeat_check = [0, 0, 0]
memories_check = [0, 0, 0]


# メイン
if __name__ == '__main__':
    #### rootの設定 ####
    root = tk.Tk()
    root.title(u'Fig_Search_Game')
    root.geometry('800x500')
    root.resizable(False, False)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)



######## トップメニュー画面 ########
    frame_top = tk.Frame(root)
    frame_top.grid(row=0, column=0, sticky="nsew", pady=20)

    top_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    top_label1 = ttk.Label(frame_top, text='数字当てゲーム')
    top_label2 = ttk.Label(frame_top, text='v1.0')
    top_label3 = ttk.Label(frame_top, text='')
    top_btn1 = ttk.Button(frame_top, text='Start', command=up_frame_select)
    top_btn2 = ttk.Button(frame_top, text='ルール', command=up_frame_rule)
    top_btn3 = ttk.Button(frame_top, text='きろく', command=up_frame_memories)
    top_btn4 = ttk.Button(frame_top, text='Exit', command=click_close)

    top_label1['font'] = top_font1
    top_label1.grid(row=0, column=0, pady=60)
    top_label2.grid(row=1, column=0, pady=10)
    top_label3.grid(row=2, column=0, pady=10)
    top_btn1.grid(row=3, column=0, pady=5)
    top_btn2.grid(row=4, column=0, pady=5)
    top_btn3.grid(row=5, column=0, pady=5)
    top_btn4.grid(row=6, column=0, pady=5)

    frame_top.grid_columnconfigure(0, weight=1)

######## 難易度選択画面 ########
    frame_select = tk.Frame(root)
    frame_select.grid(row=0, column=0, sticky="nsew", pady=20)

    select_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    select_label1 = ttk.Label(frame_select, text='数字当てゲーム')
    select_label2 = ttk.Label(frame_select, text='難易度を選んでね！')
    select_btn1 = ttk.Button(frame_select, text='Easy', command=up_frame_difficlt_check_easy)

    select_btn2 = ttk.Button(frame_select, text='Normal', command=up_frame_difficlt_check_normal)
    select_btn3 = ttk.Button(frame_select, text='Hard', command=up_frame_difficlt_check_hard)
    select_btn4 = ttk.Button(frame_select, text='戻る',command=up_frame_top)

    select_label1['font'] = select_font1
    select_label1.grid(row=0, column=0, pady=80)
    select_label2.grid(row=1, column=0, pady=10)
    select_btn1.grid(row=2, column=0, pady=5)
    select_btn2.grid(row=3, column=0, pady=5)
    select_btn3.grid(row=4, column=0, pady=5)
    select_btn4.grid(row=5, column=0, pady=10)

    frame_select.grid_columnconfigure(0, weight=1)



######## ゲーム画面 ########
    frame_game = tk.Frame(root)
    frame_game.grid(row=0, column=0, sticky="nsew", pady=20)

    game_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    game_label1 = ttk.Label(frame_game, text='数字当てゲーム')
    game_label2 = ttk.Label(frame_game, text='コンピューターが数字を選びました！\n数字を選んでください!')
    game_entry1 = ttk.Entry(frame_game)

    game_btn1 = ttk.Button(frame_game, text='')
    game_btn2 = ttk.Button(frame_game, text='トップへ戻る',command=up_frame_top)

    game_label1['font'] = select_font1
    game_label1.grid(row=0, column=0, pady=80)
    game_label2.grid(row=1, column=0, pady=10)
    game_entry1.grid(row=2, column=0, pady=10)
    
    game_btn2.grid(row=4, column=0, pady=5)
    #game_btn3.grid(row=4, column=0, pady=5)
    #game_btn4.grid(row=5, column=0, pady=10)

    frame_game.grid_columnconfigure(0, weight=1)




######## ルール画面 ########
    rule_string = tk.StringVar(value='a')
    frame_rule = tk.Frame(root)
    frame_rule.grid(row=0, column=0, sticky="nsew", pady=20)

    rule_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    rule_label1 = ttk.Label(frame_rule, text='数字当てゲーム')
    rule_label2 = ttk.Label(frame_rule, text='ルール')

    rule_btn1 = ttk.Button(frame_rule, text='Easyのルール', command=up_frame_rule_easy)
    rule_btn2 = ttk.Button(frame_rule, text='Normalのルール', command=up_frame_rule_normal)
    rule_btn3 = ttk.Button(frame_rule, text='Hardのルール', command=up_frame_rule_hard)
    


    """rule_label = ttk.Label(frame_rule, text=)
    rule_label4 = ttk.Label(frame_rule, text=)
    rule_label5 = ttk.Label(frame_rule, text=)
    """
    rule_btn4 = ttk.Button(frame_rule, text='トップへ戻る',command=up_frame_top)

    rule_label1['font'] = select_font1
    rule_label2['font'] = select_font1
    rule_label1.grid(row=0, column=0, pady=80)
    rule_label2.grid(row=1, column=0, pady=10)
    """rule_label3.grid(row=2, column=0, pady=5)
    rule_label4.grid(row=3, column=0, pady=5)
    rule_label5.grid(row=4, column=0, pady=5)"""
    
    rule_btn1.grid(row=2, column=0, pady=10)
    rule_btn2.grid(row=3, column=0, pady=5)
    rule_btn3.grid(row=4, column=0, pady=5)
    rule_btn4.grid(row=5, column=0, pady=5)

    frame_rule.grid_columnconfigure(0, weight=1)

##### 難易度イージーの画面構成
    frame_rule_easy = tk.Frame(root)
    frame_rule_easy.grid(row=0, column=0, sticky="nsew", pady=20)

    rule_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    easy_label1 = ttk.Label(frame_rule_easy, text='数字当てゲーム')
    easy_label2 = ttk.Label(frame_rule_easy, text='ルール')
    easy_label3 = ttk.Label(frame_rule_easy, text='Easy\nコンピュータが０～９の数字をランダムに１つ選びます。\nそのあとに、あなたが1つ数字を選びます。\nコンピュータとあなたの数字があっていればクリアです!!\nクリアするまでゲームは続きます。\nイージーはヒント付き!!')

    easy_btn1_2 = ttk.Button(frame_rule_easy, text='戻る', command=up_frame_rule)

    easy_label1['font'] = rule_font1
    easy_label2['font'] = rule_font1

    easy_label1.grid(row=0, column=0, pady=80)
    easy_label2.grid(row=1, column=0, pady=10)
    easy_label3.grid(row=2, column=0, pady=10)
    easy_btn1_2.grid(row=3, column=0, pady=5)

    frame_rule_easy.grid_columnconfigure(0, weight=1)


#####　難易度ノーマルの画面構成
    frame_rule_normal = tk.Frame(root)
    frame_rule_normal.grid(row=0, column=0, sticky="nsew", pady=20)

    rule_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    normal_label1 = ttk.Label(frame_rule_normal, text='数字当てゲーム')
    normal_label2 = ttk.Label(frame_rule_normal, text='ルール')
    normal_label3 = ttk.Label(frame_rule_normal, text='Nomal\nコンピュータが０～９の数字をランダムに１つ選びます。\nそのあとに、あなたが１つ数字を選びます。\nコンピュータとあなたの数字があっていればクリアです!!\nクリアするまでゲームは続きます。')

    normal_btn1_2 = ttk.Button(frame_rule_normal, text='戻る', command=up_frame_rule)

    normal_label1['font'] = rule_font1
    normal_label2['font'] = rule_font1

    normal_label1.grid(row=0, column=0, pady=80)
    normal_label2.grid(row=1, column=0, pady=10)
    normal_label3.grid(row=2, column=0, pady=10)
    normal_btn1_2.grid(row=3, column=0, pady=5)

    frame_rule_normal.grid_columnconfigure(0, weight=1)


#####　難易度ハードの画面構成
    frame_rule_hard = tk.Frame(root)
    frame_rule_hard.grid(row=0, column=0, sticky="nsew", pady=20)

    rule_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    hard_label1 = ttk.Label(frame_rule_hard, text='数字当てゲーム')
    hard_label2 = ttk.Label(frame_rule_hard, text='ルール')
    hard_label3 = ttk.Label(frame_rule_hard, text='Hard\nコンピュータが０～９の数字をランダムに１つ選びます。\nそのあとに、あなたが１つ数字を選びます。\nコンピュータとあなたの数字があっていればクリアです!!\nクリアするまでゲームは続きます。')

    hard_btn1 = ttk.Button(frame_rule_hard, text='戻る', command=up_frame_rule)

    hard_label1['font'] = rule_font1
    hard_label2['font'] = rule_font1

    hard_label1.grid(row=0, column=0, pady=80)
    hard_label2.grid(row=1, column=0, pady=10)
    hard_label3.grid(row=2, column=0, pady=10)
    hard_btn1.grid(row=3, column=0, pady=5)

    frame_rule_hard.grid_columnconfigure(0, weight=1)



#####　記録選択画面
    frame_memories = tk.Frame(root)
    frame_memories.grid(row=0, column=0, sticky="nsew", pady=20)

    rule_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    memories_label1 = ttk.Label(frame_memories, text='数字当てゲーム')
    memories_label2 = ttk.Label(frame_memories, text='きろく')
    memories_label3 = ttk.Label(frame_memories, text='ここでは、最短で当てた回数の記録が見れます!')

    memories_btn1 = ttk.Button(frame_memories, text='今回の記録', command=up_frame_memories_now)
    memories_btn2 = ttk.Button(frame_memories, text='前回までの記録', command=memories_check_display)
    memories_btn3 = ttk.Button(frame_memories, text='戻る', command=up_frame_top)

    memories_label1['font'] = rule_font1
    memories_label2['font'] = rule_font1

    memories_label1.grid(row=0, column=0, pady=80)
    memories_label2.grid(row=1, column=0, pady=10)
    memories_label3.grid(row=2, column=0, pady=10)
    memories_btn1.grid(row=3, column=0, pady=5)
    memories_btn2.grid(row=4, column=0, pady=5)
    memories_btn3.grid(row=5, column=0, pady=5)

    frame_memories.grid_columnconfigure(0, weight=1)


##### 記録を表示する画面
    frame_memories_now = tk.Frame(root)
    frame_memories_now.grid(row=0, column=0, sticky="nsew", pady=20)

    rule_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    memories_now_label1 = ttk.Label(frame_memories_now, text='数字当てゲーム')
    memories_now_label2 = ttk.Label(frame_memories_now, text='きろく')
    memories_now_label3 = ttk.Label(frame_memories_now, text='最短記録')
    
    memories_now_label_btn1 = ttk.Button(frame_memories_now, text='戻る', command=up_frame_memories)

    memories_now_label1['font'] = rule_font1
    memories_now_label2['font'] = rule_font1

    memories_now_label1.grid(row=0, column=0, pady=80)
    memories_now_label2.grid(row=1, column=0, pady=10)
    memories_now_label3.grid(row=2, column=0, pady=10)
    
    memories_now_label_btn1.grid(row=6, column=0, pady=5)


    frame_memories_now.grid_columnconfigure(0, weight=1)



##### 以前5回の記録の表示画面
    frame_memories_berore = tk.Frame(root)
    frame_memories_berore.grid(row=0, column=0, sticky="nsew", pady=20)

    rule_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    memories_before_label1 = ttk.Label(frame_memories_berore, text='数字当てゲーム')
    memories_before_label2 = ttk.Label(frame_memories_berore, text='きろく')
    memories_before_label3 = ttk.Label(frame_memories_berore, text='ここでは、過去5回の最短で当てた回数の記録が見れます!')

    memories_before_btn3 = ttk.Button(frame_memories_berore, text='戻る', command=up_frame_top)

    memories_before_label1['font'] = rule_font1
    memories_before_label2['font'] = rule_font1

    memories_before_label1.grid(row=0, column=0, pady=80)
    memories_before_label2.grid(row=1, column=0, pady=5)
    memories_before_label3.grid(row=2, column=0, pady=5)
    
    memories_before_btn3.grid(row=9, column=0, pady=10)

    frame_memories_berore.grid_columnconfigure(0, weight=1)

    frame_memories_berore.tkraise()


#### エラー画面
    frame_error = tk.Frame(root)
    frame_error.grid(row=0, column=0, sticky="nsew", pady=20)

    error_font1 = f.Font(family="Lucida Console", weight="bold", size=30)

    error_1 = ttk.Label(frame_error, text='エラー')
    error_2 = ttk.Label(frame_error, text='0~9の半角数字を入れてください')

    error_btn = ttk.Button(frame_error, text='戻る', command=up_frame_top)

    error_1['font'] = error_font1

    error_1.grid(row=0, column=0, pady=80)
    error_2.grid(row=1, column=0, pady=5)
    
    error_btn.grid(row=9, column=0, pady=10)

    frame_error.grid_columnconfigure(0, weight=1)

    frame_top.tkraise()

#### 閉じたときの処理
    root.protocol("WM_DELETE_WINDOW", click_close)
    root.mainloop()
