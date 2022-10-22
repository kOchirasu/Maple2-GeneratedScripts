""" trigger/52000030_qd/main_k.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101], jobCode=10):
            return 연출시작()
        if user_detected(boxIds=[101], jobCode=1):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Nutaman_intro.swf', movieId=1)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 이슈라대사01()


class 이슈라대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001230, script='$52000030_QD__MAIN_K__0$', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=11000076, script='$52000030_QD__MAIN_K__1$', arg4=3, arg5=0)
        set_skip(state=NPC 단체 이동)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return NPC 단체 이동()


class NPC 단체 이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001')
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005')
        move_npc(spawnId=1006, patrolName='MS2PatrolData_1006')
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1007')
        move_npc(spawnId=1008, patrolName='MS2PatrolData_1008')
        move_npc(spawnId=1009, patrolName='MS2PatrolData_1009')
        move_npc(spawnId=1010, patrolName='MS2PatrolData_1010')
        move_npc(spawnId=1011, patrolName='MS2PatrolData_1011')
        move_npc(spawnId=1012, patrolName='MS2PatrolData_1001')
        move_npc(spawnId=1013, patrolName='MS2PatrolData_1002')
        move_npc(spawnId=1014, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014]):
            return 전투판으로이동()

    def on_exit(self):
        destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014])
        create_monster(spawnIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,2001,2002], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 전투판으로이동(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=False)
        move_user(mapId=52000030, portalId=100)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2002]):
            return 차전투2()

    def on_exit(self):
        destroy_monster(spawnIds=[2001])


class 차전투2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2003,2004], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2003]):
            return 이슈라대사02()

    def on_exit(self):
        destroy_monster(spawnIds=[2004])


class 이슈라대사02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000076, script='$52000030_QD__MAIN_K__2$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 차전투3()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 차전투3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2005], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2005]):
            return 이슈라대사03()


class 이슈라대사03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001244, script='$52000030_QD__MAIN_K__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            move_user(mapId=52000031, portalId=0)
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 종료(state.State):
    pass


