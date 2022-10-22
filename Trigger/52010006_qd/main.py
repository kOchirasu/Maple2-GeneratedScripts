""" trigger/52010006_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False)
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002,3003,3004,3005], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3006,3007,3008,3009], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 미카등장()


class 미카등장(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 미카대사01()


class 미카대사01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001285, script='$52010006_QD__MAIN__0$', arg4=4)
        set_scene_skip(state=미카대사02_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 미카대사02()


class 미카대사02_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 미카대사02()


class 미카대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010006_QD__MAIN__10$', arg4=4)
        set_scene_skip(state=몬스터생성_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 몬스터생성()


class 몬스터생성_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_enter(self):
        set_scene_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001_A')
        create_monster(spawnIds=[2001], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 미카이동()


class 미카이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001_B')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=104, spawnIds=[1001]):
            return 미카교체()


class 미카교체(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001])
        create_monster(spawnIds=[1007], arg2=False)
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1001_C')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1007]):
            return 사슬()


class 사슬(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002], arg2=False)
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 카보대사01()


class 카보대사01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001319, script='$52010006_QD__MAIN__1$', arg4=5)
        set_scene_skip(state=카보대사02_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카보대사02()


class 카보대사02_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 카보대사02()


class 카보대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001319, script='$52010006_QD__MAIN__2$', arg4=5)
        set_scene_skip(state=미카친구들소환_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 미카친구들소환()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 미카친구들소환_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 미카친구들소환()


class 미카친구들소환(state.State):
    def on_enter(self):
        set_scene_skip()
        create_monster(spawnIds=[1003,1004,1005], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 스타츠대사01()


class 스타츠대사01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_A')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_A')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_A')
        set_conversation(type=2, spawnId=11001292, script='$52010006_QD__MAIN__3$', arg4=2)
        set_scene_skip(state=둔바대사01_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 둔바대사01()


class 둔바대사01_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 둔바대사01()


class 둔바대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001217, script='$52010006_QD__MAIN__11$', arg4=2)
        set_scene_skip(state=타라대사01_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 타라대사01()


class 타라대사01_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 타라대사01()


class 타라대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001218, script='$52010006_QD__MAIN__12$', arg4=3)
        set_scene_skip(state=카보대사03_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카보대사03()


class 카보대사03_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 카보대사03()


class 카보대사03(state.State):
    def on_enter(self):
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_A')
        set_conversation(type=2, spawnId=11001319, script='$52010006_QD__MAIN__4$', arg4=5)
        set_scene_skip(state=카보소환_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카보소환()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 카보소환_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 카보소환()


class 카보소환(state.State):
    def on_enter(self):
        set_scene_skip()
        destroy_monster(spawnIds=[1002])
        create_monster(spawnIds=[2002], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 카보대사04()


class 카보대사04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2002])
        create_monster(spawnIds=[1006], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001319, script='$52010006_QD__MAIN__5$', arg4=5)
        set_scene_skip(state=카보대사05_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카보대사05()


class 카보대사05_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 카보대사05()


class 카보대사05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001319, script='$52010006_QD__MAIN__6$', arg4=5)
        move_npc(spawnId=1006, patrolName='MS2PatrolData_1002_B')
        set_scene_skip(state=사슬해제_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            destroy_monster(spawnIds=[1006])
            return 사슬해제()


class 사슬해제_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 사슬해제()


class 사슬해제(state.State):
    def on_enter(self):
        set_scene_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_B')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_B')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_B')
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=3)
        set_mesh(triggerIds=[3002,3003,3004,3005], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3006,3007,3008,3009], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            move_npc(spawnId=1007, patrolName='MS2PatrolData_1001_D')
            return 스타츠대사02()


class 스타츠대사02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001292, script='$52010006_QD__MAIN__7$', arg4=5)
        set_scene_skip(state=스타츠대사03_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 스타츠대사03()


class 스타츠대사03_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 스타츠대사03()


class 스타츠대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001292, script='$52010006_QD__MAIN__8$', arg4=5)
        set_scene_skip(state=스타츠대사04_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 스타츠대사04()


class 스타츠대사04_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 스타츠대사04()


class 스타츠대사04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001292, script='$52010006_QD__MAIN__9$', arg4=5)
        set_scene_skip(state=업적이벤트발생_0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            return 업적이벤트발생()


class 업적이벤트발생_0(state.State):
    def on_enter(self):
        set_scene_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 업적이벤트발생()


class 업적이벤트발생(state.State):
    def on_enter(self):
        set_scene_skip()
        set_achievement(triggerId=103, type='trigger', achieve='RescueMika')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=2010030, portalId=4, boxId=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    pass


