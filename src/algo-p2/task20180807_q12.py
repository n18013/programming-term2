#変数moneyに数値1000を代入してください
money = 1000

items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    #変数moneyを用いて「財布には◯◯円入っています」のように出力してください


    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')

    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')

    #所持金が支払い金額以上の場合、「◯◯を△△個買いました」を表示し、所持金から支払い金額を引いてください。
    if money > total_price:
        s = "{0}を、{1}個買いました。". format(item_name,input_count)
        print(s)
        money = money - (items[item_name] * count)


    #上記条件に当てはまらない場合、「お金が足りません」「◯◯を買えませんでした」を表示してください。
    if money < total_price:
        s = ("お金が足りません" + format(item_name) + "を買えませんでした")
        print(s)

