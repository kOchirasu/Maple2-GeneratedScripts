""" trigger/52000076_qd/fog.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000813], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=136, spawnIds=[2006]):
            return 시작대기중(self.ctx)


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1098])
        self.set_effect(triggerIds=[600], visible=False) # fog 500
        self.set_effect(triggerIds=[602], visible=False) # fog 1500
        self.set_interact_object(triggerIds=[10000813], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1098]):
            return 포그(self.ctx)


class 포그(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[600], visible=True)
        self.set_interact_object(triggerIds=[10000813], state=1)
        self.show_guide_summary(entityId=20003494, textId=20003494)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000813], stateValue=0):
            return 대기시간(self.ctx)
        if self.monster_dead(boxIds=[1099]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20003494)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_interact_object(triggerIds=[10000813], state=0)
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 시작대기중(self.ctx)


initial_state = 준비
