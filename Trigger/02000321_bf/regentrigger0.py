""" trigger/02000321_bf/regentrigger0.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=100, spawnIds=[900]):
            return None


class 웜리젠91(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1,2])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1,2]):
            return 웜리젠91쿨타임(self.ctx)


class 웜리젠91쿨타임(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='9')
        self.set_timer(timerId='9', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='9'):
            self.reset_timer(timerId='9')
            return 시작대기중(self.ctx)


initial_state = 시작대기중
