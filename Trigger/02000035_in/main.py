""" trigger/02000035_in/main.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[3]):
            return 기본()
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[2]):
            return 탈주이후()
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[1]):
            return 탈주이후()
        if quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[3]):
            return 탈주이후()
        if quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[2]):
            return 탈주이후()
        if quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[1]):
            return npc스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[3]):
            return npc스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[2]):
            return npc스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[1]):
            return 기본()


class 기본(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class npc스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[1]):
            return 연출준비()
        if not quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[1]):
            return NPC스폰조건01()


class NPC스폰조건01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[2]):
            return 탈주이후()
        if quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[1]):
            return 연출준비()
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[3]):
            return NPC스폰조건02()
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[2]):
            return NPC스폰조건02()
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[1]):
            return 기본()


class NPC스폰조건02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[2]):
            return 탈주이후()
        if quest_user_detected(boxIds=[9000], questIds=[50001605], questStates=[1]):
            return 연출준비()
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[3]):
            return NPC스폰조건01()
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[2]):
            return NPC스폰조건01()
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[1]):
            return 기본()


class 탈주이후(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102,103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 연출준비00(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출준비()


class 연출준비(state.State):
    def on_enter(self):
        move_user(mapId=2000035, portalId=10)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=케이틀린슬픔_스킵완료, arg2='nextState') # setsceneskip set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 언쟁시작()


class 언쟁시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_conversation(type=2, spawnId=11003264, script='$02000035_IN__MAIN__0$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8150):
            return 케이틀린대사01()


class 케이틀린대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__1$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        set_skip(state=케이틀린대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6400):
            return 앤대사01()


class 케이틀린대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 앤대사01()


class 앤대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003264, script='$02000035_IN__MAIN__2$', arg4=5, arg5=0)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        set_skip(state=앤대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5328):
            return 케이틀린대사02()


class 앤대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 케이틀린대사02()


class 케이틀린대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__3$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        set_skip(state=케이틀린대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9404):
            return 호르헤대사01()


class 케이틀린대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 호르헤대사01()


class 호르헤대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006], returnView=False)
        set_conversation(type=2, spawnId=11003263, script='$02000035_IN__MAIN__4$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)
        set_skip(state=호르헤대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 케이틀린대사03()


class 호르헤대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 케이틀린대사03()


class 케이틀린대사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__5$', arg4=5, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        set_skip(state=케이틀린대사03_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9404):
            return 앤대사02()


class 케이틀린대사03_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 앤대사02()


class 앤대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)
        set_conversation(type=2, spawnId=11003264, script='$02000035_IN__MAIN__9$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='ChatUp_A', duration=2000)
        set_skip(state=앤대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 호르헤대사02()


class 앤대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 호르헤대사02()


class 호르헤대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006], returnView=False)
        set_conversation(type=2, spawnId=11003263, script='$02000035_IN__MAIN__10$', arg4=2, arg5=0)
        set_npc_emotion_loop(spawnId=102, sequenceName='ChatUp_A', duration=2000)
        set_skip(state=호르헤대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 케이틀린대사04()


class 호르헤대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 케이틀린대사04()


class 케이틀린대사04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__6$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        set_skip(state=케이틀린대사04_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4780):
            return 케이틀린탈주01()


class 케이틀린대사04_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 케이틀린탈주01()


class 케이틀린탈주01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_100_wayout')
        move_user_path(patrolName='MS2PatrolData_PC01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 케이틀린탈주02()


class 케이틀린탈주02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003262, script='$02000035_IN__MAIN__7$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 케이틀린탈주03()


class 케이틀린탈주03(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_101_wayout')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC멈칫()


class PC멈칫(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$02000035_IN__MAIN__11$', arg4=2, arg5=0)
        # <action name="SetPcEmotionLoop" arg1="Talk_A" arg2="1000"/>
        destroy_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 앤대사03()


class 앤대사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)
        set_conversation(type=2, spawnId=11003264, script='$02000035_IN__MAIN__8$', arg4=3, arg5=0)
        # <action name="SetNpcEmotionLoop" arg1="103" arg2="ChatUp_A" arg="3000"/>
        set_npc_emotion_sequence(spawnId=103, sequenceName='ChatUp_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4022):
            return 연출종료()


class 케이틀린슬픔_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[101])
        move_user_path(patrolName='MS2PatrolData_PC01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_achievement(triggerId=9000, type='trigger', achieve='KatelyninGrief')
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    pass


