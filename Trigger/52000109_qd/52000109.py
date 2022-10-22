""" trigger/52000109_qd/52000109.xml """
from common import *
import state


class Wait01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[200], arg2=False) # 아이샤등장
        create_monster(spawnIds=[2001], arg2=False) # 아이샤등장

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10010]):
            return Wait02()


class Wait02(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait03()


class Wait03(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000109_QD__52000109__0$', desc='$52000109_QD__52000109__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=6000, scale=2.5)
        set_onetime_effect(id=40, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        move_user(mapId=52000109, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에델슈타인전경씬01()


class 에델슈타인전경씬01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1000], returnView=False)
        set_onetime_effect(id=40, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        add_balloon_talk(spawnId=0, msg='$52000109_QD__52000109__2$', duration=5000, delayTick=1000)
        add_balloon_talk(spawnId=200, msg='$52000109_QD__52000109__3$', duration=6000, delayTick=4000)
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=15000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬02()


class 에델슈타인전경씬02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003292, illustId='Ayesha_normal', msg='$52000109_QD__52000109__4$', duration=4000, align='right')
        set_onetime_effect(id=3000982, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000982.xml')
        set_onetime_effect(id=50, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬03()


class 에델슈타인전경씬03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__5$', duration=4000, align='right')
        set_onetime_effect(id=60, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬04()


class 에델슈타인전경씬04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003292, illustId='Ayesha_normal', msg='$52000109_QD__52000109__6$', duration=4000, align='right')
        set_onetime_effect(id=3000983, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000983.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬05()


class 에델슈타인전경씬05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__7$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬06()


class 에델슈타인전경씬06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__8$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬07()


class 에델슈타인전경씬07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003292, illustId='Ayesha_normal', msg='$52000109_QD__52000109__9$', duration=4000, align='right')
        set_onetime_effect(id=3000984, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000984.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬08()


class 에델슈타인전경씬08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__10$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬10()


class 에델슈타인전경씬10(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1001], returnView=False)
        move_npc(spawnId=200, patrolName='MS2PatrolData_Isha')
        move_user_path(patrolName='MS2PatrolData_PC')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬11()


class 에델슈타인전경씬11(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__11$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬12()


class 에델슈타인전경씬12(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, illustId='0', msg='$52000109_QD__52000109__12$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬13()


class 에델슈타인전경씬13(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1002,1003], returnView=False)
        add_balloon_talk(spawnId=0, msg='$52000109_QD__52000109__13$', duration=5000, delayTick=1000)
        add_balloon_talk(spawnId=200, msg='$52000109_QD__52000109__14$', duration=6000, delayTick=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에델슈타인전경씬14()


class 에델슈타인전경씬14(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트대기01_20002302()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_npc(spawnId=200, patrolName='MS2PatrolData_Isha')
        move_user(mapId=52000109, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트대기01_20002302()


class 퀘스트대기01_20002302(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=25201091, textId=25201091, duration=5000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10010], questIds=[20002304], questStates=[2]):
            return 라딘대화씬03()
        if quest_user_detected(boxIds=[10010], questIds=[20002303], questStates=[3]):
            return 라딘대화씬01()
        if quest_user_detected(boxIds=[10010], questIds=[20002302], questStates=[3]):
            return 라딘등장씬01()
        if quest_user_detected(boxIds=[10010], questIds=[20002302], questStates=[2]):
            return 라딘등장씬01()


#  ########################20002302, 라딘 등장########################
class 라딘등장씬01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[2002], arg2=False) # 라딘등장

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 라딘등장씬02()


class 라딘등장씬02(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_2, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_npc(spawnId=2002, patrolName='MS2PatrolData_radin')
        select_camera_path(pathIds=[1004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 라딘등장씬03()


class 라딘등장씬03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003295, illustId='Radin_normal', msg='$52000109_QD__52000109__15$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 라딘등장씬04()


class 라딘등장씬04(state.State):
    def on_enter(self):
        face_emotion(spawnId=200, emotionName='hello_Cait')
        show_caption(type='NameCaption', title='$52000109_QD__52000109__16$', desc='$52000109_QD__52000109__17$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 라딘등장씬04_1()


class 라딘등장씬04_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 라딘등장씬05()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_npc(spawnId=2002, patrolName='MS2PatrolData_radin')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 라딘등장씬05()


class 라딘등장씬05(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10010], questIds=[20002303], questStates=[2]):
            return 라딘대화씬01()


#  ########################20002302, 라딘 등장########################
class 라딘대화씬01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[2004,302], arg2=False) # 라딘등장
        destroy_monster(spawnIds=[2002,200])
        move_user(mapId=52000109, portalId=11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 라딘대화씬02()


class 라딘대화씬02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10010], questIds=[20002304], questStates=[2]):
            return 라딘대화씬03()


class 라딘대화씬03(state.State):
    def on_enter(self):
        set_scene_skip(state=라딘대화씬05, arg2='exit')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 라딘대화씬04()


class 라딘대화씬04(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000109_QD__52000109__18$', desc='$52000109_QD__52000109__19$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 라딘대화씬04_1()


class 라딘대화씬04_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 라딘대화씬05()


class 라딘대화씬05(state.State):
    def on_enter(self):
        move_user(mapId=2000062, portalId=13)


