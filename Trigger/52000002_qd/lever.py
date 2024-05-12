""" trigger/52000002_qd/lever.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000607,10000608,10000609,10000610,10000611], stateValue=0):
            return 박스체크(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 시작대기중(self.ctx)


class 박스체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 안내시작(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 시작대기중(self.ctx)


class 안내시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=True)
        self.show_guide_summary(entityId=25200201, textId=25200201)
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000606], stateValue=0):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=25200201)
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[101]):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
