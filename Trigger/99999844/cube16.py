""" trigger/99999844/cube16.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Cube', value=1):
            return 큐브16(self.ctx)


class 큐브16(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4028], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[5028], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_user_value(triggerId=920016, key='CubeOff', value=1)
            return 메쉬제거(self.ctx)


class 메쉬제거(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Cube', value=2):
            self.set_user_value(triggerId=910016, key='Cube', value=1)
            return 큐브제거(self.ctx)


class 큐브제거(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4028], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[5028], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3200):
            return 큐브16(self.ctx)
        if self.user_detected(boxIds=[9004]):
            self.set_user_value(triggerId=910016, key='Cube', value=0)
            return 종료(self.ctx)
        if self.user_detected(boxIds=[9005]):
            self.set_user_value(triggerId=910016, key='Cube', value=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 대기(self.ctx)


initial_state = 대기
