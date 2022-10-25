""" trigger/52100301_qd/3000055_phase_4_camera_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=690000, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Phase_4_Camera_01', value=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=690000, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 리셋(self.ctx)


class 리셋(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Phase_4_Camera_01', value=0):
            return 대기(self.ctx)


initial_state = 대기
