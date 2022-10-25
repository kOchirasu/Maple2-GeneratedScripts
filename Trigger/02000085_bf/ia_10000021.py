""" trigger/02000085_bf/ia_10000021.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000021], state=1)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000021], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[101])


class NPC이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData1')
        self.set_conversation(type=1, spawnId=101, script='$02000085_BF__IA_10000021__0$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=21, spawnIds=[101]):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
