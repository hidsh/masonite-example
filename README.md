# masonite-example

[ココ](https://qiita.com/dumblepy/items/9aaf2e56fee05851117c)を写経

## link
[docs](https://github.com/MasoniteFramework/masonite)
[masonite repo](https://github.com/MasoniteFramework/masonite)
[discord](https://discord.com/invite/TwKeFahmPZ)

# 確認

```
$ python craft serve
```

![ss](./doc-image/ss1.png)

# テスト

```
```

# 環境
- Python 3.9.7
- masonite 4.0.2

# メモ

## 最初のお約束
```
cd masonite-example
python -m venv venv
. .venv/bin/activate
pip install masonite	<- masonite-cli は obsolete っぽいので masonite を入れる
pip install pytest      <- テストを実行するpytestが入ってないので入れる
```

## プロジェクトを作る
```
project start proj		<- ドキュメントどおりに 'project start .' するとフォルダ名重複で怒られるのでフォルダ名をつける
cd proj
start install
make					<- make したらcraftコマンドが使えるようになった
python craft serve
```


## テストを作って実行
```
python craft test login	<- tests/unit/test_login.py が生成される
python -m pytest		<- テスト実行
```

## 
```

```
## 
```
```
## 
```
```
## 
```
```
## 
```
```
