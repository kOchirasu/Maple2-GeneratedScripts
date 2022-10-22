""" trigger/02000304_bf/mesh.xml """
from common import *
import state


class 시작대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4101,4102,4103,4104,4105,4106,4107,4108,4109,4110,4111,4112,4113,4114,4115,4116], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212,4213,4214,4215,4216], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4301,4302,4303,4304,4305,4306,4307,4308,4309,4310,4311,4312,4313,4314,4315,4316], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414,4415,4416], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2001]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='10'):
            return 패턴01랜덤()


class 패턴01랜덤(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if random_condition(rate=25):
            return 패턴01_A()
        if random_condition(rate=25):
            return 패턴01_B()
        if random_condition(rate=25):
            return 패턴01_C()
        if random_condition(rate=25):
            return 패턴01_D()


class 패턴01_A(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4101], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4204], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4313], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4416], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3101], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3204], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3313], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3416], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4101], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4204], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4313], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4416], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴01종료()


class 패턴01_B(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4115], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4214], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4303], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4402], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3115], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3214], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3303], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3402], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4115], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4214], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4303], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4402], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴01종료()


class 패턴01_C(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4110], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4211], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4307], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4406], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3110], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3211], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3307], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3406], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4110], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4211], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4307], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4406], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴01종료()


class 패턴01_D(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4116], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4213], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4304], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4401], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3213], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3304], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3401], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4213], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4304], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4401], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴01종료()


class 패턴01종료(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='5'):
            set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, arg4=0, arg5=0)
            return 패턴02시작()


class 패턴02시작(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='10'):
            return 패턴02랜덤()


class 패턴02랜덤(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if random_condition(rate=25):
            return 패턴02_A()
        if random_condition(rate=25):
            return 패턴02_B()
        if random_condition(rate=25):
            return 패턴02_C()
        if random_condition(rate=25):
            return 패턴02_D()


class 패턴02_A(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4113], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4216], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4301], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4404], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3113], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3301], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3404], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4113], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4301], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4404], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴02종료()


class 패턴02_B(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4112], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4212], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4312], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4412], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3112], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3212], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3312], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3412], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4112], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4212], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4312], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4412], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴02종료()


class 패턴02_C(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4104], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4216], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4304], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4416], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3104], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3304], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3416], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4104], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4304], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4416], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴02종료()


class 패턴02_D(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4107], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4206], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4307], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4406], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3107], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3206], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3307], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3406], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4107], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4206], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4307], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4406], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴02종료()


class 패턴02종료(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='5'):
            set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, arg4=0, arg5=0)
            return 패턴03시작()


class 패턴03시작(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='15'):
            return 패턴03랜덤()


class 패턴03랜덤(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if random_condition(rate=25):
            return 패턴03_A()
        if random_condition(rate=25):
            return 패턴03_B()
        if random_condition(rate=25):
            return 패턴03_C()
        if random_condition(rate=25):
            return 패턴03_D()


class 패턴03_A(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4101,4116], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4204,4213], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4304,4313], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4401,4416], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3101,3116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3204,3213], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3304,3313], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3401,3416], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4101,4116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4204,4213], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4304,4313], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4401,4416], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴03종료()


class 패턴03_B(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4106,4111], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4207,4210], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4307,4310], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4406,4411], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3106,3111], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3207,3210], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3307,3310], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3406,3411], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4106,4111], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4207,4210], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4307,4310], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4406,4411], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴03종료()


class 패턴03_C(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4103,4114], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4202,4215], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4302,4315], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4403,4414], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3103,3114], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3202,3215], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3302,3315], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3403,3414], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4103,4114], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4202,4215], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4302,4315], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4403,4414], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴03종료()


class 패턴03_D(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4108,4110], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4205,4211], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4306,4312], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4407,4409], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3108,3110], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3205,3211], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3306,3312], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3407,3409], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4108,4110], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4205,4211], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4306,4312], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4407,4409], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴03종료()


class 패턴03종료(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='5'):
            set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, arg4=0, arg5=0)
            return 패턴04시작()


class 패턴04시작(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='15'):
            return 패턴04랜덤()


class 패턴04랜덤(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if random_condition(rate=25):
            return 패턴04_A()
        if random_condition(rate=25):
            return 패턴04_B()
        if random_condition(rate=25):
            return 패턴04_C()
        if random_condition(rate=25):
            return 패턴04_D()


class 패턴04_A(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4112,4115], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4209,4214], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4303,4308], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4402,4415], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3112,3115], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3209,3214], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3303,3308], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3402,3415], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4112,4115], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4209,4214], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4303,4308], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4402,4415], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴04종료()


class 패턴04_B(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4104,4113], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4201,4216], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4301,4316], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4404,4413], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3104,3113], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3201,3216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3301,3316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3404,3413], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4104,4113], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4201,4216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4301,4316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4404,4413], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴04종료()


