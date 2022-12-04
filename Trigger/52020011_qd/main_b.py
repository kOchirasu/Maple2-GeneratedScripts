""" trigger/52020011_qd/main_b.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_actor(triggerId=8001, visible=False, initialSequence='Attack_Idle_A')
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200130], questStates=[2]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Set(self.ctx)


class Set(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020011, portalId=6001)
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.set_actor(triggerId=8001, visible=True, initialSequence='Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Go(self.ctx)


class Go(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003599, msg='나 $npcName:11003599$의 이름으로 명한다.', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Scene_01(self.ctx)


class Scene_01(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003599, msg='이 땅의 모든 저주받은 존재여! 깊고 어두운 곳으로 떨어져라!', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Scene_02(self.ctx)


class Scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Scene_03(self.ctx)


class Scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.add_balloon_talk(spawnId=0, msg='!', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return Scene_Exit(self.ctx)


class Scene_Exit(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020020, portalId=6001)


initial_state = Idle
