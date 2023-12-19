define audio.main_menu = "music/Darude-Sandstorm.ogg"
define audio.background = "music/backmus1.mp3"
define audio.eminem = "music/backmus2.mp3"
define audio.emptystreet = "music/EmptyStreet.mp3"

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

init python: 
    renpy.music.register_channel("ambient", "ambient", True)