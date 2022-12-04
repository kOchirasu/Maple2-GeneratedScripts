""" trigger/52100105_qd/52100105_01.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[50101020], questStates=[2]):
            return wait_03(self.ctx)
        if self.quest_user_detected(boxIds=[2002], questIds=[50101030], questStates=[3]):
            return 장치가동_04(self.ctx)


class wait_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카_클라디아(self.ctx)


class 투르카_클라디아(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False) # 클라디아
        self.create_monster(spawnIds=[102], animationEffect=False) # 투르카
        self.create_monster(spawnIds=[103], animationEffect=False) # 검은 군단 병사
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.visible_my_pc(isVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 투르카_클라디아_02(self.ctx)


class 투르카_클라디아_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카_클라디아_03(self.ctx)


class 투르카_클라디아_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='right', msg='$52100105_QD__52100105_01__0$', duration=4000)
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='right', msg='$52100105_QD__52100105_01__1$', duration=4000)
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='right', msg='$52100105_QD__52100105_01__2$', duration=4000)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return 투르카_클라디아_04(self.ctx)


class 투르카_클라디아_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.add_cinematic_talk(npcId=11004392, illustId='cladia_normal', align='left', msg='$52100105_QD__52100105_01__3$', duration=3500)
        self.add_cinematic_talk(npcId=11004392, illustId='cladia_normal', align='left', msg='$52100105_QD__52100105_01__4$', duration=3500)
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='right', msg='$52100105_QD__52100105_01__5$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return 투르카_클라디아_05(self.ctx)


class 투르카_클라디아_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='left', msg='$52100105_QD__52100105_01__6$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 장치가동_01(self.ctx)


class 장치가동_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4007], returnView=False)
        self.set_npc_rotation(spawnId=102, rotation=270)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_normal', align='left', msg='$52100105_QD__52100105_01__7$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 장치가동_01_02(self.ctx)


class 장치가동_01_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 장치가동_01_03(self.ctx)


class 장치가동_01_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 장치가동_02(self.ctx)


class 장치가동_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.select_camera_path(pathIds=[4006], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 장치가동_02_01(self.ctx)


class 장치가동_02_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_rotation(spawnId=102, rotation=360)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Quest_Attack_A', duration=5000) # 클라디아
        self.add_cinematic_talk(npcId=11004392, illustId='cladia_normal', align='right', msg='$52100105_QD__52100105_01__8$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 장치가동_03(self.ctx)


class 장치가동_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002,4008], returnView=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Quest_Effect_A', duration=12000) # 클라디아
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 장치가동_04(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 정리(self.ctx)


class 장치가동_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 정리(self.ctx)


class 정리(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.destroy_monster(spawnIds=[105])
        self.destroy_monster(spawnIds=[106])
        self.destroy_monster(spawnIds=[107])
        self.visible_my_pc(isVisible=True)
        self.move_user(mapId=52100110, portalId=1)


initial_state = wait_01
