# ライブラリのインポート
import random
import time

# 問1. 1 ～ 10 までの乱数を一度に３つ発生させて、最も小さな値の秒数処理を止める関数を作成せよ。
def stoptime():
    """ここにこの関数の注釈を書く"""
    # ここに作成せよ
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    x = min([a, b, c])
    time.sleep(x)
    #模範解答 リスト内表記を使う 1行
    #minTime = min([random.randint(1,11) for _ in range(3)])

print(stoptime())
# 問2. 1 ～ 10 までの乱数を発生させ、その合計が 100 を超えるまでループするアルゴリズムを作成せよ。
# 毎回合計値を出力し、100 を超えた場合「終了」と知らせよ。
# ここに作成せよ
if __name__ == "__main__":
    y = 0
    while y <= 100:
        d = random.randint(1,10)
        y = y + d
        print(y)

    print("終了")

#模範解答
#y = 0
#while True:
 #   y += random.randint(1,11)
 #   print(y)
 #   if 100 < y:
 #       print("終了")
 #       break
# 問3. 現在時刻を表示させよ。
if __name__ == "__main__":
    # ここに作成せよ
    z = time.time()
    print(z)
#模範解答 ifの後から
    #now = datetime.datetime.now()
    #print(now)