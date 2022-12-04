""" trigger/80000009_bonus/trigger_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000208], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000208], stateValue=0):
            return 소환(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=401, spawnIds=[101]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 아이템(self.ctx)


class 아이템(trigger_api.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[504])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
