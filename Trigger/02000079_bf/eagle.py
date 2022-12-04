""" trigger/02000079_bf/eagle.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    pass


class 독수리비행(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.move_npc(spawnId=99, patrolName='MS2PatrolData_99')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1800000'):
            return None # Missing State: 종료2


initial_state = 시작대기중
