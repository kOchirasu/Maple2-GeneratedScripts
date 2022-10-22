""" trigger/02000483_bf/03_usingbomb.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5100,5101,5102,5103], visible=False) # DownArrowBomb
        set_effect(triggerIds=[5200,5201,5202,5203], visible=False) # TargetBoxGuide
        destroy_monster(spawnIds=[910,911]) # Mob

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[910,911], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ArrowGuideOn()


class ArrowGuideOn(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039703, textId=20039703, duration=4000) # 가이드 : 폭탄을 들어서 가로막힌 벽을 향해 던지기
        set_effect(triggerIds=[5100,5101,5102,5103], visible=True) # DownArrowBomb
        set_effect(triggerIds=[5200,5201,5202,5203], visible=True) # TargetBoxGuide

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9201]):
            return ArrowGuideOff()


class ArrowGuideOff(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5100,5101,5102,5103], visible=False) # DownArrowBomb
        set_effect(triggerIds=[5200,5201,5202,5203], visible=False) # TargetBoxGuide


