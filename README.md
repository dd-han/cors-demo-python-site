# cors-demo-python-site

這個專案用來 Demo 直接在 Server 程式中實作反向代理。

## 安裝

安裝 Python 3 之後請輸入以下指令確認  Python 版本

```
python --version
```

如果你使用 Mac 或 Linux ，系統上可能同時存在 Python 2 與 Python 3 ，請用 `python3` 指令取代 `python` 。

確定系統是使用 Python 3 之後，請輸入以下指令安裝 flask

```
python -m pip install Flask Requests
```

或

```
python3 -m pip install Flask Requests
```

## 執行

Windows 請用下面的指令
```
set FLASK_APP=app.py
set FLASK_DEBUG=1
```

Linux 或 Mac
```
export FLASK_APP=app.py
export FLASK_DEBUG=1
```

接著不管哪個系統都執行下面的指令：
```
flask run
```