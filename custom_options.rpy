define config.default_transform = truecenter

define easter = False
define rejectWork = 0
define took_money = False

image laptop = "images/laptop.png"
image ggsleepy = "images/gg/emotions/ggim_emotions_relaxed.png"
image nangry = "images/nastya/emotions/nim_emotions_angry.png"
image figmaempty = "images/bg/figma/bg figma empty.png"
image figmabad = "images/bg/figma/bg figma bad.png"
image figmabetter = "images/bg/figma/bg figma better.png"
image figmatutorial = "images/bg/figma/bg figma tutorial.png"
image figmabeast = "images/bg/figma/bg figma tutorial beast.png"
image figmahomemade = "images/bg/figma/bg figma homemade.png"
image figmabought = "images/bg/figma/bg figma bought.png"
image offer ="images/bg/bg_offer.png"
init python:
    rejectedNames = ["виталя", "виталий", "никита", "женя", "евгений", "абчихба", "влад", "владислав"]
    bannedNames = ["хуй", "пизда", "залупа", "еблан", "дебил", "аутист", "даун", "пенис", "головка", "член", "петух", "мудила", "пидор", "пидорас", "пидрила", "педик", "долбоёб", "хуесос", "мразь", "тварь"]

transform cleft:
    yalign -2.0

transform ccenter:
    yalign -2.0
    xalign 0.5

transform cright:
    yalign -2.0
    xalign 1.0

transform laptopscreen:
    xalign 0.505
    yalign 0.6
    zoom 0.365