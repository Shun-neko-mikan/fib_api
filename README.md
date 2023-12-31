# 問題1.フィボナッチ数を返すAPIサービスの開発

## 実行環境
* 使用言語
  * Python 3.7
* 使用フレームワーク
  * Flask
* pip追加インストール
  * Flask
  * Gunicorn
* 使用サーバ
  * render.com
## ファイル構成
ファイル構成は横図の通りになっている。
* apitest.py
* app.py
* requirements.txt

## プログラム概要
本課題を解決するために作成したAPIは、指定したn番目のフィボナッチ数を返すものである。
フィボナッチ数列の一般項である、an=an-1+an-2の特性を用いて指定したn番目のフィボナッチ数を返す関数を作成した。初めに0,1を格納したリストを用意して、n=1以外の場合、n=2を作成したリストを使用して求め、それを	nになるまで繰り返す。
私が作成したAPIは、以下の制約下で動いている
* 1<=n<=20000
* nは整数である

## エラーコードについて
今回のAPIでは、3つのエラーコードを記述した。
１つ目は、n>20000の時に{'status': 413, 'message': 'ValueError: n must be less than 20000.'}を返す。これは、nがあまりにも大きすぎる値の時、私が作成したAPIでは対応することができなかったため、あらかじめ上限を決めその値を上回った時にこのエラーコードを返す。
２つ目は、n<1の時に{'status': 400, 'message': 'ValueError: n must be positive.'}を返す。これは、与えられた課題が指定した「n番目のフィボナッチ数を返す」ため、n<1の時はこのエラーコードを返す。
３つ目は、nが数値ではない時に{'status': 400, 'message': 'ValueError: n must be a natural number.'}を返す。上記エラーコードと同様にnが自然数ではないときはフィボナッチ数を返すことができないためこのエラーを返す。
## ユニットテスト概要
今回私が作成したテストは７つである。
* n=10
* n=99
* n=20001
* n=abc
* n=3.14
* n=-1
* n=0<br>
最初の２つは、正常動作するか確かめた。3,4,5,6,7のテストは、整数ではないときや制約外の時にエラーコードを出せるか確かめるテストケースである。


## エンドポイント
https://fib-api-nbt5.onrender.com/fib
