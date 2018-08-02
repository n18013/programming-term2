#辞書型のデータ(果物名と値段)を変数に代入
fruits = {"Banana": 300,
          "Orange": 240,
          "Strawberry": 350,
          "Mango": 400}

#辞書型のデータ一覧を表示
for name in fruits.keys():
    #値段を得る
    price = fruits[name]
    #画面に出力
    s = "{0}は, {1}円です。".format(name, price)
    print(s)
