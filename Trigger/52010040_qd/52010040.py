""" trigger/52010040_qd/52010040.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000013], questStates=[2]):
            return 도입부연출01()
        if quest_user_detected(boxIds=[9001], questIds=[91000015], questStates=[3]):
            return 엔딩연출01()


class 도입부연출01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200], arg2=False) # 블리체
        create_monster(spawnIds=[300], arg2=False) # 블랙아이
        create_monster(spawnIds=[301], arg2=False) # 알론
        create_monster(spawnIds=[302], arg2=False) # 프레이
        create_monster(spawnIds=[303], arg2=False) # 오스칼
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 도입부연출02()


class 도입부연출02(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52010040_QD__52010040__0$', desc='$52010040_QD__52010040__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[2000,2001,2002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 도입부연출03_b()


class 도입부연출03_b(state.State):
    def on_enter(self):
        move_npc(spawnId=200, patrolName='MS2PatrolData_blicheCome') # 블리체 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 도입부연출03()


class 도입부연출03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 도입부연출04()


class 도입부연출04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 종료()


class 종료(state.State):
    pass


#  ########################튜토리얼 종료씬########################
class 엔딩연출01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200], arg2=False) # 블리체
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 엔딩연출02()


class 엔딩연출02(state.State):
    def on_enter(self):
        set_scene_skip(state=quit, arg2='nextState')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        add_cinematic_talk(npcId=11003536, illustId='Neirin_normal', msg='$52010040_QD__52010040__2$', duration=6200, align='right')
        select_camera_path(pathIds=[2012,2013], returnView=False)
        move_user_path(patrolName='MS2PatrolData_blicheCome')
        move_npc(spawnId=200, patrolName='MS2PatrolData_bliche_front') # 블리체 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 엔딩연출03()


class 엔딩연출03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010040_QD__52010040__3$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 엔딩연출04()


class 엔딩연출04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010040_QD__52010040__4$', duration=5400, align='right')
        select_camera_path(pathIds=[2010,2011,2014], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 엔딩연출05()


class 엔딩연출05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010040_QD__52010040__5$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4100):
            return 엔딩연출06_b()


class 엔딩연출06_b(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010040_QD__52010040__6$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 엔딩연출06()


class 엔딩연출06(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 엔딩연출07()


class 엔딩연출07(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return quit()


class quit(state.State):
    def on_enter(self):
        move_user(mapId=2000422, portalId=3)


