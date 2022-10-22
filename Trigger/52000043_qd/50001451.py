""" trigger/52000043_qd/50001451.xml """
from common import *
import state


class 시작조건(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[1]):
            return 연출시작()
        if quest_user_detected(boxIds=[199], questIds=[50001451], questStates=[2]):
            return NPC만배치()


class NPC만배치(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,2001], arg2=False)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,2001], arg2=False)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라딜레이()


class 카메라딜레이(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 준타대사01()


class 준타대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001451__0$', arg4=3)
        set_skip(state=준타대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 틴차이대사01()


class 준타대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사01()


class 틴차이대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001451__1$', arg4=4)
        set_skip(state=틴차이대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 준타대사02()


class 틴차이대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사02()


class 준타대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001451__2$', arg4=3)
        set_skip(state=준타대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 준타대사03()


class 준타대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사03()


class 준타대사03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001451__3$', arg4=4)
        set_skip(state=준타대사03스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 틴차이대사02()


class 준타대사03스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 틴차이대사02()


class 틴차이대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000043_QD__50001451__4$', arg4=5)
        set_skip(state=틴차이대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 준타대사04()


class 틴차이대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 준타대사04()


class 준타대사04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        set_conversation(type=2, spawnId=11001557, script='$52000043_QD__50001451__5$', arg4=2)
        set_skip(state=준타대사04스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 준타대사04스킵(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=False)
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=302, enable=False)
        set_achievement(triggerId=199, type='trigger', achieve='gdworry')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 종료()


class 종료(state.State):
    pass


