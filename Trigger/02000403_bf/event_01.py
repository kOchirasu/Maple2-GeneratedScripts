""" trigger/02000403_bf/event_01.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[702]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000403_BF__EVENT_01__0$', arg3='3000')


initial_state = idle
