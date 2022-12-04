""" trigger/63000067_cs/63000067_main.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.create_monster(spawnIds=[104], animationEffect=True)
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.create_monster(spawnIds=[106], animationEffect=True)
        self.create_monster(spawnIds=[107], animationEffect=True)
        self.create_monster(spawnIds=[108], animationEffect=True)
        self.create_monster(spawnIds=[109], animationEffect=True)
        self.create_monster(spawnIds=[110], animationEffect=True)
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.create_monster(spawnIds=[112], animationEffect=True)
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[30000352], questStates=[1]):
            return 인형찾기(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000352], questStates=[2]):
            return 마리엔의방(self.ctx)
        if self.user_detected(boxIds=[701]):
            return 종료_일반(self.ctx)


class 인형찾기(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26300671, textId=26300671)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[30000352], questStates=[2]):
            return 암전_01(self.ctx)


class 마리엔의방(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[30000352], questStates=[2]):
            return 암전_01(self.ctx)


class 암전_01(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=26300671)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 암전_02(self.ctx)


class 암전_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마리엔등장_01(self.ctx)


class 마리엔등장_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=스킵종료, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마리엔등장_02(self.ctx)


class 마리엔등장_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마리엔등장_03(self.ctx)

    def on_exit(self):
        self.select_camera_path(pathIds=[8002], returnView=False)


class 마리엔등장_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 마리엔등장_04(self.ctx)


class 마리엔등장_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000067_CS__63000067_MAIN__0$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 마리엔등장_05(self.ctx)


class 마리엔등장_05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000067_CS__63000067_MAIN__1$', duration=3500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 마리엔등장_06(self.ctx)


class 마리엔등장_06(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 마리엔등장_07(self.ctx)


class 마리엔등장_07(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000067_CS__63000067_MAIN__2$', duration=3500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 마리엔등장_08(self.ctx)


class 마리엔등장_08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 마리엔등장_09(self.ctx)


class 마리엔등장_09(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000067_CS__63000067_MAIN__3$', duration=2000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 마리엔등장_10(self.ctx)


class 마리엔등장_10(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004294, msg='$63000067_CS__63000067_MAIN__4$', duration=2500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 마리엔퇴장_01(self.ctx)


class 마리엔퇴장_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.destroy_monster(spawnIds=[201])
        self.set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 마리엔퇴장_02(self.ctx)


class 마리엔퇴장_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료_퀘스트(self.ctx)


class 스킵종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료_퀘스트(self.ctx)


class 종료_퀘스트(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


class 종료_일반(trigger_api.Trigger):
    pass


initial_state = 준비
