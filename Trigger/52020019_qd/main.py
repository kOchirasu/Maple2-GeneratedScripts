""" trigger/52020019_qd/main.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_sound(triggerId=7001, arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200010], questStates=[1]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        create_monster(spawnIds=[101], arg2=True) # 이오네
        create_monster(spawnIds=[102], arg2=True) # 미카엘
        move_user(mapId=52020019, portalId=6001)
        select_camera_path(pathIds=[4001], returnView=False)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Camera_Work_01()


class Camera_Work_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4002,4003], returnView=False)
        set_scene_skip(arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ShowCaption()


class ShowCaption(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$map:52020019$', desc='$npcName:11003614$의 두 번째 시험장.', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=2000, scale=1.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Camera_Work_02()


class Camera_Work_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_01()


class EventScene_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003614, msg='자, 시작하세요.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_02()


class EventScene_02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_03()


class EventScene_03(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_3002')
        add_cinematic_talk(npcId=11003598, msg='오호.... 제법 기합을 넣을 줄 아시는군요.', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_04()


class EventScene_04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003598, msg='그럼 시작하기전에....', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_05()


class EventScene_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003598, msg='정식으로 제 소개를 하죠.', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_06()


class EventScene_06(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003598, msg='제 이름은 $npcName:11003598$.', duration=2500, illustId='Michael_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_07()


class EventScene_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003598, msg='크리티아스 제 3기사. 몽환의 $npcName:11003598$입니다.', duration=3000, illustId='Michael_normal', align='Center')
        show_caption(type='NameCaption', title='$npcName:11003598$', desc='몽환의 기사', align='centerLeft', offsetRateX=0.05, offsetRateY=0.15, duration=3000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return EventScene_08()


class EventScene_08(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EventScene_09()


class EventScene_09(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Bore_A'])
        add_balloon_talk(spawnId=0, msg='!!!', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_10()


class EventScene_10(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_sequence(spawnId=102, sequenceName='Emotion_B')
        add_cinematic_talk(npcId=11003598, msg='자, 그럼 당신의 실력을 확인해보도록 하죠.', duration=3000, illustId='Michael_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return White()


class White(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Battle_Ready()


class Battle_Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True)
        destroy_monster(spawnIds=[102]) # 미카엘
        create_monster(spawnIds=[201], arg2=True) # 미카엘 몬스터

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Battle()


class Battle(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return Battle_Stop()


class Battle_Stop(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='그만!', duration=3000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Battle_End()


class Battle_End(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[201]) # 미카엘

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return EventScene_11()


class EventScene_11(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003614, msg='그만 하세요.', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_12()


class EventScene_12(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003598, msg='이런, 이제 막 재미있어지려는 참이었는데 아쉽군요.', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_13()


class EventScene_13(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003598, msg='뭐, 다음 기회라는 것도 있으니 이번엔 여기까지만 하겠습니다.', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_14()


class EventScene_14(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003614, msg='.......', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_15()


class EventScene_15(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003614, msg='돌아가죠. $npcName:11003598$.', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_16()


class EventScene_16(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003598, msg='네. 분부대로.', duration=2500, illustId='Michael_normal', align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return QuestComplete()


class QuestComplete(state.State):
    def on_enter(self):
        set_achievement(type='trigger', achieve='ForgottenrRoad')
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Warp()


class Warp(state.State):
    def on_enter(self):
        move_user(mapId=2020006, portalId=6002)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200010], questStates=[1]):
            return QuestComplete()


