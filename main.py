import csv
import pyautogui as p
import pyperclip
import time as t
import platform

csv_file = "csv/test.csv"
start_row = 0

xy_create  = 475, 779 # 問題作成一覧の、右下の丸い問題作成への遷移ボタンの中央
xy_problem = 279, 256 # 「問題文」欄の中央。ズレても余裕あり。
xy_answer  = 88,  422 # 「解答」欄。1文字目と2文字目の間。
# xy_auto    = 194, 499 # 選択肢の「自動作成」ボタン。少しシビア。
xy_ok      = 373, 616 # ダイアログのOKボタン。中央から少し右にずらした。
xy_save    = 285, 652 # 中央の保存ボタン。

# 「解答」欄の1文字目と2文字目の間をクリックしたときの動作
xy_namida  = 88,  447 # 涙吹き出しの形をしたボタン
xy_select  = 217, 395 # 「すべて選択」ボタン。ただし、「Google」と「Wikipedia」の間。
xy_cut     = 121, 377 # 「切り取り」ボタンの中央。

problem_column = 0
answer_column = 2
choice_column = 1

def paste():
    if platform.system() == "Windows":
        p.hotkey("ctrl", "v")
    else:
        p.hotkey("command", "v")

print("[INFO] " + csv_file + "の", end="")
print(str(start_row) + "行目から始めます!")

# アプリにフォーカスをあてる。
p.click(*xy_create)

ct = 0
with open(csv_file, "r", encoding = "utf_8") as f:
    reader = csv.reader(f)
    for row in reader:
      ct += 1
      if ct < start_row:
        continue

      print(str(ct) + "問目:", end = "")

      # 問題一覧の右下の「問題作成画面への遷移ボタン」をクリック。
      p.click(*xy_create)

      # 問題文を記入
      pyperclip.copy(row[problem_column])
      p.click(*xy_problem)
      t.sleep(0.5)
      paste()
      t.sleep(0.5)

      # 「選択肢」を「解答」欄に記入。
      answer_length = len(row[choice_column])
      pyperclip.copy(row[choice_column])
      p.click(*xy_answer)
      paste()
      t.sleep(0.05)

      # 選択肢の自動生成。
      p.press('enter') # 次の「自動生成」ボタンにフォーカス
      p.press('enter') # 自動生成ボタンをクリック
      # p.click(*xy_auto) # 自動生成ボタンをクリック
      p.click(*xy_ok)
      t.sleep(0.25 + 0.08 * answer_length)

      # 解答を正式なものに書き換える。
      # 文字間にでる「涙吹き出し」ボタンをクリックして、
      # 「すべて選択」をクリックし、「切り取り」をクリックし、
      # csvをコピーして「command + v」で貼り付け。
      if 2 < len(row) and row[answer_column]:
        p.click(*xy_answer)
        p.click(*xy_namida)
        p.click(*xy_select)
        p.click(*xy_cut)
        pyperclip.copy(row[answer_column])
        paste()

      # 保存ボタンを押して保存する(そして、問題一覧へ)。
      p.click(*xy_save)
      t.sleep(1.5)
      p.click(*xy_ok)
      t.sleep(0.4)

      print(row[1])
