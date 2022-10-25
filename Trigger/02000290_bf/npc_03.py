""" trigger/02000290_bf/npc_03.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000460], state=1)
        self.create_monster(spawnIds=[903])

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000460], stateValue=0):
            return NPC대사(self.ctx)


class NPC대사(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=903, script='$02000290_BF__NPC_03__0$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.move_npc(spawnId=903, patrolName='MS2PatrolData903')
        self.set_conversation(type=1, spawnId=903, script='$02000290_BF__NPC_03__1$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[903])


initial_state = 시작대기중
