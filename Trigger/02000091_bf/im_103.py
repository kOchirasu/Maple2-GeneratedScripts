""" trigger/02000091_bf/im_103.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000534], state=1)
        self.set_actor(triggerId=2103, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000534], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[103])
        self.set_actor(triggerId=2103, visible=False, initialSequence='Idle_A')


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_Gull_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=1103, spawnIds=[103]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])
        self.set_timer(timerId='103', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='103'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
