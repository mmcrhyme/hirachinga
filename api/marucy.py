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
    new_text_set33 = TextSet(scene_id=1)
    new_text_set34 = TextSet(scene_id=1)

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
    session.add(new_text_set33)
    session.add(new_text_set34)

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

    new_text97 = Text(
    text="(質問をする!)ひらちん「山崎先生!課題で分からない点があるので質問させてください!」",
    background_image="97.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=18
    )
    # session.add(new_text1)


    # new_text1 = Text(text="Example text 1", background_image="Example background 1", gender="Example gender", progress="Example progress", mental="Example mental", money="Example money", satisfaction="Example satisfaction", text_set_id=new_text_set1.id)
    # new_text2 = Text(text="Example text 2", background_image="Example background 2", gender="Example gender", progress="Example progress", mental="Example mental", money="Example money", satisfaction="Example satisfaction", text_set_id=new_text_set1.id)
    # ... continue for all 14 texts
    new_text98 = Text(
    text="山崎先生「お!ひらちい頑張ってるね!もちろんだよ!何でも質問してくれ!」",
    background_image="98.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=18
    )

    new_text99 = Text(
    text="課題進捗が50%上がった。/ メンタルが20上がった。",
    background_image="99.png",
    gender="male",
    progress= 50,
    mental= 20,
    money= 0,
    satisfaction= 0,
    text_set_id=18
    )

    new_text100 = Text(
    text="Takuya:「今日は20時から1時の営業で、確か指名は女性Bだけ。課題あるから何事もなくアフターなしで帰りたいなぁ。」",
    background_image="100.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=18
    )

    new_text101 = Text(
    text="Takuya:「あ、いらっしゃい。今日は指名してくれてありがとう。」",
    background_image="101.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=18
    )

    new_text102 = Text(
    text="女性B:「今日は最初から最後まで指名してるから、ゆっくり話せるの嬉しい♪」",
    background_image="102.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=18
    )

    new_text103 = Text(
    text="Takuya:「そうだね。じゃああっちの..席...で.......(驚汗)」",
    background_image="103.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=18
    )

    new_text104 = Text(
    text="女性C:「ちょっとTakuya〜!1年前からこの日って約束して指名してたのに誰よこいつ。Takuyaは私のものよ〜!!!」",
    background_image="104.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=18
    )

    new_text105 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="105.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=18
    )

    new_text106 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="106.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=18
    )

    new_text107 = Text(
    text="(質問をする!)ひらちん「山崎先生!課題で分からない点があるので質問させてください!」",
    background_image="107.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=19
    )

    new_text108 = Text(
    text="山崎先生「ごめんね、今から帰っておじゃる丸観るからまた今度ね。」",
    background_image="108.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=19
    )

    new_text109 = Text(
    text="課題進捗が20%上がった。/ メンタルが10下がった。/ おじゃる丸に嫉妬するようになった。",
    background_image="109.png",
    gender="male",
    progress= 20,
    mental= -10,
    money= 0,
    satisfaction= 0,
    text_set_id=19
    )

    new_text110 = Text(
    text="Takuya:「今日は20時から1時の営業で、確か指名は女性Bだけ。課題あるから何事もなくアフターなしで帰りたいなぁ。」",
    background_image="110.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=19
    )

    new_text111 = Text(
    text="Takuya:「あ、いらっしゃい。今日は指名してくれてありがとう。」",
    background_image="111.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=19
    )

    new_text112 = Text(
    text="女性B:「今日は最初から最後まで指名してるから、ゆっくり話せるの嬉しい♪」",
    background_image="112.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=19
    )

    new_text113 = Text(
    text="Takuya:「そうだね。じゃああっちの..席...で.......(驚汗)」",
    background_image="113.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=19
    )

    new_text114 = Text(
    text="女性C:「ちょっとTakuya〜!1年前からこの日って約束して指名してたのに誰よこいつ。Takuyaは私のものよ〜!!!」",
    background_image="114.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=19
    )

    new_text115 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="115.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=19
    )

    new_text116 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="116.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=19
    )

    new_text117 = Text(
   text="(目で訴える)ひらちん(じーっ。。。じーっ。。。じー's。。。)",
    background_image="117.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=20
    )

    new_text118 = Text(
    text="山崎先生「お、どうしたひらちい!課題進捗はどんな感じ?」",
    background_image="118.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=20
    )

    new_text119 = Text(
    text="素直に分からないところ1つ1つ質問できた。/ 課題進捗が60%上がった。/ メンタルが30上がった。/ 山崎先生のことが大好きになった。",
    background_image="119.png",
    gender="male",
    progress= 60,
    mental= 30,
    money= 0,
    satisfaction= 0,
    text_set_id=20
    )

    new_text120 = Text(
    text="Takuya:「今日は20時から1時の営業で、確か指名は女性Bだけ。課題あるから何事もなくアフターなしで帰りたいなぁ。」",
    background_image="120.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=20
    )

    new_text121 = Text(
    text="Takuya:「あ、いらっしゃい。今日は指名してくれてありがとう。」",
    background_image="121.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=20
    )

    new_text122 = Text(
    text="女性B:「今日は最初から最後まで指名してるから、ゆっくり話せるの嬉しい♪」",
    background_image="122.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=20
    )

    new_text123 = Text(
    text="Takuya:「そうだね。じゃああっちの..席...で.......(驚汗)」",
    background_image="123.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=20
    )

    new_text124 = Text(
    text="女性C:「ちょっとTakuya〜!1年前からこの日って約束して指名してたのに誰よこいつ。Takuyaは私のものよ〜!!!」",
    background_image="124.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=20
    )

    new_text125 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="125.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=20
    )

    new_text126 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="126.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=20
    )

    new_text127 = Text(
    text="(目で訴える)ひらちん(じーっ。。。じーっ。。。じー's。。。)",
    background_image="127.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=21
    )

    new_text128 = Text(
    text="(.................。山崎先生もこちらをじーっと見つめ返している。)(山崎先生のテレパシー:「K、僕と悪魔の契約を結ぶか...?」)",
    background_image="128.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=21
    )

    new_text129 = Text(
    text="山崎先生と悪魔の契約を交わし、山崎先生の目を手に入れた。/ 課題進捗が80%上がった。/ メンタルが60下がった。",
    background_image="129.png",
    gender="male",
    progress= 80,
    mental= -60,
    money= 0,
    satisfaction= 0,
    text_set_id=21
    )

    new_text130 = Text(
    text="Takuya:「今日は20時から1時の営業で、確か指名は女性Bだけ。課題あるから何事もなくアフターなしで帰りたいなぁ。」",
    background_image="130.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=21
    )

    new_text131 = Text(
    text="Takuya:「あ、いらっしゃい。今日は指名してくれてありがとう。」",
    background_image="131.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=21
    )

    new_text132 = Text(
    text="女性B:「今日は最初から最後まで指名してるから、ゆっくり話せるの嬉しい♪」",
    background_image="132.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=21
    )

    new_text133 = Text(
    text="Takuya:「そうだね。じゃああっちの..席...で.......(驚汗)」",
    background_image="133.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=21
    )

    new_text134 = Text(
    text="女性C:「ちょっとTakuya〜!1年前からこの日って約束して指名してたのに誰よこいつ。Takuyaは私のものよ〜!!!」",
    background_image="134.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=21
    )

    new_text135 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="135.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=21
    )

    new_text136 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="136.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=21
    )

    new_text137 = Text(
    text="(遠慮しておく) ひらちん「山崎先生、忙しそうだしまずは自分でエラーと戦ってみるかぁ。」",
    background_image="137.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=22
    )

    new_text138 = Text(
    text="意外と集中できて、課題が進んだ。/ 課題進捗が60%上がった。/ メンタルが30上がった。",
    background_image="138.png",
    gender="male",
    progress= 60,
    mental= 30,
    money= 0,
    satisfaction= 0,
    text_set_id=22
    )

    new_text139 = Text(
    text="Takuya:「今日は20時から1時の営業で、確か指名は女性Bだけ。課題あるから何事もなくアフターなしで帰りたいなぁ。」",
    background_image="139.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=22
    )

    new_text140 = Text(
    text="Takuya:「あ、いらっしゃい。今日は指名してくれてありがとう。」",
    background_image="140.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=22
    )

    new_text141 = Text(
    text="女性B:「今日は最初から最後まで指名してるから、ゆっくり話せるの嬉しい♪」",
    background_image="141.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=22
    )

    new_text142 = Text(
    text="Takuya:「そうだね。じゃああっちの..席...で.......(驚汗)」",
    background_image="142.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=22
    )

    new_text143 = Text(
    text="女性C:「ちょっとTakuya〜!1年前からこの日って約束して指名してたのに誰よこいつ。Takuyaは私のものよ〜!!!」",
    background_image="143.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=22
    )

    new_text144 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="144.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=22
    )

    new_text145 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="145.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=22
    )

    new_text146 = Text(
    text="(質問をする!)ひらちん「山崎先生!課題で分からない点があるので質問させてください!」",
    background_image="146.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=23
    )

    new_text147 = Text(
    text="山崎先生「お!ひらちい頑張ってるね!もちろんだよ!何でも質問してくれ!」",
    background_image="147.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=23
    )

    new_text148 = Text(
    text="課題進捗が50%上がった。/ メンタルが20上がった。",
    background_image="148.png",
    gender="male",
    progress= 50,
    mental= 20,
    money= 0,
    satisfaction= 0,
    text_set_id=23
    )

    new_text149 = Text(
    text="Takuya:「今日は20時から1時の営業で、確か指名は女性Bだけ。課題あるから何事もなくアフターなしで帰りたいなぁ。」",
    background_image="149.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=23
    )

    new_text150 = Text(
    text="Takuya:「あ、いらっしゃい。今日は指名してくれてありがとう。」",
    background_image="150.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=23
    )

    new_text151 = Text(
    text="女性B:「今日は最初から最後まで指名してるから、ゆっくり話せるの嬉しい♪」",
    background_image="151.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=23
    )

    new_text152 = Text(
    text="Takuya:「そうだね。じゃああっちの..席...で.......(驚汗)」",
    background_image="152.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=23
    )

    new_text153 = Text(
    text="女性C:「ちょっとTakuya〜!1年前からこの日って約束して指名してたのに誰よこいつ。Takuyaは私のものよ〜!!!」",
    background_image="153.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=23
    )

    new_text154 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="154.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=23
    )

    new_text155 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="155.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=23
    )

    new_text156 = Text(
    text="(質問をする!)ひらちん「山崎先生!課題で分からない点があるので質問させてください!」",
    background_image="156.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=24
    )

    new_text157 = Text(
    text="山崎先生「ごめんね、今から帰っておじゃる丸観るからまた今度ね。」",
    background_image="157.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=24
    )

    new_text158 = Text(
    text="課題進捗が20%上がった。/ メンタルが10下がった。/ おじゃる丸に嫉妬するようになった。",
    background_image="158.png",
    gender="male",
    progress= 20,
    mental= -10,
    money= 0,
    satisfaction= 0,
    text_set_id=24
    )

    new_text159 = Text(
    text="Takuya:「今日は20時から1時の営業で、確か指名は女性Bだけ。課題あるから何事もなくアフターなしで帰りたいなぁ。」",
    background_image="159.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=24
    )

    new_text160 = Text(
    text="Takuya:「あ、いらっしゃい。今日は指名してくれてありがとう。」",
    background_image="160.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=24
    )

    new_text161 = Text(
    text="女性B:「今日は最初から最後まで指名してるから、ゆっくり話せるの嬉しい♪」",
    background_image="161.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=24
    )

    new_text162 = Text(
    text="Takuya:「そうだね。じゃああっちの..席...で.......(驚汗)」",
    background_image="162.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=24
    )

    new_text163 = Text(
    text="女性C:「ちょっとTakuya〜!1年前からこの日って約束して指名してたのに誰よこいつ。Takuyaは私のものよ〜!!!」",
    background_image="163.png",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=24
    )

    new_text164 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="164.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=24
    )

    new_text165 = Text(
    text="女の子2人が目の前で殴り合いのケンカをはじめてしまった。女性Bは割りと優しいから話せばわかってくれるけど、女性Cは怒らせたら特に手を付けられないタイプ。女性Cは超太客というのもあり上手くこの場を落ち着かせたい。どうやって鎮火させよう?",
    background_image="165.png",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=24
    )


    session.add(new_text97)
    session.add(new_text98)
    session.add(new_text99)
    session.add(new_text100)
    session.add(new_text101)
    session.add(new_text102)
    session.add(new_text103)
    session.add(new_text104)
    session.add(new_text105)
    session.add(new_text106)
    session.add(new_text107)
    session.add(new_text108)
    session.add(new_text109)
    session.add(new_text110)
    session.add(new_text111)
    session.add(new_text112)
    session.add(new_text113)
    session.add(new_text114)
    session.add(new_text115)
    session.add(new_text116)
    session.add(new_text117)
    session.add(new_text118)
    session.add(new_text119)
    session.add(new_text120)
    session.add(new_text121)
    session.add(new_text122)
    session.add(new_text123)
    session.add(new_text124)
    session.add(new_text125)
    session.add(new_text126)
    session.add(new_text127)
    session.add(new_text128)
    session.add(new_text129)
    session.add(new_text130)
    session.add(new_text131)
    session.add(new_text132)
    session.add(new_text133)
    session.add(new_text134)
    session.add(new_text135)
    session.add(new_text136)
    session.add(new_text137)
    session.add(new_text138)
    session.add(new_text139)
    session.add(new_text140)
    session.add(new_text141)
    session.add(new_text142)
    session.add(new_text143)
    session.add(new_text144)
    session.add(new_text145)
    session.add(new_text146)
    session.add(new_text147)
    session.add(new_text148)
    session.add(new_text149)
    session.add(new_text150)
    session.add(new_text151)
    session.add(new_text152)
    session.add(new_text153)
    session.add(new_text154)
    session.add(new_text155)
    session.add(new_text156)
    session.add(new_text157)
    session.add(new_text158)
    session.add(new_text159)
    session.add(new_text160)
    session.add(new_text161)
    session.add(new_text162)
    session.add(new_text163)
    session.add(new_text164)
    session.add(new_text165)


    # create 2 Choices
    new_choice50 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=18)
    new_choice51 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=18)
    new_choice52 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=19)
    new_choice53 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=19)
    new_choice54 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=20)
    new_choice55 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=20)
    new_choice56 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=21)
    new_choice57 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=21)
    new_choice58 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=22)
    new_choice59 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=22)
    new_choice60 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=23)
    new_choice61 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=23)
    new_choice62 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=24)
    new_choice63 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=24)
    new_choice64 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=25)
    new_choice65 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=25)
    new_choice66 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=26)
    new_choice67 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=26)
    new_choice68 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=27)
    new_choice69 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=27)
    new_choice70 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=28)
    new_choice71 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=28)
    new_choice72 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=29)
    new_choice73 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=29)
    new_choice74 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=30)
    new_choice75 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=30)
    new_choice76 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=31)
    new_choice77 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=31)
    new_choice78 = Choice(choice_text="ケンカをとめるために間に入る", scene_id=1, belong_text_set_id=32)
    new_choice79 = Choice(choice_text="しばらくそっとしておく", scene_id=1, belong_text_set_id=32)

    session.add(new_choice50)
    session.add(new_choice51)
    session.add(new_choice52)
    session.add(new_choice53)
    session.add(new_choice54)
    session.add(new_choice55)
    session.add(new_choice56)
    session.add(new_choice57)
    session.add(new_choice58)
    session.add(new_choice59)
    session.add(new_choice60)
    session.add(new_choice61)
    session.add(new_choice62)
    session.add(new_choice63)
    session.add(new_choice64)
    session.add(new_choice65)
    session.add(new_choice66)
    session.add(new_choice67)
    session.add(new_choice68)
    session.add(new_choice69)
    session.add(new_choice70)
    session.add(new_choice71)
    session.add(new_choice72)
    session.add(new_choice73)
    session.add(new_choice74)
    session.add(new_choice75)
    session.add(new_choice76)
    session.add(new_choice77)
    session.add(new_choice78)
    session.add(new_choice79)
    session.flush()

    # create 3 ChoiceTextSets
    new_choice_text_set68 = ChoiceTextSet(choice_id=new_choice50.id, text_set_id=new_text_set33.id)
    new_choice_text_set69 = ChoiceTextSet(choice_id=new_choice50.id, text_set_id=new_text_set34.id)
    new_choice_text_set70 = ChoiceTextSet(choice_id=new_choice51.id, text_set_id=new_text_set33.id)
    new_choice_text_set71 = ChoiceTextSet(choice_id=new_choice51.id, text_set_id=new_text_set34.id)
    new_choice_text_set72 = ChoiceTextSet(choice_id=new_choice52.id, text_set_id=new_text_set33.id)
    new_choice_text_set73 = ChoiceTextSet(choice_id=new_choice52.id, text_set_id=new_text_set34.id)
    new_choice_text_set74 = ChoiceTextSet(choice_id=new_choice53.id, text_set_id=new_text_set33.id)
    new_choice_text_set75 = ChoiceTextSet(choice_id=new_choice53.id, text_set_id=new_text_set34.id)
    new_choice_text_set76 = ChoiceTextSet(choice_id=new_choice54.id, text_set_id=new_text_set33.id)
    new_choice_text_set77 = ChoiceTextSet(choice_id=new_choice54.id, text_set_id=new_text_set34.id)
    new_choice_text_set78 = ChoiceTextSet(choice_id=new_choice55.id, text_set_id=new_text_set33.id)
    new_choice_text_set79 = ChoiceTextSet(choice_id=new_choice55.id, text_set_id=new_text_set34.id)
    new_choice_text_set80 = ChoiceTextSet(choice_id=new_choice56.id, text_set_id=new_text_set33.id)
    new_choice_text_set81 = ChoiceTextSet(choice_id=new_choice56.id, text_set_id=new_text_set34.id)
    new_choice_text_set82 = ChoiceTextSet(choice_id=new_choice57.id, text_set_id=new_text_set33.id)
    new_choice_text_set83 = ChoiceTextSet(choice_id=new_choice57.id, text_set_id=new_text_set34.id)
    new_choice_text_set84 = ChoiceTextSet(choice_id=new_choice58.id, text_set_id=new_text_set33.id)
    new_choice_text_set85 = ChoiceTextSet(choice_id=new_choice58.id, text_set_id=new_text_set34.id)
    new_choice_text_set86 = ChoiceTextSet(choice_id=new_choice59.id, text_set_id=new_text_set33.id)
    new_choice_text_set87 = ChoiceTextSet(choice_id=new_choice59.id, text_set_id=new_text_set34.id)
    new_choice_text_set88 = ChoiceTextSet(choice_id=new_choice60.id, text_set_id=new_text_set33.id)
    new_choice_text_set89 = ChoiceTextSet(choice_id=new_choice60.id, text_set_id=new_text_set34.id)
    new_choice_text_set90 = ChoiceTextSet(choice_id=new_choice61.id, text_set_id=new_text_set33.id)
    new_choice_text_set91 = ChoiceTextSet(choice_id=new_choice61.id, text_set_id=new_text_set34.id)
    new_choice_text_set92 = ChoiceTextSet(choice_id=new_choice62.id, text_set_id=new_text_set33.id)
    new_choice_text_set93 = ChoiceTextSet(choice_id=new_choice62.id, text_set_id=new_text_set34.id)
    new_choice_text_set94 = ChoiceTextSet(choice_id=new_choice63.id, text_set_id=new_text_set33.id)
    new_choice_text_set95 = ChoiceTextSet(choice_id=new_choice63.id, text_set_id=new_text_set34.id)
    new_choice_text_set96 = ChoiceTextSet(choice_id=new_choice64.id, text_set_id=new_text_set33.id)
    new_choice_text_set97 = ChoiceTextSet(choice_id=new_choice64.id, text_set_id=new_text_set34.id)
    new_choice_text_set98 = ChoiceTextSet(choice_id=new_choice65.id, text_set_id=new_text_set33.id)
    new_choice_text_set99 = ChoiceTextSet(choice_id=new_choice65.id, text_set_id=new_text_set34.id)
    new_choice_text_set100 = ChoiceTextSet(choice_id=new_choice66.id, text_set_id=new_text_set33.id)
    new_choice_text_set101 = ChoiceTextSet(choice_id=new_choice66.id, text_set_id=new_text_set34.id)
    new_choice_text_set102 = ChoiceTextSet(choice_id=new_choice67.id, text_set_id=new_text_set33.id)
    new_choice_text_set103 = ChoiceTextSet(choice_id=new_choice67.id, text_set_id=new_text_set34.id)
    new_choice_text_set104 = ChoiceTextSet(choice_id=new_choice68.id, text_set_id=new_text_set33.id)
    new_choice_text_set105 = ChoiceTextSet(choice_id=new_choice68.id, text_set_id=new_text_set34.id)
    new_choice_text_set106 = ChoiceTextSet(choice_id=new_choice69.id, text_set_id=new_text_set33.id)
    new_choice_text_set107 = ChoiceTextSet(choice_id=new_choice69.id, text_set_id=new_text_set34.id)
    new_choice_text_set108 = ChoiceTextSet(choice_id=new_choice70.id, text_set_id=new_text_set33.id)
    new_choice_text_set109 = ChoiceTextSet(choice_id=new_choice70.id, text_set_id=new_text_set34.id)
    new_choice_text_set110 = ChoiceTextSet(choice_id=new_choice71.id, text_set_id=new_text_set33.id)
    new_choice_text_set111 = ChoiceTextSet(choice_id=new_choice71.id, text_set_id=new_text_set34.id)
    new_choice_text_set112 = ChoiceTextSet(choice_id=new_choice72.id, text_set_id=new_text_set33.id)
    new_choice_text_set113 = ChoiceTextSet(choice_id=new_choice72.id, text_set_id=new_text_set34.id)
    new_choice_text_set114 = ChoiceTextSet(choice_id=new_choice73.id, text_set_id=new_text_set33.id)
    new_choice_text_set115 = ChoiceTextSet(choice_id=new_choice73.id, text_set_id=new_text_set34.id)
    new_choice_text_set116 = ChoiceTextSet(choice_id=new_choice74.id, text_set_id=new_text_set33.id)
    new_choice_text_set117 = ChoiceTextSet(choice_id=new_choice74.id, text_set_id=new_text_set34.id)
    new_choice_text_set118 = ChoiceTextSet(choice_id=new_choice75.id, text_set_id=new_text_set33.id)
    new_choice_text_set119 = ChoiceTextSet(choice_id=new_choice75.id, text_set_id=new_text_set34.id)
    new_choice_text_set120 = ChoiceTextSet(choice_id=new_choice76.id, text_set_id=new_text_set33.id)
    new_choice_text_set121 = ChoiceTextSet(choice_id=new_choice76.id, text_set_id=new_text_set34.id)
    new_choice_text_set122 = ChoiceTextSet(choice_id=new_choice77.id, text_set_id=new_text_set33.id)
    new_choice_text_set123 = ChoiceTextSet(choice_id=new_choice77.id, text_set_id=new_text_set34.id)
    new_choice_text_set124 = ChoiceTextSet(choice_id=new_choice78.id, text_set_id=new_text_set33.id)
    new_choice_text_set125 = ChoiceTextSet(choice_id=new_choice78.id, text_set_id=new_text_set34.id)
    new_choice_text_set126 = ChoiceTextSet(choice_id=new_choice79.id, text_set_id=new_text_set33.id)
    new_choice_text_set127 = ChoiceTextSet(choice_id=new_choice79.id, text_set_id=new_text_set34.id)


    session.add(new_choice_text_set68)
    session.add(new_choice_text_set69)
    session.add(new_choice_text_set70)
    session.add(new_choice_text_set71)
    session.add(new_choice_text_set72)
    session.add(new_choice_text_set73)
    session.add(new_choice_text_set74)
    session.add(new_choice_text_set75)
    session.add(new_choice_text_set76)
    session.add(new_choice_text_set77)
    session.add(new_choice_text_set78)
    session.add(new_choice_text_set79)
    session.add(new_choice_text_set80)
    session.add(new_choice_text_set81)
    session.add(new_choice_text_set82)
    session.add(new_choice_text_set83)
    session.add(new_choice_text_set84)
    session.add(new_choice_text_set85)
    session.add(new_choice_text_set86)
    session.add(new_choice_text_set87)
    session.add(new_choice_text_set88)
    session.add(new_choice_text_set89)
    session.add(new_choice_text_set90)
    session.add(new_choice_text_set91)
    session.add(new_choice_text_set92)
    session.add(new_choice_text_set93)
    session.add(new_choice_text_set94)
    session.add(new_choice_text_set95)
    session.add(new_choice_text_set96)
    session.add(new_choice_text_set97)
    session.add(new_choice_text_set98)
    session.add(new_choice_text_set99)
    session.add(new_choice_text_set100)
    session.add(new_choice_text_set101)
    session.add(new_choice_text_set102)
    session.add(new_choice_text_set103)
    session.add(new_choice_text_set104)
    session.add(new_choice_text_set105)
    session.add(new_choice_text_set106)
    session.add(new_choice_text_set107)
    session.add(new_choice_text_set108)
    session.add(new_choice_text_set109)
    session.add(new_choice_text_set110)
    session.add(new_choice_text_set111)
    session.add(new_choice_text_set112)
    session.add(new_choice_text_set113)
    session.add(new_choice_text_set114)
    session.add(new_choice_text_set115)
    session.add(new_choice_text_set116)
    session.add(new_choice_text_set117)
    session.add(new_choice_text_set118)
    session.add(new_choice_text_set119)
    session.add(new_choice_text_set120)
    session.add(new_choice_text_set121)
    session.add(new_choice_text_set122)
    session.add(new_choice_text_set123)
    session.add(new_choice_text_set124)
    session.add(new_choice_text_set125)
    session.add(new_choice_text_set126)
    session.add(new_choice_text_set127)

    # commit the session
    session.commit()


    print("Data inserted successfully.")

if __name__ == "__main__":
    main()
