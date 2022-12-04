""" trigger/52000125_qd/main_01.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100190,60100191,60100192,60100193,60100194,60100195], questStates=[2]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_01(self.ctx)


# 씬 진행
class scene_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.create_monster(spawnIds=[201], animationEffect=True) # 연출 제타 (11003207)
        self.move_user(mapId=52000125, portalId=6001)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Clap_A')
        self.add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN_01__0$', duration=3000, align='center')
        self.set_scene_skip(state=scene_08, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='ChatUp')
        self.add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN_01__1$', duration=1000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003208, msg='$52000125_QD__MAIN_01__2$', duration=2000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN_01__3$', duration=3000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003,4004,4005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201]) # 연출용 제타()
        self.create_monster(spawnIds=[202], animationEffect=True) # 퀘스트용 제타 ()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100195], questStates=[2]):
            return eventtalk_start(self.ctx)


# 마크&제타 재회
class eventtalk_start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return eventtalk_01(self.ctx)


class eventtalk_01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_3003')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_3004')
        self.add_balloon_talk(spawnId=102, msg='$52000125_QD__MAIN_01__4$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return eventtalk_02(self.ctx)


class eventtalk_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='ChatUp_A')
        self.add_balloon_talk(spawnId=202, msg='$52000125_QD__MAIN_01__5$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return eventtalk_03(self.ctx)


class eventtalk_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Talk_A')
        self.add_balloon_talk(spawnId=202, msg='$52000125_QD__MAIN_01__6$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return eventtalk_04(self.ctx)


class eventtalk_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='ChatUp_A')
        self.add_balloon_talk(spawnId=202, msg='$52000125_QD__MAIN_01__7$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return eventtalk_05(self.ctx)


class eventtalk_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Idle_A')
        self.add_balloon_talk(spawnId=102, msg='$52000125_QD__MAIN_01__8$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return eventtalk_06(self.ctx)


class eventtalk_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Idle_A')
        self.add_balloon_talk(spawnId=202, msg='$52000125_QD__MAIN_01__9$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=20000):
            return eventtalk_02(self.ctx)


initial_state = idle
