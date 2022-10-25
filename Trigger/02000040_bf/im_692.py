""" trigger/02000040_bf/im_692.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000692], state=1)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[107])


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000692], stateValue=0):
            return 시간텀(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[107])
        self.create_monster(spawnIds=[1107])


class 시간텀(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1107, patrolName='MS2PatrolData_1107')
        self.set_conversation(type=1, spawnId=1107, script='$02000040_BF__IM_692__0$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=1107, spawnIds=[1107]):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1107])
        self.set_timer(timerId='1107', seconds=60)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1107'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
