label second_act:
    scene bg gg hallway with fade
    play sound doorknock
    pause 1.0
    show ggim shirt at cleft with dissolve
    play sound dooropens
    scene bg gg hallway opened
    show ggim shirt at cleft
    show nim uniform_suitcase at ccenter with dissolve
    show nim at cright with easeinleft
    
    play sound dooropens
    scene bg gg hallway
    show nim uniform_suitcase at cright
    show ggim shirt at cleft

    gg "О, привет, я тебя ждал. "
    nastya "Привет."
    gg "Заходи, чувствуй себя как дома."
    nastya wonder "А у тебя тут чистенько, я себе по-другому представляла твою квартиру. "
    gg "Ну... что есть - то есть."
    scene bg gg room with dissolve
    show ggim shirt at cleft with easeinright

    show nim uniform_suitcase wonder at cright with easeinright

    nastya "Вау!.."
    extend " Такого я точно не ожидала."
    gg "Не обращай внимания, давай сфокусируемся на дизайне."

    scene bg gg and nastya studying with fade
        
    play sound audio.keyboardsearching
    nastya "Короче, начну с того, что вообще делает UX/UI дизайнер. Для начала расскажу про UI дизайн."
    nastya "Простым языком это создание внешнего оформления сайта, или же пользовательского интерфейса:"
    nastya "Наполнение сайта, выбор цветов, построение визуальной композиции, оформление кнопок и подобные графические штуки."
    show ggsleepy:
        yalign 0.776
        xalign 0.499
        zoom 0.7
    nastya "А UX дизайн — это когда ты делаешь продукт удобным, понятным и логичным для всех пользователей."
    nastya "От этого зависит скорость и удобство нахождения нужной услуги клиентом."
    nastya "Как-то так."  
    show nangry:
        yalign 0.42
        xalign 0.793
        zoom 0.68
    extend " Ты вообще понимаешь, что я говорю?"
    gg "Ага... "
    extend" Что дальше?"
    nastya "Я ещё ничего не успела рассказать, а ты уже засыпаешь… Давай, взбодрись, это только начало."
    hide ggsleepy
    gg "Ладно, ладно, я постараюсь."
    hide nangry
    $ nvl_mode = "classic"
    nvl clear
    nvl_nastya "Итак, работа UX/UI-специалиста делится на несколько этапов:"
    nvl_nastya """1. Анализ целевой аудитории.\n2. Анализ конкурентов.\n3. Проектирование пользовательского пути.\n4. Создание прототипа.\n5. Тестирование.\n6. Поддержка и развитие продукта."""

    nvl_nastya "Все эти моменты крайне важны в работе UI/UX-специалиста, если придерживаться подобной конструкции, то может получиться очень даже качественный продукт."
    gg "Ммм, круто. И сколько тебе платят за это?"
    nastya "Ну, так как я начинающий специалист, моя зарплата варьируется от 60-ти до 70-ти тысяч, но она может доходить даже до 200 тысяч."
    gg "Неплохо..."
    nastya "Ну что, мне удалось тебя хоть немного заинтересовать?"
    gg 'В целом, вроде интересно и платят неплохо, но мне бы на практике посмотреть ещё, понравится мне или нет. С чего мне лучше начать?'
    nastya "Ну раз у тебя неплохо получается рисовать, то давай попробуем сделать кое-что для моего проекта."
    nastya "В общем я сейчас больше UI дизайном занимаюсь, поскольку в UX я ещё не до конца разобралась, и мне осталось сделать оформление для одной страницы кое-какого сайта. "
    nastya "Короче нужно сделать завлекающую, тематическую витрину для одного недавно открывшегося скейт магазина, справишься?"
    gg "Аа... А как? Я же вообще не знаю где и как всё это делать. "
    nastya 'У тебя есть ноутбук или компьютер? '
    gg "Да, вот он."
    scene bg gg laptop with fade
    nastya "Отлично, тогда включай его и открывай {i}Figma{/i}. "
    gg "Чего? Какую фигу?"
    nastya "{b}Figma{/b} - это онлайн-сервис для разработки интерфейсов, в нём можно даже работать с другими людьми в реальном времени."
    show figmaempty at laptopscreen with dissolve
    nastya "Я тебе скину проект, в котором я собиралась делать страницу для сайта и завтра смогу посмотреть и подкорректировать, что ты успеешь сделать до завтрашнего вечера. "
    gg "Это конечно круто, но я всё ещё не умею пользоваться этим сервисом."
    nastya "Не бойся, здесь не так уж и сложно разобраться, к тому же в ютубе полно гайдов по этому сервису."
    nastya "До завтрашнего вечера у тебя ещё много времени, учитывая, что ты не учишься и не работаешь."
    gg "Ладно, и как примерно должна выглядеть эта страница?"
    nastya "Ну что ж... Так, как ты представляешь себе сайт для скейтеров. Ты же и сам катаешься на скейте, так? Тогда тебе будет легче. "
    gg "Думаю, ты права. Я попробую. "
    nastya "Объём работы невелик, думаю ты справишься. Чтобы тебе было полегче, я тебе скину, как я оформила другие страницы. "
    gg "Хорошо, я постараюсь."
    scene bg gg room with dissolve
    show ggim shirt at cleft with dissolve
    show nim uniform_suitcase at cright with dissolve
    nastya "Ладно, надеюсь ты справишься, а то уже послезавтра утром мне нужно будет продемонстрировать свой проект."
    gg shocked "И ты готова мне доверится на все 100? Даже если я вообще без понятия как мне всё это сделать?"
    nastya "Ну... Когда сроки поджимают - больше мотивации работать, так что я думаю ты справишься, если ещё и хорошо сделаешь, то я тебе заплачу."
    gg -shocked "Ну ты даёшь, я такого не ожидал..."
    nastya "Да ладно тебе, у тебя всё получится, я в тебя верю. Что ж, у меня ещё много дел, так что я, пожалуй, пойду."
    gg "Давай..."
    scene bg gg hallway with fade
    show ggim shirt at cleft with easeinleft
    show nim uniform_suitcase at ccenter with easeinleft
    
    nastya "Ну всё, пока, завтра ещё увидимся."
    gg "Пока."
    play sound dooropens
    scene bg gg hallway opened
    show nim uniform_suitcase at ccenter
    show ggim shirt at cleft
    hide nim with dissolve
    pause 1.0
    play sound dooropens
    scene bg gg hallway
    show ggim shirt at cleft
    gg "Что ж, нужно действовать"
    scene bg gg laptop with fade
    show figmaempty at laptopscreen with dissolve
    gg "Так, как же тут картинку добавить..."
    play sound keyboardsearching
    pause 2.0
    play sound "<from 0 to 2>"+clockclicking
    pause 2.0
    show figmabad at laptopscreen with dissolve
    gg "Это точно не то, что нужно"
    scene bg gg room night with fade
    show ggim shirt at ccenter with dissolve
    menu:
        "{i}После проделанной работы [gg_name] ловит себя на мысли, что стоит сдаться.{/i}"
        "Лучше заказать оформление у знающего человека, сам я вряд ли смогу его сделать так сразу. ":
            gg "{i}Обучением займусь позже, голова раскалывается от  количества информации...{/i}"
            $ rejectWork += 1
            call going_out from _call_going_out
        "Нельзя сдаваться, я должен научиться делать хоть это. Если у меня не получится, Настя сильно расстроится":
            call trying_to_work from _call_trying_to_work
    
    scene bg blank with fade
    "На следующий день."

    scene bg nastya room with fade
    show nim dress wonder at ccenter with dissolve
    nastya "Я опаздываю!"
    
    play ambient silentoffice fadein 0.5
    scene bg office hallway with fade
    show nim suit at ccenter with easeinleft
    hide nim with easeoutright
    scene bg office presentation zero with dissolve
    nastya "Извините за опоздание."
    scene bg office presentation first with fade
    nastya "Здравствуйте, уважаемые коллеги, сегодня я вам продемонстрирую свой проект. "
    nastya "Цель моего проекта - сделать полноценный сайт для “скейтеров”, который бы завлекал клиентов своим оформлением и при этом был бы очень удобен в эксплуатации и функционален."
    scene bg office presentation second
    nastya "Итак, перейдём к сайту. При входе на сайт нас встречает витрина, на которой будет отображаться название магазина."
    nastya "Чуть ниже мини-карта, на которой будут показаны все города, в которых есть наш магазин. "
    scene bg office presentation third
    nastya "Выбрав город, нас перекидывает на основной сайт магазина, где нас встретит слайдер с актуальными акциями и новинками, которые доступны в выбранном вами городе."
    scene bg office presentation first
    nastya "После, мы можем промотать вниз, где будут все возможные скейт-товары. "
    nastya "Их удобно искать при помощи каталога, различных фильтров и поисковой строки."
    scene bg office presentation second
    nastya "У каждого товара есть свой рейтинг, составленный на основе отзывов пользователей. "
    nastya "Также будут фотографии товара и важная информация о нём. "
    scene bg office presentation third
    nastya "Если у пользователя будут вопросы, он сможет задать их в техподдержку, которая будет стараться отвечать на вопросы клиентов как можно скорее. "
    nastya "А если ответы от техподдержки так и не смогли помочь клиенту, в самом низу будет представлен номер нашей горячей линии и почтовый адрес. "
    nastya "На этом всё, надеюсь вам понравилась моя работа."
    scene bg office presentation empty
    show worker first at cleft with dissolve:
        zoom 0.9
    show nim suit at cright with dissolve:
    nastya "Извините, можете сказать, как вы оценили мою работу?"
    nach "Ваша работа достойна похвал, вы хорошо постарались."
    nastya happy "Рада слышать. Я бы хотела попросить вас еще раз взглянуть на стартовую страницу сайта."
    nastya -happy "Вот, эту страницу сделал мой знакомый, он художник и совсем недавно начал разбираться в UI-дизайне, и я хотела поинтересоваться, как вам его работа?"
    show laptop behind worker with dissolve
    if (rejectWork == 0):
        nach "Понятно. Ну в целом не плохо, я даже и не заметил, что её делали не вы."
        nastya happy "Отлично! В общем к чему я это всё. "
        nastya "Я бы хотела предложить вам взять его на стажировку."
        nastya -happy "Видите, как хорошо у него получается, а он лишь пару дней учится. "
        nach "Ну если вы готовы за него поручиться, то можно попробовать. "
        nach "Хорошие работники нам лишними не будут. "
        nach "Скажите ему, чтобы приходил на собеседование через неделю."
        nastya "Обещаю, он вас не разочарует."
        nach "Хочется верить, не подведите."
    else:
        nach "Понятно. Если честно я сильно удивлён. "
        nach "Когда я смотрел ваше выступление, эта страница сильно выделялась между другими. "
        nach "Страничка получилась хорошая, похвальная работа. "
        nastya wonder "Не ожидала, что вам так понравится. "
        nastya -wonder "В общем. Я бы хотела попросить вас дать ему шанс проявить себя. "
        nastya "Не могли бы его взять на испытательный срок или что-то в этом духе? "
        nach "Судя по его работе, это настоящий талант, если он только начинает учиться. "
        nach "Пусть завтра же приходит к нам в офис.  "
        nastya happy "Хорошо! Спасибо!"
    
    stop ambient fadeout 0.5
    play ambient room fadein 0.5
    scene bg nastya room with fade
    show nim suit at cright with easeinright
    $ MC_Name = "Настя"
    $ nvl_mode = "phone"
    $ phone_position_x = 0.3
    nvl clear
    nvl_narrator "[gg_name]"
    nastya_phone "Привет. У меня для тебя хорошие новости."
    gg_phone "Привет, какие?"
    nastya_phone "Я замолвила словечко за тебя на работе и теперь тебя приглашают на собеседование."
    gg_phone "Вау! Спасибо большое. Даже и не знаю, как тебя отблагодарить."
    if (rejectWork == 0):
        nastya_phone wonder "Да ладно тебе, я почти ничего не сделала, всё это твоя заслуга. "
        nastya_phone -wonder "Кстати, тебя ждут через неделю, так что подготовься получше, не подведи."
        gg_phone "Я тебя понял. Ну, времени достаточно, думаю я успею подтянуть свои знания. "
        gg_phone "Спасибо тебе ещё раз. "
        nastya_phone "Давай, я в тебя верю, у тебя всё получится."
        gg_phone "Спасибо."
    else:
        nastya_phone angry " Рано радоваться, арт-директор подумал, что у тебя талант, так что твоё собеседование уже завтра.  "
        gg_phone "Да ну! Как я за день должен достичь такого уровня... "
        nastya_phone "А это уже твоя проблема, нужно было самому страницу делать."
        nastya_phone "Давай, иди готовься, времени мало. "
        gg_phone "Уже начал. "
    return
    
