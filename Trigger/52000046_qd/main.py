""" trigger/52000046_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[60100215], questStates=[2]):
            return ready(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[60100215], questStates=[3]):
            return scene_04(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.destroy_monster(spawnIds=[1001,1002,2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return camera(self.ctx)


class camera(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001,4002,4003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='ChatUp_A')
        self.add_cinematic_talk(npcId=11003216, msg='$52000046_QD__MAIN__0$', duration=3000, align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_caption(scale=2.3, type='NameCaption', title='$52000046_QD__MAIN__1$', desc='$52000046_QD__MAIN__2$', align='centerLeft', offsetRateX=-0.15, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1001,1002,2002])
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return emd(self.ctx)


class emd(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
