# insert_data.py
from api.db import get_db
from api.models.models import Scene, TextSet, Choice, Text, ChoiceTextSet
from sqlalchemy.orm import Session

def main():
    # from api.models.models import Scene, TextSet, Choice, Text, ChoiceTextSet
    # from api.db import get_db

    # get a session
    session = next(get_db())

    # create a Scene
    # new_scene = Scene()
    # session.add(new_scene)
    # session.flush()

    # create 3 TextSets
    new_text_set97 = TextSet(scene_id=1)
    new_text_set98 = TextSet(scene_id=1)
    new_text_set99 = TextSet(scene_id=1)
    new_text_set100 = TextSet(scene_id=1)
    new_text_set101 = TextSet(scene_id=1)
    new_text_set102 = TextSet(scene_id=1)
    new_text_set103 = TextSet(scene_id=1)
    new_text_set104 = TextSet(scene_id=1)
    new_text_set105 = TextSet(scene_id=1)
    new_text_set106 = TextSet(scene_id=1)
    new_text_set107 = TextSet(scene_id=1)
    new_text_set108 = TextSet(scene_id=1)
    new_text_set109 = TextSet(scene_id=1)
    new_text_set110 = TextSet(scene_id=1)

    session.add(new_text_set1)
    session.add(new_text_set2)
    session.add(new_text_set3)
    session.add(new_text_set4)
    session.add(new_text_set5)
    session.add(new_text_set6)
    session.add(new_text_set7)
    session.add(new_text_set8)
    session.add(new_text_set9)
    session.add(new_text_set10)
    session.add(new_text_set11)
    session.add(new_text_set12)
    session.flush()

    # text_sets = []
    # for _ in range(7):
    #     new_text_set = TextSet(scene_id=new_scene.id)
    #     session.add(new_text_set)
    #     text_sets.append(new_text_set)
    # session.flush()

    # new_text_sets = [TextSet(scene_id=new_scene.id) for _ in range(7)]
    # for new_text_set in new_text_sets:
    #     session.add(new_text_set)
    # session.flush()



    # create 14 Texts

    new_text1 = Text(
    text="ひらちん「俺の名前はひらちん。G's ACADEMY LAB15期に入学した。実はホストの仕事を続けながらジーズに通っているのだが、毎回の課題提出がとっても大変だ。今日もこうして火曜の課題発表が終わったと思ったら、木曜朝提出の課題が出される。果たして今週の俺は木曜朝までに課題を提出できるのだろうか...。」",
    background_image="1.png",
    gender="male",
    progress= 0,
    mental= 50,
    money= 300,
    satisfaction= 50,
    text_set_id=1
    )
    # session.add(new_text1)


    # new_text1 = Text(text="Example text 1", background_image="Example background 1", gender="Example gender", progress="Example progress", mental="Example mental", money="Example money", satisfaction="Example satisfaction", text_set_id=new_text_set1.id)
    # new_text2 = Text(text="Example text 2", background_image="Example background 2", gender="Example gender", progress="Example progress", mental="Example mental", money="Example money", satisfaction="Example satisfaction", text_set_id=new_text_set1.id)
    # ... continue for all 14 texts
    new_text2 = Text(
    text="ひらちん:「お、今日夕方から同伴予定の女の子Aから連絡だ。」",
    background_image="2.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=1
    )

    new_text3 = Text(
    text="女性A:「今日Takuyaに会えるの楽しみー!どれくらいお金持っていけばいいかな?」",
    background_image="3.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=1
    )

    new_text4 = Text(
    text="女性A:「今日Takuyaに会えるの楽しみー!どれくらいお金持っていけばいいかな?」",
    background_image="4.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=1
    )

    new_text5 = Text(
    text="Takuya:「持ってこれるだけ持ってこい」",
    background_image="5.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=2
    )

    new_text6 = Text(
    text="女性A:「わかった!今月はTakuyaに貢ぐって決めてたからいっぱい持っていく!」",
    background_image="6.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=2
    )

    new_text7 = Text(
    text="女の子の満足度が10上がった。/ メンタルが10上がった。",
    background_image="7.png",
    gender="male",
    progress= 0,
    mental= 10,
    money= 0,
    satisfaction= 10,
    text_set_id=2
    )

    new_text8 = Text(
    text="女性A:「今日はTakuyaとディナーからお店までたくさん一緒に居れるの嬉しいなぁ」",
    background_image="8.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=2
    )

    new_text9 = Text(
    text="Takuya:「お、おう。そうだね」(課題やらなきゃやべぇなぁ...。)",
    background_image="9.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=2
    )

    new_text10 = Text(
    text="女性A:「そういえば、今日はアフター何時まで一緒に居れるの?」",
    background_image="10.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=2
    )

    new_text11 = Text(
    text="女性A:「そういえば、今日はアフター何時まで一緒に居れるの?」",
    background_image="11.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=2
    )

    new_text12 = Text(
    text="Takuya:「持ってこれるだけ持ってこい」",
    background_image="12.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=3
    )

    new_text13 = Text(
    text="女性A:「わかったよぉ。」(今月お金厳しいし、ちょっと言い方きつかったなぁ。。)",
    background_image="13.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=3
    )

    new_text14 = Text(
    text="女の子の満足度が10下がった。/ メンタルが10上がった。",
    background_image="14.png",
    gender="male",
    progress= 0,
    mental= 10,
    money= 0,
    satisfaction= -10,
    text_set_id=3
    )

    new_text15 = Text(
    text="女性A:「今日はTakuyaとディナーからお店までたくさん一緒に居れるの嬉しいなぁ」",
    background_image="15.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=3
    )

    new_text16 = Text(
    text="Takuya:「お、おう。そうだね」(課題やらなきゃやべぇなぁ...。)",
    background_image="16.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=3
    )

    new_text17 = Text(
    text="女性A:「そういえば、今日はアフター何時まで一緒に居れるの?」",
    background_image="17.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=3
    )

    new_text18 = Text(
    text="女性A:「そういえば、今日はアフター何時まで一緒に居れるの?」",
    background_image="18.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=3
    )

    new_text19 = Text(
    text="Takuya:「無理しない範囲で大丈夫だよ」",
    background_image="19.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=4
    )

    new_text20 = Text(
    text="女性A:「優しいね。ありがとう。」(本当は貢いでほしいと思ってるのに、優しいなぁ)",
    background_image="20.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=4
    )

    new_text21 = Text(
    text="お金が50万減った。/ 女の子の満足度が10上がった。/ メンタルが5下がった。",
    background_image="21.png",
    gender="male",
    progress= 0,
    mental= -5,
    money= -50,
    satisfaction= 10,
    text_set_id=4
    )

    new_text22 = Text(
    text="女性A:「今日はTakuyaとディナーからお店までたくさん一緒に居れるの嬉しいなぁ」",
    background_image="22.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=4
    )

    new_text23 = Text(
    text="Takuya:「お、おう。そうだね」(課題やらなきゃやべぇなぁ...。)",
    background_image="23.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=4
    )

    new_text24 = Text(
    text="女性A:「そういえば、今日はアフター何時まで一緒に居れるの?」",
    background_image="24.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=4
    )

    new_text25 = Text(
    text="女性A:「そういえば、今日はアフター何時まで一緒に居れるの?」",
    background_image="25.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=4
    )

    new_text26 = Text(
    text="Takuya:「アフター1時間だけなら一緒に居れるよ」",
    background_image="26.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=5
    )

    new_text27 = Text(
    text="女性A:「そうだよね。忙しいもんね。でも少しでも時間開けてくれてありがとう。」",
    background_image="27.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=5
    )

    new_text28 = Text(
    text="お金が30万増えた。/ 女の子の満足度が5上がった。/ メンタルが5上がった。",
    background_image="28.png",
    gender="male",
    progress= 0,
    mental= 5,
    money= 30,
    satisfaction= 5,
    text_set_id=5
    )

    new_text29 = Text(
    text="Takuya:「改めて、今日は指名してくれてありがとう。2人の出会いに乾杯しよう。」",
    background_image="29.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=5
    )

    new_text30 = Text(
    text="女性A:「ドリンク、、何にしようかな?」",
    background_image="30.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=5
    )

    new_text31 = Text(
    text="女性A:「ドリンク、、何にしようかな?」",
    background_image="31.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=5
    )

    new_text32 = Text(
    text="Takuya:「アフター1時間だけなら一緒に居れるよ」",
    background_image="32.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=6
    )

    new_text33 = Text(
    text="女性A:「は?今日私の誕生日ってこと覚えてないの?(怒)ありえない!」",
    background_image="33.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=6
    )

    new_text34 = Text(
    text="急いで誕生日プレゼントを買いにいき、お金が200万減った。/ 女の子の満足度が30下がった。/ メンタルが20下がった。",
    background_image="34.png",
    gender="male",
    progress= 0,
    mental= -20,
    money= -200,
    satisfaction= -30,
    text_set_id=6
    )

    new_text35 = Text(
    text="Takuya:「改めて、今日は指名してくれてありがとう。2人の出会いに乾杯しよう。」",
    background_image="35.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=6
    )

    new_text36 = Text(
    text="女性A:「ドリンク、、何にしようかな?」",
    background_image="36.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=6
    )

    new_text37 = Text(
    text="女性A:「ドリンク、、何にしようかな?」",
    background_image="37.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=6
    )

    new_text38 = Text(
    text="Takuya:「最後までいっちゃおう〜！」",
    background_image="38.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=7
    )

    new_text39 = Text(
    text="女性A:「え!いいの!?やった〜!今日は幸せな日になりそう〜!」",
    background_image="39.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=7
    )

    new_text40 = Text(
    text="お金が100万増えた。/  女の子の満足度が10上がった。/ メンタルが10下がった。",
    background_image="40.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=7
    )

    new_text41 = Text(
    text="Takuya:「改めて、今日は指名してくれてありがとう。2人の出会いに乾杯しよう。」",
    background_image="41.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=7
    )
    new_text42 = Text(
    text="女性A:「ドリンク、、何にしようかな?」",
    background_image="42.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=7
    )
    new_text43 = Text(
    text="女性A:「ドリンク、、何にしようかな?」",
    background_image="43.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=7
    )




    session.add(new_text1)
    session.add(new_text2)
    session.add(new_text3)
    session.add(new_text4)
    session.add(new_text5)
    session.add(new_text6)
    session.add(new_text7)
    session.add(new_text8)
    session.add(new_text9)
    session.add(new_text10)
    session.add(new_text11)
    session.add(new_text12)
    session.add(new_text13)
    session.add(new_text14)
    session.add(new_text15)
    session.add(new_text16)
    session.add(new_text17)
    session.add(new_text18)
    session.add(new_text19)
    session.add(new_text20)
    session.add(new_text21)
    session.add(new_text22)
    session.add(new_text23)
    session.add(new_text24)
    session.add(new_text25)
    session.add(new_text26)
    session.add(new_text27)
    session.add(new_text28)
    session.add(new_text29)
    session.add(new_text30)
    session.add(new_text31)
    session.add(new_text32)
    session.add(new_text33)
    session.add(new_text34)
    session.add(new_text35)
    session.add(new_text36)
    session.add(new_text37)
    session.add(new_text38)
    session.add(new_text39)
    session.add(new_text40)
    session.add(new_text41)
    session.add(new_text42)
    session.add(new_text43)

    # create 2 Choices
    # new_choice1 = Choice(choice_text="持ってこれるだけ持ってこい", scene_id=new_scene.id)
    # new_choice2 = Choice(choice_text="無理しない範囲で大丈夫だよ", scene_id=new_scene.id)
    new_choice1 = Choice(choice_text="持ってこれるだけ持ってこい", scene_id=1, belong_text_set_id=1)
    new_choice2 = Choice(choice_text="無理しない範囲で大丈夫だよ", scene_id=1, belong_text_set_id=1)
    # new_choice3 = Choice(choice_text="アフター1時間だけなら一緒に居れるよ", scene_id=1)
    # new_choice4 = Choice(choice_text="最後までいっちゃおう〜!", scene_id=1)
    new_choice3 = Choice(choice_text="アフター1時間だけなら一緒に居れるよ", scene_id=1, belong_text_set_id=2)
    new_choice4 = Choice(choice_text="最後までいっちゃおう〜!", scene_id=1, belong_text_set_id=2)
    new_choice5 = Choice(choice_text="アフター1時間だけなら一緒に居れるよ", scene_id=1, belong_text_set_id=3)
    new_choice6 = Choice(choice_text="最後までいっちゃおう〜!", scene_id=1, belong_text_set_id=3)
    new_choice7 = Choice(choice_text="アフター1時間だけなら一緒に居れるよ", scene_id=1, belong_text_set_id=4)
    new_choice8 = Choice(choice_text="最後までいっちゃおう〜!", scene_id=1, belong_text_set_id=4)
    # new_choice5 = Choice(choice_text="シャンパンタワーいれてほしいな", scene_id=1)
    # new_choice6 = Choice(choice_text="好きなの飲みなよ", scene_id=1)
    # new_choice7 = Choice(choice_text="今日課題があるから実はあんまり飲めないんだ", scene_id=1)
    new_choice9 = Choice(choice_text="シャンパンタワーいれてほしいな", scene_id=1, belong_text_set_id=5)
    new_choice10 = Choice(choice_text="好きなの飲みなよ", scene_id=1, belong_text_set_id=5)
    new_choice11 = Choice(choice_text="今日課題があるから実はあんまり飲めないんだ", scene_id=1, belong_text_set_id=5)
    new_choice12 = Choice(choice_text="シャンパンタワーいれてほしいな", scene_id=1, belong_text_set_id=6)
    new_choice13 = Choice(choice_text="好きなの飲みなよ", scene_id=1, belong_text_set_id=6)
    new_choice14 = Choice(choice_text="今日課題があるから実はあんまり飲めないんだ", scene_id=1, belong_text_set_id=6)
    new_choice15 = Choice(choice_text="シャンパンタワーいれてほしいな", scene_id=1, belong_text_set_id=7)
    new_choice16 = Choice(choice_text="好きなの飲みなよ", scene_id=1, belong_text_set_id=7)
    new_choice17 = Choice(choice_text="今日課題があるから実はあんまり飲めないんだ", scene_id=1, belong_text_set_id=7)

    session.add(new_choice1)
    session.add(new_choice2)
    session.add(new_choice3)
    session.add(new_choice4)
    session.add(new_choice5)
    session.add(new_choice6)
    session.add(new_choice7)
    session.add(new_choice8)
    session.add(new_choice9)
    session.add(new_choice10)
    session.add(new_choice11)
    session.add(new_choice12)
    session.add(new_choice13)
    session.add(new_choice14)
    session.add(new_choice15)
    session.add(new_choice16)
    session.add(new_choice17)
    session.flush()

    # create 3 ChoiceTextSets
    new_choice_text_set1 = ChoiceTextSet(choice_id=new_choice1.id, text_set_id=new_text_set2.id)
    new_choice_text_set2 = ChoiceTextSet(choice_id=new_choice1.id, text_set_id=new_text_set3.id)
    new_choice_text_set3 = ChoiceTextSet(choice_id=new_choice2.id, text_set_id=new_text_set4.id)
    # new_choice_text_set4 = ChoiceTextSet(choice_id=new_choice3.id, text_set_id=new_text_set5.id)
    # new_choice_text_set5 = ChoiceTextSet(choice_id=new_choice3.id, text_set_id=new_text_set6.id)
    # new_choice_text_set6 = ChoiceTextSet(choice_id=new_choice4.id, text_set_id=new_text_set7.id)
    # new_choice_text_set7 = ChoiceTextSet(choice_id=new_choice5.id, text_set_id=new_text_set8.id)
    # new_choice_text_set8 = ChoiceTextSet(choice_id=new_choice5.id, text_set_id=new_text_set9.id)
    # new_choice_text_set9 = ChoiceTextSet(choice_id=new_choice6.id, text_set_id=new_text_set10.id)
    # new_choice_text_set10 = ChoiceTextSet(choice_id=new_choice7.id, text_set_id=new_text_set11.id)
    # new_choice_text_set11 = ChoiceTextSet(choice_id=new_choice7.id, text_set_id=new_text_set12.id)
    new_choice_text_set4 = ChoiceTextSet(choice_id=new_choice3.id, text_set_id=new_text_set5.id)
    new_choice_text_set5 = ChoiceTextSet(choice_id=new_choice3.id, text_set_id=new_text_set6.id)
    new_choice_text_set6 = ChoiceTextSet(choice_id=new_choice4.id, text_set_id=new_text_set7.id)
    new_choice_text_set7 = ChoiceTextSet(choice_id=new_choice5.id, text_set_id=new_text_set5.id)
    new_choice_text_set8 = ChoiceTextSet(choice_id=new_choice5.id, text_set_id=new_text_set6.id)
    new_choice_text_set9 = ChoiceTextSet(choice_id=new_choice6.id, text_set_id=new_text_set7.id)
    new_choice_text_set10 = ChoiceTextSet(choice_id=new_choice7.id, text_set_id=new_text_set5.id)
    new_choice_text_set11 = ChoiceTextSet(choice_id=new_choice7.id, text_set_id=new_text_set6.id)
    new_choice_text_set12 = ChoiceTextSet(choice_id=new_choice8.id, text_set_id=new_text_set7.id)

    new_choice_text_set13 = ChoiceTextSet(choice_id=new_choice9.id, text_set_id=new_text_set8.id)
    new_choice_text_set14 = ChoiceTextSet(choice_id=new_choice9.id, text_set_id=new_text_set9.id)
    new_choice_text_set15 = ChoiceTextSet(choice_id=new_choice10.id, text_set_id=new_text_set10.id)
    new_choice_text_set16 = ChoiceTextSet(choice_id=new_choice11.id, text_set_id=new_text_set11.id)
    new_choice_text_set17 = ChoiceTextSet(choice_id=new_choice11.id, text_set_id=new_text_set12.id)
    new_choice_text_set18 = ChoiceTextSet(choice_id=new_choice12.id, text_set_id=new_text_set8.id)
    new_choice_text_set19 = ChoiceTextSet(choice_id=new_choice12.id, text_set_id=new_text_set9.id)
    new_choice_text_set20 = ChoiceTextSet(choice_id=new_choice13.id, text_set_id=new_text_set10.id)
    new_choice_text_set21 = ChoiceTextSet(choice_id=new_choice14.id, text_set_id=new_text_set11.id)
    new_choice_text_set22 = ChoiceTextSet(choice_id=new_choice14.id, text_set_id=new_text_set12.id)
    new_choice_text_set23 = ChoiceTextSet(choice_id=new_choice15.id, text_set_id=new_text_set8.id)
    new_choice_text_set24 = ChoiceTextSet(choice_id=new_choice15.id, text_set_id=new_text_set9.id)
    new_choice_text_set25 = ChoiceTextSet(choice_id=new_choice16.id, text_set_id=new_text_set10.id)
    new_choice_text_set26 = ChoiceTextSet(choice_id=new_choice17.id, text_set_id=new_text_set11.id)
    new_choice_text_set27 = ChoiceTextSet(choice_id=new_choice17.id, text_set_id=new_text_set12.id)


    session.add(new_choice_text_set1)
    session.add(new_choice_text_set2)
    session.add(new_choice_text_set3)
    session.add(new_choice_text_set4)
    session.add(new_choice_text_set5)
    session.add(new_choice_text_set6)
    session.add(new_choice_text_set7)
    session.add(new_choice_text_set8)
    session.add(new_choice_text_set9)
    session.add(new_choice_text_set10)
    session.add(new_choice_text_set11)
    session.add(new_choice_text_set12)
    session.add(new_choice_text_set13)
    session.add(new_choice_text_set14)
    session.add(new_choice_text_set15)
    session.add(new_choice_text_set16)
    session.add(new_choice_text_set17)
    session.add(new_choice_text_set18)
    session.add(new_choice_text_set19)
    session.add(new_choice_text_set20)
    session.add(new_choice_text_set21)
    session.add(new_choice_text_set22)
    session.add(new_choice_text_set23)
    session.add(new_choice_text_set24)
    session.add(new_choice_text_set25)
    session.add(new_choice_text_set26)
    session.add(new_choice_text_set27)

    # commit the session
    session.commit()


    print("Data inserted successfully.")

if __name__ == "__main__":
    main()
