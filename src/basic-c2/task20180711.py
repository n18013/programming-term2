#じゃんけん

a = "rock"
b = "scissors"
c = "paper"

#相手が出す選択
sentaku = input('何を出しますか?1:rock、2:scissors、3:paper')

#入力されたら
if sentaku == ('2'):
    print ("one!two!three!")
    print ("CPUがグーを出しました。You lose")
elif sentaku == ('3'):
    print ("one!two!three!")
    print ("CPUがチョキを出しました。You lose")
elif sentaku == ('1'):
    print ("one!two!three!")
    print ("CPUがパーを出しました。You lose")
else :
    print ("入力が不正です。終了します。")

#結果


