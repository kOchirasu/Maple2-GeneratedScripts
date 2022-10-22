""" trigger/52000046_qd/10003042.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002,2002], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[10003042], questStates=[2]):
            return 연출시작()

    def on_exit(self):
        destroy_monster(spawnIds=[2002])
        create_monster(spawnIds=[2001], arg2=False)


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        add_buff(boxIds=[199], skillId=70000095, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 자베스대사01()


class 자베스대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000046_QD__10003042__0$', arg4=3)
        set_skip(state=자베스대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 브라보대사01()


class 자베스대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 브라보대사01()


class 브라보대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000046_QD__10003042__1$', arg4=3)
        set_skip(state=브라보대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 제이시대사01()


class 브라보대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 제이시대사01()


class 제이시대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000515, script='$52000046_QD__10003042__2$', arg4=5)
        set_skip(state=제이시대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출종료()


class 제이시대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2001])
        create_monster(spawnIds=[2002], arg2=False)
        add_buff(boxIds=[199], skillId=70000096, level=1)
        move_user(mapId=52000046, portalId=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10):
            move_user_path(patrolName='MS2PatrolData_9000')
            return 종료()


class 종료(state.State):
    pass


