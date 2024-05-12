""" trigger/52010028_qd/main.xml """
import trigger_api


# 흘러내린 시간의 틈 : 52010028
class 던전에들어왔으면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2002]):
            return black(self.ctx)


class black(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.visible_my_pc(isVisible=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 떨어져서아파(self.ctx)


class 떨어져서아파(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=True)
        self.select_camera_path(pathIds=[4007], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_sequence(sequenceNames=['Damg_C'])
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 웰컴문구1(self.ctx)


class 웰컴문구1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_loop(sequenceName='Emotion_Bloompicnic_A', duration=7000)
        self.create_monster(spawnIds=[9999], animationEffect=False, animationDelay=0) # 구르는 천둥:11003390
        self.face_emotion(spawnId=0, emotionName='Trigger_disappoint')
        self.show_caption(type='VerticalCaption', title='$52010028_QD__MAIN__0$', desc='$52010028_QD__MAIN__1$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        self.add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__2$', duration=3000)
        self.set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=401, enable=True, path='BG/sound/Eff_DevilPortal_01.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 웰컴문구2(self.ctx)


class 웰컴문구2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__3$', duration=2000)
        self.set_onetime_effect(id=302, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시선이동(self.ctx)


class 시선이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=303, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=403, enable=True, path='BG/sound/Eff_ShakeLand_01.xml')
        self.add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 웰컴문구3(self.ctx)


class 웰컴문구3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 웰컴문구4(self.ctx)


class 웰컴문구4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=1)
        self.add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__7$', duration=3000)
        self.destroy_monster(spawnIds=[9999]) # 구르는 천둥:11003390

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 웰컴문구4_1(self.ctx)


class 웰컴문구4_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이제가자(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_pc_emotion_loop(sequenceName='Idle_A', duration=500)
        self.destroy_monster(spawnIds=[9999]) # 구르는 천둥:11003390

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이제가자(self.ctx)


class 이제가자(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010028_QD__MAIN__8$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return idle(self.ctx)


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010028_QD__MAIN__35$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2001]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=True) # 구르는 천둥:11003390
        self.create_monster(spawnIds=[201], animationEffect=True) # 붉은 늑대의 심장:11003387
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52010028, portalId=7001)
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__9$', duration=3000)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Down_Idle_A', duration=1500000)
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Attack_Idle_A', duration=1500000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC진입(self.ctx)


class PC진입(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrolName='3002')
        self.add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__10$', duration=2000)
        self.add_balloon_talk(spawnId=0, msg='$52010028_QD__MAIN__11$', duration=2000, delayTick=1000)
        self.face_emotion(spawnId=201, emotionName='Trigger_Crazy')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출_01(self.ctx)


class 연출_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__12$', duration=3000)
        self.face_emotion(spawnId=101, emotionName='Trigger_Danger')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출_02(self.ctx)


class 연출_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4010], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 연출_02_1(self.ctx)


class 연출_02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Attack_02_D')
        self.set_effect(triggerIds=[5001], visible=True)
        self.add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__13$', duration=3000)
        self.show_caption(type='VerticalCaption', title='$52010028_QD__MAIN__14$', desc='$52010028_QD__MAIN__15$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        self.add_cinematic_talk(npcId=11003390, msg='$52010028_QD__MAIN__16$', duration=3000, illustId='0', align='Left')
        self.add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__17$', duration=2000)
        self.add_cinematic_talk(npcId=11003390, msg='$52010028_QD__MAIN__18$', duration=3000)
        self.set_onetime_effect(id=304, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.face_emotion(spawnId=201, emotionName='Trigger_Crazy')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return 연출_03(self.ctx)


class 연출_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=False)
        self.add_cinematic_talk(npcId=11003390, msg='$52010028_QD__MAIN__19$', duration=3000, illustId='0', align='Left')
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Idle_A', duration=10000)
        self.select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출_04(self.ctx)


class 연출_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_3001')
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__20$', duration=3000, illustId='0', align='Left')
        self.add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__21$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 연출_04_01(self.ctx)


class 연출_04_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Attack_02_D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return 연출_04_02(self.ctx)


class 연출_04_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawnId=201, emotionName='Trigger_Fury')
        self.set_effect(triggerIds=[5002], visible=True)
        self.add_cinematic_talk(npcId=11003387, msg='$52010028_QD__MAIN__22$', duration=3000, delayTick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 연출_05(self.ctx)


class 연출_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawnId=201, emotionName='Trigger_Crazy')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=9999999)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출_06(self.ctx)


