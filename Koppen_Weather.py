import random
koppen_key_english = ['Af','Aw','Cs','Cfa','Cfb',
'Df','Dw','BW','BS','ET','EF']
koppen_key_japanse = ['熱帯雨林気候','サバナ気候','地中海性気候',
'温暖湿潤気候','西岸海洋性気候','冷帯湿潤気候','冷帯冬季少雨気候',
'砂漠気候','ステップ気候','ツンドラ気候','氷雪気候']
question_english_japanese = 0
question = 0
print('記号から日本語か日本語から記号化選択してください')
question_english_japanese = int(input('記→日なら1,日→記なら2'))
while True:
    if (question_english_japanese == 1):
        question = random.randint(0,10)
        print(koppen_key_english[question])
        answer_japanese = str(input('答えを入力してね　'))
        if (question == koppen_key_japanse.index(answer_japanese)):
            print('正解です。次の問題へ進みましょう。')
            continue
        else:
            print('不正解です。')
            print('答えは'+str(koppen_key_japanse[question])+'です。')
            print('次へ進みましょう。')
            continue
    elif (question_english_japanese == 2):
        question = random.randint(0,10)
        print(koppen_key_japanse[question])
        answer_english = str(input('答えを入力してね。 '))
        if (question == koppen_key_english.index(answer_english)):
            print('正解です。次へ進みましょう。')
            continue
        else:
            print('不正解です。　')
            print('答えは'+str(koppen_key_english[question]+'です。'))
            print('次へ進みましょう。')
            continue
