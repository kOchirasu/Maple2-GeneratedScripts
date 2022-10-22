""" trigger/02000484_bf/01_climbthewall.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5100,5101,5102,5103,5104,5105,5106], visible=False) # ArrowGuide01
        set_effect(triggerIds=[5200,5201,5202,5203], visible=False) # DownArrowBomb
        set_effect(triggerIds=[5300,5301,5302,5303,5304], visible=False) # ArrowGuide02
        set_effect(triggerIds=[5400,5401,5402], visible=False) # ArrowGuide03
        set_effect(triggerIds=[5500,5501,5502,5503,5504], visible=False) # ArrowGuide04
        set_ladder(triggerIds=[510], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[511], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[512], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[513], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[514], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[515], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[516], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[517], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[518], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[519], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[520], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[521], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[522], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[530], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[531], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[532], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[533], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[534], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_AlwaysOn
        set_interact_object(triggerIds=[10002030], state=0) # Lever
        set_interact_object(triggerIds=[10002031], state=0) # Lever
        destroy_monster(spawnIds=[901,902,903,910,911,912,913,920,921,922,923,930,931,932,933,934]) # Mob

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FirstArrowGuide01()


class FirstArrowGuide01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039801, textId=20039801, duration=4000) # 가이드 : 벽을 타고 올라가기
        set_effect(triggerIds=[5100,5101,5102,5103,5104,5105,5106], visible=True) # ArrowGuide01

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return TerraceMobAttack01()


class TerraceMobAttack01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[901,902,903], arg2=False) # Mob_Actor
        set_conversation(type=1, spawnId=901, script='$02000484_BF__01_CLIMBTHEWALL__0$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=902, script='$02000484_BF__01_CLIMBTHEWALL__1$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=903, script='$02000484_BF__01_CLIMBTHEWALL__2$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TerraceMobAttack02()


class TerraceMobAttack02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[910,911,912,913], arg2=False)
        set_effect(triggerIds=[5500,5501,5502,5503,5504], visible=True) # ArrowGuide04

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LiftUpBombGuide01()


class LiftUpBombGuide01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039802, textId=20039802, duration=4000) # 가이드 : 폭탄을 들어서 가로막힌 벽을 향해 던지기
        set_effect(triggerIds=[5200,5201,5202,5203], visible=True) # DownArrowBomb

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9150]):
            return SecondArrowGuide01()


class SecondArrowGuide01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5500,5501,5502,5503,5504], visible=False) # ArrowGuide04
        set_effect(triggerIds=[5300,5301,5302,5303,5304], visible=True) # ArrowGuide02

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return TowerUnderMobAttack01()


class TowerUnderMobAttack01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039805, textId=20039805, duration=3000) # 가이드 : 레버를 당기기
        create_monster(spawnIds=[920,921,922,923], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return TowerUnderMobAttack01End()


class TowerUnderMobAttack01End(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[920,921,922,923]):
            return SwichOn()


class SwichOn(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002030], state=1) # LeverForLadder01

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002030], arg2=0):
            return LadderOnToTowerUp01()


class LadderOnToTowerUp01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039804, textId=20039804, duration=3000) # 가이드 : 사다리를 타고 위로 올라가기
        set_ladder(triggerIds=[510], visible=True, animationEffect=True, animationDelay=1) # Ladder01
        set_ladder(triggerIds=[511], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        set_ladder(triggerIds=[512], visible=True, animationEffect=True, animationDelay=3) # Ladder01
        set_ladder(triggerIds=[513], visible=True, animationEffect=True, animationDelay=4) # Ladder01
        set_ladder(triggerIds=[514], visible=True, animationEffect=True, animationDelay=5) # Ladder01
        set_ladder(triggerIds=[515], visible=True, animationEffect=True, animationDelay=6) # Ladder01
        set_ladder(triggerIds=[516], visible=True, animationEffect=True, animationDelay=7) # Ladder01
        set_ladder(triggerIds=[517], visible=True, animationEffect=True, animationDelay=8) # Ladder01
        set_ladder(triggerIds=[518], visible=True, animationEffect=True, animationDelay=9) # Ladder01
        set_ladder(triggerIds=[519], visible=True, animationEffect=True, animationDelay=10) # Ladder01
        set_ladder(triggerIds=[520], visible=True, animationEffect=True, animationDelay=11) # Ladder01
        set_ladder(triggerIds=[521], visible=True, animationEffect=True, animationDelay=12) # Ladder01
        set_ladder(triggerIds=[522], visible=True, animationEffect=True, animationDelay=13) # Ladder01

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9300]):
            return GuideMoveToBridge01()


class GuideMoveToBridge01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5400,5401,5402], visible=True) # ArrowGuide03
        create_monster(spawnIds=[930,931,932,933,934], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9400]):
            return GuideMoveToBridge01_Guide()


class GuideMoveToBridge01_Guide(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9350]):
            return GuideMoveToBridge01End()


class GuideMoveToBridge01End(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20039805, textId=20039805, duration=3000) # 가이드 : 레버를 당기기

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[930,931,932,933,934]):
            return GuidePullTheLever01()


class GuidePullTheLever01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002031], state=1) # LeverForLadder01
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002031], arg2=0):
            return LadderOnToNextMap01()


class LadderOnToNextMap01(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=True, minimapVisible=False)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039804, textId=20039804, duration=3000) # 가이드 : 사다리를 타고 위로 올라가기
        set_ladder(triggerIds=[530], visible=True, animationEffect=True, animationDelay=1) # Ladder02
        set_ladder(triggerIds=[531], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        set_ladder(triggerIds=[532], visible=True, animationEffect=True, animationDelay=3) # Ladder02
        set_ladder(triggerIds=[533], visible=True, animationEffect=True, animationDelay=4) # Ladder02
        set_ladder(triggerIds=[534], visible=True, animationEffect=True, animationDelay=5) # Ladder02


