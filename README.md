導入方法
==========

* Pythonのインストール
下記リンクよりダウンロードしてください。

  https://pythonlinks.python.jp/
※インストール済みの場合は不要


* 仮想環境の作成
```Python
python -m virtualenv venv
```
※作成済みの場合は不要


* 仮想環境の起動
```bash
source ./venv/bin/activate
```


* Djangoのインストール
```bash
pip install django
```
※インストール済みの場合は不要


* ライブラリのインストール
```bash
pip install 〇〇
```


* DB生成
```Python
python manage.py makemigrations
```
```Python
python manage.py makemigrations app
```
```Python
python manage.py migrate
```


* プログラム実行
```Python
python manage.py runserver
```






