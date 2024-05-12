""" trigger/52000033_qd/audiencewithereb_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[60100010], questStates=[1]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000033, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return pcmove(self.ctx)


class pcmove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1) # 보험용
        self.set_cinematic_ui(type=3) # 보험용
        self.move_user_path(patrolName='MS2PatrolData_1004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ErebTalk_01(self.ctx)


class ErebTalk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[700], returnView=False) # 에레브 얼굴로 클로즈업
        self.add_cinematic_talk(npcId=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__0$', duration=5000)
        self.set_scene_skip(state=end, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ErebTalk_02(self.ctx)


class ErebTalk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[901], returnView=False) # 에레브 얼굴로 클로즈업
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__1$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Erebintroduce(self.ctx)


class Erebintroduce(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(scale=2.3, type='NameCaption', title='$52000033_QD__AUDIENCEWITHEREB_02__18$', desc='$52000033_QD__AUDIENCEWITHEREB_02__19$', align='centerLeft', offsetRateX=-0.15, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ErebTalk_03(self.ctx)


class ErebTalk_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__2$', duration=3000)
        self.add_cinematic_talk(npcId=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return Kaltalk_01(self.ctx)


class Kaltalk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11001665, msg='$52000033_QD__AUDIENCEWITHEREB_02__4$', duration=3000, illustId='Karl_normal', align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Kaltalk_02(self.ctx)


class Kaltalk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[902], returnView=False) # 칼 얼굴로 클로즈업
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11001665, msg='$52000033_QD__AUDIENCEWITHEREB_02__5$', duration=3000)
        self.add_cinematic_talk(npcId=11001665, msg='$52000033_QD__AUDIENCEWITHEREB_02__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return kaltroduce(self.ctx)


class kaltroduce(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(scale=2.3, type='NameCaption', title='$52000033_QD__AUDIENCEWITHEREB_02__20$', desc='$52000033_QD__AUDIENCEWITHEREB_02__21$', align='centerLeft', offsetRateX=-0.15, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_01(self.ctx)


class talk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[601], returnView=False) # 뒷 뷰
        self.add_cinematic_talk(npcId=11001663, illustId='Ereb_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__7$', duration=1000, delayTick=0, align='left') # 에레브
        self.add_cinematic_talk(npcId=11001665, illustId='Karl_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__8$', duration=3000, delayTick=0, align='right') # 칼

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_02(self.ctx)


class talk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11001666, illustId='Fray_serious', msg='$52000033_QD__AUDIENCEWITHEREB_02__9$', duration=3000, delayTick=3, align='center')
        self.add_cinematic_talk(npcId=11001663, illustId='Ereb_closeEye', msg='$52000033_QD__AUDIENCEWITHEREB_02__10$', duration=1000, delayTick=0, align='left') # 에레브
        self.add_cinematic_talk(npcId=11001665, illustId='Karl_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__11$', duration=1000, delayTick=0, align='right') # 칼

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6649):
            return talk_03(self.ctx)


class talk_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11001666, illustId='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__12$', duration=3000, align='Right')
        self.add_cinematic_talk(npcId=11001666, illustId='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__13$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return talk_04(self.ctx)


class talk_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11001666, illustId='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__14$', duration=3000, align='Right')
        self.add_cinematic_talk(npcId=11001666, illustId='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__15$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return talk_05(self.ctx)


class talk_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11001663, illustId='Ereb_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__16$', duration=3000, delayTick=0, align='left') # 에레브
        self.add_cinematic_talk(npcId=11001665, illustId='Karl_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__17$', duration=3000, delayTick=3, align='right') # 칼
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=9001, type='trigger', achieve='AudienceWithEreb')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[60100010], questStates=[1]):
            return end(self.ctx)


initial_state = idle