label going_out:
    scene bg gg room with fade
    show ggim shirt at ccenter with dissolve
    gg "{i}Так. С чего бы начать? Посмотреть гайды что ли?{/i}"

    play sound keyboardsearching
    scene bg gg laptop with fade
    show figmatutorial at laptopscreen with dissolve

    gg "То, что нужно. Запишу его контакты"

    with fade

    nvl clear
    $ MC_Name = gg_name
    $ nvl_mode = "phone"
    $ phone_position_x = 0.5
    nvl_narrator "Незнакомец"
    gg_phone "Здравствуйте, я хотел бы воспользоваться вашими услугами."
    ftutor_phone "Здравствуйте, что именно вы хотите, чтобы я сделал?"
    gg_phone "Мне всего лишь нужно сделать оформление для одной страницы."
    ftutor_phone "Хорошо. Как вы хотите её оформить?"
    gg_phone "Не могу точно сказать, но оно должно быть тематически связано с скейтами, граффити и подобной тематикой. Эта страница для одного скейт-сайта."
    ftutor_phone "Хорошо. С учётом того, что объём работы невелик, стоимость составит 800р."
    gg_phone "Сможете успеть к вечеру?"
    ftutor_phone "Да, конечно."
    gg_phone "Отлично, буду ждать."
    window hide

    gg "{i}Ну, пока работа делается за меня, попробую и сам попрактиковаться.{/i}"
    
    stop ambient fadeout 0.5
    play music audio.mrbeast
    $ renpy.notify("OMFG - Hello")
    pause 10.0
    stop music fadeout 1.0
    pause 1.0
    show figmaempty at laptopscreen with dissolve
    pause 1.0
    show figmabetter at laptopscreen with dissolve
    pause 1.0
    play ambient room fadein 0.5
    gg "{i}Всё таки хорошо, что я не сам сделал работу для Насти...{/i}"
    ftutor_phone "Здравствуйте, я закончил с оформлением."
    gg_phone "Ого, так быстро!"
    ftutor_phone "{image=images/bg/figma/bg_figma_bought_small.png}"
    scene bg figma bought with dissolve
    pause 2.0
    scene bg gg laptop
    show figmabetter at laptopscreen
    ftutor_phone "Вас устраивает финальный вид работы?"
    gg_phone "Да, всё замечательно."
    ftutor_phone "Спасибо за покупку моих услуг, буду ждать вашего следующего заказа. "
    window hide
    $ nvl_mode = "classic"

    "Довольный работой фрилансера, [gg_name] ждёт Настю."
    scene bg blank with fade
    "Спустя некоторое время."
    scene bg gg hallway with fade
    play sound doorknock
    pause 1.0
    show ggim shirt at cleft with dissolve
    play sound dooropens
    scene bg gg hallway opened
    show ggim shirt at cleft
    show nim uniform at ccenter with dissolve
    show nim at cright with easeinleft
    
    play sound dooropens
    scene bg gg hallway
    show nim uniform at cright
    show ggim shirt at cleft
    gg "Привет, заходи."
    scene bg gg room with fade
    show ggim shirt at cleft with easeinright
    show nim uniform at cright with easeinright
    nastya "Ну что, как там дела со страницей? Надеюсь, у тебя всё получилось?"
    gg "Да, всё сделано в лучшем виде."
    
    nastya wonder "Круто, не ожидала, что у тебя получится."
    gg "Пошли покажу, что получилось."
    scene bg gg laptop with dissolve
    show figmabought at laptopscreen with dissolve
    nastya "Вау, круто! Ты точно сам это всё делал? "
    gg "Ну да, а как ещё?"
    nastya "А ты можешь меня научить так же делать? Скажи, в чём секрет?"
    gg "Нууу.... На самом деле я её не сам делал. Я его заказал у одного фрилансера... "
    scene bg gg room with dissolve
    show ggim shirt stoneface at cleft with dissolve
    show nim uniform at cright with dissolve
    nastya "..."
    gg "..."
    nastya angry "В чем тогда смысл твоего обучения? Я просила сделать именно тебя, а ты взял и попросил другого, вместо того, чтобы научиться самому."
    gg sad "Я пытался, но у меня не получалось. Поэтому, чтобы не подставлять тебя, я решил заказать у знающего человека."
    nastya sad "Спасибо тебе, конечно, но ты всё равно меня в очередной раз расстроил."
    gg wonder "Да ладно тебе, я обещаю, что научусь делать также, а может и лучше. Мне просто нужно больше времени."
    nastya "Больше времени... Ладно, это на твоей совести."
    gg -wonder "Я понимаю..."
    nastya "Что ж, раз дело сделано, то я пойду. У меня ещё дела есть."
    gg happy "Давай, а я пока буду продолжать учиться."
    nastya "Хорошо, может у тебя и правда получится, только если ты будешь учиться, а не тратить время впустую."
    gg "Я постараюсь, положись на меня."
    nastya "Ладно, до встречи."
    gg "Пока."
    return

