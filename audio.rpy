define audio.cafe = "music/Frank Sinatra-Fly Me To The Moon.mp3"
define audio.background = "music/backmus1.mp3"
define audio.eminem = "music/backmus2.mp3"
define audio.mrbeast = "music/beastmus.mp3"
define audio.emptystreet = "music/EmptyStreet.mp3"
define audio.afterdark = "music/Mr.Kitty - After Dark.ogg"
define audio.weloveburningtown = "music/Shantae and the Pirates Curse OST-We Love Burning Town.ogg"
define audio.room = "music/RoomAmbient.mp3"
define audio.silentoffice = "music/SilentOffice.mp3"

define audio.goodending = "music/GoodEnding.mp3"
define audio.badending = "music/BadEnding.mp3"
define audio.neutralgoodending = "music/NeutralGoodEnding.mp3"
define audio.falleninlove = "music/FallenInLove.mp3"

define audio.cooking = "sounds/Cooking.mp3"
define audio.crickets = "sounds/Crickets.mp3"
define audio.doorknock = "sounds/DoorKnock.mp3"
define audio.dooropens = "sounds/DoorOpens.mp3"
define audio.drivingaway = "sounds/DrivingAway.mp3"
define audio.keyboardsearching = "sounds/KeyboardSearching.mp3"
define audio.rains = "sounds/Rains.mp3"
define audio.skating = "sounds/Skating.mp3"
define audio.writing = "sounds/Write.mp3"
define audio.snoring = "sounds/Snoring.mp3"
define audio.hearbeat = "sounds/Heartbeat.ogg"
define audio.openpaper = "sounds/OpenPaper.mp3"
define audio.clockclicking = "sounds/СlockClicking.mp3"
define audio.scream = "sounds/Scream.mp3"

init python: 
    renpy.music.register_channel("ambient", "ambient", True)
    renpy.music.register_channel("sound2", "sfx", False)