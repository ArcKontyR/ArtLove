label third_act:
    if (rejectWork == 0):
        jump good_ending
    else:
        jump bad_ending
    return

label good_ending:
    play ambient silentoffice fadein 0.5
    scene bg office hallway with fade
    play sound "<from 0 to 2.7>" + audio.heartbeat
    "Спустя неделю"
    show ggim bluesuit at cright with easeinleft
    show nim suit at cleft with easeinleft
    
    nastya "Тебе в кабинет № 219, вперёд, ты сможешь!"
    gg "Фух, надеюсь всё получится."
    hide ggim with easeoutright
    scene bg office director with fade
    show worker first at cleft with dissolve:
        zoom 0.9
    show ggim bluesuit at cright with easeinright
    gg "Здравствуйте,  я пришёл на собеседование."
    nach "Да-да. Заходите, присаживайтесь."
    nach "Ну что ж. Вы довольно быстро учитесь."
    nach "За столь короткий срок обучения вы довольно быстро достигли высокого уровня, но всё же я пока не могу полностью довериться вам. Слишком маленький у вас опыт в работе. "
    gg shocked "Я не претендую на высокую должность."
    nach "Ладно-ладно. Я уже убедился в вашем рвении к знаниям, а это я очень ценю в людях."
    nach "Вы приняты!"
    show ggim happy
    nach "Будете помощником Анастасии, у вас с ней много общего, так что думаю она быстро вас подучит."
    gg "Большое вам спасибо! Я вас не подведу, буду стараться изо всех сил!"
    nach "Рад слышать, [gg_name]. Будьте готовы, завтра ваш первый полноценный рабочий день в нашей компании. "
    gg stoneface "Хорошо, благодарю за предоставленную возможность."
    scene bg office hallway with fade
    show nim suit at cleft with dissolve
    show ggim bluesuit at cright with easeinright
    nastya "Ну что, тебя взяли?"
    gg happy "Да. Более того, теперь я твой помощник."
    gg -happy "Директор сказал, что ты сможешь помочь мне быстро освоиться. "
    nastya happy "Да ладно! Я так рада."
    nastya -happy "Ну что ж, тогда до завтра? "
    gg "Да... До завтра."
    hide nim with easeoutleft
    pause 1.0
    hide ggim with easeoutleft
    stop ambient fadeout 0.5
    play ambient emptystreet fadein 0.5
    scene bg office outside with fade
    show ggim bluesuit at cleft with easeinleft
    show nim suit at cright with easeinright
    nastya "Привет! Ну что, готов к труду и обороне?"
    gg happy "Ха, конечно. С чего начнём?"
    play ambient silentoffice fadein 0.5
    scene bg office nastya with fade
    show nim suit at cright with easeinleft
    show ggim bluesuit at cleft with easeinleft
    nastya "Начнем с того, что..."   
    scene bg office nastya night with dissolve
    show nim suit at cright with dissolve
    show ggim bluesuit at cleft with dissolve
    pause 1.0
    hide ggim with easeoutleft
    hide nim with easeoutleft
    play ambient emptystreet fadein 0.5
    scene bg office outside night with fade
    show ggim bluesuit at cleft with dissolve
    show nim suit at cright with dissolve  
    if (took_money == False):
        jump neutral_good_ending
    
    nastya "Ладно, [gg_name]. Думаю, надо по домам идти, завтра работу никто не отменял."
    gg "Может сходим в ресторан или кафешку? Поужинаем, отметим наш первый совместный рабочий день как никак."
    nastya wonder "Ты приглашаешь меня на свидание?"
    gg happy "Ну да."
    nastya happy "Хорошо, я согласна."
    gg -happy "Тогда я даже знаю куда мы пойдём. "
    nastya wonder "И куда же? "
    gg "Увидишь... "
    stop ambient fadeout 0.5
    scene bg cafe with fade 
    play music cafe fadein 0.5
    $ renpy.notify("Frank Sinatra - Fly me to the moon")
    show nim suit at cleft with easeinleft:
        xalign 0.1
    show ggim bluesuit at cleft behind nim with easeinleft:
        xalign -0.1
    
    gg "Вот мы и пришли... "
    nastya happy "Да ты романтик. Запомнил то место, где чуть не довёл меня до слёз. "
    gg happy "Сегодня я попытаюсь сделать так, чтобы это место ассоциировалось у тебя с совсем другим событием. "
    nastya interested "Интересно… "
    gg -happy "За время моего обучения мы сильно сблизились, и я понял, что хочу провести всю жизнь с тобой. "
    
    gg "Настя, ты выйдешь за меня?"
    show nim wonder with ease:
        xalign 0.2
    pause 1.5
    show nim happy with ease:
        xalign 0.0
    nastya "Да! Я согласна!"
    stop music fadeout 1.0
    scene bg blank with fade
    "Спустя год."
    play music goodending fadein 1.0
    $ renpy.notify("Florence + The Machine - Dog Days Are Over")
    scene bg gg and nastya house with fade
    show ggim blacksuit at cleft with dissolve
    show nim dress at cright with dissolve
    pause 1.0
    scene bg gg laptop with fade
    show offer at laptopscreen with dissolve
    pause 1.0
    scene bg_offer with dissolve
    gg "Настя, ты не поверишь..."
    nastya "Чего там такое?"
    gg "Меня пригласили в UDV Group."
    nastya "Какой ты у меня молодец!"

    scene bg udv hall with fade
    show anna at cleft with dissolve:
        zoom 0.9
    show ggim blacksuit at cright with easeinright

    "Анна Викторовна" "Рада приветствовать у нас!"
    scene bg good ending with fade
    show ggim blacksuit at ccenter with easeinleft
    $ renpy.notify("Концовка \"Великая идиллия.\"")
    gg "Вот и пришёл конец нашей истории. Всегда найдутся те, кто будет говорить, что у тебя ничего не получится."
    gg wonder "Никого не слушай, если действительно хочешь чего-то добиться."
    gg shocked "Они говорят, что ничего не выйдет, потому что не смогли сделать это сами."
    gg happy "Наслаждайся окольными путями. Всем сердцем."
    gg -happy "Потому что там ты найдёшь то, что тебе важнее цели. "
    hide ggim with easeoutright
    pause
    return

