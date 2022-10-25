""" trigger/52000155_qd/52000155.xml """
import common


class wait_01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001,5002], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[40002728], questStates=[3]):
            return 전직하러_01(self.ctx)
        if self.quest_user_detected(boxIds=[2002], questIds=[40002725], questStates=[3]):
            return 가이드_01(self.ctx)
        if self.user_detected(boxIds=[2002]):
            return wait_02(self.ctx)


class wait_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return wait_03(self.ctx)


class wait_03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.move_user(mapId=52000155, portalId=6001)
        self.select_camera_path(pathIds=[4003,4004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 빅스제시_01(self.ctx)


class 빅스제시_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 정리_01(self.ctx)


class 정리_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 정리_02(self.ctx)


class 정리_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 밝아짐(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 밝아짐(self.ctx)


class 밝아짐(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[40002725], questStates=[2]):
            return 만취상태(self.ctx)


class 만취상태(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000155_QD__52000155__0$', arg3=False)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 만취상태_01(self.ctx)


class 만취상태_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.destroy_monster(spawnIds=[108])
        self.destroy_monster(spawnIds=[109])
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Down_Idle_A', duration=90000000)
        self.set_npc_emotion_loop(spawnId=106, sequenceName='Down_Idle_A', duration=90000000)
        self.move_user(mapId=52000155, portalId=6002)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 정리2_02(self.ctx)


class 정리2_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정리2_03(self.ctx)


class 정리2_03(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[40002726], questStates=[2]):
            return 가이드_01(self.ctx)


class 가이드_01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001,5002], visible=True)
        self.destroy_monster(spawnIds=[110])
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.show_guide_summary(entityId=25201551, textId=25201551, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[40002727], questStates=[2]):
            return 가이드_02(self.ctx)


class 가이드_02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001,5002], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[40002728], questStates=[2]):
            return 전직하러_01(self.ctx)


class 전직하러_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전직하러_02(self.ctx)


class 전직하러_02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000157, portalId=6003)


initial_state = wait_01
