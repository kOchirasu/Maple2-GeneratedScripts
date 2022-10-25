""" trigger/52000002_qd/sheep_03.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[613], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000614], stateValue=0):
            return NPC교체(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return NPC소멸(self.ctx)


class NPC교체(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_interact_object(triggerIds=[10000614], state=2)
        self.create_monster(spawnIds=[1093])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return NPC이동(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return NPC소멸(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=6)
        self.set_effect(triggerIds=[613], visible=True)
        self.move_npc(spawnId=1093, patrolName='MS2PatrolData_1093')
        self.set_conversation(type=1, spawnId=1093, script='$52000002_QD__SHEEP_03__0$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='6'):
            return NPC소멸(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1093])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 시작대기중(self.ctx)


initial_state = 시작대기중
