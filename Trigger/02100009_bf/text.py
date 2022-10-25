""" trigger/02100009_bf/text.xml """
import common


class 유저감지(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 알림(self.ctx)


class 알림(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.any_one():
            return 알림_2(self.ctx)
        if self.all_of():
            return 완료알림(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='10000')


class 알림_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 알림_3(self.ctx)

    def on_exit(self):
        self.set_event_ui(type=1, arg2='$02100009_BF__resurrection_2__0$', arg3='4000')


class 알림_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 알림(self.ctx)
        if self.all_of():
            return 완료알림(self.ctx)


class 완료알림(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5500):
            return None


initial_state = 유저감지
