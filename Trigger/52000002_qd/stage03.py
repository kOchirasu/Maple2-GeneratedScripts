""" trigger/52000002_qd/stage03.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000612,10000613,10000614,10000615,10000616], stateValue=2):
            return 박스체크(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 시작대기중(self.ctx)


class 박스체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[105]):
            return 안내시작(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 시작대기중(self.ctx)


class 안내시작(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25200206, textId=25200206)
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[105]):
            return 종료(self.ctx)
        if not self.user_detected(boxIds=[101]):
            return 시작대기중(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=25200206)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[101]):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
