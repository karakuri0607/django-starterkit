導入方法
==========

* Pythonのインストール
下記リンクよりダウンロードしてください。

  https://pythonlinks.python.jp/
※インストール済みの場合は不要


* 仮想環境の作成
```Python console
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
```Python console
python manage.py makemigrations
```
```Python console
python manage.py makemigrations app
```
```Python console
python manage.py migrate
```


* プログラム実行
```Python console
python manage.py runserver
```






