""" trigger/02000149_in/ia_103.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000192], state=1)
        self.set_actor(triggerId=203, visible=True, initialSequence='Sit_Chair_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000192], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=203, visible=False, initialSequence='Sit_Chair_Idle_A')
        self.create_monster(spawnIds=[403])


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=403, patrolName='MS2PatrolData_503')
        self.set_conversation(type=1, spawnId=403, script='$02000149_IN__IA_103__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=403, script='$02000149_IN__IA_103__1$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=603, spawnIds=[403]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[403])
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
