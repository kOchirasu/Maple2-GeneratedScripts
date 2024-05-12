""" trigger/02000349_bf/npc_06.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[906])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000811], stateValue=0):
            return NPC대사(self.ctx)


class NPC대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=906, script='$02000349_BF__NPC_06__0$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=3)
        self.move_npc(spawnId=906, patrolName='MS2PatrolData906')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[906])


initial_state = 시작대기중
