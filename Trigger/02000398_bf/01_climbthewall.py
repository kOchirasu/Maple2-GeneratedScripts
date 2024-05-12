""" trigger/02000398_bf/01_climbthewall.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5100,5101,5102,5103,5104,5105,5106], visible=False) # ArrowGuide01
        self.set_effect(triggerIds=[5200,5201,5202,5203], visible=False) # DownArrowBomb
        self.set_effect(triggerIds=[5300,5301,5302,5303,5304], visible=False) # ArrowGuide02
        self.set_effect(triggerIds=[5400,5401,5402], visible=False) # ArrowGuide03
        self.set_effect(triggerIds=[5500,5501,5502,5503,5504], visible=False) # ArrowGuide04
        self.set_ladder(triggerIds=[510], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[511], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[512], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[513], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[514], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[515], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[516], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[517], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[518], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[519], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[520], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[521], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[522], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[530], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[531], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[532], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[533], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[534], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008], visible=True, arg3=0, delay=0, scale=0) # Invisible_AlwaysOn
        self.set_interact_object(triggerIds=[10001132], state=1) # Lever
        self.set_interact_object(triggerIds=[10001133], state=1) # Lever
        self.destroy_monster(spawnIds=[901,902,903,910,911,912,913,920,921,922,923,930,931,932,933,934]) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return FirstArrowGuide01(self.ctx)


class FirstArrowGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039801, textId=20039801, duration=4000) # 가이드 : 벽을 타고 올라가기
        self.set_effect(triggerIds=[5100,5101,5102,5103,5104,5105,5106], visible=True) # ArrowGuide01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9100]):
            # 테라스 도착
            return TerraceMobAttack01(self.ctx)


class TerraceMobAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[901,902,903], animationEffect=False) # Mob_Actor
        self.set_conversation(type=1, spawnId=901, script='$02000398_BF__01_CLIMBTHEWALL__0$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=902, script='$02000398_BF__01_CLIMBTHEWALL__1$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=903, script='$02000398_BF__01_CLIMBTHEWALL__2$', arg4=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return TerraceMobAttack02(self.ctx)


class TerraceMobAttack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[910,911,912,913], animationEffect=False)
        self.set_effect(triggerIds=[5500,5501,5502,5503,5504], visible=True) # ArrowGuide04

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LiftUpBombGuide01(self.ctx)


class LiftUpBombGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 폭탄을 들어서 가로막힌 벽을 향해 던지기
        self.show_guide_summary(entityId=20039802, textId=20039802, duration=4000)
        self.set_effect(triggerIds=[5200,5201,5202,5203], visible=True) # DownArrowBomb

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9150]):
            # 테라스 너머 중간 벽
            return SecondArrowGuide01(self.ctx)


class SecondArrowGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5500,5501,5502,5503,5504], visible=False) # ArrowGuide04
        self.set_effect(triggerIds=[5300,5301,5302,5303,5304], visible=True) # ArrowGuide02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9200]):
            # 탑 아래층 도착
            return TowerUnderMobAttack01(self.ctx)


class TowerUnderMobAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039803, textId=20039803, duration=3000) # 가이드 : 레버를 당기기
        self.create_monster(spawnIds=[920,921,922,923], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001132], stateValue=0):
            return LadderOnToTowerUp01(self.ctx)


class LadderOnToTowerUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039804, textId=20039804, duration=3000) # 가이드 : 사다리를 타고 위로 올라가기
        self.set_ladder(triggerIds=[510], visible=True, animationEffect=True, animationDelay=1) # Ladder01
        self.set_ladder(triggerIds=[511], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        self.set_ladder(triggerIds=[512], visible=True, animationEffect=True, animationDelay=3) # Ladder01
        self.set_ladder(triggerIds=[513], visible=True, animationEffect=True, animationDelay=4) # Ladder01
        self.set_ladder(triggerIds=[514], visible=True, animationEffect=True, animationDelay=5) # Ladder01
        self.set_ladder(triggerIds=[515], visible=True, animationEffect=True, animationDelay=6) # Ladder01
        self.set_ladder(triggerIds=[516], visible=True, animationEffect=True, animationDelay=7) # Ladder01
        self.set_ladder(triggerIds=[517], visible=True, animationEffect=True, animationDelay=8) # Ladder01
        self.set_ladder(triggerIds=[518], visible=True, animationEffect=True, animationDelay=9) # Ladder01
        self.set_ladder(triggerIds=[519], visible=True, animationEffect=True, animationDelay=10) # Ladder01
        self.set_ladder(triggerIds=[520], visible=True, animationEffect=True, animationDelay=11) # Ladder01
        self.set_ladder(triggerIds=[521], visible=True, animationEffect=True, animationDelay=12) # Ladder01
        self.set_ladder(triggerIds=[522], visible=True, animationEffect=True, animationDelay=13) # Ladder01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9300]):
            return GuideMoveToBridge01(self.ctx)


class GuideMoveToBridge01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5400,5401,5402], visible=True) # ArrowGuide03
        self.create_monster(spawnIds=[930,931,932,933,934], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9400]):
            # 다리 끝 도착
            return GuidePullTheLever01(self.ctx)


class GuidePullTheLever01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039803, textId=20039803, duration=3000) # 가이드 : 레버를 당기기

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001133], stateValue=0):
            return LadderOnToNextMap01(self.ctx)


class LadderOnToNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=False, enable=True, minimapVisible=False)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039804, textId=20039804, duration=3000) # 가이드 : 사다리를 타고 위로 올라가기
        self.set_ladder(triggerIds=[530], visible=True, animationEffect=True, animationDelay=1) # Ladder02
        self.set_ladder(triggerIds=[531], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.set_ladder(triggerIds=[532], visible=True, animationEffect=True, animationDelay=3) # Ladder02
        self.set_ladder(triggerIds=[533], visible=True, animationEffect=True, animationDelay=4) # Ladder02
        self.set_ladder(triggerIds=[534], visible=True, animationEffect=True, animationDelay=5) # Ladder02


initial_state = Wait
