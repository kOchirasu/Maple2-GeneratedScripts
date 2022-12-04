""" trigger/52000014_qd/steam_5000.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[501], animationEffect=False)
        self.create_monster(spawnIds=[502], animationEffect=False)
        self.create_monster(spawnIds=[503], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발사01(self.ctx)


class 발사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)
        self.create_monster(spawnIds=[500], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[500])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 딜레이01(self.ctx)


initial_state = 대기
