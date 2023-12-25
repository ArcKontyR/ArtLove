init python:

    mr = MusicRoom(fadeout = 1.0)

    mr.add("music/backmus1.mp3")
    mr.add("music/backmus2.mp3")
    mr.add("music/beastmus.mp3")
    mr.add("music/FallenInLove.mp3")
    mr.add("music/GoodEnding.mp3")
    mr.add("music/Mr.Kitty - After Dark.ogg")
    mr.add("music/NeutralGoodEnding.mp3")
    mr.add("music/Frank Sinatra-Fly Me To The Moon.mp3")
    mr.add("music/Shantae and the Pirates Curse OST-We Love Burning Town.ogg")

    ar = MusicRoom(fadeout = 1.0)
    ar.add("music/BadEnding.mp3")
    ar.add("music/EmptyStreet.mp3")
    ar.add("music/RoomAmbient.mp3")
    ar.add("music/SilentOffice.mp3")

# Step 3. Create the music room screen.
screen music_room:

    tag menu
    add gui.main_menu_background
    vbox:
        hbox:  
            null width 54      
            frame:
                ypos 0.15
                xsize 850
                vbox:
                    hbox:
                        label _("Громкость музыки") 
                        null width 100
                        bar value Preference("music volume")
                
                    # The buttons that play each track.
                    textbutton "Меню" action mr.Play("music/backmus1.mp3")
                    textbutton "Shantae and the Pirates Curse OST - We Love Burning Town" action mr.Play("music/Shantae and the Pirates Curse OST-We Love Burning Town.ogg")
                    textbutton "Frank Sinatra - Fly Me To The Moon" action mr.Play("music/Frank Sinatra-Fly Me To The Moon.mp3")
                    textbutton "Eminem - Without Me" action mr.Play("music/backmus2.mp3")
                    textbutton "OMFG - Hello" action mr.Play("music/beastmus.mp3")
                    textbutton "Florence & The Machine - Dog Days Are Over" action mr.Play("music/GoodEnding.mp3")
                    textbutton "W1SP - Клетка (Instrumental)" action mr.Play("music/NeutralGoodEnding.mp3")
                    textbutton "The Beatles - And I Love Her" action mr.Play("music/FallenInLove.mp3")
                    textbutton "Mr.Kitty - After Dark" action mr.Play("music/Mr.Kitty - After Dark.ogg")

                    null height 25

                    # Buttons that let us advance tracks.
                    textbutton _("Cледующее") action mr.Next():
                        xalign 0.5
                    textbutton _("Предыдущее") action mr.Previous():
                        xalign 0.5

                    null height 20
        
            null width 110
            frame:    
                ypos 0.15
                xsize 850
                vbox:
                    hbox:
                        label _("Громкость фоновых звуков")
                        null width 100
                        bar value Preference("ambient volume")
                    # The buttons that play each track.
                    
                    textbutton "Улица" action ar.Play("music/EmptyStreet.mp3")
                    textbutton "Комната" action ar.Play("music/RoomAmbient.mp3")
                    textbutton "Офис" action ar.Play("music/SilentOffice.mp3")
                    textbutton "\"Брошенный\"" action ar.Play("music/BadEnding.mp3")
                   

                    null height 25

                    # Buttons that let us advance tracks.
                    textbutton _("Cледующее") action ar.Next():
                        xalign 0.5
                    textbutton _("Предыдущее") action ar.Previous():
                        xalign 0.5

                    null height 20

        # The button that lets the user exit the music room.
    textbutton _("Главное меню") action ShowMenu("main_menu"):
        yalign 0.9
        xalign 0.5

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "music/backmus1.mp3")