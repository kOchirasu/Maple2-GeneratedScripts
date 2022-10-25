""" trigger/02000064_tw_triatown02/stagetrigger_01.xml """
import common


class KickMusicAudience(common.Trigger):
    def on_enter(self):
        self.kick_music_audience(boxId=101, portalId=802)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return KickMusicAudience(self.ctx)


initial_state = KickMusicAudience
