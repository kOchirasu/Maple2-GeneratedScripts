""" trigger/99999985_plantest_08/ia_111.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000010], state=1)
        self.set_actor(triggerId=1111, visible=True, initialSequence='SOS_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[307])


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000010], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(triggerId=1111, visible=False, initialSequence='SOS_B')
        self.destroy_monster(spawnIds=[307])
        self.create_monster(spawnIds=[111])


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=111, patrolName='MS2PatrolData111')
        self.set_conversation(type=1, spawnId=111, script='$02000116_BF__IA_111__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=111, script='$02000116_BF__IA_111__1$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=111, spawnIds=[111]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[111])
        self.set_timer(timerId='111', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='111'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
