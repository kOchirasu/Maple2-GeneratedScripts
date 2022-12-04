""" trigger/80000008_bonus/trigger_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[801,802,803,804,805], visible=False)
        self.set_effect(triggerIds=[806,807,808,809,810], visible=False)
        self.set_mesh(triggerIds=[201,202,203,204,205], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000212], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000212], stateValue=0):
            return 소환(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=401, spawnIds=[105]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[105])
        self.set_timer(timerId='5', seconds=1)
        self.set_timer(timerId='6', seconds=1, startDelay=1)
        self.set_effect(triggerIds=[801,802,803,804,805], visible=True)
        self.set_effect(triggerIds=[806,807,808,809,810], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 꽝(self.ctx)


class 꽝(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.destroy_monster(spawnIds=[105])
        self.set_mesh(triggerIds=[201,202,203,204,205], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000208], state=2)
        self.set_interact_object(triggerIds=[10000209], state=2)
        self.set_interact_object(triggerIds=[10000210], state=2)
        self.set_interact_object(triggerIds=[10000211], state=2)
        self.set_interact_object(triggerIds=[10000212], state=2)


initial_state = 대기
