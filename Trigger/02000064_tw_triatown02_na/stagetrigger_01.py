""" trigger/02000064_tw_triatown02_na/stagetrigger_01.xml """
from common import *
import state


class KickMusicAudience(state.State):
    def on_enter(self):
        kick_music_audience(boxId=101, portalId=802)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KickMusicAudience()


