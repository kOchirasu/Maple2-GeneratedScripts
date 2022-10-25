""" trigger/80000009_bonus/trigger_04.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000211], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000211], stateValue=0):
            return 소환(self.ctx)


class 소환(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_301')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=401, spawnIds=[104]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104])
        self.set_timer(timerId='4', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            return 아이템(self.ctx)


class 아이템(common.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[502])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
