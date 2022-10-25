""" trigger/99999844/cube7_1.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CubeOff', value=1):
            return Off_1(self.ctx)


class Off_1(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return On_1(self.ctx)


class On_1(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return Off_2(self.ctx)


class Off_2(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return On_2(self.ctx)


class On_2(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return Off_3(self.ctx)


class Off_3(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return On_3(self.ctx)


class On_3(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return Off_4(self.ctx)


class Off_4(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=150):
            return On_4(self.ctx)


class On_4(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=150):
            return Off_5(self.ctx)


class Off_5(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=150):
            return On_5(self.ctx)


class On_5(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=150):
            return Off_6(self.ctx)


class Off_6(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=150):
            return On_6(self.ctx)


class On_6(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=150):
            return Off_7(self.ctx)


class Off_7(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5010], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            self.set_user_value(triggerId=920007, key='CubeOff', value=0)
            self.set_user_value(triggerId=910007, key='Cube', value=2)
            return 대기(self.ctx)


initial_state = 대기
