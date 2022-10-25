""" trigger/52000014_qd/steam_5700.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 딜레이01(self.ctx)


class 딜레이01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 발사01(self.ctx)


class 발사01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=1)
        self.create_monster(spawnIds=[570], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 발사02(self.ctx)


class 발사02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.create_monster(spawnIds=[571], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 딜레이02(self.ctx)


class 딜레이02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=1)
        self.destroy_monster(spawnIds=[570])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            return 발사03(self.ctx)


class 발사03(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=2)
        self.create_monster(spawnIds=[571], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 초기화(self.ctx)


class 초기화(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[571])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 딜레이01(self.ctx)


initial_state = 대기
