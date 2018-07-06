#会計を求める
#値段
beer_v = 200
otumami_v = 100
yakitori_v = 100
#個数
beer_c = 2
otumami_c = 1
yakitori_c = 2
#割引
rate = 0.8
point = 150
# 計算
sum_v = (beer_v * beer_c) + (otumami_v * otumami_c) + (yakitori_v * yakitori_c)
payment = ((beer_v * beer_c) + (otumami_v * otumami_c) + ((yakitori_v * rate) * yakitori_c)) - (point)

# 結果を表示
print("買い物の合計は", sum_v, "円")
print("割引してもらうと", payment, "円")
