# みんはや

CSVファイル形式の問題セットを、みんはやに自動で問題を追加するPythonプログラム。 

## 検証バージョン

みんはや： 4.0.9
Python    3.10.1 [Clang 12.0.5]
csv       1.0
pyautogui 0.9.53
pyperclip 1.8.2
platform  1.0.8

みんはやのバージョンは、最初のタイトルページで確認する。  
右上のハンバーガーメニューから「タイトルへ」で戻ることも可能。  

Python関連は、以下の方法で確認できる。
> python version.py


## 使い方

1. パソコンで[NoxPlayer](https://www.bignox.com/)などのエミュレータを通して、｢みんはや｣を起動する。

2. `main.py`の座標を書き換える。

具体的には`cursor.py`を実行して、実際にみんはやを操作し、パソコン上の座標を把握する。

【注意!!】プログラムを始める前に、Pythonプログラムの停止方法を覚える。
- Mac: `control + c`で、KeyboardInterruptでPythonで停止させる。
- Mac: `control + z`で、zshを通してプログラムを停止させる

座標を把握したら、`main.py`の座標を書き換える。

3. `main.py`(`readcsv.py`)を実行して、CSVファイルから問題リストを入力していく。  

> python main.py

`start_row`は、入力を始める行。 

プログラムを始める前に、停止させる方法を覚える。もしくは、問題数が少ない状態でやる。
- Mac: `control + c`で、KeyboardInterruptでPythonで停止させる。
- Mac: `control + z`で、zshを通してプログラムを停止させる

念の為、先に問題投稿をしておいた方が良い。  
誤った問題を投稿する可能性があるため。



## 注意事項

main.pyを使う際の注意事項：  
画面を拡大して左端に画面を寄せるなど、位置を固定させる。  
クイズリスト一覧(問題集のタイトル一覧)ではなく、問題一覧画面にする。  


## 参考

クイズアプリ「みんはや」にたくさんの作った問題セットを(半)自動で追加させる  
https://qiita.com/TEA437354/items/0b79b84fb323844b4dd8

## main.pyの見方

```python
import platform
def paste():
    if platform.system() == "Windows":
        p.hotkey("ctrl", "v")
    else:
        p.hotkey("command", "v")
```
WindowsとMacでペーストのショートカットが異なる。
なお、Macの`platform.system()`は`"Darwin"`である。


##

「解答」欄で、`enter`を押すと、「自動生成」ボタンにフォーカスする。
そのまま、`enter`を押すと、「自動生成」のダイアログがでる。

自動生成のボタンのカーソル位置を決めなくていいので、楽そう。

## cursor.pyの見方

【注意!!】プログラムを始める前に、Pythonプログラムの停止方法を覚える。
- Mac: `control + c`で、KeyboardInterruptでPythonで停止させる。
- Mac: `control + z`で、zshを通してプログラムを停止させる


```python
def on_click(x, y, button, pressed):
    if pressed:
        print(type(button))
        print('{:.1f}, {:.1f}'.format(x, y))
```

第1引数`x`は、普通のx軸。左が0である。  
第2引数`y`は、下方向のy軸。上が0となる。  
第3引数は、`<enum 'Button'>`。  
第4引数`pressed`は、押されたときに`True`で、離れたときに`False`となる。  
