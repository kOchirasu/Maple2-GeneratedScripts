""" trigger/52000002_qd/sheep_04.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[614], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000616], stateValue=0):
            return NPC교체(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return NPC소멸(self.ctx)


class NPC교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_interact_object(triggerIds=[10000616], state=2)
        self.create_monster(spawnIds=[1094])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return NPC이동(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return NPC소멸(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='6', seconds=6)
        self.move_npc(spawnId=1094, patrolName='MS2PatrolData_1094')
        self.set_effect(triggerIds=[614], visible=True)
        self.set_conversation(type=1, spawnId=1094, script='$52000002_QD__SHEEP_04__0$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return NPC소멸(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1094])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 시작대기중(self.ctx)


initial_state = 시작대기중
