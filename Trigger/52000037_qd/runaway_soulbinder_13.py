""" trigger/52000037_qd/runaway_soulbinder_13.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9400], questIds=[50001411], questStates=[2], jobCode=110):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=603, enable=True)
        move_user(mapId=52000037, portalId=11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return PC말풍선딜레이()


class PC말풍선딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            move_user_path(patrolName='MS2PatrolData_PC1102A')
            return PC말풍선01()


class PC말풍선01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선02()


class PC말풍선02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선03()


class PC말풍선03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__2$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 말풍선딜레이()


class 말풍선딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            move_user_path(patrolName='MS2PatrolData_PC1102B')
            return PC말풍선04()


class PC말풍선04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__3$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PC말풍선05()


class PC말풍선05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__4$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NPC등장()


class NPC등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[211,212,213], arg2=False)
        select_camera(triggerId=604, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NPC대사01()


class NPC대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001727, script='$52000037_QD__RUNAWAY_SOULBINDER_13__5$', arg4=2)
        set_skip(state=NPC대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NPC대사02()


class NPC대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return NPC대사02()


class NPC대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001725, script='$52000037_QD__RUNAWAY_SOULBINDER_13__6$', arg4=2)
        set_skip(state=NPC대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC도주()


class NPC대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return PC도주()


class PC도주(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        select_camera(triggerId=605, enable=True)
        move_user_path(patrolName='MS2PatrolData_PC1102C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PC말풍선06()


class PC말풍선06(state.State):
    def on_enter(self):
        move_npc(spawnId=211, patrolName='MS2PatrolData_NPC1102')
        move_npc(spawnId=212, patrolName='MS2PatrolData_NPC1102')
        move_npc(spawnId=213, patrolName='MS2PatrolData_NPC1102')
        set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__7$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        move_user(mapId=2000043, portalId=5)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 종료()


class 종료(state.State):
    pass


