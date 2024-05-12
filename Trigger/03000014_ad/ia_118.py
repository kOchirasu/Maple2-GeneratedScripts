""" trigger/03000014_ad/ia_118.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000118], state=1)
        self.set_actor(triggerId=118, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000118], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(triggerId=118, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[96], animationEffect=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=96, patrolName='MS2PatrolData406')
        self.set_conversation(type=1, spawnId=96, script='$03000014_AD__IA_118__0$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=296, spawnIds=[96]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[96])
        self.set_timer(timerId='306', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='306'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
