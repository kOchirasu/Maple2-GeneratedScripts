""" trigger/52000014_qd/steam_5400.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 발사01(self.ctx)


class 발사01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)
        self.create_monster(spawnIds=[540], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 초기화(self.ctx)


class 초기화(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[540])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 발사01(self.ctx)


initial_state = 대기
