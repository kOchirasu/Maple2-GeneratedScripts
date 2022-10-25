""" trigger/02020111_bf/message.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Message', value=0):
            return 메세지출력(self.ctx)


class 메세지출력(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020111_BF__MESSAGE__0$', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Message', value=1):
            return 시작(self.ctx)


initial_state = 시작