label neutral_good_ending:
    nastya "[gg_name], рабочий день закончен, нам пора. "
    gg shocked "А? У меня еще не полностью готова работа. Я задержусь. "
    nastya "Да ладно тебе, успеешь доделать завтра, не перетруждай себя."
    nastya "Пошли, прогуляемся и зайдём по пути куда-нибудь. "
    gg -shocked "Прости, но я останусь, это правда важно для меня. "
    show nim sad
    pause 1.0
    hide nim with easeoutleft
    play music neutralbadending fadein 0.5
    scene bg good ending with fade
    $ renpy.notify("Концовка \"Главное - работа!\"")
    show ggim bluesuit at ccenter with easeinleft
    gg "Вот и пришёл конец нашей истории."
    gg happy "Я считаю, что не нужно думать о множестве возможностей, ты можешь сделать только что-то одно. Так освой это. "
    gg -happy "Всегда следует считать, что ты являешься лучшим и тот, с кем ты должен сражаться, — это не кто иной, как твой собственный образ. "
    hide ggim with easeoutright
    pause
    return

label bad_ending:
    scene bg blank with fade
    "На следующий день."
    play ambient silentoffice fadein 0.5
    scene bg office director with fade
    show worker first at cleft with dissolve:
        zoom 0.9
    show ggim bluesuit at cright with easeinleft
    gg "Здравствуйте, я к вам на собеседование пришёл. "
    nach "Да-да. Заходите, присаживайтесь. "
    gg shocked "Извините, а мы с вами не виделись раньше? "
    nach "Нет, не думаю. А что? "
    gg -shocked "Да так, ничего. Забудьте. "
    nach "Ладно, перейдём к делу. Вы меня сильно удивили своей работой. "
    nach "Настя сказала мне, что вы учитесь всего пару недель, а уже имеете такие успехи. "
    nach "Так вот, у меня не укладывается в голове, как вы достигли такого успеха за столь короткий срок?"
    gg "Даже и не знаю, что сказать... Наверно, у меня талант. "
    nach "Талант значит... Это хорошо, талантливые люди нам нужны. Тогда скажите мне..."
    with fade
    nach "Ну что, [gg_name]. Вы, конечно, что-то да понимаете, но мне не верится, что ту страницу вы делали сами."
    menu:
        
        nach "Скажите честно, вам кто-нибудь помогал в её создании?"
        "Соврать":
            pass
        "Сказать правду":
            jump neutral_bad_ending
    gg "Конечно, сам. "
    nach "Вот как... Хотите я вам раскрою один секрет?"
    gg "Допустим..."
    nach "Когда Анастасия выступала со своим проектом и я увидел эту страницу, я почувствовал что-то неладное, будто бы я уже где-то видел эту работу. "
    nach "Так вот, я потом ещё пару раз глянул на эту страничку и понял, что я делал её на заказ одному человеку по имени \"[gg_name]\". Понимаете, к чему я клоню? "
    gg stoneface "Да уж. Как удачно всё совпало... "
    nach "Не то слово. Я понадеялся, что вы хотя бы сознаетесь, что есть хотя бы один повод оставить вас на испытательный срок, но как оказалось вы того не стоите. "
    gg sad "Простите, я не хотел, просто были такие обстоятельства, что мне пришло... "
    nach "Мне плевать, что у вас там были за обстоятельства. Вы как минимум могли бы хоть сейчас сказать правду, и, может быть, я бы даже подумал оставить вас..."
    nach "Таким как вы здесь не место. Выметайтесь из моего кабинета и сделайте так, чтобы я вас больше не видел. Всё ясно? "
    gg angry "Да пошёл ты!"
    hide ggim with easeoutright
    scene bg office hallway with dissolve
    show nim suit at cleft with dissolve
    show ggim bluesuit angry at cright with easeinright
    nastya wonder "[gg_name]!"
    hide ggim with easeoutleft
    show worker first at cright with easeinright:
        zoom 0.9
    nach "Анастасия Сергеевна, зайдите ко мне. "
    hide worker first with easeoutright
    scene bg office director with dissolve
    show worker first at cleft with dissolve:
        zoom 0.9
    show nim suit at cright with easeinright
    nastya "Здравствуйте, вы что-то хотели?"
    nach "Вы уволены. "
    nastya wonder "Что? Почему? Что я такого сделала? "
    nach "Для начала, вы поручились за человека, который мало того что почти ничего не понимает в том, чем мы занимаемся, так он ещё и страницу делал не сам, при этом уверял, что это его работа. "
    nach "Кроме того, вы, прекрасно всё это зная, не задумываясь вставили эту страницу в свой проект. "
    pause 1.0
    nach "Ну и стоил этот парень вашей работы?"
    nastya sad "Простите, пожалуйста, такое больше не повториться, честное слово! "
    nach "Это точно, ведь вы у нас больше не работаете. Удачи, Анастасия, уверен вы сможете найти работу в другой компании. "

    play ambient emptystreet fadein 0.5
    scene bg office outside with fade
    show nim suit angry at ccenter with dissolve
    nastya "{i}Какая я дура, зачем я решила помогать этому придурку?! {/i}"
    nastya "{i}Если б не он, все мои проблемы просто испарились бы!{/i}"

    stop ambient fadeout 0.5
    scene bg blank with fade
    "Спустя год."
    play ambient badending fadein 1.0
    scene bg udv hall with fade
    show nim suit at ccenter with dissolve
    pause 1.0
    scene bg gg pyatorochka with fade
    gg stoneface "Свободная касса!"

    scene bg bad ending with fade
    show ggim graffitymaker at ccenter with easeinleft
    $ renpy.notify("Концовка \"Брошенный.\"")
    gg "Вот и пришёл конец нашей истории. Я скажу то, что для тебя не новость. "
    gg stoneface "Мир не такой уж солнечный и приветливый, это очень опасное место. "
    gg "Думая лишь о результате, люди начинают искать короткий путь. "
    gg "А на короткой дороге можно потерять истину из виду. "
    gg "И желание что-либо делать пропадёт. "
    gg "Думаю, важно лишь стремление узнать истину. "
    hide ggim with easeoutright
    pause
    return

