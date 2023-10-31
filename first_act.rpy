label first_act:

    # Акт №1: Старый друг
    
    nvl_narrator """
    Два года назад [gg_name] окончил университет, отучившись на программиста.

    Годы его обучения были очень трудными для него морально, из-за того, 
    что он часто прогуливал пары и порой сидел на них в телефоне, 
    преподаватели оскорбляли его и давили морально, говорили, что он ничего не добьётся.

    Это всё больше вгоняло его в депрессию и отнимало желание учиться дальше.

    Но [gg_name] был не так уж и глуп, он смог с лёгкостью закрыть свои долги по учёбе, 
    сдать сессии и защитить диплом, чему сильно удивлялись его учителя.
    
    К сожалению, из-за травли в институте у него пропал весь интерес и желание быть программистом.
    """

    nvl clear

    nvl_narrator """
    Он закрылся в себе и начал искать себя в искусстве, рисуя граффити на стенах домов и заборах.

    Однажды он решил в отместку за издевательства и унижения, полученные от педагогов, разрисовать весь университет.

    Итак, начав глубокой ночью и закончив под утро, когда студенты уже потихоньку шли на учёбу, 
    проходящая мимо девушка, заметила, как [gg_name] рисует на стенах университета и увидела в его рисунках талант.
    """

    nvl clear

    nvl_narrator """
    Воодушевлённая его работой, она подошла к незнакомцу и узнала в нём своего бывшего одногруппника и спросила его:
    """
    

    nvl_nastya "[gg_name]... Это ты?"
 
    nvl_narrator """ 
    Растерявшись от неожиданной встречи и думая, что это один из преподавателей, который его унижал в университете, 
    он обернулся и увидел свою бывшую подругу, в которую был тайно влюблён всё это время.
    """

    nvl clear

    gg "Привет, Настя"

    nastya "Шикарные рисунки, у тебя талант."

    gg "..."

    nastya "Ты что, стал художником?"

    gg "Нет, иногда шляюсь по разным подработкам, чтобы заработать денег на краску, 
    а граффити – моё хобби и ничто другое меня не интересует…"
    
    nastya "Слушай, у меня к тебе есть интересное предложение, давай завтра, 
    часа в 2 встретимся в кафешке “Тардис”, там я тебе расскажу всё поподробней."

    gg "Ну давай..."

    nar "В далеке начинает что-то кричать директор университета, в это время [gg_name] встал на свой скейтборд" 
    
    gg "Походу мне пора, до завтра"

    nar "Думая, что выглядит круто, [gg_name] уехал в закат."

    nar "На следующий день [gg_name] проспал и пришёл в кафе, опоздав на 20 минут, 
    заметил за столиком, ждущую его Настю, идёт к её столику и садится напротив неё."

    nar "Настя, собираясь уходить, заметила нашего страдальца"

    gg "Привет."

    nastya "Привет, уже думала, что ты не придёшь."

    gg "Давай быстрей, что там за предложение?"

    nastya "В общем, я сейчас работаю ui/ux дизайнером и так как ты очень хорошо рисуешь,
    я хочу тебе предложить попробовать себя в этой сфере."

    # развилка: соглашается / не соглашается

    gg "Меня это не интересует, да и не умею я."

    nastya "У тебя же ни гроша в кармане, ходишь в лохмотьях, давай я тебя научу, уверена тебе понравится."

    gg "Я выше этого и не собираюсь учиться этой фигне. Разговор окончен"

    nar "Вернувшись домой, чтобы успокоиться [gg_name] слушает западный рэпчик и жарит себе пельмени. Через пару часов, домой возвращается грустная мама нашего героя."

    #nar "Поздравляю вы прошли новеллу, с чем я поздравляю вас и желаю всего наилучшего :3"

    gg "Привет, {w=1} мам. Чего такая грустная?"

    gmom "Почему ты так поступил с той девушкой?"

    gg "Что? Ты о чём? Какой девушкой?"

    gmom "Я сидела за соседним стоиликом в том же кафе на обеде и сышала весь ваш разговор."

    gg "Понятно. Давай закроем эту тему, я не хочу об этом говорить."

    gmom "Нет! Объяснись! Почему ты не хочешь работать?"

    gg "Мне не нужно это."

    gmom "Почему? Я переживаю за твою жизнь, что ты будешь делать когда меня не станет?"

    gg "Отвянь! Я сам разберусь!"

    gg "Слушай, мам..."

    extend " ладно, не плачь, мам, я попробую обучиться этому дизайну..."

    gmom "Спасибо, сынок..."

    gg "Завтра пойду к Насте и попрошу её о помощи."

    gmom "У тебя обязательно всё получится."