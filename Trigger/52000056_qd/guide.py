""" trigger/52000056_qd/guide.xml """
import trigger_api


class 가이드(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10010001, textId=10010001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103,104,105,106]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=3000):
            return 가이드(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10010001)


class 종료(trigger_api.Trigger):
    pass


initial_state = 가이드
