""" trigger/52000106_qd/52000106.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002323], questStates=[1]):
            return 그림자의침략01()
        if quest_user_detected(boxIds=[10011], questIds=[20002323], questStates=[2]):
            return 그림자의침략완료02()
        if quest_user_detected(boxIds=[10011], questIds=[20002325], questStates=[2]):
            return 리엔을떠나다01()
        if quest_user_detected(boxIds=[10011], questIds=[20002323], questStates=[3]):
            return 그림자의침략완료02()


#  ########################그림자의침략 도입부 연출########################
class 그림자의침략01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 그림자의침략02()


class 그림자의침략02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1000,1001], returnView=False)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 그림자의침략03()


class 그림자의침략03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1002,1003], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_ririn_Turn')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 그림자의침략04()


class 그림자의침략04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[700,701,702,703], arg2=False)
        set_effect(triggerIds=[901], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 그림자의침략05()


class 그림자의침략05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[704,705,706,707], arg2=False)
        set_effect(triggerIds=[901], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 그림자의침략06()


class 그림자의침략06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[708,709,710,711], arg2=False)
        set_effect(triggerIds=[901], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 그림자의침략07()


class 그림자의침략07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[712,713,714,715], arg2=False)
        set_effect(triggerIds=[901], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 그림자의침략08()


class 그림자의침략08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[716,717,718,719], arg2=False)
        set_effect(triggerIds=[901], visible=True)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 그림자의침략09()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_npc(spawnId=101, patrolName='MS2PatrolData_ririn_Turn')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        reset_camera(interpolationTime=0.5)
        create_monster(spawnIds=[700,701,702,703], arg2=False)
        create_monster(spawnIds=[704,705,706,707], arg2=False)
        create_monster(spawnIds=[708,709,710,711], arg2=False)
        create_monster(spawnIds=[712,713,714,715], arg2=False)
        create_monster(spawnIds=[716,717,718,719], arg2=False)
        create_monster(spawnIds=[716,717,718,719], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 그림자의침략09()


#  ########################그림자의침략 플레이 진행########################
class 그림자의침략09(state.State):
    def on_enter(self):
        add_buff(boxIds=[10011], skillId=70000109, level=1, arg4=False, arg5=False) # 초생회
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0.5)
        show_guide_summary(entityId=25201061, textId=25201061, duration=5000)
        move_npc(spawnId=101, patrolName='MS2PatrolData_ririn_go')
        add_balloon_talk(spawnId=0, msg='$52000106_QD__52000106__0$', duration=6000, delayTick=1000)
        add_balloon_talk(spawnId=101, msg='$52000106_QD__52000106__1$', duration=6000, delayTick=2000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002323], questStates=[2]):
            return 그림자의침략완료01()


#  ########################그림자의침략 마무리########################
class 그림자의침략완료01(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='$52000106_QD__52000106__2$', duration=6000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 그림자의침략완료02()


class 그림자의침략완료02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        create_monster(spawnIds=[102], arg2=False)
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 그림자의침략완료03()


class 그림자의침략완료03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0.5)
        set_onetime_effect(id=20, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        move_user(mapId=52000106, portalId=3)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002324], questStates=[1]):
            return 할아버지의물품조사01()
        if quest_user_detected(boxIds=[10011], questIds=[20002324], questStates=[2]):
            return 할아버지의물품조사01()
        if quest_user_detected(boxIds=[10011], questIds=[20002324], questStates=[3]):
            return 할아버지의물품조사01()


#  ########################할아버지의 물품 조사########################
class 할아버지의물품조사01(state.State):
    def on_enter(self):
        create_item(spawnIds=[200])
        show_guide_summary(entityId=25201062, textId=25201062, duration=5000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002325], questStates=[2]):
            return 리엔을떠나다01()


#  ########################PC,리엔을 떠나다########################
class 리엔을떠나다01(state.State):
    def on_enter(self):
        set_scene_skip(state=리엔을떠나다09, arg2='exit')
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_ririn_goodBye_0')
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 리엔을떠나다02()


class 리엔을떠나다02(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1004,1005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 리엔을떠나다03()


class 리엔을떠나다03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003174, msg='$52000106_QD__52000106__3$', duration=4000, align='right')
        select_camera_path(pathIds=[1006,1007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 리엔을떠나다04()


class 리엔을떠나다04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003174, msg='$52000106_QD__52000106__4$', duration=5000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 리엔을떠나다05()


class 리엔을떠나다05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1008,1009], returnView=False)
        add_cinematic_talk(npcId=11003174, illustId='Ririn_normal', msg='$52000106_QD__52000106__5$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 리엔을떠나다06()


class 리엔을떠나다06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003174, illustId='Ririn_normal', msg='$52000106_QD__52000106__6$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 리엔을떠나다07()


class 리엔을떠나다07(state.State):
    def on_enter(self):
        set_onetime_effect(id=40, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 리엔을떠나다08()


class 리엔을떠나다08(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        show_caption(type='VerticalCaption', title='$52000106_QD__52000106__7$', desc='$52000106_QD__52000106__8$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 리엔을떠나다08_1()


class 리엔을떠나다08_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 리엔을떠나다09()


class 리엔을떠나다09(state.State):
    def on_enter(self):
        move_user(mapId=52000115, portalId=1)


