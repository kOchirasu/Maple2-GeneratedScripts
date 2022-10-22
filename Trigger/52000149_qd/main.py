""" trigger/52000149_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,111,112])
        set_effect(triggerIds=[6001,6002], visible=True)
        set_npc_emotion_loop(spawnId=111, sequenceName='Sit_Down_A', duration=100000000) # 아시모프
        set_npc_emotion_loop(spawnId=112, sequenceName='Event_02_Idle', duration=100000000) # 아노스
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001633], questStates=[2]):
            return 빈집()
        if quest_user_detected(boxIds=[9000], questIds=[50001633], questStates=[1]):
            return 기본상태()
        if quest_user_detected(boxIds=[9000], questIds=[50001632], questStates=[3]):
            return 기본상태()
        if quest_user_detected(boxIds=[9000], questIds=[50001632], questStates=[2]):
            return 기본상태()
        if quest_user_detected(boxIds=[9000], questIds=[50001632], questStates=[1]):
            return 전경_연출준비()
        if quest_user_detected(boxIds=[9000], questIds=[50001631], questStates=[3]):
            return 기본상태()
        if quest_user_detected(boxIds=[9000], questIds=[50001631], questStates=[2]):
            return 기본상태()
        if quest_user_detected(boxIds=[9000], questIds=[50001631], questStates=[1]):
            return 기본상태()


class 기본상태(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001632], questStates=[1]):
            return 전경_연출준비()


class 전경_연출준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000149, portalId=10)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 전경_연출시작()


class 전경_연출시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000,8010], returnView=False)
        move_user_path(patrolName='MS2PatrolData_pc')
        set_scene_skip(state=아노스아파_스킵완료, arg2='nextState') # setsceneskip 1 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라_아노스줌인()


class 카메라_아노스줌인(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        add_cinematic_talk(npcId=11003436, msg='$52000149_QD__MAIN__0$', duration=3000)
        set_skip(state=아노스아파_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라_아노스줌인01()


class 카메라_아노스줌인01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라_케이틀린01()


class 카메라_케이틀린01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002,8004], returnView=False)
        add_cinematic_talk(npcId=11003436, msg='$52000149_QD__MAIN__1$', duration=3000)
        set_skip(state=아노스아파_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라_케이틀린0102()


class 카메라_케이틀린0102(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라_케이틀린02()


class 카메라_케이틀린02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        set_npc_emotion_loop(spawnId=102, sequenceName='Idle_A', duration=3000)
        add_cinematic_talk(npcId=11003436, msg='$52000149_QD__MAIN__2$', duration=3000)
        add_balloon_talk(spawnId=102, msg='$52000149_QD__MAIN__3$', duration=3000, delayTick=0)
        move_npc(spawnId=102, patrolName='MS2PatrolData_katelyn')
        set_skip(state=아노스아파_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 호르헤이동()


class 호르헤이동(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Jorge')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 빈집(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111,112])
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 연출종료()


class 아노스아파_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        move_user(mapId=52000149, portalId=11)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Jorge')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        set_achievement(triggerId=9000, type='trigger', achieve='AnosReturns')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


