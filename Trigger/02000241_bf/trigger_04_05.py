""" trigger/02000241_bf/trigger_04_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[308], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[408]):
            return 버튼눌림(self.ctx)


class 버튼눌림(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[308], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[707,708], visible=False)
        self.set_mesh(triggerIds=[309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324], visible=False)


initial_state = 대기
