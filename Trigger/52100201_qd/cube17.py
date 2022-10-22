""" trigger/52100201_qd/cube17.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Cube', value=1):
            return 큐브17()


class 큐브17(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4029,4030,4031,4032], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[5029,5030,5031,5032], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_user_value(triggerId=920017, key='CubeOff', value=1)
            return 메쉬제거()


class 메쉬제거(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Cube', value=2):
            set_user_value(triggerId=910017, key='Cube', value=1)
            return 큐브제거()


class 큐브제거(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4029,4030,4031,4032], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[5029,5030,5031,5032], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 큐브17()
        if user_detected(boxIds=[9004]):
            set_user_value(triggerId=910017, key='Cube', value=0)
            return 종료()
        if user_detected(boxIds=[9005]):
            set_user_value(triggerId=910017, key='Cube', value=0)
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 대기()


