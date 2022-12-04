""" trigger/52000033_qd/audiencewithereb_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[60100245], questStates=[2]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=end, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return pcmove(self.ctx)


class pcmove(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return ErebTalk_01(self.ctx)


class ErebTalk_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[700], returnView=False) # 에레브 얼굴로 클로즈업
        self.add_cinematic_talk(npcId=11001663, illustId='Ereb_normal', msg='$52000033_QD__AUDIENCEWITHEREB_03__0$', duration=3000, delayTick=0, align='left') # 에레브

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ErebTalk_02(self.ctx)


class ErebTalk_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[901], returnView=False) # 에레브 얼굴로 클로즈업
        self.add_cinematic_talk(npcId=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_03__1$', duration=3000, delayTick=0, align='left') # 에레브

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ErebTalk_03(self.ctx)


class ErebTalk_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[601], returnView=False) # 뒷 뷰

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[601], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return story_01(self.ctx)


class story_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000033_QD__AUDIENCEWITHEREB_03__2$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return story_02(self.ctx)


class story_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000033_QD__AUDIENCEWITHEREB_03__3$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return story_03(self.ctx)


class story_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000033_QD__AUDIENCEWITHEREB_03__4$', arg3=False)
        self.move_npc(spawnId=601, patrolName='MS2PatrolData_1005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ErebTalk_04(self.ctx)


class ErebTalk_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001663, illustId='Ereb_surprise', msg='$52000033_QD__AUDIENCEWITHEREB_03__5$', duration=3000, delayTick=0, align='left') # 에레브

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ErebTalk_05(self.ctx)


class ErebTalk_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=True)
        self.add_cinematic_talk(npcId=11001663, illustId='Ereb_closeEye', msg='$52000033_QD__AUDIENCEWITHEREB_03__6$', duration=3000, delayTick=0, align='left') # 에레브
        self.add_balloon_talk(spawnId=401, msg='$52000033_QD__AUDIENCEWITHEREB_03__7$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ErebTalk_06(self.ctx)


class ErebTalk_06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001663, illustId='Ereb_serious', msg='$52000033_QD__AUDIENCEWITHEREB_03__8$', duration=3000, delayTick=0, align='left') # 에레브
        self.move_npc(spawnId=601, patrolName='MS2PatrolData_1006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ErebTalk_07(self.ctx)


class ErebTalk_07(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001663, illustId='Ereb_closeEye', msg='$52000033_QD__AUDIENCEWITHEREB_03__9$', duration=3000, delayTick=0, align='left') # 에레브
        self.destroy_monster(spawnIds=[601])
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[601])
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
