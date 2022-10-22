""" trigger/52000056_qd/50001460.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[606], visible=False)
        set_effect(triggerIds=[607], visible=False)
        set_effect(triggerIds=[608], visible=False)
        set_effect(triggerIds=[609], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_effect(triggerIds=[611], visible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008], visible=True, arg3=0, arg4=0, arg5=0)
        set_gravity(gravity=-9.8)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103,104,105,106]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        move_user(mapId=52000056, portalId=3)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC말풍선01()


class PC말풍선01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000056_QD__50001460__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 낙하준비()


class 낙하준비(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008], visible=False, arg3=0, arg4=200, arg5=2)
        set_gravity(gravity=-37)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 낙하시작()


class 낙하시작(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 낙하종료()


class 낙하종료(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC말풍선02()


class PC말풍선02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000056_QD__50001460__1$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PC말풍선03()


class PC말풍선03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000056_QD__50001460__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_effect(triggerIds=[601], visible=True)
            set_effect(triggerIds=[602], visible=True)
            set_effect(triggerIds=[603], visible=True)
            set_effect(triggerIds=[604], visible=True)
            set_effect(triggerIds=[605], visible=True)
            set_effect(triggerIds=[606], visible=True)
            set_effect(triggerIds=[607], visible=True)
            set_effect(triggerIds=[608], visible=True)
            set_effect(triggerIds=[609], visible=True)
            set_effect(triggerIds=[610], visible=True)
            set_effect(triggerIds=[611], visible=True)
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            set_gravity(gravity=-9.8)
            return 이펙트종료대기()


class 이펙트종료대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            set_effect(triggerIds=[601], visible=False)
            set_effect(triggerIds=[602], visible=False)
            set_effect(triggerIds=[603], visible=False)
            set_effect(triggerIds=[604], visible=False)
            set_effect(triggerIds=[605], visible=False)
            set_effect(triggerIds=[606], visible=False)
            set_effect(triggerIds=[607], visible=False)
            set_effect(triggerIds=[608], visible=False)
            set_effect(triggerIds=[609], visible=False)
            set_effect(triggerIds=[610], visible=False)
            set_effect(triggerIds=[611], visible=False)
            return 종료()


class 종료(state.State):
    pass


