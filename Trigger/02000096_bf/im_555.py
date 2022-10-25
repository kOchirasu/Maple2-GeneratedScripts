""" trigger/02000096_bf/im_555.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000555], state=1)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000555], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[104])


class NPC이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_555')
        self.set_conversation(type=1, spawnId=104, script='$02000096_BF__IM_555__0$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=555, spawnIds=[104]):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104])
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
