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
    new_scene = Scene()
    session.add(new_scene)
    session.flush()

    # create 3 TextSets
    new_text_set1 = TextSet(scene_id=new_scene.id)
    new_text_set2 = TextSet(scene_id=new_scene.id)
    new_text_set3 = TextSet(scene_id=new_scene.id)
    new_text_set4 = TextSet(scene_id=new_scene.id)
    new_text_set5 = TextSet(scene_id=new_scene.id)
    new_text_set6 = TextSet(scene_id=new_scene.id)
    new_text_set7 = TextSet(scene_id=new_scene.id)
    new_text_set8 = TextSet(scene_id=new_scene.id)
    new_text_set9 = TextSet(scene_id=new_scene.id)
    new_text_set10 = TextSet(scene_id=1)
    new_text_set11 = TextSet(scene_id=1)
    new_text_set12 = TextSet(scene_id=1)
    new_text_set13 = TextSet(scene_id=1)
    new_text_set14 = TextSet(scene_id=1)
    new_text_set15 = TextSet(scene_id=1)
    new_text_set16 = TextSet(scene_id=1)
    new_text_set17 = TextSet(scene_id=1)
    new_text_set18 = TextSet(scene_id=1)
    new_text_set19 = TextSet(scene_id=1)
    new_text_set20 = TextSet(scene_id=1)
    new_text_set21 = TextSet(scene_id=1)
    new_text_set22 = TextSet(scene_id=1)
    new_text_set23 = TextSet(scene_id=1)
    new_text_set24 = TextSet(scene_id=1)
    new_text_set25 = TextSet(scene_id=1)
    new_text_set26 = TextSet(scene_id=1)
    new_text_set27 = TextSet(scene_id=1)
    new_text_set28 = TextSet(scene_id=1)
    new_text_set29 = TextSet(scene_id=1)
    new_text_set30 = TextSet(scene_id=1)
    new_text_set31 = TextSet(scene_id=1)
    new_text_set32 = TextSet(scene_id=1)
    


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
    session.add(new_text_set13)
    session.add(new_text_set14)
    session.add(new_text_set15)
    session.add(new_text_set16)
    session.add(new_text_set17)
    session.add(new_text_set18)
    session.add(new_text_set19)
    session.add(new_text_set20)
    session.add(new_text_set21)
    session.add(new_text_set22)
    session.add(new_text_set23)
    session.add(new_text_set24)
    session.add(new_text_set25)
    session.add(new_text_set26)
    session.add(new_text_set27)
    session.add(new_text_set28)
    session.add(new_text_set29)
    session.add(new_text_set30)
    session.add(new_text_set31)
    session.add(new_text_set32)
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
    background_image="src/img/40.png",
    gender="male",
    progress= 0,
    mental= -10,
    money= 100,
    satisfaction= 10,
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





    new_text44 = Text(
    text="Takuya:「シャンパンタワーいれてほしいな」",
    background_image="44.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=8
    )

    new_text45 = Text(
    text="女性A:「もちろんだよ!Takuyaに貢げて幸せ♡」",
    background_image="45.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=8
    )

    new_text46 = Text(
    text="お金が200万増えた。/ 女性の満足度が20上がった。/ メンタルが15上がった。",
    background_image="46.png",
    gender="male",
    progress= 0,
    mental= 15,
    money= 200,
    satisfaction= 20,
    text_set_id=8
    )

    new_text47 = Text(
    text="女性A:「同伴のときも聞いたけど、アフターはどうしよっか?」",
    background_image="47.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=8
    )

    new_text48 = Text(
    text="女性A:「同伴のときも聞いたけど、アフターはどうしよっか?」",
    background_image="48.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=8
    )

    new_text49 = Text(
    text="Takuya:「シャンパンタワーいれてほしいな」",
    background_image="49.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=9
    )

    new_text50 = Text(
    text="女性A:「んー、ちょっと考えさせて。一旦チャミスルで!」",
    background_image="50.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=9
    )

    new_text51 = Text(
    text="お金が50万減った。/ メンタルが10下がった。",
    background_image="51.png",
    gender="male",
    progress= 0,
    mental= -10,
    money= -50,
    satisfaction= 0,
    text_set_id=9
    )

    new_text52 = Text(
    text="女性A:「同伴のときも聞いたけど、アフターはどうしよっか?」",
    background_image="52.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=9
    )

    new_text53 = Text(
    text="女性A:「同伴のときも聞いたけど、アフターはどうしよっか?」",
    background_image="53.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=9
    )

    new_text54 = Text(
    text="Takuya:「好きなの飲みなよ」",
    background_image="54.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=10
    )

    new_text55 = Text(
    text="女性A:「えー、優しい!じゃあアルマンドおろしちゃおうかな!」",
    background_image="55.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=10
    )

    new_text56 = Text(
    text="お金が100万増えた。/ 女性の満足度が10上がった。/ メンタルが10上がった。",
    background_image="56.png",
    gender="male",
    progress= 0,
    mental= 10,
    money= 100,
    satisfaction= 10,
    text_set_id=10
    )

    new_text57 = Text(
    text="女性A:「同伴のときも聞いたけど、アフターはどうしよっか?」",
    background_image="57.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=10
    )
    new_text58 = Text(
    text="女性A:「同伴のときも聞いたけど、アフターはどうしよっか?」",
    background_image="58.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=10
    )

    new_text59 = Text(
    text="Takuya:「今日実は帰ったら課題をやらないとだから、あんまりお酒飲めないんだ」",
    background_image="59.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=11
    )

    new_text60 = Text(
    text="女性A:「え、つまんなー。なにそれ〜。」",
    background_image="60.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=11
    )

    new_text61 = Text(
    text="女の子の満足度が15下がった。/ メンタルが10下がった。",
    background_image="61.png",
    gender="male",
    progress= 0,
    mental= -10,
    money= 0,
    satisfaction= -15,
    text_set_id=11
    )

    new_text62 = Text(
    text="女性A:「同伴のときも聞いたけど、アフターはどうしよっか?」",
    background_image="62.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=11
    )

    new_text63 = Text(
    text="女性A:「同伴のときも聞いたけど、アフターはどうしよっか?」",
    background_image="63.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=11
    )

    new_text64 = Text(
    text="Takuya:「今日実は帰ったら課題をやらないとだから、あんまりお酒飲めないんだ」",
    background_image="64.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=12
    )

    new_text65 = Text(
    text="女性A:「勉強!?えらいねー!じゃあ今日は私だけ飲むから無理しないでいいよ。」",
    background_image="65.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=12
    )

    new_text66 = Text(
    text="お金が50万増えた。/ 女性の満足度が10上がった。/ メンタルが10上がった。",
    background_image="66.png",
    gender="male",
    progress= 0,
    mental= 10,
    money= 50,
    satisfaction= 10,
    text_set_id=12
    )

    new_text67 = Text(
    text="女性A:「同伴のときも聞いたけど、アフターはどうしよっか?」",
    background_image="67.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=12
    )

    new_text68 = Text(
    text="女性A:「同伴のときも聞いたけど、アフターはどうしよっか?」",
    background_image="68.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=12
    )

    new_text69 = Text(
    text="Takuya:「1時間だけならOK」",
    background_image="69.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=14
    )

    new_text70 = Text(
    ext="女性A:「おっけー。1時間だけでも嬉しい。楽しもうね。」",
    background_image="70.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=14
    )

    new_text71 = Text(
    text="本日はアフターが1時間で終わった。帰宅後、課題に少し取り組めた。",
    background_image="71.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=14
    )

    new_text72 = Text(
    text="お金が30万減った。/ 女の子の満足度が10上がった。/ 課題進捗が20%上がっ﻿た。/ メンタルが10減った。",
    background_image="72.png",
    gender="male",
    progress= 20,
    mental= -10,
    money= -30,
    satisfaction= 10,
    text_set_id=14
    )

    new_text73 = Text(
    text="ひらちん「次の日、俺はなんとか9時に起床してジーズにきた。今日は水曜もくもくの日。集中して課題を終わらせる気持ちで頑張るぞ!」",
    background_image="73.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=14
    )

    new_text74 = Text(
    text="ひらちん「あ、山崎先生だ!忙しそうだし、質問していいのかなぁ。どうしよう。」",
    background_image="74.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=14
    )

    new_text75 = Text(
    text="ひらちん「あ、山崎先生だ!忙しそうだし、質問していいのかなぁ。どうしよう。」",
    background_image="75.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=14
    )

    new_text76 = Text(
    text="Takuya:「誕生日だと思うから最後まで付き合うよ」",
    background_image="76.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=15
    )

    new_text77 = Text(
    text="女性A:「私の誕生日忘れてたくせに調子のいいこといっちゃって。当たり前でしょ。」",
    background_image="77.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=15
    )

    new_text78 = Text(
    text="誕生日忘れていたことを根に持たれ、慰めるために結局朝4時までアフターが続いた。朝6時就寝。この日課題には手をつけられなかった。",
    background_image="78.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=15
    )

    new_text79 = Text(
    text="お金が50万減った。/ 女の子の満足度が10﻿上がった。/ 課題進捗は0のままだ。/ メンタルが20下がった。",
    background_image="79.png",
    gender="male",
    progress= 0,
    mental= -20,
    money= -50,
    satisfaction= 10,
    text_set_id=15
    )

    new_text80 = Text(
    text="ひらちん「次の日、起きたら10時27分だ。さてと、Zoomの背景をとよぴーさんに設定して、リモート参加するか。今日は水曜もくもくの日。課題頑張らないとだけどまだ眠たい。。」",
    background_image="80.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=15
    )

    new_text81 = Text(
    ext="ひらちん「あ、山崎先生だ!忙しそうだし、質問していいのかなぁ。どうしよう。」",
    background_image="81.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=15
    )

    new_text82 = Text(
    text="ひらちん「あ、山崎先生だ!忙しそうだし、質問していいのかなぁ。どうしよう。」",
    background_image="82.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=15
    )

    new_text83 = Text(
    text="Takuya:「もちろん最後まで一緒だよ」",
    background_image="83.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=16
    )

    new_text84 = Text(
    text="女性A:「ありがとう!Takuya大好き!」",
    background_image="84.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=16
    )

    new_text85 = Text(
    text="同伴時に今日は最後まで一緒に居ると約束したため、朝4時まで楽しいアフターが続いた。朝6時就寝。この日課題には手をつけられなかった。",
    background_image="85.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=16
    )

    new_text86 = Text(
    text="お金が30万減った。/ 女の子の満足度が20上がった。/ 課題進捗は0のままだ。/ メンタルが10下がった。",
    background_image="86.png",
    gender="male",
    progress= 0,
    mental= -10,
    money= -30,
    satisfaction= 20,
    text_set_id=16
    )

    new_text87 = Text(
    text="ひらちん「次の日、起きたら10時27分だ。さてと、Zoomの背景をとよぴーさんに設定して、リモート参加するか。今日は水曜もくもくの日。課題頑張らないとだけどまだ眠たい。。」",
    background_image="87.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=16
    )

    new_text88 = Text(
    text="ひらちん「あ、山崎先生だ!忙しそうだし、質問していいのかなぁ。どうしよう。」",
    background_image="88.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=16
    )

    new_text89 = Text(
    text="ひらちん「あ、山崎先生だ!忙しそうだし、質問していいのかなぁ。どうしよう。」",
    background_image="89.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=16
    )

    new_text90 = Text(
    text="Takuya:「今日課題があるからアフターなしでお願いしたい」",
    background_image="90.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=17
    )

    new_text91 = Text(
    text="女性A:「そっか、仕方ないよね。わかったよ。課題頑張ってね。」",
    background_image="91.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=17
    )

    new_text92 = Text(
    text="本日は女の子の気遣いもあり、アフターがなく帰宅することができた。深夜1時から寝るまでの間、もくもくと課題に取り組んだ。",
    background_image="92.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=17
    )

    new_text93 = Text(
    text="女の子の満足度が10上がった。/ 課題進捗が40%上がった。/ メンタルが20上がった。",
    background_image="93.png",
    gender="male",
    progress= 40,
    mental= 20,
    money= 0,
    satisfaction= 10,
    text_set_id=17
    )

    new_text94= Text(
    text="ひらちん「次の日、9時に起床。昨晩はアフターがなかったからよく眠れた。今日は水曜もくもくの日。昨晩エラーが出てしまった部分を山崎先生に聞いて、課題終わらせるぞ!」",
    background_image="94.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=17
    )

    new_text95 = Text(
    text="ひらちん「あ、山崎先生だ!忙しそうだし、質問していいのかなぁ。どうしよう。」",
    background_image="95.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=17
    )

    new_text96 = Text(
    text="ひらちん「あ、山崎先生だ!忙しそうだし、質問していいのかなぁ。どうしよう。」",
    background_image="96.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=17
    )



    new_text9 = Text(
    
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
    session.add(new_text44)
    session.add(new_text45)
    session.add(new_text46)
    session.add(new_text47)
    session.add(new_text48)
    session.add(new_text49)
    session.add(new_text50)
    session.add(new_text51)
    session.add(new_text52)
    session.add(new_text53)
    session.add(new_text54)
    session.add(new_text55)
    session.add(new_text56)
    session.add(new_text57)
    session.add(new_text58)
    session.add(new_text59)
    session.add(new_text60)
    session.add(new_text61)
    session.add(new_text62)
    session.add(new_text63)
    session.add(new_text64)
    session.add(new_text65)
    session.add(new_text66)
    session.add(new_text67)
    session.add(new_text68)
    session.add(new_text69)
    session.add(new_text70)
    session.add(new_text71)
    session.add(new_text72)
    session.add(new_text73)
    session.add(new_text74)
    session.add(new_text75)
    session.add(new_text76)
    session.add(new_text77)
    session.add(new_text78)
    session.add(new_text79)
    session.add(new_text80)
    session.add(new_text81)
    session.add(new_text82)
    session.add(new_text83)
    session.add(new_text84)
    session.add(new_text85)
    session.add(new_text86)
    session.add(new_text87)
    session.add(new_text88)
    session.add(new_text89)
    session.add(new_text90)
    session.add(new_text91)
    session.add(new_text92)
    session.add(new_text93)
    session.add(new_text94)
    session.add(new_text95)
    session.add(new_text96)
    # session.add(new_text97)
    # session.add(new_text98)
    # session.add(new_text99)
    # session.add(new_text100)
    # session.add(new_text101)
    # session.add(new_text102)
    # session.add(new_text103)
    # session.add(new_text104)
    # session.add(new_text105)
    # session.add(new_text106)

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


    new_choice18 = Choice(choice_text="1時間だけならOK", scene_id=1, belong_text_set_id=8)
    new_choice19 = Choice(choice_text="誕生日だと思うから最後まで付き合うよ", scene_id=1, belong_text_set_id=8)
    new_choice20 = Choice(choice_text="もちろん最後まで一緒だよ", scene_id=1, belong_text_set_id=8)
    new_choice21 = Choice(choice_text="今日課題があるからアフターなしでお願いしたい", scene_id=1, belong_text_set_id=8)
    new_choice22 = Choice(choice_text="1時間だけならOK", scene_id=1, belong_text_set_id=9)
    new_choice23 = Choice(choice_text="誕生日だと思うから最後まで付き合うよ", scene_id=1, belong_text_set_id=9)
    new_choice24 = Choice(choice_text="もちろん最後まで一緒だよ", scene_id=1, belong_text_set_id=9)
    new_choice25 = Choice(choice_text="今日課題があるからアフターなしでお願いしたい", scene_id=1, belong_text_set_id=9)
    new_choice26 = Choice(choice_text="1時間だけならOK", scene_id=1, belong_text_set_id=10)
    new_choice27 = Choice(choice_text="誕生日だと思うから最後まで付き合うよ", scene_id=1, belong_text_set_id=10)
    new_choice28 = Choice(choice_text="もちろん最後まで一緒だよ", scene_id=1, belong_text_set_id=10)
    new_choice29 = Choice(choice_text="今日課題があるからアフターなしでお願いしたい", scene_id=1, belong_text_set_id=10)
    new_choice30 = Choice(choice_text="1時間だけならOK", scene_id=1, belong_text_set_id=11)
    new_choice31 = Choice(choice_text="誕生日だと思うから最後まで付き合うよ", scene_id=1, belong_text_set_id=11)
    new_choice32 = Choice(choice_text="もちろん最後まで一緒だよ", scene_id=1, belong_text_set_id=11)
    new_choice33 = Choice(choice_text="今日課題があるからアフターなしでお願いしたい", scene_id=1, belong_text_set_id=11)
    new_choice34 = Choice(choice_text="1時間だけならOK", scene_id=1, belong_text_set_id=12)
    new_choice35 = Choice(choice_text="誕生日だと思うから最後まで付き合うよ", scene_id=1, belong_text_set_id=12)
    new_choice36 = Choice(choice_text="もちろん最後まで一緒だよ", scene_id=1, belong_text_set_id=12)
    new_choice37 = Choice(choice_text="今日課題があるからアフターなしでお願いしたい", scene_id=1, belong_text_set_id=12)
    new_choice38 = Choice(choice_text="質問する!", scene_id=1, belong_text_set_id=14)
    new_choice39 = Choice(choice_text="目で訴える", scene_id=1, belong_text_set_id=14)
    new_choice40 = Choice(choice_text="遠慮しておく", scene_id=1, belong_text_set_id=14)
    new_choice41 = Choice(choice_text="質問する!", scene_id=1, belong_text_set_id=15)
    new_choice42 = Choice(choice_text="目で訴える", scene_id=1, belong_text_set_id=15)
    new_choice43 = Choice(choice_text="遠慮しておく", scene_id=1, belong_text_set_id=15)
    new_choice44 = Choice(choice_text="質問する!", scene_id=1, belong_text_set_id=16)
    new_choice45 = Choice(choice_text="目で訴える", scene_id=1, belong_text_set_id=16)
    new_choice46 = Choice(choice_text="遠慮しておく", scene_id=1, belong_text_set_id=16)
    new_choice47 = Choice(choice_text="質問する!", scene_id=1, belong_text_set_id=17)
    new_choice48 = Choice(choice_text="目で訴える", scene_id=1, belong_text_set_id=17)
    new_choice49 = Choice(choice_text="遠慮しておく", scene_id=1, belong_text_set_id=17)



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
    session.add(new_choice18)
    session.add(new_choice19)
    session.add(new_choice20)
    session.add(new_choice21)
    session.add(new_choice22)
    session.add(new_choice23)
    session.add(new_choice24)
    session.add(new_choice25)
    session.add(new_choice26)
    session.add(new_choice27)
    session.add(new_choice28)
    session.add(new_choice29)
    session.add(new_choice30)
    session.add(new_choice31)
    session.add(new_choice32)
    session.add(new_choice33)
    session.add(new_choice34)
    session.add(new_choice35)
    session.add(new_choice36)
    session.add(new_choice37)
    session.add(new_choice38)
    session.add(new_choice39)
    session.add(new_choice40)
    session.add(new_choice41)
    session.add(new_choice42)
    session.add(new_choice43)
    session.add(new_choice44)
    session.add(new_choice45)
    session.add(new_choice46)
    session.add(new_choice47)
    session.add(new_choice48)
    session.add(new_choice49)
    
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

    new_choice_text_set28 = ChoiceTextSet(choice_id=new_choice18.id, text_set_id=new_text_set14.id)
    new_choice_text_set29 = ChoiceTextSet(choice_id=new_choice19.id, text_set_id=new_text_set15.id)
    new_choice_text_set30 = ChoiceTextSet(choice_id=new_choice20.id, text_set_id=new_text_set16.id)
    new_choice_text_set31 = ChoiceTextSet(choice_id=new_choice21.id, text_set_id=new_text_set17.id)
    new_choice_text_set32 = ChoiceTextSet(choice_id=new_choice22.id, text_set_id=new_text_set14.id)
    new_choice_text_set33 = ChoiceTextSet(choice_id=new_choice23.id, text_set_id=new_text_set15.id)
    new_choice_text_set34 = ChoiceTextSet(choice_id=new_choice24.id, text_set_id=new_text_set16.id)
    new_choice_text_set35 = ChoiceTextSet(choice_id=new_choice25.id, text_set_id=new_text_set17.id)
    new_choice_text_set36 = ChoiceTextSet(choice_id=new_choice26.id, text_set_id=new_text_set14.id)
    new_choice_text_set37 = ChoiceTextSet(choice_id=new_choice27.id, text_set_id=new_text_set15.id)
    new_choice_text_set38 = ChoiceTextSet(choice_id=new_choice28.id, text_set_id=new_text_set16.id)
    new_choice_text_set39 = ChoiceTextSet(choice_id=new_choice29.id, text_set_id=new_text_set17.id)
    new_choice_text_set40 = ChoiceTextSet(choice_id=new_choice30.id, text_set_id=new_text_set14.id)
    new_choice_text_set41 = ChoiceTextSet(choice_id=new_choice31.id, text_set_id=new_text_set15.id)
    new_choice_text_set42 = ChoiceTextSet(choice_id=new_choice32.id, text_set_id=new_text_set16.id)
    new_choice_text_set43 = ChoiceTextSet(choice_id=new_choice33.id, text_set_id=new_text_set17.id)
    new_choice_text_set44 = ChoiceTextSet(choice_id=new_choice34.id, text_set_id=new_text_set14.id)
    new_choice_text_set45 = ChoiceTextSet(choice_id=new_choice35.id, text_set_id=new_text_set15.id)
    new_choice_text_set46 = ChoiceTextSet(choice_id=new_choice36.id, text_set_id=new_text_set16.id)
    new_choice_text_set47 = ChoiceTextSet(choice_id=new_choice37.id, text_set_id=new_text_set17.id)



    new_choice_text_set48 = ChoiceTextSet(choice_id=new_choice38.id, text_set_id=new_text_set18.id)
    new_choice_text_set49 = ChoiceTextSet(choice_id=new_choice38.id, text_set_id=new_text_set19.id)
    new_choice_text_set50 = ChoiceTextSet(choice_id=new_choice39.id, text_set_id=new_text_set20.id)
    new_choice_text_set51 = ChoiceTextSet(choice_id=new_choice39.id, text_set_id=new_text_set21.id)
    new_choice_text_set52 = ChoiceTextSet(choice_id=new_choice40.id, text_set_id=new_text_set22.id)

    new_choice_text_set53 = ChoiceTextSet(choice_id=new_choice41.id, text_set_id=new_text_set23.id)
    new_choice_text_set54 = ChoiceTextSet(choice_id=new_choice41.id, text_set_id=new_text_set24.id)
    new_choice_text_set55 = ChoiceTextSet(choice_id=new_choice42.id, text_set_id=new_text_set25.id)
    new_choice_text_set56 = ChoiceTextSet(choice_id=new_choice42.id, text_set_id=new_text_set26.id)
    new_choice_text_set57 = ChoiceTextSet(choice_id=new_choice43.id, text_set_id=new_text_set27.id)

    new_choice_text_set58 = ChoiceTextSet(choice_id=new_choice44.id, text_set_id=new_text_set23.id)
    new_choice_text_set59 = ChoiceTextSet(choice_id=new_choice44.id, text_set_id=new_text_set24.id)
    new_choice_text_set60 = ChoiceTextSet(choice_id=new_choice45.id, text_set_id=new_text_set25.id)
    new_choice_text_set61 = ChoiceTextSet(choice_id=new_choice45.id, text_set_id=new_text_set26.id)
    new_choice_text_set62 = ChoiceTextSet(choice_id=new_choice46.id, text_set_id=new_text_set27.id)

    new_choice_text_set63 = ChoiceTextSet(choice_id=new_choice47.id, text_set_id=new_text_set28.id)
    new_choice_text_set64 = ChoiceTextSet(choice_id=new_choice47.id, text_set_id=new_text_set29.id)
    new_choice_text_set65 = ChoiceTextSet(choice_id=new_choice48.id, text_set_id=new_text_set30.id)
    new_choice_text_set66 = ChoiceTextSet(choice_id=new_choice48.id, text_set_id=new_text_set31.id)
    new_choice_text_set67 = ChoiceTextSet(choice_id=new_choice49.id, text_set_id=new_text_set32.id)


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
    session.add(new_choice_text_set22)
    session.add(new_choice_text_set23)
    session.add(new_choice_text_set24)
    session.add(new_choice_text_set25)
    session.add(new_choice_text_set26)
    session.add(new_choice_text_set27)
    session.add(new_choice_text_set28)
    session.add(new_choice_text_set29)
    session.add(new_choice_text_set30)
    session.add(new_choice_text_set31)
    session.add(new_choice_text_set32)
    session.add(new_choice_text_set33)
    session.add(new_choice_text_set34)
    session.add(new_choice_text_set35)
    session.add(new_choice_text_set36)
    session.add(new_choice_text_set37)
    session.add(new_choice_text_set38)
    session.add(new_choice_text_set39)
    session.add(new_choice_text_set40)
    session.add(new_choice_text_set41)
    session.add(new_choice_text_set42)
    session.add(new_choice_text_set43)
    session.add(new_choice_text_set44)
    session.add(new_choice_text_set45)
    session.add(new_choice_text_set46)
    session.add(new_choice_text_set47)
    session.add(new_choice_text_set48)
    session.add(new_choice_text_set49)
    session.add(new_choice_text_set50)
    session.add(new_choice_text_set51)
    session.add(new_choice_text_set52)
    session.add(new_choice_text_set53)
    session.add(new_choice_text_set54)
    session.add(new_choice_text_set55)
    session.add(new_choice_text_set56)
    session.add(new_choice_text_set57)
    session.add(new_choice_text_set58)
    session.add(new_choice_text_set59)
    session.add(new_choice_text_set60)
    session.add(new_choice_text_set61)
    session.add(new_choice_text_set62)
    session.add(new_choice_text_set63)
    session.add(new_choice_text_set64)
    session.add(new_choice_text_set65)
    session.add(new_choice_text_set66)
    session.add(new_choice_text_set67)

    # commit the session
    session.commit()


    print("Data inserted successfully.")

if __name__ == "__main__":
    main()
