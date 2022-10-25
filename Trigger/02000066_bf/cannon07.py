""" trigger/02000066_bf/cannon07.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[8007])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return 생성(self.ctx)


class 생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[8007], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[8007]):
            return 대기시간(self.ctx)


class 대기시간(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='60', seconds=60)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='60'):
            return 시작(self.ctx)


initial_state = 시작
