label first_act:
    # Акт №1: Старый друг
    play ambient audio.emptystreet
    nvl_narrator """
    Два года назад [gg_name] окончил университет, отучившись на программиста.

    Годы обучения были трудны для него. Из-за того, 
    что [gg_name] часто прогуливал пары и не старался учиться, 
    преподаватели, говорили, что он ничего не добьётся.

    Помимо этого, у него не было друзей, которые могли бы его поддержать.

    Это всё больше вгоняло его в депрессию и отнимало желание учиться дальше.

    Однако, [gg_name] был умён и он смог с лёгкостью закрыть свои долги по учёбе, 
    сдать сессии и защитить диплом, чему сильно удивлялись его преподаватели.
    
    К сожалению, из-за травли в институте у него пропал весь интерес и желание работать.
    """
    nvl clear
    nvl_narrator """
    Он закрылся в себе и начал искать себя в искусстве, рисуя граффити на стенах домов и заборах.

    Однажды он решил в отместку за унижения преподавателей нарисовать граффити на своём институте.

    Начав глубокой ночью и закончив под утро, когда студенты уже потихоньку шли на учёбу, 
    проходящая мимо девушка, заметила, как какой-то парень рисует на стенах университета и увидела в его рисунках талант.
    
    Воодушевлённая его работой, она подошла к незнакомцу и узнала в нём своего бывшего одногруппника и спросила его:
    """
    
    nvl_nastya "[gg_name]... Это ты?"
 
    nvl_narrator """ 
    Растерявшись от неожиданной встречи и думая, что это один из преподавателей, который его унижал в университете, 
    он обернулся и увидел свою бывшую подругу, в которую был тайно влюблён всё это время.
    """

    nvl clear
    show nim suit wonder at cright

    show ggim graffitymaker at cleft
    gg "Привет, Настя."
    nastya happy "Шикарные рисунки, у тебя талант."
    gg stoneface "..."
    nastya wonder "Ты что, стал художником?"
    show direc behind ggim with dissolve:
        xalign 0.2
        yalign 0.9
        zoom 0.5

    gg "Нет, иногда хожу по разным подработкам, чтобы заработать денег на краску, 
    а граффити – моё хобби и ничто другое меня не интересует…"  
    nastya -wonder "Слушай, у меня к тебе есть интересное предложение, давай завтра, 
    часа в 2 встретимся в кафешке “Тардис”, там я тебе расскажу всё поподробней."
    
    show direc:
        ease 1.0 xalign 0.0

    gg "Ну давай..."
    play sound scream
    gg "Походу мне пора, до завтра."

    play sound audio.drivingaway
    hide ggim with easeoutleft
    
    stop music fadeout 0.5
    hide nim with easeoutright
    
    
    play music audio.cafe fadein 0.5
    $ renpy.notify("Frank Sinatra - Fly me to the moon")
    scene bg cafe with fade

    

    show nim at cleft with easeinleft:
        pause 1.0
        linear 1.5 xalign 0.8

    pause 2.0
    show nim sweater_sit:
        xalign 0.8
        yalign -3.63
    pause 1.0
    show nim angry
    show ggim sweater_cap at cleft with easeinleft
    gg "Привет."
    nastya "Привет, уже думала, что ты не придёшь."

    show ggim at cleft with easeinleft:
        ease 0.5 xalign 0.6
    show nim with easeoutright:
        xalign 1.0 

    pause 0.5

    show ggim sweater_cap_sit:
        yalign -3.38
        easein_back 0.5 xalign 0.6

    gg sweater_sit "Давай быстрей, что там за предложение?"
    nastya -angry "В общем, я сейчас работаю UI/UX дизайнером и так как ты очень хорошо рисуешь,
    я хочу тебе предложить попробовать себя в этой сфере."
    gg annoyed "Меня это не интересует, да и не умею я."
    nastya wonder "У тебя же ни гроша в кармане, ходишь в лохмотьях, давай я тебя научу, уверена тебе понравится."
    gg angry "У меня уже есть то, чем я хочу заниматься и я не собираюсь тратить время на подобного рода бесполезные вещи. Разговор окончен."

    show nim angry
    show ggim sweater_cap angry at cleft with easeoutleft
    hide ggim with easeoutleft
    
    stop music fadeout 0.3
    scene bg gg kitchen
    with fade
    play music eminem
    $ renpy.notify("Eminem - Without Me")
    show ggim shorts at cleft with dissolve

    show mom sad at cright with easeinright:
        zoom 0.9

    gg "Привет, {w=0.2} мам. Чего такая грустная?"
    gmom "Почему ты так поступил с той девушкой?"
    stop music fadeout 0.6
    play ambient room
    gg shocked "Что? Ты о чём? Какой девушкой?"
    gmom "Я сидела за соседним столиком в том же кафе на обеде и слышала весь ваш разговор."
    gg stoneface"Понятно. Давай закроем эту тему, я не хочу об этом говорить."
    gmom -sad "Нет! Объяснись! Почему ты не хочешь работать?"
    gg annoyed "Мне не нужно это."
    gmom happy "Почему? Я переживаю за твою жизнь, что ты будешь делать когда меня не станет?"
    gg angry"Отвянь! Я сам разберусь!"

    hide ggim with easeoutleft
    pause 0.5
    play sound audio.dooropens 
    scene bg gg room with dissolve

    show ggim shorts angry at ccenter with easeinright

    pause 1.0
    gg sad "Блин, что-то я перегнул, надо бы извиниться."
    hide ggim with easeoutright

    scene bg gg kitchen with dissolve

    show ggim shorts sad at cleft with easeinleft
    show mom sad at cright with dissolve:
        zoom 0.9

    gg "Слушай, мам..."
    extend " ладно, не плачь, мам, я попробую обучиться этому дизайну..."

    show mom happy:
        ease 0.5 xalign 0.2

    gmom "Спасибо, сынок..."
    gg -sad "Завтра пойду к Насте и попрошу её о помощи."
    gmom "У тебя обязательно всё получится."

    scene bg blank with fade
    "На следующее утро..."
    scene bg gg room with fade
    nvl clear
    show ggim at cright with dissolve
    window hide
    $ nvl_mode = "phone"
    
    nvl_narrator "Настя"
    gg_phone "Привет, Настя. Прости, за тот случай в кафешке, я был не прав. "
    gg_phone "Ты тут?"
    nastya_phone "Я дала тебе шанс и предложила помощь, ты отказался и нагрубил. Зачем мне снова пытаться тебя вытащить? "
    show ggim sad
    gg_phone "Прости. Я исправлюсь. "
    nastya_phone "Вряд ли."
    nvl_narrator "Пользователь заблокировал вас"
    window hide
    $ nvl_mode = "classic"
    nvl clear

    show ggim at ccenter with easeinright

    gg "{i}Что же делать?{/i}"
    pause 1.0
    show ggim happy
    gg "{i}Придумал! Закажу Насте букет цветов, ей обязательно понравится!{/i}"

    play sound audio.keyboardsearching
    
    scene bg nastya kitchen with fade
    show nim dress at ccenter with dissolve
    play sound audio.doorknock
    pause 0.5
    show nim wonder
    pause 1.0
    hide nim with easeoutright
    pause 1.0
    scene bg nastya hallway with dissolve
    show nim dress at cright with easeinright
    play sound audio.dooropens
    scene bg nastya hallway opened
    show nim dress at cright
    show courier flowers at center:
        zoom 0.8
    
    courier "Здравствуйте, вам были заказаны цветы от некого [gg_name], вот, держите и распишитесь вот здесь."
    show nim wonder
    play sound "<from 0 to 2>" + audio.write
    pause 2.0
    show nim dress_flowers
    courier -flowers "Спасибо, до свидания, хорошего вечера."
    nastya "До свидания... "
    hide courier with dissolve
    play sound audio.dooropens
    scene bg nastya hallway 
    show nim dress_flowers wonder at cright
    pause 0.2
    hide nim with easeoutright

    pause 0.7

    scene bg nastya kitchen with dissolve
    show nim dress_flowers at ccenter with easeinright
    pause 0.7
    show nim dress
    show flowers with dissolve:
        xalign 0.83
        yalign 0.65
        zoom 0.3

    nastya wonder "Что это? Записка?"
    play sound "<from 0 to 1>" + openpaper
    pause 1.0
    gg "{i}\"Я поступил некрасиво, прости меня. P.S. Выгляни в окно.\"{/i}"
    
    nastya angry "{i}Что интересного я могу увидеть в окне?{/i}"
    nastya wonder "{i}Только не говорите мне, что...{/i}"

    $ MC_Name = "Настя"
    $ nvl_mode = "phone"

    nvl clear
    scene bg nastya outwindow with fade
    pause 2.0

    nvl_narrator "[gg_name]"
    nvl_narrator "Пользователь заблокирован"
    nvl_narrator "Вы разблокировали пользователя"
    nastya_phone "Ты явно спятил, но, признаюсь, выглядит впечатляюще, ахаха."
    nastya_phone "Я так понимаю, этим ты хотел сказать, что передумал насчет решения с работой?"
    gg_phone "Да, но я бы хотел попросить тебя о помощи, поможешь мне стать дизайнером?"
    nastya_phone "Конечно!"
    window hide
    $ MC_Name = "[gg_name]"
    $ nvl_mode = "classic"