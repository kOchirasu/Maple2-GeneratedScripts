""" trigger/02000116_bf/ia_109.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000008], state=1)
        self.set_actor(triggerId=1091, visible=True, initialSequence='SOS_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[305])


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000008], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=1091, visible=False, initialSequence='SOS_B')
        self.destroy_monster(spawnIds=[305])
        self.create_monster(spawnIds=[109])


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=109, patrolName='MS2PatrolData109')
        self.set_conversation(type=1, spawnId=109, script='$02000116_BF__IA_109__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=109, script='$02000116_BF__IA_109__1$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=109, spawnIds=[109]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[109])
        self.set_timer(timerId='109', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='109'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
