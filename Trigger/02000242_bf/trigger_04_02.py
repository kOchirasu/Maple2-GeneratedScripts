""" trigger/02000242_bf/trigger_04_02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[303], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[703,704], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[402]):
            return 버튼눌림(self.ctx)


class 버튼눌림(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[303], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[703,704], visible=False)
        self.set_timer(timerId='1', seconds=180)


initial_state = 대기
