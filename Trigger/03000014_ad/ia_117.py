""" trigger/03000014_ad/ia_117.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000117], state=1)
        self.set_actor(triggerId=117, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000117], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(triggerId=117, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[95], animationEffect=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=95, patrolName='MS2PatrolData405')
        self.set_conversation(type=1, spawnId=95, script='$03000014_AD__IA_117__0$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=295, spawnIds=[95]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[95])
        self.set_timer(timerId='305', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='305'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
