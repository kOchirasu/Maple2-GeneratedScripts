""" trigger/02000087_bf/candle1.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000134], state=1)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000134], stateValue=0):
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_201')
        self.set_conversation(type=1, spawnId=101, script='$02000087_BF__CANDLE1__0$', arg4=2)
        self.set_timer(timerId='1', seconds=6)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
