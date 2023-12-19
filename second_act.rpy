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
    gg "Заходи, чувствуй себя как дома"
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
    gg "Ладно, и как примерно должна выглядеть эта страница."
    nastya "Ну что ж... Так, как ты представляешь себе сайт для скейтеров. Ты же и сам катаешься на скейте, так. Тогда тебе будет легче. "
    gg "Думаю, ты права. Я попробую. "
    nastya "Ну что ж, объём работы невелик, думаю ты справишься. Чтобы тебе было полегче, я тебе скину, как я оформила другие страницы. "
    gg "Хорошо, я постараюсь."
    scene bg gg room with dissolve
    show ggim shirt at cleft with dissolve
    show nim uniform_suitcase at cright with dissolve
    nastya "Ладно, надеюсь ты справишься, а то уже послезавтра утром мне нужно будет продемонстрировать свой проект."
    gg shocked "И ты готова мне доверится на все 100. Даже если я вообще без понятия как мне всё это сделать."
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
        "Лучше заказать оформление у знающего человека, сам я вряд ли смогу его сделать так сразу. Обучением займусь позже, голова раскалывается от  количества информации...":
            $ rejectWork += 1
            call going_out
        "Нельзя сдаваться, я должен научиться делать хоть это. Если у меня не получится, Настя сильно расстроится":
            call trying_to_work
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
    show figmabeast at laptopscreen with dissolve
    play music audio.mrbeast
    $ renpy.notify("MrBeast Song (SXCREDMANE Phonk Remix)")

    pause 4.0
    stop music fadeout 1.0
    pause 1.0
    play music audio.background
    show figmaempty at laptopscreen with dissolve
    pause 1.0
    show figmabetter at laptopscreen with dissolve
    pause 1.0
    gg "{i}Всё таки хорошо, что я не сам сделал работу для Насти...{/i}"
    ftutor_phone "Здравствуйте, я закончил с оформлением."
    gg_phone "Ого, так быстро!"
    ftutor_phone "{image=images/bg/figma/bg_figma_bought_small.png}"
    ftutor_phone "Вас устраивает финальный вид работы?"
    gg_phone "Да, всё замечательно."
    ftutor_phone "Спасибо за покупку моих услуг, буду ждать вашего следующего заказа. "
    window hide
    $ nvl_mode = "classic"

    "Довольный работой фрилансера, [gg_name] ждёт Настю."
    "Спустя некоторое время"
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
    scene bg gg room with fade
    play sound snoring
    pause 1.0
    play sound2 doorknock
    play sound snoring
    pause 1.0
    play sound2 doorknock
    play sound snoring
    pause 1.0
    show ggim shirt relaxed at ccenter with dissolve
    gg "А? Чего? Кто?"
    scene bg gg hallway with fade
    play sound doorknock
    play sound doorknock
    play sound doorknock
    pause 1.0
    show ggim shirt at cleft with dissolve
    play sound dooropens
    scene bg gg hallway opened
    show ggim shirt at cleft
    show nim at ccenter with dissolve
    show nim at cright with easeinleft
    
    play sound dooropens
    scene bg gg hallway
    show nim at cright
    show ggim at cleft

    scene bg gg room with fade
    show ggim at ccenter with dissolve
    play sound audio.doorknock
    pause 0.5
    scene bg gg entrance with dissolve
    play sound dooropens
    show nastya fifth at center with dissolve:
        ypos 1.2
        zoom 0.9
    gg "Привееет!"
    nastya "Привет, ты чего такой радостный?"
    gg "Просто я много работал и очень ждал, когда ты придёшь, чтобы оценить мой труд."
    nastya "Понятно, ну тогда пошли, мне даже интересно стало, что у тебя получилось."
    scene bg gg room with dissolve
    show gg second with dissolve:
        ypos 1.2
        zoom 0.9
    show nastya fifth at center with dissolve:
        ypos 1.2
        zoom 0.9
    nastya "Ну довольно неплохо. В целом мне нравится."
    gg "Спасибо, я старался."
    nastya "Конечно, я потом немного подправлю, но в целом для первого раза у тебя очень хорошо получилось. Я тобой горжусь."
    gg "Рад, что тебе понравилось."
    menu:
        nastya "Ну что, я же тебе говорила, что заплачу... вот - держи."
        "Взять деньги":
            $ took_money = True
            gg "Это было не обязательно, но спасибо, очень приятно."
        "Не брать деньги":
            gg "Оставь себе, мне не нужны твои деньги."
    nastya "Хотела бы я ещё поговорить, но мне пора, ещё много дел предстоит сделать."
    gg "Ладно, не переживай, мы ещё успеем поговорить."
    nastya "Хорошо, тогда я пойду. Пока, ещё увидимся."
    gg "Конечно... пока."
    return
