""" trigger/52010028_qd/main.xml """
from common import *
import state


#  흘러내린 시간의 틈 : 52010028  
class 던전에들어왔으면(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2002]):
            return black()


class black(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        visible_my_pc(isVisible=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 떨어져서아파()


class 떨어져서아파(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        select_camera_path(pathIds=[4007], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_pc_emotion_sequence(sequenceNames=['Damg_C'])
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 웰컴문구1()


class 웰컴문구1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_pc_emotion_loop(sequenceName='Emotion_Bloompicnic_A', duration=7000)
        create_monster(spawnIds=[9999], arg2=False, arg3=0) # 구르는 천둥:11003390
        face_emotion(spawnId=0, emotionName='Trigger_disappoint')
        show_caption(type='VerticalCaption', title='$52010028_QD__MAIN__0$', desc='$52010028_QD__MAIN__1$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__2$', duration=3000)
        set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=401, enable=True, path='BG/sound/Eff_DevilPortal_01.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 웰컴문구2()


class 웰컴문구2(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__3$', duration=2000)
        set_onetime_effect(id=302, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__4$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시선이동()


class 시선이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=303, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=403, enable=True, path='BG/sound/Eff_ShakeLand_01.xml')
        add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__5$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 웰컴문구3()


class 웰컴문구3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 웰컴문구4()


class 웰컴문구4(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__7$', duration=3000)
        destroy_monster(spawnIds=[9999]) # 구르는 천둥:11003390

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 웰컴문구4_1()


class 웰컴문구4_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이제가자()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_pc_emotion_loop(sequenceName='Idle_A', duration=500)
        destroy_monster(spawnIds=[9999]) # 구르는 천둥:11003390

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이제가자()


class 이제가자(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52010028_QD__MAIN__8$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return idle()


class idle(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52010028_QD__MAIN__35$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True) # 구르는 천둥:11003390
        create_monster(spawnIds=[201], arg2=True) # 붉은 늑대의 심장:11003387
        select_camera_path(pathIds=[4001], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52010028, portalId=7001)
        set_scene_skip(state=Skip_2, arg2='nextState')
        add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__9$', duration=3000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Down_Idle_A', duration=1500000)
        set_npc_emotion_loop(spawnId=201, sequenceName='Attack_Idle_A', duration=1500000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC진입()


class PC진입(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user_path(patrolName='3002')
        add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__10$', duration=2000)
        add_balloon_talk(spawnId=0, msg='$52010028_QD__MAIN__11$', duration=2000, delayTick=1000)
        face_emotion(spawnId=201, emotionName='Trigger_Crazy')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출_01()


class 연출_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)
        add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__12$', duration=3000)
        face_emotion(spawnId=101, emotionName='Trigger_Danger')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출_02()


class 연출_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 연출_02_1()


class 연출_02_1(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Attack_02_D')
        set_effect(triggerIds=[5001], visible=True)
        add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__13$', duration=3000)
        show_caption(type='VerticalCaption', title='$52010028_QD__MAIN__14$', desc='$52010028_QD__MAIN__15$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        add_cinematic_talk(npcId=11003390, msg='$52010028_QD__MAIN__16$', duration=3000, illustId='0', align='Left')
        add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__17$', duration=2000)
        add_cinematic_talk(npcId=11003390, msg='$52010028_QD__MAIN__18$', duration=3000)
        set_onetime_effect(id=304, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        face_emotion(spawnId=201, emotionName='Trigger_Crazy')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 연출_03()


class 연출_03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        add_cinematic_talk(npcId=11003390, msg='$52010028_QD__MAIN__19$', duration=3000, illustId='0', align='Left')
        set_npc_emotion_loop(spawnId=201, sequenceName='Idle_A', duration=10000)
        select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출_04()


class 연출_04(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_3001')
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__20$', duration=3000, illustId='0', align='Left')
        add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__21$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 연출_04_01()


class 연출_04_01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Attack_02_D')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 연출_04_02()


class 연출_04_02(state.State):
    def on_enter(self):
        face_emotion(spawnId=201, emotionName='Trigger_Fury')
        set_effect(triggerIds=[5002], visible=True)
        add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__22$', duration=3000, delayTick=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 연출_05()


class 연출_05(state.State):
    def on_enter(self):
        face_emotion(spawnId=201, emotionName='Trigger_Crazy')
        set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=9999999)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출_06()


class 연출_06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출_07()


class 연출_07(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투준비()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        move_user_path(patrolName='3002')
        set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=9999999)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투준비()


class 전투준비(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=201, sequenceName='Down_Idle_A', duration=3000)
        move_npc(spawnId=201, patrolName='MS2PatrolData_3003')
        destroy_monster(spawnIds=[201], arg2=True) # 붉은 늑대의 심장:11003387
        create_monster(spawnIds=[501], arg2=True) # 붉은 늑대의 심장:22000324

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투메시지()


class 전투메시지(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0.5)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52010028_QD__MAIN__23$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전투()


class 전투(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[501]):
            return 전투종료()


class 전투종료(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투종료대사()


class 전투종료대사(state.State):
    def on_enter(self):
        set_achievement(triggerId=2001, type='trigger', achieve='Maze')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip(state=이동, arg2='exit')
        move_user(mapId=52010028, portalId=7002)
        create_monster(spawnIds=[202], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투종료이후연출()


class 전투종료이후연출(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=1500000)
        face_emotion(spawnId=101, emotionName='Trigger_Dead')
        select_camera_path(pathIds=[4012], returnView=False)
        set_npc_emotion_loop(spawnId=202, sequenceName='Dead_Idle_A', duration=150000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 찾으러왔어01()


class 찾으러왔어01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__24$', duration=3000)
        create_monster(spawnIds=[301], arg2=True)
        face_emotion(spawnId=301, emotionName='Trigger_Dead')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 찾으러왔어02()


class 찾으러왔어02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        move_npc(spawnId=301, patrolName='MS2PatrolData_3004')
        add_balloon_talk(spawnId=301, msg='$52010028_QD__MAIN__25$', duration=2000, delayTick=1000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=150000)
        face_emotion(spawnId=101, emotionName='Trigger_Dead')
        face_emotion(spawnId=301, emotionName='down_Idle')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 찾으러왔어03()


class 찾으러왔어03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[302], arg2=True)
        create_monster(spawnIds=[303], arg2=True)
        move_npc(spawnId=302, patrolName='MS2PatrolData_3005')
        move_npc(spawnId=303, patrolName='MS2PatrolData_3006')
        add_balloon_talk(spawnId=302, msg='$52010028_QD__MAIN__26$', duration=2000, delayTick=1000)
        add_balloon_talk(spawnId=303, msg='$52010028_QD__MAIN__27$', duration=2000, delayTick=1200)
        move_user(mapId=52010028, portalId=7003)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 찾으러왔어04()


class 찾으러왔어04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[304], arg2=True)
        create_monster(spawnIds=[305], arg2=True)
        move_npc(spawnId=304, patrolName='MS2PatrolData_3007')
        move_npc(spawnId=305, patrolName='MS2PatrolData_3008')
        add_balloon_talk(spawnId=304, msg='$52010028_QD__MAIN__28$', duration=2000, delayTick=1000)
        add_balloon_talk(spawnId=305, msg='$52010028_QD__MAIN__29$', duration=2000, delayTick=1200)
        move_user(mapId=52010028, portalId=7003)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 어서와()


class 어서와(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=1500000)
        face_emotion(spawnId=101, emotionName='Trigger_Dead')
        add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__30$', duration=3000)
        add_cinematic_talk(npcId=11003456, msg='$52010028_QD__MAIN__31$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8191):
            return 어서와02()


class 어서와02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_npc_emotion_sequence(spawnId=305, sequenceName='Bore_A')
        set_npc_emotion_sequence(spawnId=304, sequenceName='Talk_A')
        add_balloon_talk(spawnId=305, msg='$52010028_QD__MAIN__32$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=304, msg='$52010028_QD__MAIN__33$', duration=2000, delayTick=500)
        add_balloon_talk(spawnId=302, msg='$52010028_QD__MAIN__34$', duration=2000, delayTick=500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 어서와03()


class 어서와03(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        move_user(mapId=52010032, portalId=1)


