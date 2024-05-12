""" trigger/03000014_ad/ia_114.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000114], state=1)
        self.set_actor(triggerId=114, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000114], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(triggerId=114, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[92], animationEffect=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=92, patrolName='MS2PatrolData402')
        self.set_conversation(type=1, spawnId=92, script='$03000014_AD__IA_114__0$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=292, spawnIds=[92]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[92])
        self.set_timer(timerId='302', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='302'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