class 연출_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출_07(self.ctx)


class 연출_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투준비(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.move_user_path(patrolName='3002')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=9999999)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투준비(self.ctx)


class 전투준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Down_Idle_A', duration=3000)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_3003')
        self.destroy_monster(spawnIds=[201], arg2=True) # 붉은 늑대의 심장:11003387
        self.create_monster(spawnIds=[501], animationEffect=True) # 붉은 늑대의 심장:22000324

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투메시지(self.ctx)


class 전투메시지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0.5)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010028_QD__MAIN__23$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투(self.ctx)


class 전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[501]):
            return 전투종료(self.ctx)


class 전투종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투종료대사(self.ctx)


class 전투종료대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=2001, type='trigger', achieve='Maze')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=이동, action='exit')
        self.move_user(mapId=52010028, portalId=7002)
        self.create_monster(spawnIds=[202], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투종료이후연출(self.ctx)


class 전투종료이후연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=1500000)
        self.face_emotion(spawnId=101, emotionName='Trigger_Dead')
        self.select_camera_path(pathIds=[4012], returnView=False)
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Dead_Idle_A', duration=150000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 찾으러왔어01(self.ctx)


class 찾으러왔어01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__24$', duration=3000)
        self.create_monster(spawnIds=[301], animationEffect=True)
        self.face_emotion(spawnId=301, emotionName='Trigger_Dead')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 찾으러왔어02(self.ctx)


class 찾으러왔어02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_3004')
        self.add_balloon_talk(spawnId=301, msg='$52010028_QD__MAIN__25$', duration=2000, delayTick=1000)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=150000)
        self.face_emotion(spawnId=101, emotionName='Trigger_Dead')
        self.face_emotion(spawnId=301, emotionName='down_Idle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 찾으러왔어03(self.ctx)


class 찾으러왔어03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[302], animationEffect=True)
        self.create_monster(spawnIds=[303], animationEffect=True)
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_3005')
        self.move_npc(spawnId=303, patrolName='MS2PatrolData_3006')
        self.add_balloon_talk(spawnId=302, msg='$52010028_QD__MAIN__26$', duration=2000, delayTick=1000)
        self.add_balloon_talk(spawnId=303, msg='$52010028_QD__MAIN__27$', duration=2000, delayTick=1200)
        self.move_user(mapId=52010028, portalId=7003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 찾으러왔어04(self.ctx)


class 찾으러왔어04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[304], animationEffect=True)
        self.create_monster(spawnIds=[305], animationEffect=True)
        self.move_npc(spawnId=304, patrolName='MS2PatrolData_3007')
        self.move_npc(spawnId=305, patrolName='MS2PatrolData_3008')
        self.add_balloon_talk(spawnId=304, msg='$52010028_QD__MAIN__28$', duration=2000, delayTick=1000)
        self.add_balloon_talk(spawnId=305, msg='$52010028_QD__MAIN__29$', duration=2000, delayTick=1200)
        self.move_user(mapId=52010028, portalId=7003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 어서와(self.ctx)


class 어서와(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=1500000)
        self.face_emotion(spawnId=101, emotionName='Trigger_Dead')
        self.add_cinematic_talk(npcId=0, msg='$52010028_QD__MAIN__30$', duration=3000)
        self.add_cinematic_talk(npcId=11003456, msg='$52010028_QD__MAIN__31$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8191):
            return 어서와02(self.ctx)


class 어서와02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.set_npc_emotion_sequence(spawnId=305, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=304, sequenceName='Talk_A')
        self.add_balloon_talk(spawnId=305, msg='$52010028_QD__MAIN__32$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=304, msg='$52010028_QD__MAIN__33$', duration=2000, delayTick=500)
        self.add_balloon_talk(spawnId=302, msg='$52010028_QD__MAIN__34$', duration=2000, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 어서와03(self.ctx)


class 어서와03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52010032, portalId=1)


initial_state = 던전에들어왔으면
