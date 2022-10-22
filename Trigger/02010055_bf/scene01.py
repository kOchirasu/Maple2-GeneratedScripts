""" trigger/02010055_bf/scene01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_effect(triggerIds=[699], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 바르칸트대사()


class 바르칸트대사(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        set_effect(triggerIds=[699], visible=True)
        set_conversation(type=2, spawnId=23000068, script='$02010055_BF__SCENE01__0$', arg4=4)
        set_skip(state=바르칸트대사2스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 바르칸트대사2()


class 바르칸트대사2스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 바르칸트대사2()


class 바르칸트대사2(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        set_effect(triggerIds=[699], visible=True)
        set_conversation(type=2, spawnId=23000068, script='$02010055_BF__SCENE01__1$', arg4=4)
        set_skip(state=종료준비)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 종료()


class 종료준비(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


