""" trigger/52000046_qd/main_01.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[60100220], questStates=[1]):
            return ready(self.ctx)


# 이벤트 시작
class ready(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=scene_10, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_01(self.ctx)


class scene_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(pathIds=[4004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_02(self.ctx)


class scene_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000046, portalId=6001)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_03(self.ctx)


class scene_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_04(self.ctx)


class scene_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003215, msg='$52000046_QD__MAIN_01__0$', duration=3735, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_05(self.ctx)


class scene_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003215, msg='$52000046_QD__MAIN_01__1$', duration=2000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_06(self.ctx)


class scene_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003215, msg='$52000046_QD__MAIN_01__2$', duration=2000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_07(self.ctx)


class scene_07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003215, msg='$52000046_QD__MAIN_01__3$', duration=2000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_08(self.ctx)


class scene_08(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$52000046_QD__MAIN_01__4$', duration=3000)
        self.create_monster(spawnIds=[201], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_09(self.ctx)


class scene_09(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_10(self.ctx)

    def on_exit(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/Eff_jump_Landing.xml')


class scene_10(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='lenonn')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return warp(self.ctx)


class warp(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000127, portalId=1)


initial_state = idle
