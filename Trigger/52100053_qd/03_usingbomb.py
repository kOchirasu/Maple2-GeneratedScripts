""" trigger/52100053_qd/03_usingbomb.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5100,5101,5102,5103], visible=False) # DownArrowBomb
        self.set_effect(triggerIds=[5200,5201,5202,5203], visible=False) # TargetBoxGuide
        self.destroy_monster(spawnIds=[910,911]) # Mob

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9200]):
            return LoadingDelay(self.ctx)


class LoadingDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[910,911], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ArrowGuideOn(self.ctx)


class ArrowGuideOn(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039703, textId=20039703, duration=4000) # 가이드 : 폭탄을 들어서 가로막힌 벽을 향해 던지기
        self.set_effect(triggerIds=[5100,5101,5102,5103], visible=True) # DownArrowBomb
        self.set_effect(triggerIds=[5200,5201,5202,5203], visible=True) # TargetBoxGuide

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9201]):
            return ArrowGuideOff(self.ctx)


class ArrowGuideOff(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5100,5101,5102,5103], visible=False) # DownArrowBomb
        self.set_effect(triggerIds=[5200,5201,5202,5203], visible=False) # TargetBoxGuide


initial_state = Wait
