""" trigger/02000443_bf/summon.xml """
import common


class special_1_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='special_1', value=1):
            return special_1_2(self.ctx)


class special_1_2(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8001, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return special_2_1(self.ctx)


class special_2_1(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8001, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='special_2', value=1):
            return special_2_2(self.ctx)


class special_2_2(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8001, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return special_3_1(self.ctx)


class special_3_1(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8001, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='special_3', value=1):
            return special_3_2(self.ctx)


class special_3_2(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8001, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return special_4_1(self.ctx)


class special_4_1(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8001, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='special_4', value=1):
            return special_4_2(self.ctx)


class special_4_2(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8001, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return special_5_1(self.ctx)


class special_5_1(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8001, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='special_5', value=1):
            return special_5_2(self.ctx)


class special_5_2(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8001, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=8001, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return None


initial_state = special_1_1
