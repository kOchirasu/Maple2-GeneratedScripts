""" trigger/02000116_bf/ia_110.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000009], state=1)
        self.set_actor(triggerId=1101, visible=True, initialSequence='SOS_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[306])


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000009], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(triggerId=1101, visible=False, initialSequence='SOS_B')
        self.destroy_monster(spawnIds=[306])
        self.create_monster(spawnIds=[110])


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=110, patrolName='MS2PatrolData110')
        self.set_conversation(type=1, spawnId=110, script='$02000116_BF__IA_110__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=110, script='$02000116_BF__IA_110__1$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=110, spawnIds=[110]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[110])
        self.set_timer(timerId='110', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='110'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
