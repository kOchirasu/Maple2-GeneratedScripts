""" trigger/52000181_qd/52000181.xml """
import common


class wait_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2001], jobCode=0):
            return wait_01_02(self.ctx)


class wait_01_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return wait_01_03(self.ctx)


class wait_01_03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=520001781, portalId=1)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연구실도착_01(self.ctx)


class 연구실도착_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연구실도착_02(self.ctx)


class 연구실도착_02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3001')
        self.move_user_path(patrolName='MS2PatrolData_3002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 정리_01(self.ctx)


class 정리_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 정리_02(self.ctx)


class 정리_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정리_03(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정리_03(self.ctx)


class 정리_03(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.destroy_monster(spawnIds=[101], arg2=False)
        self.move_user(mapId=52000181, portalId=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002765], questStates=[3]):
            return 프론티아재단으로_01(self.ctx)


class 프론티아재단으로_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 프론티아재단으로_02(self.ctx)


class 프론티아재단으로_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000186, portalId=1)


initial_state = wait_01