class 패턴04_C(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4102,4114], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4203,4215], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4302,4314], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4403,4415], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3102,3114], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3203,3215], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3302,3314], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3403,3415], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4102,4114], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4203,4215], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4302,4314], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4403,4415], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴04종료()


class 패턴04_D(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4112,4116], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4209,4213], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4304,4308], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4401,4405], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3112,3116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3209,3213], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3304,3308], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3401,3405], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4112,4116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4209,4213], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4304,4308], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4401,4405], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴04종료()


class 패턴04종료(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='5'):
            set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, arg4=0, arg5=0)
            return 패턴05시작()


class 패턴05시작(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='15'):
            return 패턴05랜덤()


class 패턴05랜덤(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if random_condition(rate=25):
            return 패턴05_A()
        if random_condition(rate=25):
            return 패턴05_B()
        if random_condition(rate=25):
            return 패턴05_C()
        if random_condition(rate=25):
            return 패턴05_D()


class 패턴05_A(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4101,4106,4111], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4204,4207,4210], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4307,4310,4313], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4406,4411,4416], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3101,3106,3111], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3204,3207,3210], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3307,3310,3313], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3406,3411,3416], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4101,4106,4111], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4204,4207,4210], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4307,4310,4313], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4406,4411,4416], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴05종료()


class 패턴05_B(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4104,4107,4110], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4201,4206,4211], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4306,4311,4316], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4407,4410,4413], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3104,3107,3110], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3201,3206,3211], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3306,3311,3316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3407,3410,3413], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4104,4107,4110], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4201,4206,4211], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4306,4311,4316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4407,4410,4413], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴05종료()


class 패턴05_C(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4101,4104,4113], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4201,4204,4216], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4301,4313,4316], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4404,4413,4416], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3101,3104,3113], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3201,3204,3216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3301,3313,3316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3404,3413,3416], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4101,4104,4113], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4201,4204,4216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4301,4313,4316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4404,4413,4416], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴05종료()


class 패턴05_D(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4103,4106,4108], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4202,4205,4207], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4310,4312,4315], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4409,4411,4414], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3103,3106,3108], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3202,3205,3207], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3310,3312,3315], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3409,3411,3414], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4103,4106,4108], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4202,4205,4207], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4310,4312,4315], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4409,4411,4414], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴05종료()


class 패턴05종료(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='5'):
            set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, arg4=0, arg5=0)
            return 패턴06시작()


class 패턴06시작(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='15'):
            return 패턴06랜덤()


class 패턴06랜덤(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if random_condition(rate=25):
            return 패턴06_A()
        if random_condition(rate=25):
            return 패턴06_B()
        if random_condition(rate=25):
            return 패턴06_C()
        if random_condition(rate=25):
            return 패턴06_D()


class 패턴06_A(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4104,4107,4112], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4201,4206,4209], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4308,4311,4316], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4405,4410,4413], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3104,3107,3112], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3201,3206,3209], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3308,3311,3316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3405,3410,3413], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4104,4107,4112], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4201,4206,4209], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4308,4311,4316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4405,4410,4413], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴06종료()


class 패턴06_B(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4112,4115,4116], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4209,4213,4214], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4303,4304,4308], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4401,4402,4405], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3112,3115,3116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3209,3213,3214], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3303,3304,3308], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3401,3402,3405], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4112,4115,4116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4209,4213,4214], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4303,4304,4308], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4401,4402,4405], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴06종료()


class 패턴06_C(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4101,4102,4105], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4203,4204,4208], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4309,4313,4314], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4412,4415,4416], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3101,3102,3105], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3203,3204,3208], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3309,3313,3314], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3412,3415,3416], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4101,4102,4105], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4203,4204,4208], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4309,4313,4314], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4412,4415,4416], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴06종료()


class 패턴06_D(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4107,4109,4115], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4206,4212,4214], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4308,4310,4316], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4405,4411,4413], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3107,3109,3115], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3206,3212,3214], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3308,3310,3316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3405,3411,3413], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4107,4109,4115], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4206,4212,4214], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4308,4310,4316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4405,4411,4413], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴06종료()


class 패턴06종료(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='5'):
            set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, arg4=0, arg5=0)
            return 패턴07시작()


class 패턴07시작(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=15)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='15'):
            return 패턴07랜덤()


class 패턴07랜덤(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if random_condition(rate=10):
            return 패턴07_A()
        if random_condition(rate=10):
            return 패턴07_B()
        if random_condition(rate=10):
            return 패턴07_C()
        if random_condition(rate=10):
            return 패턴07_D()
        if random_condition(rate=10):
            return 패턴07_E()
        if random_condition(rate=10):
            return 패턴07_F()
        if random_condition(rate=10):
            return 패턴07_G()
        if random_condition(rate=10):
            return 패턴07_H()
        if random_condition(rate=10):
            return 패턴07_I()
        if random_condition(rate=10):
            return 패턴07_J()


class 패턴07_A(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4101,4106,4111,4116], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4204,4207,4210,4213], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4304,4307,4310,4313], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4401,4406,4411,4416], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3101,3106,3111,3116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3204,3207,3210,3213], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3304,3307,3310,3313], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3401,3406,3411,3416], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4101,4106,4111,4116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4204,4207,4210,4213], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4304,4307,4310,4313], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4401,4406,4411,4416], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴07종료()


