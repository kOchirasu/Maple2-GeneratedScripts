""" trigger/02000041_bf/elite.xml """
import common


class 생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001,1002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1001,1002]):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='30', seconds=30, startDelay=0, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='30'):
            return 생성(self.ctx)


initial_state = 생성
