""" trigger/52000195_qd/52000195.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003407], questStates=[1]):
            return CameraEffect01()
        if not quest_user_detected(boxIds=[2001], questIds=[10003407], questStates=[1]):
            return 이동()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204]) # 에레브
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_cinematic_ui(type=1)
        move_user(mapId=52000195, portalId=5001)
        select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=1)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_3()


class CameraEffect03_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        show_caption(type='VerticalCaption', title='$52000195_QD__52000195__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CameraEffect03_4()


class CameraEffect03_4(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_5()


class CameraEffect03_5(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[204])
        visible_my_pc(isVisible=True) # 유저 투명 처리 품
        set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        add_buff(boxIds=[2001], skillId=99910402, level=1, arg4=False, arg5=True) # 에레브 변신
        add_buff(boxIds=[2001], skillId=99910402, level=1, arg4=False, arg5=False) # 에레브 변신

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_6()


class CameraEffect03_6(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_7()


class CameraEffect03_7(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11001302, msg='$52000195_QD__52000195__1$', align='left', illustId='Ereb_surprise', duration=3000)
        add_cinematic_talk(npcId=11001302, msg='$52000195_QD__52000195__2$', align='left', illustId='Ereb_serious', duration=3000)
        add_cinematic_talk(npcId=11001302, msg='$52000195_QD__52000195__3$', align='left', illustId='Ereb_serious', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return CameraEffect03_8()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[204])
        visible_my_pc(isVisible=True) # 유저 투명 처리 품
        set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        add_buff(boxIds=[2001], skillId=99910402, level=1, arg4=False, arg5=True) # 에레브 변신
        add_buff(boxIds=[2001], skillId=99910402, level=1, arg4=False, arg5=False) # 에레브 변신

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_8()


class CameraEffect03_8(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2002]):
            return 과거장면_01()


class 과거장면_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 과거장면_02()


class 과거장면_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        create_monster(spawnIds=[201]) # 바론
        create_monster(spawnIds=[202]) # 칼
        create_monster(spawnIds=[203]) # 에레브
        remove_buff(boxId=2002, skillId=99910402)
        visible_my_pc(isVisible=False) # 유저 투명 처리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 과거장면_03()


class 과거장면_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_2, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 과거장면_05()


class 과거장면_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)
        set_cinematic_ui(type=3)
        set_npc_emotion_loop(spawnId=202, sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=11004787, msg='$52000195_QD__52000195__4$', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 과거장면_06()


class 과거장면_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)
        set_npc_emotion_loop(spawnId=201, sequenceName='Talk_A', duration=8000)
        add_cinematic_talk(npcId=11004778, msg='$52000195_QD__52000195__5$', align='right', illustId='Karl_normal', duration=4000)
        add_cinematic_talk(npcId=11004778, msg='$52000195_QD__52000195__6$', align='right', illustId='Karl_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 과거장면_07()


class 과거장면_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_npc_emotion_loop(spawnId=202, sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=11004787, msg='$52000195_QD__52000195__7$', align='right', illustId='Baron_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 과거장면_08()


class 과거장면_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)
        move_npc(spawnId=202, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 과거장면_08_1()


class 과거장면_08_1(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=201, sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=11004778, msg='$52000195_QD__52000195__8$', align='right', illustId='Karl_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 과거장면_08_2()


class 과거장면_08_2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])
        select_camera_path(pathIds=[4009], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 과거장면_09()


class 과거장면_09(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=203, sequenceName='Bore_B')
        add_cinematic_talk(npcId=11004785, msg='$52000195_QD__52000195__9$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 과거장면_10()


class 과거장면_10(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11004785, msg='$52000195_QD__52000195__10$', illustId='Ereb_surprise', duration=4000)
        add_cinematic_talk(npcId=11004785, msg='$52000195_QD__52000195__11$', illustId='Ereb_surprise', duration=4000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 업적달성()


class Skip_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 업적달성()


class 업적달성(state.State):
    def on_enter(self):
        set_achievement(triggerId=2002, achieve='DreamofEreb')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        move_user(mapId=52000193, portalId=5001)


