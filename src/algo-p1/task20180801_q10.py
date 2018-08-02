# 複数の条件を組み合わせて判断したり、「でない場合」の判断をしてみよう
x = 20
# xが10以上、かつ、30以下の場合に「xは10以上30以下です」と出力してください
if (10 <= x) and (x < 30):
    print('xは10以上30以下です')


y = 60
# yが10未満、または、30より大きい場合に「yは10未満または30より大きいです」と出力してください
if (10 >= y) and (y > 30):
    print('yは10未満または30より大きいです')


z = 55
# zが77ではない場合に「zは77ではありません」と出力してください(不等号でなく、notを用いてください)
if not z == 77:
    print('zは77ではありません')
