# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    $ gg_name = "______"

    stop ambient fadeout 0.8
    
    call introduction from _call_introduction
    show guard at center with dissolve:
        xalign 0.0
        yalign 0.85
        zoom 0.4
    $ gg_name = renpy.input("Эй, это опять ты, [gg_name] ?!? А ну проваливай, ещё раз тебя увижу - ноги переломаю.", default="Введите имя", length = 12, allow="йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ")
    
    if gg_name == "Введите имя" or gg_name == "":
        $ gg_name = "Валера"
    if gg_name.lower() in rejectedNames:
        call easter from _call_easter
    if gg_name.lower() in bannedNames:
        call lockin from _call_lockin
    
    stop ambient fadeout 0.4

    scene bg institute alt
    with fade
    hide guard
    
    $ MC_Name = gg_name
    # if gg_name == "Banksy":
    # jump secretEnding
    
    call first_act from _call_first_act
    call second_act from _call_second_act 
    call third_act from _call_third_act

    return
