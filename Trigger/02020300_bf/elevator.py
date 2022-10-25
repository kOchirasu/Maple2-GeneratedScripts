""" trigger/02020300_bf/elevator.xml """
import common


class 메시지_대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='elevator', value=1):
            return 엘리베이터_정지(self.ctx)


class 엘리베이터_정지(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020300_BF__MAIN__12$', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            self.set_breakable(triggerIds=[5001], enable=False)
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='elevator', value=0):
            return 메시지_대기(self.ctx)


initial_state = 메시지_대기
