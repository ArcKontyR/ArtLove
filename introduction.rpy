label introduction:
    scene bg skatepark night front
    play ambient audio.crickets

    $ nvl_mode = "classic"

    gg "Каждый день я просыпаюсь с чувством того, что я не определился, кем хочу стать в этом мире."

    scene bg skatepark night alt
    play sound audio.skating

    gg "Юные годы прошли, учеба закончилась, друзья разъехались и нашли себя в чём-то."

    scene bg skatepark night front
    play sound audio.skating

    gg "Мои родители твердят о том, что нужно остепениться, жениться, найти работу..."

    scene bg skatepark night alt
    play sound audio.skating
    gg "Но единственное, что мне нравится - "

    extend " рисовать."
    return

label easter:
    #play music "<from 8 to 15.64>" + audio.weloveburningtown
    $ renpy.notify("Найдена пасхалка. Не влияет на сюжет.")
    pause 2.0
    $ easter = True
    play music "<from 8>" + audio.weloveburningtown
    $ renpy.notify("Shantae and the Pirates Curse OST - We Love Burning Town")
    scene bg placeholder with irisout
    show nim angry at cright with easeinright

    nastya wonder "Серьёзно? [gg_name]?"
    nastya angry "Переосмысли свои жизненные приоритеты пожалуйста."

    show ggim stoneface at cleft with easeinleft:

    gg "А что собственно не так с этим именем? Красивое и популярное имя!"
    nastya wonder "Ты видел хотя бы одного человека с этим именем, который при этом не был бы странным?"
    gg shocked "А как же я?"
    nastya angry "А я про что говорю? Иди отсюда!"
    gg sad "Ладно..."
    hide ggim with easeoutleft
    show nim at ccenter with ease
    nastya -angry "А вообще любое имя прекрасно, но есть много людей, которые могут очернить данное ему имя!"
    nastya "Так что не волнуйся! И пойдем смотреть за этой прекрасной историей."
    if gg_name == "Абчихба":
        nastya angry "Правда имя [gg_name] это жесть конечно..."
    return
    
label lockin:
    $ easter = True
    $ renpy.movie_cutscene(videos.ughhowuncultured)
    $ gg_name = "Валера"
    return
