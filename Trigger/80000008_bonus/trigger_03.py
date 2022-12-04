""" trigger/80000008_bonus/trigger_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000210], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000210], stateValue=0):
            return 소환(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=401, spawnIds=[103]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])
        self.set_timer(timerId='3', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 아이템(self.ctx)


class 아이템(trigger_api.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[503])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
