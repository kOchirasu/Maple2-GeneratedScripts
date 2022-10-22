""" trigger/52010007_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[100], questIds=[10002834], questStates=[1]):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1002,1003,1004], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_A')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_A')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_A')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1002]):
            return 둔바대사01()
        if npc_detected(boxId=102, spawnIds=[1003]):
            return 둔바대사01()


class 둔바대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001217, script='$52010007_QD__MAIN__0$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에레브대사01()


class 에레브대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010007_QD__MAIN__1$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NPC이동2()


class NPC이동2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_B')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_B')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 말풍선대사01()


class 말풍선대사01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1003, script='$52010007_QD__MAIN__2$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 말풍선대사02()


class 말풍선대사02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1003, script='$52010007_QD__MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 말풍선대사03()


class 말풍선대사03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1004, script='$52010007_QD__MAIN__4$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 스타츠대사01()


class 스타츠대사01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001292, script='$52010007_QD__MAIN__5$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 스타츠이동()


class 스타츠이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 타라이동()


class 타라이동(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_C')
        set_conversation(type=1, spawnId=1004, script='$52010007_QD__MAIN__6$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 둔바이동()


class 둔바이동(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1002])
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_C')
        set_conversation(type=1, spawnId=1003, script='$52010007_QD__MAIN__7$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에레브대사02()


class 에레브대사02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[1003,1004])
        set_conversation(type=2, spawnId=11000075, script='$52010007_QD__MAIN__8$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에레브대사03()


class 에레브대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010007_QD__MAIN__9$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            select_camera(triggerId=301, enable=False)
            set_achievement(triggerId=100, type='trigger', achieve='Find_Lamestone')
            return 종료()


class 종료(state.State):
    pass


