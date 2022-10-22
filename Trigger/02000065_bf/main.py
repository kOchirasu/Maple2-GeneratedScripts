""" trigger/02000065_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001630], questStates=[3]):
            return 기본상태()
        if quest_user_detected(boxIds=[9000], questIds=[50001630], questStates=[2]):
            return 앤있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001630], questStates=[1]):
            return 앤있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001625], questStates=[3]):
            return 앤있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001625], questStates=[2]):
            return 연출2준비()
        if quest_user_detected(boxIds=[9000], questIds=[50001625], questStates=[1]):
            return 앤있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001624], questStates=[3]):
            return 앤있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001624], questStates=[2]):
            return 앤있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001624], questStates=[1]):
            return 앤있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001623], questStates=[3]):
            return 앤있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001623], questStates=[2]):
            return 앤있음()
        if quest_user_detected(boxIds=[9000], questIds=[50001623], questStates=[1]):
            return 연출1준비()
        if quest_user_detected(boxIds=[9000], questIds=[50001622], questStates=[3]):
            return 기본상태()


class 기본상태(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,111])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 앤있음(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001625], questStates=[2]):
            return 연출2준비()
        if wait_tick(waitTick=100):
            return 종료()


class 연출1준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[101], arg2=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출1앤등장준비()


class 연출1앤등장준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 앤등장()


class 앤등장(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_ann01')
        add_cinematic_talk(npcId=11003432, illustId='Ann_normal', msg='$02000065_BF__MAIN__0$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 앤등장2()


class 앤등장2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        add_balloon_talk(spawnId=101, msg='$02000065_BF__MAIN__1$', duration=3000, delayTick=0)
        # <action name="NPC를이동시킨다" arg1="101" arg2="MS2PatrolData_ann02" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출종료()


class 연출2준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[111], arg2=False)
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출2준비1()


class 연출2준비1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 앤대사01()


class 앤대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010,8011], returnView=False)
        add_cinematic_talk(npcId=11003432, msg='$02000065_BF__MAIN__2$', duration=3000)
        set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=3000)
        set_scene_skip(state=칼과앤_스킵완료, arg2='nextState') # setsceneskip set
        set_skip(state=앤대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 칼대사01()


class 앤대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칼대사01()


class 칼대사01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000074, msg='$02000065_BF__MAIN__3$', duration=3000)
        set_skip(state=칼대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 앤대사02()


class 칼대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 앤대사02()


class 앤대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003432, msg='$02000065_BF__MAIN__4$', duration=4000)
        set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=3000)
        set_skip(state=앤대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6400):
            return 칼대사02()


class 앤대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칼대사02()


class 칼대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000074, msg='$02000065_BF__MAIN__5$', duration=3000)
        set_skip(state=칼대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8071):
            return 앤대사03()


class 칼대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 앤대사03()


class 앤대사03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003432, msg='$02000065_BF__MAIN__6$', duration=3000)
        set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=2000)
        set_skip(state=앤대사03_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6713):
            return 칼대사03()


class 앤대사03_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칼대사03()


class 칼대사03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000074, msg='$02000065_BF__MAIN__7$', duration=4000)
        set_skip(state=칼대사03_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9769):
            return 앤대사04()


class 칼대사03_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 앤대사04()


class 앤대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003432, msg='$02000065_BF__MAIN__8$', duration=3000)
        set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=2000)
        set_skip(state=앤대사04_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 칼대사04()


class 앤대사04_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 칼대사04()


class 칼대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000074, msg='$02000065_BF__MAIN__9$', duration=3000)
        set_skip(state=칼대사04_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7471):
            return 앤대사05()


class 칼대사04_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 앤대사05()


class 앤대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        set_conversation(type=2, spawnId=11003432, script='$02000065_BF__MAIN__10$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3160):
            return 카메라아웃()


class 카메라아웃(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000,8001], returnView=False)
        visible_my_pc(isVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 칼과앤_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        visible_my_pc(isVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        set_achievement(triggerId=9000, type='trigger', achieve='meetingAnn')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


