""" trigger/02000247_bf/trigger_01_02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[401]):
            return 버튼눌림(self.ctx)
        if self.user_detected(boxIds=[405]):
            return 사라짐(self.ctx)


class 버튼눌림(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[401]):
            return 대기(self.ctx)
        if self.user_detected(boxIds=[405]):
            return 사라짐(self.ctx)


class 사라짐(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0, scale=0)


initial_state = 대기
