導入方法
==========

* 仮想環境の作成
```bash
python -m virtualenv venv
```
※作成済みの場合は不要


* 仮想環境の起動
```bash
source ./venv/bin/activate
```


* Pythonのインストール
下記リンクよりダウンロードしてください。

  https://pythonlinks.python.jp/
※インストール済みの場合は不要



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
```bash
python manage.py makemigrations
```
```bash
python manage.py makemigrations app
```
```bash
python manage.py migrate
```


* プログラム実行
```bash
python manage.py runserver
```






