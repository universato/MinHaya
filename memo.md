pynputは外部パッケージなので、pipを使ってインストールします。
pip install pynput

## 参考

クイズアプリ「みんはや」にたくさんの作った問題セットを(半)自動で追加させる
https://qiita.com/TEA437354/items/0b79b84fb323844b4dd8

## リファクタリング

2022/11/2
```python
format(x, '.1f') + ',' + format(y, '.1f')  # Before
'{:.1f}, {:.1f}'.format(x, y)              # After
```

# 2022/11/2

左端に隣接。上下を目いっぱいに拡大。

左右の中央は、279 ~ 289。
保存ボタンの「保存」の字の間が285~286なので、左右の中央は285っぽい。

```python
xy_create  = 475, 779 # 問題作成一覧の、右下の丸い問題作成への遷移ボタンの中央
xy_problem = 279, 256 # 「問題文」欄の中央。ズレても余裕あり。
xy_answer  = 88,  422  # 「解答」欄。1文字目と2文字目の間。
xy_auto    = 194, 499 # 選択肢の「自動作成」ボタン。少しシビア。
xy_ok      = 373, 616 # ダイアログのOKボタン。中央から少し右にずらした。
xy_save    = 285, 652 # 中央の保存ボタン。

xy_namida  = 88,  447 # 涙吹き出しの形をしたボタン
xy_select  = 217, 395 # 「すべて選択」ボタン。ただし、「Google」と「Wikipedia」の間。
xy_cut     = 121, 377 # 「切り取り」ボタンの中央。
```

```python
# xy_answer  = 415, 420 # 「解答」欄。中央から右にずらした。右半分の真ん中。上下が少しシビア。
```
### 問題集の中の問題一覧の、右下の丸いクイズ作成への遷移ボタン。

473, 784

丸いボタンの上下左右。
472.83, 751.19 Button.left True
472.88, 815.08 Button.left True
443.16, 784.05 Button.left True
504.19, 783.94 Button.left True

丸いボタンの上下左右。ちょっと左右を押したときの上下軸がずれた感じがある。
473.31, 751.75 Button.left True
472.78, 816.01 Button.left True
441.69, 783.29 Button.left True
504.14, 781.96 Button.left True

左上に画面を固定した状態で、下に思いっきり引っ張って画面を下に拡大。下の方に少しだけ隙間がある。
丸いボタンの上下左右。
473.85, 753.97 Button.left True
472.57, 817.28 Button.left True
442.33, 785.02 Button.left True
504.68, 783.81 Button.left True

###

問題文の枠の中央。
279, 256

62, 194 # 左上
512, 324 # 右下

上下左右
280.70, 194.57 Button.left True
278.17, 324.01 Button.left True
61.82, 257.62 Button.left True
512.14, 253.54 Button.left True

### 「解答」欄

287, 420 # 解答欄の中央
415, 420  # 解答欄の中央から右にずらした。右半分の真ん中。

解答欄の上に「Google」や「Wikipedia」のボタンがあるので、
フェールセーフ(?)で押さないように右にズラしたい。

60 ~ 513, 404 ~ 440

上下左右
287.88, 404.75 Button.left True
289.63, 440.09 Button.left True
59.39, 420.32 Button.left True
513.02, 420.64 Button.left True

### 自動生成の中央

194, 499

159~230, 483~516 

上下左右
195.37, 483.84 Button.left True
193.00, 516.09 Button.left True
159.85, 499.62 Button.left True
230.62, 499.14 Button.left True

### ダイアログのOKボタン(自動生成の確認)

「解答選択肢を自動生成しますか？」の1文。
「キャンセル」と「OK」のボタンがある。

348, 616 # ダイアログのOKボタンの中央
373, 616 # 中央から右にずらしたバージョン。


294 ~ 405, 593 ~ 644

失敗したときように、少し右にずらしたい。  
ダイアログがでないと、保存ボタンを押してしまう可能性があるため。
372.80, 618.02 # 中央から右にずらしたバージョン。

上下左右
348.33, 592.89 Button.left True
347.86, 644.33 Button.left True
294.10, 615.57 Button.left True
405.43, 616.63 Button.left True


### 保存ボタンの中央

285, 652 # 保存ボタンの中央

上下左右
285.10, 628.77 Button.left True
284.53, 678.35 Button.left True
230.66, 652.12 Button.left True
341.41, 652.93 Button.left True


### 涙吹き出し

, 447 # 中央
, 433~455

88.26, 448.09 Button.left True
88.26, 448.09 Button.left False
88.26, 448.09 Button.left True
88.26, 448.09 Button.left False
88.26, 447.86 Button.left True
88.26, 447.86 Button.left False
88.00, 450.73 Button.left True
88.00, 450.62 Button.left False
88.87, 440.95 Button.left True
88.87, 440.95 Button.left False
86.43, 443.58 Button.left True
86.43, 443.58 Button.left False
87.68, 457.16 Button.left True
87.68, 457.16 Button.left False
88.16, 450.72 Button.left True
88.16, 450.72 Button.left False
88.96, 441.13 Button.left True
89.58, 446.58 Button.left True
88.80, 443.38 Button.left True
88.80, 443.38 Button.left True
88.80, 443.38 Button.left True
88.80, 443.38 Button.left True
88.80, 443.38 Button.left True
88.80, 443.38 Button.left True
88.80, 443.38 Button.left True
88.80, 443.38 Button.left True
88.80, 443.38 Button.left True
88.80, 451.85 Button.left True
88.80, 451.85 Button.left True
88.80, 451.85 Button.left True
88.80, 451.85 Button.left True
88.80, 451.85 Button.left True
84.86, 428.51 Button.left True
87.33, 456.44 Button.left True
88.89, 436.23 Button.left True
88.89, 436.23 Button.left True
88.89, 435.76 Button.left True
88.89, 440.77 Button.left True
88.89, 442.21 Button.left True
88.89, 442.21 Button.left True
88.89, 449.75 Button.left True
88.89, 454.51 Button.left True
89.65, 438.80 Button.left True
89.65, 438.80 Button.left True
89.16, 449.68 Button.left True

# 2022/8

469, 780
200, 260
150, 425
183, 500
335, 620
280, 652
328, 612


問題一覧から、右下の問題作成ボタン
468.64337158203125 780.3049926757812
470.5357666015625 781.076171875

問題文を入力
147.66256713867188 236.88629150390625
289.2723693847656 271.6503601074219

解答を入力
142.66468811035156 421.42828369140625
155.6611785888672 430.47576904296875

選択肢の自動作成
182.6595458984375 502.6976623535156
184.887451171875 499.5057373046875

自動作成しますか？ OK！
337.0457763671875 631.8050537109375
333.2934265136719 618.9077758789062

保存ボタン
291.2351989746094 651.8182373046875
279.56182861328125 653.9478149414062

OKボタン
327.7088623046875 611.62646484375
330.1531982421875 613.1004638671875

# 保存ボタン
少し下の方

286.55 662.38
287, 662

保存 ダイアログ 少し右上
353.82 602.93
353, 603
