""" trigger/52010064_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False) # 유저 투명 처리
        create_monster(spawnIds=[101], arg2=False) # 트리스탄

    def on_tick(self) -> state.State:
        if check_user():
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[91000073], questStates=[3]):
            return 돌아가()
        if quest_user_detected(boxIds=[9000], questIds=[91000073], questStates=[2]):
            return CameraEffect01()
        if quest_user_detected(boxIds=[9000], questIds=[91000073], questStates=[1]):
            return CameraEffect01()
        if quest_user_detected(boxIds=[9000], questIds=[91000072], questStates=[3]):
            return 돌아가()
        if not quest_user_detected(boxIds=[9000], questIds=[91000073], questStates=[1]):
            return 돌아가()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=quit01, arg2='nextState') # setsceneskip 1 set
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_achievement(triggerId=9000, type='trigger', achieve='flyingtristan') # 퀘스트 완료 업적

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[8000], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 트리스탄대사01()


class 트리스탄대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8010], returnView=False)
        add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__0$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄대사02()


class 트리스탄대사02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__1$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄대사03()


class 트리스탄대사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__2$', duration=3000, align='right')
        move_npc(spawnId=101, patrolName='MS2PatrolData_Tristan_walking')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄대사04()


class 트리스탄대사04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__3$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄대사05()


class 트리스탄대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__4$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트리스탄대사06()


class 트리스탄대사06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__5$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마무리줌아웃()


class 마무리줌아웃(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        set_cinematic_ui(type=0)
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return quit01()


class quit01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return quit03()


class quit03(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        move_user(mapId=52010052, portalId=1) # 작전실로 자동 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return quit03()


class 돌아가(state.State):
    def on_enter(self):
        move_user(mapId=52010052, portalId=1) # 작전실로 자동 이동
        visible_my_pc(isVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 돌아가()


class 종료(state.State):
    pass


