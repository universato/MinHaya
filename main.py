import csv
import pyautogui as p
import pyperclip
import time as t

csv_file = "csv/op.csv"
start_row = 0

# アプリにフォーカスをあてる。
p.click(475, 779)

ct = 0
print("starts")
with open(csv_file, "r", encoding = "utf_8") as f:
    reader = csv.reader(f)
    for row in reader:
      ct += 1
      print(str(ct) + "問目:", end = "")
      if ct < start_row:
        continue

      # 問題一覧の右下の「問題作成画面への遷移ボタン」をクリック。
      p.click(475, 779)

      # 問題文を記入
      pyperclip.copy(row[0])
      p.click(200, 260)
      t.sleep(0.2)
      p.hotkey("command", "v")
      t.sleep(0.2)

      # 選択肢を解答に記入。
      answer_length = len(row[1])
      pyperclip.copy(row[1])
      p.click(150, 425)
      t.sleep(0.05)
      p.hotkey("command", "v")
      t.sleep(0.05)

      # 選択肢の自動生成。
      p.click(183, 500)
      t.sleep(0.1)
      p.click(335, 620)
      t.sleep(0.25 + 0.08 * answer_length)

      # 解答を正式なものに書き換える。
      if 2 < len(row):
        p.click(87, 422)
        t.sleep(0.01)
        p.click(86, 448)
        t.sleep(0.01)
        p.click(86, 386)
        t.sleep(0.01)
        p.click(86, 386)
        t.sleep(0.1)
        pyperclip.copy(row[2])
        p.click(150, 425)
        t.sleep(0.05)
        p.hotkey("command", "v")
        t.sleep(0.05)

      # 保存ボタンを押して保存する(そして、問題一覧へ)。
      p.click(287, 662)
      t.sleep(1.5)
      p.click(353, 603)
      t.sleep(0.4)

      print(row[1])
