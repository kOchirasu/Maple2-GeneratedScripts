""" trigger/52000159_qd/52000159.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002735], questStates=[2]):
            return 정리_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002736], questStates=[2]):
            return 정리_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002737], questStates=[2]):
            return 정리_01()
        if user_detected(boxIds=[2001], jobCode=0):
            return wait_01_1()


class wait_01_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52000159, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 어쌔신과거_01()


class 어쌔신과거_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 어쌔신과거_02()


class 어쌔신과거_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)
        select_camera_path(pathIds=[4003,4004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 어쌔신과거_03()


class 어쌔신과거_03(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        show_caption(type='VerticalCaption', title='$52000159_QD__52000159__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 어쌔신과거_04()


class 어쌔신과거_04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__1$', duration=4000)
        move_user_path(patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 어쌔신과거_05()


class 어쌔신과거_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__2$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__3$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__4$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__5$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 어쌔신과거_06()


class 어쌔신과거_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__6$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__7$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 어쌔신과거_07()


class 어쌔신과거_07(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__8$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__9$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 쉐도클로_01()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 쉐도클로_01()


class 쉐도클로_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4006], returnView=False)
        create_monster(spawnIds=[103], arg2=False)
        set_effect(triggerIds=[5001], visible=True)
        create_monster(spawnIds=[105], arg2=False)
        set_effect(triggerIds=[5002], visible=True)
        create_monster(spawnIds=[106], arg2=False)
        set_effect(triggerIds=[5003], visible=True)
        create_monster(spawnIds=[107], arg2=False)
        set_effect(triggerIds=[5004], visible=True)
        create_monster(spawnIds=[108], arg2=False)
        set_effect(triggerIds=[5005], visible=True)
        create_monster(spawnIds=[101], arg2=False)
        set_effect(triggerIds=[5006], visible=True)
        move_user(mapId=52000159, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 쉐도클로_02()


class 쉐도클로_02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리_01()


class 정리_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 정리_02()


class 정리_02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[110], arg2=False)
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[112], arg2=False)
        create_monster(spawnIds=[113], arg2=False)
        destroy_monster(spawnIds=[101], arg2=False)
        destroy_monster(spawnIds=[103], arg2=False)
        destroy_monster(spawnIds=[105], arg2=False)
        destroy_monster(spawnIds=[106], arg2=False)
        destroy_monster(spawnIds=[107], arg2=False)
        destroy_monster(spawnIds=[108], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 밝아짐()


class 밝아짐(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002735], questStates=[2]):
            return 남자의죽음_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002736], questStates=[2]):
            return 남자의죽음_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002737], questStates=[2]):
            return 남자의죽음_01()


class 남자의죽음_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 남자의죽음_01_02()


class 남자의죽음_01_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera_path(pathIds=[4007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 남자의죽음_02()


class 남자의죽음_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=Skip_2, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 남자의죽음_03()


class 남자의죽음_03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=104, sequenceName='Attack_01_B')
        set_npc_emotion_loop(spawnId=102, sequenceName='Dead_B', duration=9E+12)
        set_effect(triggerIds=[5007], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 남자의죽음_03_01()


class 남자의죽음_03_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 남자의죽음_04()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 남자의죽음_04()


class 남자의죽음_04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[114], arg2=False)
        set_npc_emotion_loop(spawnId=114, sequenceName='Dead_B', duration=9E+12)
        create_monster(spawnIds=[115], arg2=False)
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 남자의죽음_05()


class 남자의죽음_05(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002737], questStates=[2]):
            return 쉐도클로표창_01()


class 쉐도클로표창_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 쉐도클로표창_01_01()


class 쉐도클로표창_01_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        visible_my_pc(isVisible=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 쉐도클로표창_02()


class 쉐도클로표창_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_loop(spawnId=104, sequenceName='Attack_Idle_A', duration=4000)
        set_scene_skip(state=Skip_3, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 쉐도클로표창_03()


class 쉐도클로표창_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_npc_emotion_loop(spawnId=104, sequenceName='Attack_01_B', duration=80000)
        set_time_scale(enable=True, startScale=0.1, endScale=0.1, duration=10, interpolator=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 쉐도클로표창_03_01()


class 쉐도클로표창_03_01(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=115, sequenceName='Dead_A', duration=80000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 쉐도클로표창_04()


class Skip_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 쉐도클로표창_04()


class 쉐도클로표창_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 쉐도클로표창_05()


class 쉐도클로표창_05(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        move_user(mapId=52000158, portalId=6001)


