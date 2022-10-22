""" trigger/52000136_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601,602], visible=False)
        create_monster(spawnIds=[101], arg2=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[1]):
            return 기본()
        if quest_user_detected(boxIds=[9000], questIds=[50001603], questStates=[3]):
            return 기본()
        if quest_user_detected(boxIds=[9000], questIds=[50001603], questStates=[2]):
            return 연출시작()


class 기본(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 첫진입()


class 첫진입(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000136_QD__MAIN__0$', duration=3000, align='left')
        set_scene_skip(state=불안한케이틀린_스킵완료, arg2='nextState') # setsceneskip 1 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전경스케치01()


class 전경스케치01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_skip(state=불안한케이틀린_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전경스케치02()


class 전경스케치02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        move_user(mapId=52000136, portalId=10)
        set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 케이틀린발견01()


class 케이틀린발견01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        move_npc(spawnId=101, patrolName='Patrol_101_katelyn_wander')
        add_balloon_talk(spawnId=101, msg='$52000136_QD__MAIN__1$', duration=1000, delayTick=0)
        add_balloon_talk(spawnId=101, msg='$52000136_QD__MAIN__2$', duration=1000, delayTick=500)
        add_balloon_talk(spawnId=101, msg='$52000136_QD__MAIN__3$', duration=1000, delayTick=500)
        set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 케이틀린발견02()


class 케이틀린발견02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000136_QD__MAIN__4$', duration=3000, align='left')
        move_user_path(patrolName='MS2PatrolData_PC')
        set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 케이틀린발견03()


class 케이틀린발견03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        add_balloon_talk(spawnId=101, msg='$52000136_QD__MAIN__5$', duration=3000, delayTick=500)
        move_npc(spawnId=101, patrolName='Patrol_101_katelyn_run')
        set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 케이틀린대사01()


class 케이틀린대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8006], returnView=False)
        set_conversation(type=2, spawnId=11003261, script='$52000136_QD__MAIN__6$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4300)
        set_skip(state=불안한케이틀린_스킵완료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC대사01()


class PC대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000136_QD__MAIN__7$', duration=3000, align='left')
        set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 케이틀린대사02()


class 케이틀린대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        set_conversation(type=2, spawnId=11003261, script='$52000136_QD__MAIN__8$', arg4=3, arg5=0)
        set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 문줌인()


class 문줌인(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010,8011], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 불안한케이틀린_스킵완료(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010,8011], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        move_user(mapId=52000136, portalId=11)
        move_npc(spawnId=101, patrolName='Patrol_101_katelyn_run') # 케이틀린 위치로

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


