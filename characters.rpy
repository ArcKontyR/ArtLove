define gg = Character("[gg_name]", color = "#ff0000", image = 'ggim')
define gg_phone = Character("[gg_name]", kind=nvl, callback = Phone_ReceiveSound, color = "#ff0000")

define gmom = Character("Мама", color = "#e600e6", image = 'mom' )

define nvl_nastya = Character(_("Настя"),kind=nvl , color = "#62ffe5ff")
define nastya = Character(_("Настя"), color = "#62ffe5ff",image = 'nim')
define nastya_phone = Character(_("Настя"), kind=nvl, callback = Phone_ReceiveSound, color = "#62ffe5ff")

define courier = Character(_("Курьер"), color = "#00ca00", image = 'courier')
define ftutor_phone = Character(_("Незнакомец"), kind=nvl, color = "#ffc400")

layeredimage ggim:
    zoom 0.9
    group costumes auto:
        attribute jacket default
    
    group emotions auto:
        attribute smile default
    
layeredimage nim:
    zoom 0.9
    group costumes auto:
        attribute sweater default
    
    group emotions auto:
        attribute smile default