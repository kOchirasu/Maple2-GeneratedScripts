""" trigger/02020062_bf/message.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020062_BF__MESSAGE__0$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FieldGameStart') >= 1:
            # <게임 시작 결정>
            return 종료(self.ctx)
        if self.user_value(key='FieldGameStart') >= 2:
            # <방폭 결정>
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
