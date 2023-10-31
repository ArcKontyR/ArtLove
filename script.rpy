# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    $ gg_name = "???"
    call introduction
    with fade
    $ gg_name = renpy.input("Эй, это опять ты, [gg_name] ?!? А ну проваливай, ещё раз тебя увижу - ноги переломаю.", default="Введите имя", length = 12, allow="йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ")
    
    if gg_name == "Введите имя" or gg_name == "":
        $ gg_name = "Валера"

    $ MC_Name = gg_name
    # if gg_name == "Banksy":
    # jump secretEnding
    
    call first_act 
    with dissolve
    call second_act

    return
