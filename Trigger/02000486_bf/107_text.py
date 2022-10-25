""" trigger/02000486_bf/107_text.xml """
import common


class 유저감지(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9901]):
            return 알림(self.ctx)


class 알림(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.any_one():
            return 텍스트(self.ctx)


class 텍스트(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000486_BF__107_TEXT__0$', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return None


initial_state = 유저감지
