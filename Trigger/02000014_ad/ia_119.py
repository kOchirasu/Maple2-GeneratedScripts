""" trigger/02000014_ad/ia_119.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000119], state=1)
        self.set_actor(triggerId=119, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000119], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(triggerId=119, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[97], animationEffect=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=97, patrolName='MS2PatrolData407')
        self.set_conversation(type=1, spawnId=97, script='$02000014_AD__IA_119__0$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=297, spawnIds=[97]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[97])
        self.set_timer(timerId='307', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='307'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
