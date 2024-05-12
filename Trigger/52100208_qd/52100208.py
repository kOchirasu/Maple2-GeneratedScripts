""" trigger/52100208_qd/52100208.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003300], questStates=[2]):
            return wait_01_02(self.ctx)


class wait_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52100208, portalId=5001)
        self.set_effect(triggerIds=[6001], visible=False)
        self.set_effect(triggerIds=[6002], visible=False)
        self.set_effect(triggerIds=[6003], visible=False)
        self.destroy_monster(spawnIds=[201,202,203,204,205,206,207,208,209])
        self.create_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202])
        self.create_monster(spawnIds=[203])
        self.create_monster(spawnIds=[204])
        self.create_monster(spawnIds=[205])
        self.create_monster(spawnIds=[206])
        self.create_monster(spawnIds=[207])
        self.create_monster(spawnIds=[208])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대면(self.ctx)


class 투르카대면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대면_02(self.ctx)


class 투르카대면_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11004678, illustId='Neirin_surprise', align='left', msg='$52100208_QD__52100208__0$', duration=4000)
        self.add_cinematic_talk(npcId=11004675, illustId='Bliche_mad', align='right', msg='$52100208_QD__52100208__1$', duration=4500)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8500):
            return PC이동(self.ctx)


class PC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_3002')
        self.add_cinematic_talk(npcId=0, msg='$52100208_QD__52100208__2$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 투르카대면_02_01(self.ctx)


class 투르카대면_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004683, msg='$52100208_QD__52100208__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 투르카대면_03(self.ctx)


class 투르카대면_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52100208_QD__52100208__4$', duration=2500)
        self.add_cinematic_talk(npcId=0, msg='$52100208_QD__52100208__5$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 투르카대면_04(self.ctx)


class 투르카대면_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4004,4005,4006], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 투르카대면_05(self.ctx)


class 투르카대면_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[209], animationEffect=False)
        self.set_effect(triggerIds=[6001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 투르카대면_06(self.ctx)


class 투르카대면_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=0, msg='$52100208_QD__52100208__6$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 투르카대면_07(self.ctx)


class 투르카대면_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4007], returnView=False)
        self.move_npc(spawnId=209, patrolName='MS2PatrolData_3001')
        self.add_cinematic_talk(npcId=11004683, msg='$52100208_QD__52100208__7$', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 투르카대면_07_01(self.ctx)


class 투르카대면_07_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4020], returnView=False)
        self.set_npc_emotion_loop(spawnId=208, sequenceName='Attack_Idle_A', duration=100000000)
        self.add_cinematic_talk(npcId=11004682, illustId='ArcaneBlader_unfair', align='right', msg='$52100208_QD__52100208__8$', duration=3000)
        self.add_cinematic_talk(npcId=11004680, illustId='Eone_serious', align='right', msg='$52100208_QD__52100208__9$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6500):
            return 투르카대면_08(self.ctx)


class 투르카대면_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4008,4009], returnView=False)
        self.add_cinematic_talk(npcId=11004683, msg='$52100208_QD__52100208__10$', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6500):
            return 투르카대면_09(self.ctx)


class 투르카대면_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=209, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11004683, msg='$52100208_QD__52100208__11$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5500):
            return 투르카대면_10(self.ctx)


class 투르카대면_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4010], returnView=False)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11004675, illustId='Bliche_mad', align='right', msg='$52100208_QD__52100208__12$', duration=4000)
        self.add_cinematic_talk(npcId=11004588, illustId='Conder_normal', align='left', msg='$52100208_QD__52100208__13$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 투르카대면_11(self.ctx)


class 투르카대면_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4011,4012], returnView=False)
        self.add_cinematic_talk(npcId=11004683, msg='$52100208_QD__52100208__14$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 투르카대면_12(self.ctx)


class 투르카대면_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=209, sequenceName='Bore_B')
        self.add_cinematic_talk(npcId=11004683, msg='$52100208_QD__52100208__15$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 투르카대면_13(self.ctx)


class 투르카대면_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4014,4015], returnView=False)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Angry_A'])
        self.add_cinematic_talk(npcId=0, msg='$52100208_QD__52100208__16$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 투르카대면_13_02(self.ctx)


class 투르카대면_13_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4016], returnView=False)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_3003')
        self.add_cinematic_talk(npcId=11004588, illustId='Conder_normal', align='right', msg='$52100208_QD__52100208__17$', duration=4000)
        self.add_cinematic_talk(npcId=11004588, illustId='Conder_normal', align='right', msg='$52100208_QD__52100208__18$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 투르카대면_13_03(self.ctx)


class 투르카대면_13_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4013], returnView=False)
        self.add_cinematic_talk(npcId=11004683, msg='$52100208_QD__52100208__19$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 투르카대면_13_04(self.ctx)


class 투르카대면_13_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=209, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대면_13_05(self.ctx)


class 투르카대면_13_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4017], returnView=False)
        self.set_effect(triggerIds=[6003], visible=True)
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Stun_A', duration=100000000)
        self.add_cinematic_talk(npcId=11004588, illustId='0', msg='$52100208_QD__52100208__20$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 투르카대면_13_06(self.ctx)


class 투르카대면_13_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_3004')
        self.add_cinematic_talk(npcId=11004678, illustId='Neirin_surprise', align='left', msg='$52100208_QD__52100208__21$', duration=4000)
        self.add_cinematic_talk(npcId=11004677, illustId='Schatten_surprise', align='right', msg='$52100208_QD__52100208__22$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 투르카대면_14(self.ctx)


class 투르카대면_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4013], returnView=False)
        self.add_cinematic_talk(npcId=11004683, msg='$52100208_QD__52100208__23$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 투르카대면_15(self.ctx)


class 투르카대면_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6002], visible=True)
        self.destroy_monster(spawnIds=[209], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 투르카대면_16(self.ctx)


class 투르카대면_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4018], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52100208_QD__52100208__24$', duration=3000)
        self.add_cinematic_talk(npcId=11004679, illustId='Mason_closeEye', align='right', msg='$52100208_QD__52100208__25$', duration=4000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 정리_02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정리_02(self.ctx)


class 정리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정리_03(self.ctx)


class 정리_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=2020071, portalId=2)


initial_state = wait_01