label neutral_bad_ending:
    gg sad "Если честно, это не я её делал. Я её заказал у одного человека, потому что у меня ничего не получалось и я не хотел, чтобы у Насти были неприятности из-за меня. "
    nach "Понятно... Ну, я рад, что вы признались. Теперь понятно, к чему вы спросили про то, не встречались ли мы раньше. "
    nach "Это у меня вы заказывали эту страничку. В свободное от работы время я делаю различные мини-проекты на заказ, честно говоря, я сразу и не узнал свою работу. "
    gg shocked "И что теперь, получается я не прошёл собеседование?"
    nach "Если б вы соврали, то я бы точно вас выгнал, но как оказалось вы честный и добрый человек, да и какой-то набор знаний у вас всё-таки есть... "
    nach "Ладно, я пойду вам на уступки, но при одном условии."
    gg happy "Да, конечно, что угодно."
    nach "У вас будет ровно месяц, чтобы превзойти мою работу. Согласны?"
    gg -happy "Конечно. Я буду стараться."
    nach "Вот и славно. Будете помощником Анастасии, она вас порекомендовала, вот пусть с вами и мучается."
    gg "Спасибо большое, я вас не подведу."
    nach "Давай иди отсюда, пока я не передумал. "
    hide ggim with easeoutright
    scene bg office hallway with dissolve
    show nim suit at cleft with dissolve
    show ggim bluesuit at cright with easeinright
    nastya wonder "Ну что, тебя взяли? "
    gg happy "Да. Но с небольшим условием, я должен за месяц сделать страницу лучше, чем та, которую заказал..."
    extend " Зато я теперь твой помощник. "
    nastya "Ого! Я уж подумала, что тебя вообще не возьмут, да ты везунчик. "
    gg -happy "Наверно так и есть... "
    nastya -wonder "Ладно, завтра увидимся, мне работать пора."
    hide nim with easeoutleft
    gg stoneface "Пока."
    hide ggim with easeoutleft
    play ambient room fadein 0.5
    scene bg gg room night with fade
    show ggim bluesuit at ccenter with easeinright
    pause 1.0
    play ambient silentoffice fadein 0.5
    scene bg office nastya with fade
    show nim suit at cright with easeinleft
    show ggim bluesuit at cleft with easeinleft
    gg "Привет"
    nastya "Привет. Ну что, готов к сегодняшнему дню? "
    gg "Конечно, что будем делать?"
    nastya "Начнем с того, что..."   
    scene bg office nastya night with dissolve
    show nim suit at cright with dissolve
    show ggim bluesuit at cleft with dissolve
    pause 1.0
    hide ggim with easeoutleft
    hide nim with easeoutleft
    play ambient emptystreet fadein 0.5
    scene bg office outside night with fade
    show ggim bluesuit at cleft with dissolve
    show nim suit at cright with dissolve
    gg "Слушай, Насть. Давай сходим куда-нибудь, отметим наш первый совместный рабочий день? "
    nastya "Прости, я не в настроении. К тому же на работу завтра, так что может быть в другой раз? "
    gg stoneface "Ну ладно, как скажешь. Тогда до завтра."
    nastya "Ага, пока. "
    hide ggim with easeoutleft
    hide nim with easeoutright

    scene bg gg room with fade
    stop ambient fadeout 0.5
    play music falleninlove fadein 1.0
    $ renpy.notify("The Beatles - And I Love Her")
    show ggim shirt sad at ccenter with dissolve
    gg "Что же я сделал не так? Почему Настя стала так себя холодно вести по отношению ко мне?"
    gg "Собеседование ведь прошло на удивление удачно..."

    scene bg blank with fade
    "Спустя год."
    
    scene bg office splitted with fade
    show ggim bluesuit stoneface at cright with dissolve
    show nim suit at cleft with dissolve
    pause 1.0
    scene bg office director with fade
    show ggim bluesuit happy at ccenter with dissolve:
        xalign 0.7
    show worker first at ccenter with dissolve:
        xalign 0.3
        zoom 0.9
    pause 1.0
    scene bg office presentation zero with fade
    show anna at ccenter with dissolve:
        xalign 0.3
        zoom 0.9
    show ggim bluesuit at ccenter with dissolve:
        xalign 0.7
    pause 1.0
    scene bg blank with fade
    "Спустя 2 года."
    scene bg office meeting with fade
    show ggim blacksuit stoneface at ccenter with dissolve
    gg "{i}Интересно, как ты там, Настя?{/i}"
    gg "{i}Я стал уважаемым человеком, благодаря тебе, надеюсь и ты смогла им стать...{/i}"
    gg sad "{i}Я скучаю...{/i}"
    
    scene bg bad ending with fade
    show ggim blacksuit stoneface at ccenter with easeinleft
    $ renpy.notify("Концовка \"Уважаемый человек.\"")
    gg "Вот и пришёл конец нашей истории. Чтобы стать лучше, нужно принимать свои ошибки и учиться на них, ведь ошибки — это не конец пути, а новый шанс на успех. "
    gg "Единственный человек, который не делает ошибок, это человек, который никогда ничего не делает. "
    hide ggim with easeoutright
    pause
    return

