""" trigger/02000197_bf/im_567.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000567], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[106])


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000567], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[106])
        self.create_monster(spawnIds=[1106])


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1106, patrolName='MS2PatrolData_567')
        self.set_conversation(type=1, spawnId=1106, script='$02000197_BF__IM_567__0$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=567, spawnIds=[1106]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1106])
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