label trying_to_work:
    stop ambient fadeout 0.5
    scene bg gg room with fade
    play sound "<from 0 to 2>"+snoring
    pause 2.0
    play sound2 doorknock
    play sound "<from 0 to 2>"+snoring
    pause 2.0
    play sound2 doorknock
    play sound "<from 0 to 2>"+snoring
    pause 2.0
    play sound2 doorknock
    show ggim shirt relaxed at ccenter with dissolve
    gg "А? Чего? Кто?"
    play ambient room fadein 0.5
    scene bg gg hallway with fade
    play sound doorknock
    pause 1.5
    play sound doorknock
    pause 1.5
    play sound doorknock
    pause 1.5
    show ggim shirt relaxed at cleft with easeinleft
    play sound dooropens
    scene bg gg hallway opened
    show ggim shirt relaxed at cleft
    show nim angry at ccenter with dissolve
    show nim at cright with easeinleft
  
    play sound dooropens
    scene bg gg hallway
    show nim angry at cright
    show ggim shirt at cleft

    
    gg happy "Привееет!"
    nastya "Привет, ты чего такой радостный?"
    gg "Просто я много работал и очень ждал, когда ты придёшь, чтобы оценить мой труд."
    nastya -angry "Понятно, ну тогда пошли, мне даже интересно стало, что у тебя получилось."
    scene bg gg room with dissolve
    show ggim shirt at cleft with easeinright
    show nim at cright with easeinright
    pause 1.0
    scene bg gg laptop with dissolve
    show figmahomemade at laptopscreen with dissolve
    nastya "Ну довольно неплохо. В целом мне нравится."
    scene bg gg room with dissolve
    show ggim shirt at cleft with dissolve
    show nim at cright with dissolve
    gg happy "Спасибо, я старался."
    nastya "Конечно, я потом немного подправлю, но в целом для первого раза у тебя очень хорошо получилось. Я тобой горжусь."
    gg -happy "Рад, что тебе понравилось."
    menu:
        nastya "Ну что, я же тебе говорила, что заплачу... держи."
        "Взять деньги":
            $ took_money = True
            gg "Это было не обязательно, но спасибо, очень приятно."
        "Не брать деньги":
            show nim sad
            gg "Оставь себе, мне не нужны твои деньги."
    nastya -sad "Хотела бы я ещё поговорить, но мне пора, ещё много дел предстоит сделать."
    gg "Ладно, не переживай, мы ещё успеем поговорить."
    nastya "Хорошо, тогда я пойду. Пока, ещё увидимся."
    gg "Конечно... пока."
    return
