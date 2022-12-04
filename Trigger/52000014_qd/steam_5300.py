""" trigger/52000014_qd/steam_5300.xml """
import trigger_api


class 대기(trigger_api.Trigger):
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
        self.set_timer(timerId='2', seconds=1)
        self.create_monster(spawnIds=[530], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 발사02(self.ctx)


class 발사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.create_monster(spawnIds=[531], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 딜레이02(self.ctx)


class 딜레이02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=1)
        self.destroy_monster(spawnIds=[530])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 발사03(self.ctx)


class 발사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=2)
        self.create_monster(spawnIds=[531], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[531])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 딜레이01(self.ctx)


initial_state = 대기
