# Определение персонажей игры.

define alex = Character('Алекс', color="#c8ffc8")
define misha = Character('Михаил', color="#c8ffc8")
define richard = Character('Ричард', color="#c8ffc8")
define emanon = Character('???', color="#c8ffc8")
define boy1 = Character('Мальчик 1', color="#c8ffc8", image="boy1.png")
define boy2 = Character('Мальчик 2', color="#c8ffc8")
define boy3 = Character('Мальчик 3', color="#c8ffc8")
define boy4 = Character('Мальчик 4', color="#c8ffc8")
define boy5 = Character('Мальчик 5', color="#c8ffc8")
define prin = Character('Директриса', color="#c8ffc8")
define geor = Character('Доктор Георгина', color="#c8ffc8")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

label start:

    scene door

    menu:
        "debug":
            jump day5_scene1
        "start game":
            jump night0_scene1
        "exit":
            return