class 패턴07_B(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4104,4107,4110,4113], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4201,4206,4211,4216], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4301,4306,4311,4316], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4404,4407,4410,4413], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3104,3107,3110,3113], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3201,3206,3211,3216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3301,3306,3311,3316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3404,3407,3410,3413], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4104,4107,4110,4113], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4201,4206,4211,4216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4301,4306,4311,4316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4404,4407,4410,4413], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴07종료()


class 패턴07_C(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4102,4105,4107,4110], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4203,4206,4208,4211], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4302,4305,4307,4310], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4403,4406,4408,4411], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3102,3105,3107,3110], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3203,3206,3208,3211], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3302,3305,3307,3310], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3403,3406,3408,3411], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4102,4105,4107,4110], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4203,4206,4208,4211], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4302,4305,4307,4310], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4403,4406,4408,4411], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴07종료()


class 패턴07_D(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4109,4111,4114,4116], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4209,4211,4214,4216], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4309,4311,4314,4316], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4409,4411,4414,4416], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3109,3111,3114,3116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3209,3211,3214,3216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3309,3311,3314,3316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3409,3411,3414,3416], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4109,4111,4114,4116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4209,4211,4214,4216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4309,4311,4314,4316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4409,4411,4414,4416], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴07종료()


class 패턴07_E(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4101,4104,4113,4116], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4201,4204,4213,4216], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4301,4304,4313,4316], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4401,4404,4413,4416], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3101,3104,3113,3116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3201,3204,3213,3216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3301,3304,3313,3316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3401,3404,3413,3416], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4101,4104,4113,4116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4201,4204,4213,4216], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4301,4304,4313,4316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4401,4404,4413,4416], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴07종료()


class 패턴07_F(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4106,4107,4110,4111], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4206,4207,4210,4211], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4306,4307,4310,4311], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4406,4407,4410,4411], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3106,3107,3110,3111], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3206,3207,3210,3211], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3306,3307,3310,3311], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3406,3407,3410,3411], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4106,4107,4110,4111], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4206,4207,4210,4211], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4306,4307,4310,4311], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4406,4407,4410,4411], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴07종료()


class 패턴07_G(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4111,4112,4115,4116], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4209,4210,4213,4214], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4303,4304,4307,4308], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4401,4402,4405,4406], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3111,3112,3115,3116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3209,3210,3213,3214], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3303,3304,3307,3308], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3401,3402,3405,3406], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4111,4112,4115,4116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4209,4210,4213,4214], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4303,4304,4307,4308], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4401,4402,4405,4406], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴07종료()


class 패턴07_H(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4102,4103,4114,4115], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4202,4203,4214,4215], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4302,4303,4314,4315], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4402,4403,4414,4415], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3102,3103,3114,3115], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3202,3203,3214,3215], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3302,3303,3314,3315], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3402,3403,3414,3415], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4102,4103,4114,4115], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4202,4203,4214,4215], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4302,4303,4314,4315], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4402,4403,4414,4415], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴07종료()


class 패턴07_I(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4104,4108,4112,4116], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4201,4205,4209,4213], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4304,4308,4312,4316], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4401,4405,4409,4413], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3104,3108,3112,3116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3201,3205,3209,3213], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3304,3308,3312,3316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3401,3405,3409,3413], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4104,4108,4112,4116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4201,4205,4209,4213], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4304,4308,4312,4316], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4401,4405,4409,4413], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴07종료()


class 패턴07_J(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4108,4111,4114,4116], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4205,4210,4213,4215], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4302,4304,4307,4312], visible=True, arg3=0, arg4=0, arg5=2)
        set_mesh(triggerIds=[4401,4403,4406,4409], visible=True, arg3=0, arg4=0, arg5=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3108,3111,3114,3116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3205,3210,3213,3215], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3302,3304,3307,3312], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[3401,3403,3406,3409], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4108,4111,4114,4116], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4205,4210,4213,4215], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4302,4304,4307,4312], visible=False, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[4401,4403,4406,4409], visible=False, arg3=0, arg4=0, arg5=2)
            return 패턴07종료()


class 패턴07종료(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 종료()
        if time_expired(timerId='5'):
            set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, arg4=0, arg5=0)
            return 패턴07시작()


class 종료(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416], visible=True, arg3=0, arg4=0, arg5=0)
        set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1800000'):
            return None # Missing State: 종료2


