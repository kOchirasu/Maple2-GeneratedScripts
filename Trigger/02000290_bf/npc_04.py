""" trigger/02000290_bf/npc_04.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000461], state=1)
        self.create_monster(spawnIds=[904])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000461], stateValue=0):
            return NPC대사(self.ctx)


class NPC대사(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=904, script='$02000290_BF__NPC_04__0$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.move_npc(spawnId=904, patrolName='MS2PatrolData904')
        self.set_conversation(type=1, spawnId=904, script='$02000290_BF__NPC_04__1$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[904])


initial_state = 시작대기중
