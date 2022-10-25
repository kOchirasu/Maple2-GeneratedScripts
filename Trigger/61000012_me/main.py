""" trigger/61000012_me/main.xml """
import common


class 입장(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 입장
