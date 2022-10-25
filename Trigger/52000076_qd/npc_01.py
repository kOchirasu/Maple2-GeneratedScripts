""" trigger/52000076_qd/npc_01.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901])

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000806], stateValue=0):
            return NPC대사(self.ctx)


class NPC대사(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=901, script='$02000349_BF__NPC_01__0$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.move_npc(spawnId=901, patrolName='MS2PatrolData901')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[901])


initial_state = 시작대기중
