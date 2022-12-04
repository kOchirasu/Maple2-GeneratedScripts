""" trigger/02000064_tw_triatown02_jp/stagetrigger_01.xml """
import trigger_api


class KickMusicAudience(trigger_api.Trigger):
    def on_enter(self):
        self.kick_music_audience(boxId=101, portalId=802)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return KickMusicAudience(self.ctx)


initial_state = KickMusicAudience
