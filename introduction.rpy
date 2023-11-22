label introduction:
    
    scene bg skatepark night front
    play ambient audio.crickets

    $ nvl_mode = "classic"


    #show gg first at center:
    #    yalign 0.07
    #    xalign 0.6
    #    zoom 0.4

    gg "Каждый день я просыпаюсь с чувством того, что я не определился, кем хочу стать в этом мире."

    scene bg skatepark night alt
    play sound audio.skating
    #show gg first at center:
    #    xalign -0.1
    #    zoom 0.6

    gg "Юные годы прошли, учеба закончилась, друзья разъехались и нашли себя в чём-то."

    scene bg skatepark night front
    play sound audio.skating
    #show gg first at center:
    #    yalign 0.07
    #    xalign 0.6
    #    zoom 0.4

    gg "Мои родители твердят о том, что нужно остепениться, жениться, найти работу..."

    scene bg skatepark night alt
    play sound audio.skating
    #show gg first at center:
    #    xalign -0.1
    #    zoom 0.6

    gg "Но единственное, что мне нравится - "

    extend " рисовать."
    return

label easter:
    #play music "<from 8 to 15.64>" + audio.weloveburningtown
    $ easter = True
    play music "<from 8>" + audio.weloveburningtown
    $ renpy.notify("Shantae and the Pirates Curse OST - We Love Burning Town")
    scene bg placeholder with irisout
    show nastya second angry at right with easeinright:
        ypos 1.2
        zoom 0.9

    nastya "Серьёзно? [gg_name]?"
    nastya "Переосмысли свои жизненные приоритеты пожалуйста."

    show gg second stoneface at left with easeinleft:
        ypos 1.2
        zoom 0.9

    gg "А что собственно не так с этим именем? Красивое и популярное имя!"
    nastya "Ты видел хотя бы одного человека с этим именем, который при этом не был бы странным?"
    gg "А как же я?"
    nastya "А я про что говорю? Иди отсюда!"
    gg "Ладно..."
    hide gg with easeoutleft
    show nastya second at center with ease:
        ypos 1.2
        zoom 0.9
    nastya "А вообще любое имя прекрасно, но есть много людей, которые могут очернить данное ему имя!"
    nastya "Так что не волнуйся! И пойдем смотреть за этой прекрасной историей."
    if gg_name == "Абчихба":
        show nastya second angry
        nastya "Правда имя [gg_name] это жесть конечно..."
    return
    
label lockin:
    $ easter = True
    $ renpy.movie_cutscene(videos.ughhowuncultured)
    $ gg_name = "Валера"
    return
    
