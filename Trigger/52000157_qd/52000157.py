""" trigger/52000157_qd/52000157.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001,5002], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[40002731], questStates=[2]):
            return 이별준비(self.ctx)
        if self.quest_user_detected(boxIds=[2002], questIds=[40002731], questStates=[3]):
            return 프론티아재단으로_01(self.ctx)
        if self.user_detected(boxIds=[2002]):
            return 전직컷씬01(self.ctx)


class 전직컷씬01(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='jobChange_thief.swf', movieId=1)
        self.create_monster(spawnIds=[107], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 정산끝(self.ctx)
        if self.wait_tick(waitTick=8000):
            return 정산끝(self.ctx)


class 정산끝(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[40002728], questStates=[3]):
            return 전직이펙트_01(self.ctx)


class 전직이펙트_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전직이펙트_02(self.ctx)


class 전직이펙트_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 떠나기전준비(self.ctx)


class 떠나기전준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[40002731], questStates=[2]):
            return 이별준비(self.ctx)


class 이별준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이별준비_01(self.ctx)


class 이별준비_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.destroy_monster(spawnIds=[107])
        self.destroy_monster(spawnIds=[105])
        self.destroy_monster(spawnIds=[106])
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.move_user(mapId=52000157, portalId=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이별준비_02(self.ctx)


class 이별준비_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이별준비_03(self.ctx)


class 이별준비_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[40002731], questStates=[3]):
            return 프론티아재단으로_01(self.ctx)


class 프론티아재단으로_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 프론티아재단으로_02(self.ctx)


class 프론티아재단으로_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000186, portalId=1)


initial_state = wait_01
