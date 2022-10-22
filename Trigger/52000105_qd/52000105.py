""" trigger/52000105_qd/52000105.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200], arg2=False) # 텐

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002320], questStates=[1]):
            return 몬스터처치훈련01()
        if quest_user_detected(boxIds=[10011], questIds=[20002321], questStates=[1]):
            return 몬스터처치훈련02()
        if quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[1]):
            return 할아버지대련01()
        if quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[2]):
            return 대련종료씬시작01()
        if quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[3]):
            return 대련종료씬시작01()


#  ########################씬2 몬스터 소환 교육01~02########################
class 몬스터처치훈련01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[300,301,302], arg2=False)
        show_guide_summary(entityId=25201051, textId=25201051, duration=5000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002321], questStates=[1]):
            return 몬스터처치훈련02()


class 몬스터처치훈련02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[400,401,402], arg2=False)
        show_guide_summary(entityId=25201052, textId=25201052, duration=5000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[1]):
            return 할아버지대련01()


#  ########################씬3 할아버지 대련########################
class 할아버지대련01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52000105, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 할아버지대련02_b()


class 할아버지대련02_b(state.State):
    def on_enter(self):
        move_npc(spawnId=200, patrolName='MS2PatrolData_ten_comeFront')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1000,1001,1002,1003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return 할아버지대련03()


class 할아버지대련03(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=1, endScale=0.5, duration=2, interpolator=2) # 2초간 느려지기 시작
        set_npc_emotion_loop(spawnId=200, sequenceName='Attack_Idle_A', duration=15000)
        select_camera_path(pathIds=[1004,1005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 할아버지대련04()


class 할아버지대련04(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=6000)
        select_camera_path(pathIds=[1006,1007], returnView=False)
        add_balloon_talk(spawnId=0, msg='$52000105_QD__52000105__0$', duration=6000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 할아버지대련05_B()


class 할아버지대련05_B(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_PC_Run_0')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 할아버지대련05()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 할아버지대련05()


class 할아버지대련05(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        destroy_monster(spawnIds=[200])
        create_monster(spawnIds=[500], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0.5)
        show_guide_summary(entityId=25201053, textId=25201053, duration=5000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[2]):
            return 대련종료씬시작01()


class 대련종료씬시작01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        set_cinematic_ui(type=1)
        destroy_monster(spawnIds=[203])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 대련종료씬시작02()


#  ########################대련 종료씬########################
class 대련종료씬시작02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[200])
        set_cinematic_ui(type=1)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        create_monster(spawnIds=[202], arg2=False)
        move_user(mapId=52000105, portalId=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 대련종료씬시작02_01()


class 대련종료씬시작02_01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_2, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 대련종료씬시작03()


class 대련종료씬시작03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=202, sequenceName='Attack_Idle_A', duration=5000)
        move_user_path(patrolName='MS2PatrolData_PC_Run_0')
        select_camera_path(pathIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2012,2013], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 대련종료씬시작04()


class 대련종료씬시작04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2014,2015], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대련종료씬시작06()


class 대련종료씬시작06(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=0.3, endScale=0.3, duration=2.5, interpolator=3) # 2초간 느려지기 시작
        set_npc_emotion_sequence(spawnId=202, sequenceName='Attack_01_B')
        select_camera_path(pathIds=[2016,2017], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return 대련종료씬시작07()


class 대련종료씬시작07(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Dead_A'])
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 대련종료씬시작07_b()


class 대련종료씬시작07_b(state.State):
    def on_enter(self):
        set_onetime_effect(id=100, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 대련종료씬시작08()


class 대련종료씬시작08(state.State):
    def on_enter(self):
        set_onetime_effect(id=100, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        set_pc_emotion_sequence(sequenceNames=['Stuck_A'])
        select_camera_path(pathIds=[2018,2019], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대련종료씬시작09()


class 대련종료씬시작09(state.State):
    def on_enter(self):
        set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대련종료씬시작10()


class 대련종료씬시작10(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        set_onetime_effect(id=10, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        reset_camera(interpolationTime=1)
        set_pc_emotion_loop(sequenceName='Stun_A', duration=6500)
        create_monster(spawnIds=[201], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_ririn_go')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대련종료씬시작11()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        reset_camera(interpolationTime=1)
        set_pc_emotion_loop(sequenceName='Stun_A', duration=6500)
        create_monster(spawnIds=[201], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_ririn_go')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 대련종료씬시작11()


class 대련종료씬시작11(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[3]):
            return 떠나는할아버지01()


#  ########################씬4 떠나는할아버지01########################
class 떠나는할아버지01(state.State):
    def on_enter(self):
        set_scene_skip(state=떠나는할아버지07, arg2='exit')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 떠나는할아버지02()


class 떠나는할아버지02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_npc(spawnId=202, patrolName='MS2PatrolData_ten_exit_0')
        move_npc(spawnId=201, patrolName='MS2PatrolData_ririn_Turn')
        move_user_path(patrolName='MS2PatrolData_PC_Turn')
        select_camera_path(pathIds=[1008,1009], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 떠나는할아버지03()


class 떠나는할아버지03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003175, illustId='Ten_normal', msg='$52000105_QD__52000105__1$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 떠나는할아버지04()


class 떠나는할아버지04(state.State):
    def on_enter(self):
        move_npc(spawnId=202, patrolName='MS2PatrolData_tenExit_1')
        add_balloon_talk(spawnId=0, msg='$52000105_QD__52000105__2$', duration=6000, delayTick=1000)
        add_balloon_talk(spawnId=201, msg='$52000105_QD__52000105__3$', duration=6000, delayTick=1500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 떠나는할아버지05()


class 떠나는할아버지05(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 떠나는할아버지06()


class 떠나는할아버지06(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        show_caption(type='VerticalCaption', title='$52000105_QD__52000105__4$', desc='$52000105_QD__52000105__5$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 떠나는할아버지07()


class 떠나는할아버지07(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=52000106, portalId=1)


