""" trigger/52000130_qd/52000130_main.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701]):
            return 잠시대기(self.ctx)


class 잠시대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC이동_01(self.ctx)


class PC이동_01(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카일과대화_01(self.ctx)


class 카일과대화_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카일과대화_02(self.ctx)


class 카일과대화_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=카일이동_01, action='nextState')
        self.add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__0$', duration=3000, align='right')
        # <action name="SetNpcEmotionSequence" arg1="101" arg2="Talk_A" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 카일과대화_03(self.ctx)


class 카일과대화_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카일과대화_04(self.ctx)


class 카일과대화_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000130_QD__52000130_MAIN__1$', duration=3500, align='right')
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 카일과대화_05(self.ctx)


class 카일과대화_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카일과대화_06(self.ctx)


class 카일과대화_06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__2$', duration=3000, align='right')
        # <action name="SetNpcEmotionSequence" arg1="101" arg2="Talk_A" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3300):
            return 카일이동_01(self.ctx)


class 카일이동_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카일이동_02(self.ctx)


class 카일이동_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카일공격_01(self.ctx)


class 카일공격_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카일공격_02(self.ctx)


class 카일공격_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Emotion_Failure_A', duration=30000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 습격후대화_01(self.ctx)


class 습격후대화_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 습격후대화_02(self.ctx)


class 습격후대화_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=씬스킵_01, action='exit')
        self.add_cinematic_talk(npcId=0, msg='$52000130_QD__52000130_MAIN__3$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 습격후대화_03(self.ctx)


class 습격후대화_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__4$', duration=3500, align='right')
        self.add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__5$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 습격후대화_04(self.ctx)


class 습격후대화_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000130_QD__52000130_MAIN__6$', duration=2500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 습격후대화_05(self.ctx)


class 습격후대화_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__7$', duration=3500, align='right')
        self.add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 습격후대화_06(self.ctx)


class 습격후대화_06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000130_QD__52000130_MAIN__9$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 습격후대화_07(self.ctx)


class 습격후대화_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__10$', duration=3500, align='right')
        self.add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__11$', duration=2500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7500):
            return 습격후대화_08(self.ctx)


class 습격후대화_08(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000130_QD__52000130_MAIN__12$', duration=2500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 페이드아웃_01(self.ctx)


class 페이드아웃_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 페이드아웃_02(self.ctx)


class 페이드아웃_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__13$', duration=5000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 강제이동(self.ctx)


class 씬스킵_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000131, portalId=1)


initial_state = 준비
