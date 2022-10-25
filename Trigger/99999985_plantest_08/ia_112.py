""" trigger/99999985_plantest_08/ia_112.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000011], state=1)
        self.set_actor(triggerId=1121, visible=True, initialSequence='SOS_B')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[308])


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000011], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=1121, visible=False, initialSequence='SOS_B')
        self.destroy_monster(spawnIds=[308])
        self.create_monster(spawnIds=[112])


class NPC이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=112, patrolName='MS2PatrolData112')
        self.set_conversation(type=1, spawnId=112, script='$02000116_BF__IA_112__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=112, script='$02000116_BF__IA_112__1$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=112, spawnIds=[112]):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[112])
        self.set_timer(timerId='112', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='112'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
