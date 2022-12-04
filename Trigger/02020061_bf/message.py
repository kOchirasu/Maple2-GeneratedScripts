""" trigger/02020061_bf/message.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020061_BF__MESSAGE__0$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FieldGameStart', value=1):
            return 종료(self.ctx)
        if self.user_value(key='FieldGameStart', value=2):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
