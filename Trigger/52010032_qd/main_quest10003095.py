""" trigger/52010032_qd/main_quest10003095.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False) # 나메드 치유 시전 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # 붉은 늑대의 심장 치유 이펙트

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003095], questStates=[1]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.move_user(mapId=52010032, portalId=7001)
        self.create_monster(spawnIds=[101], animationEffect=True) # 붉은늑대의심장:
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=100000000)
        self.face_emotion(spawnId=101, emotionName='Trigger_Dead')
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[201], animationEffect=True) # 나메드:

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 치유의식_01(self.ctx)


class 치유의식_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__0$', duration=4000)
        self.add_balloon_talk(spawnId=0, msg='$52010032_QD__MAIN_QUEST10003095__1$', duration=2000, delayTick=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 치유의식_02(self.ctx)


class 치유의식_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3002')
        self.set_npc_emotion_sequence(spawnId=401, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__2$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return 치유의식_03(self.ctx)


class 치유의식_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_B')
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_pc_emotion_loop(sequenceName='Emotion_Dance_Event01', duration=7000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__3$', duration=5000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__4$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 치유의식_04(self.ctx)


class 치유의식_04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 치유의식_04_1(self.ctx)


class 치유의식_04_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Down_Idle_A', duration=100000000)
        self.add_cinematic_talk(npcId=11003406, msg='$52010032_QD__MAIN_QUEST10003095__5$', duration=4000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__6$', duration=3000)
        self.add_cinematic_talk(npcId=11003406, msg='$52010032_QD__MAIN_QUEST10003095__7$', duration=3000)
        self.add_balloon_talk(spawnId=0, msg='$52010032_QD__MAIN_QUEST10003095__8$', duration=2000, delayTick=6000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11000):
            return 치유의식_05(self.ctx)


class 치유의식_05(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 치유의식_05_1(self.ctx)


class 치유의식_05_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[4003,4001], returnView=False)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_B')
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=100000000)
        self.face_emotion(spawnId=101, emotionName='Trigger_Dead')
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        self.add_cinematic_talk(npcId=0, msg='$52010032_QD__MAIN_QUEST10003095__9$', duration=3000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__10$', duration=4000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__11$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 의식종료_01(self.ctx)


class 의식종료_01(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A')
        self.move_user_path(patrolName='MS2PatrolData_3007')
        self.add_cinematic_talk(npcId=0, msg='$52010032_QD__MAIN_QUEST10003095__12$', duration=3000)
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__13$', duration=3000)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 의식종료_02(self.ctx)


class 의식종료_02(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=2001, type='trigger', achieve='Namid2')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_achievement(triggerId=2001, type='trigger', achieve='Namid2')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.create_monster(spawnIds=[202], animationEffect=True) # 나메드:
        self.destroy_monster(spawnIds=[201])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[101])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return None # Missing State: 


initial_state = idle
