""" trigger/99999905/seagull_04.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10504]):
            return 이동(self.ctx)


class 이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            self.move_npc(spawnId=2004, patrolName='MS2PatrolData_2004')
            return None # Missing State: 종료


initial_state = 시작
