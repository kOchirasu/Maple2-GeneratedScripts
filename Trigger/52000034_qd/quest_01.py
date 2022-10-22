""" trigger/52000034_qd/quest_01.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[40002600], questStates=[3]):
            return 기본NPC배치()
        if not quest_user_detected(boxIds=[101], questIds=[40002600], questStates=[3]):
            return 제이시추가배치()


class 제이시추가배치(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001,2002,2003], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[40002603], questStates=[2]):
            return 연출01시작()
        if not quest_user_detected(boxIds=[101], questIds=[40002603], questStates=[2]):
            return 종료()


class 기본NPC배치(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001,2002], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 연출01시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        destroy_monster(spawnIds=[2001,2002,2003])
        create_monster(spawnIds=[1001,1002,1003], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 자베스대사01()


class 자베스대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__0$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 자베스대사02()


class 자베스대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__1$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 브라보대사01()


class 브라보대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__2$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 브라보대사02()


class 브라보대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__3$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 브라보대사03()


class 브라보대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__4$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 자베스대사03()


class 자베스대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__5$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 자베스대사04()


class 자베스대사04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__6$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 브라보대사04()


class 브라보대사04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__7$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 브라보대사05()


class 브라보대사05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__8$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 자베스대사05()


class 자베스대사05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__9$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 자베스대사06()


class 자베스대사06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000034_QD__QUEST_01__10$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 브라보대사06()


class 브라보대사06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__11$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 브라보대사07()


class 브라보대사07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000034_QD__QUEST_01__12$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 잠시대기()


class 잠시대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 제이시대사01()


class 제이시대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001690, script='$52000034_QD__QUEST_01__13$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출01종료()


class 연출01종료(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=301, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[1003])
        create_monster(spawnIds=[2003], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


