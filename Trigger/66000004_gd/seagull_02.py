""" trigger/66000004_gd/seagull_02.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10502]):
            return 이동(self.ctx)


class 이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2002')
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1800000'):
            return None # Missing State: 종료2


initial_state = 시작
