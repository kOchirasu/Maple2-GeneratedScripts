""" trigger/52000002_qd/stage02.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[107]):
            return 안내시작(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 시작대기중(self.ctx)


class 안내시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=25200205, textId=25200205)
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000612,10000613,10000614,10000615,10000616], stateValue=2):
            return 종료(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 시작대기중(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=25200205)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[101]):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
