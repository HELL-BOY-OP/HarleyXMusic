from HarleyXMusic.core.bot import Anony
from HarleyXMusic.core.dir import dirr
from HarleyXMusic.core.git import git
from HarleyXMusic.core.userbot import Userbot
from HarleyXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Harley()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
