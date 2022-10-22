""" trigger/63000027_cs/collapse02.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032], visible=True, arg3=0, arg4=0, arg5=0) # GroundGroup01
        set_mesh(triggerIds=[4100,4101,4102,4103,4104,4105,4106,4107,4108,4109,4110,4111,4112,4113,4114,4115,4116,4117,4118,4119,4120,4121,4122,4123,4124,4125,4126,4127,4128,4129,4130,4131,4132,4133,4134,4135,4136,4137,4138,4139,4140,4141,4142,4143,4144,4145,4146,4147,4148,4149,4150,4151,4152,4153,4154,4155,4156,4157,4158,4159,4160,4161,4162,4163,4164,4165,4166,4167,4168,4169,4170,4171,4172,4173,4174,4175,4176,4177,4178,4179,4180,4181,4182,4183,4184], visible=True, arg3=0, arg4=0, arg5=0) # GroundGroup02
        set_user_value(key='CollapseStart', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='CollapseStart', value=1):
            return Delay01()


#  최초 입장 
class Delay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Collapse01()


class Collapse01(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032], visible=False, meshCount=33, arg4=0, delay=100) # GroundGroup01
        set_random_mesh(triggerIds=[4100,4101,4102,4103,4104,4105,4106,4107,4108,4109,4110,4111,4112,4113,4114,4115,4116,4117,4118,4119,4120,4121,4122,4123,4124,4125,4126,4127,4128,4129,4130,4131,4132,4133,4134,4135,4136,4137,4138,4139,4140,4141,4142,4143,4144,4145,4146,4147,4148,4149,4150,4151,4152,4153,4154,4155,4156,4157,4158,4159,4160,4161,4162,4163,4164,4165,4166,4167,4168,4169,4170,4171,4172,4173,4174,4175,4176,4177,4178,4179,4180,4181,4182,4183,4184], visible=False, meshCount=85, arg4=0, delay=120) # GroundGroup02

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Collapse02()


class Collapse02(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='ZoomIn', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='CollapseEnd', value=1)


