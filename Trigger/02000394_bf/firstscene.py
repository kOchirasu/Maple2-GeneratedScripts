""" trigger/02000394_bf/firstscene.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100]):
            return 카메라연출01(self.ctx)


class 카메라연출01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=3000, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라연출02(self.ctx)


class 카메라연출02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3000,3001,3002,3003], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return 종료(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0.6)


class 종료(common.Trigger):
    pass


initial_state = 대기
