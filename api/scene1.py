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
    session.add(new_text_set1)
    session.add(new_text_set2)
    session.add(new_text_set3)
    session.add(new_text_set4)
    session.flush()

    # create 14 Texts

    new_text1 = Text(
    text="ひらちん：「お、今日夕方から同伴予定の女の子Aから連絡だ。」",
    background_image="Example background",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=new_text_set1.id
    )
    # session.add(new_text1)


    # new_text1 = Text(text="Example text 1", background_image="Example background 1", gender="Example gender", progress="Example progress", mental="Example mental", money="Example money", satisfaction="Example satisfaction", text_set_id=new_text_set1.id)
    # new_text2 = Text(text="Example text 2", background_image="Example background 2", gender="Example gender", progress="Example progress", mental="Example mental", money="Example money", satisfaction="Example satisfaction", text_set_id=new_text_set1.id)
    # ... continue for all 14 texts
    new_text2 = Text(
    text="女性A：「今日Takuyaに会えるの楽しみー！どれくらいお金持っていけばいいかな？」",
    background_image="Example background",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=new_text_set1.id
    )

    new_text3 = Text(
    text="女性A：「今日Takuyaに会えるの楽しみー！どれくらいお金持っていけばいいかな？」",
    background_image="Example background",
    gender="female",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=new_text_set1.id
    )

    new_text4 = Text(
    text="Takuya：「無理しない範囲で大丈夫だよ」",
    background_image="Example background",
    gender="male",
    progress= 0,
    mental= 0,
    money= 0,
    satisfaction= 0,
    text_set_id=new_text_set2.id
    )





    session.add(new_text1)
    session.add(new_text2)
    session.add(new_text3)
    session.add(new_text4)
    # ... continue for all 14 texts

    # create 2 Choices
    new_choice1 = Choice(choice_text="持ってこれるだけ持ってこい", scene_id=new_scene.id)
    new_choice2 = Choice(choice_text="無理しない範囲で大丈夫だよ", scene_id=new_scene.id)
    session.add(new_choice1)
    session.add(new_choice2)
    session.flush()

    # create 3 ChoiceTextSets
    new_choice_text_set1 = ChoiceTextSet(choice_id=new_choice2.id, text_set_id=new_text_set2.id)
    new_choice_text_set2 = ChoiceTextSet(choice_id=new_choice1.id, text_set_id=new_text_set3.id)
    new_choice_text_set3 = ChoiceTextSet(choice_id=new_choice1.id, text_set_id=new_text_set4.id)
    session.add(new_choice_text_set1)
    session.add(new_choice_text_set2)
    session.add(new_choice_text_set3)

    # commit the session
    session.commit()


    print("Data inserted successfully.")

if __name__ == "__main__":
    main()
