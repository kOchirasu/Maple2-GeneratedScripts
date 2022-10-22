""" trigger/02000224_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[2]):
            return 다음맵으로()
        if quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[1]):
            return 연출준비00()
        if quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[3]):
            return 아르마노있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[2]):
            return 아르마노있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[1]):
            return 아르마노있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[3]):
            return 아르마노있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[2]):
            return 아르마노있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[1]):
            return 기본상태()


class 기본상태(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 아르마노있음(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[1]):
            return 연출준비()
        if not quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[1]):
            return 퀘스트조건체크()
        if wait_tick(waitTick=100):
            return 종료()


class 다음맵으로(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[104], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 연출종료()


class 연출준비00(state.State):
    def on_enter(self):
        set_scene_skip(state=아르마노말썽_스킵완료, arg2='exit') # setsceneskip 정의
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출준비()


class 연출준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=False)
        move_user(mapId=2000224, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 티니에등장()


class 티니에등장(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__18$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Bore_C', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 티니에이동01()


class 티니에이동01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_girl01')
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__0$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아르마노대사01()


class 아르마노대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__1$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        set_skip(state=아르마노대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 티니에대사01()


class 아르마노대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 티니에대사01()


class 티니에대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__2$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        set_skip(state=티니에대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6765):
            return 아르마노대사02()


class 티니에대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아르마노대사02()


class 아르마노대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_girl02')
        set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__3$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        set_skip(state=아르마노대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4597):
            return 티니에대사02()


class 아르마노대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 티니에대사02()


class 티니에대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__4$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        set_skip(state=티니에대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7471):
            return 티니에이동02()


class 티니에대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 티니에이동02()


class 티니에이동02(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_girl02')
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__5$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10109):
            return 티니에대사03()


class 티니에대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__6$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        set_skip(state=티니에대사03_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9090):
            return 아르마노대사03()


class 티니에대사03_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아르마노대사03()


class 아르마노대사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__7$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        set_skip(state=아르마노대사03_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5146):
            return 티니에대사04()


class 아르마노대사03_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 티니에대사04()


class 티니에대사04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__8$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        set_skip(state=티니에대사04_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7418):
            return 아르마노대사04()


class 티니에대사04_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아르마노대사04()


class 아르마노대사04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__9$', arg4=4, arg5=0)
        set_skip(state=아르마노대사04_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아르마노대사05()


class 아르마노대사04_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아르마노대사05()


class 아르마노대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__10$', arg4=3, arg5=0)
        set_skip(state=아르마노대사05_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3030):
            return 아르마노탈주()


class 아르마노대사05_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아르마노탈주()


class 아르마노탈주(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_boy01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 티니에대사05()


class 티니에대사05(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_girl03')
        destroy_monster(spawnIds=[101])
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__11$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 티니에대사06()


class 티니에대사06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        move_user_path(patrolName='MS2PatrolData_PC01')
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__12$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Bore_C', duration=4000)
        set_skip(state=티니에대사06_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11023):
            return PC대사01()


class 티니에대사06_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return PC대사01()


class PC대사01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$02000224_BF__MAIN__13$', arg4=3, arg5=0)
        set_pc_emotion_loop(sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 티니에대사07()


class 티니에대사07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__14$', arg4=4, arg5=0)
        set_npc_emotion_sequence(spawnId=103, sequenceName='ChatUp_A')
        set_skip(state=티니에대사07_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7810):
            return PC대사02()


class 티니에대사07_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 티니에대사08()


class PC대사02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$02000224_BF__MAIN__15$', arg4=3, arg5=0)
        set_pc_emotion_loop(sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 티니에대사08()


class 티니에대사08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__16$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        set_skip(state=티니에대사08_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7497):
            return 티니에대사09()


class 티니에대사08_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 티니에대사09()


class 티니에대사09(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__17$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7157):
            return 연출종료()


class 아르마노말썽_스킵완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,103])
        create_monster(spawnIds=[104], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        set_achievement(triggerId=9000, type='trigger', achieve='foolishson')
        move_user(mapId=2000054, portalId=10)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


