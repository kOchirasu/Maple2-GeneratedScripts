""" trigger/02000484_bf/01_climbthewall.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=False, enable=False, minimap_visible=False)
        self.set_effect(trigger_ids=[5100,5101,5102,5103,5104,5105,5106], visible=False) # ArrowGuide01
        self.set_effect(trigger_ids=[5200,5201,5202,5203], visible=False) # DownArrowBomb
        self.set_effect(trigger_ids=[5300,5301,5302,5303,5304], visible=False) # ArrowGuide02
        self.set_effect(trigger_ids=[5400,5401,5402], visible=False) # ArrowGuide03
        self.set_effect(trigger_ids=[5500,5501,5502,5503,5504], visible=False) # ArrowGuide04
        self.set_ladder(trigger_ids=[510], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[511], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[512], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[513], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[514], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[515], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[516], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[517], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[518], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[519], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[520], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[521], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[522], visible=False, enable=False, fade=0) # Ladder01
        self.set_ladder(trigger_ids=[530], visible=False, enable=False, fade=0) # Ladder02
        self.set_ladder(trigger_ids=[531], visible=False, enable=False, fade=0) # Ladder02
        self.set_ladder(trigger_ids=[532], visible=False, enable=False, fade=0) # Ladder02
        self.set_ladder(trigger_ids=[533], visible=False, enable=False, fade=0) # Ladder02
        self.set_ladder(trigger_ids=[534], visible=False, enable=False, fade=0) # Ladder02
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008], visible=True, start_delay=0, interval=0, fade=0) # Invisible_AlwaysOn
        self.set_interact_object(trigger_ids=[10002030], state=0) # Lever
        self.set_interact_object(trigger_ids=[10002031], state=0) # Lever
        self.destroy_monster(spawn_ids=[901,902,903,910,911,912,913,920,921,922,923,930,931,932,933,934]) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FirstArrowGuide01(self.ctx)


class FirstArrowGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039801, text_id=20039801, duration=4000) # 가이드 : 벽을 타고 올라가기
        self.set_effect(trigger_ids=[5100,5101,5102,5103,5104,5105,5106], visible=True) # ArrowGuide01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            # 테라스 도착
            return TerraceMobAttack01(self.ctx)


class TerraceMobAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901,902,903], auto_target=False) # Mob_Actor
        self.set_dialogue(type=1, spawn_id=901, script='$02000484_BF__01_CLIMBTHEWALL__0$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=902, script='$02000484_BF__01_CLIMBTHEWALL__1$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=903, script='$02000484_BF__01_CLIMBTHEWALL__2$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TerraceMobAttack02(self.ctx)


class TerraceMobAttack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[910,911,912,913], auto_target=False)
        self.set_effect(trigger_ids=[5500,5501,5502,5503,5504], visible=True) # ArrowGuide04

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LiftUpBombGuide01(self.ctx)


class LiftUpBombGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 폭탄을 들어서 가로막힌 벽을 향해 던지기
        self.show_guide_summary(entity_id=20039802, text_id=20039802, duration=4000)
        self.set_effect(trigger_ids=[5200,5201,5202,5203], visible=True) # DownArrowBomb

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9150]):
            # 테라스 너머 중간 벽
            return SecondArrowGuide01(self.ctx)


class SecondArrowGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5500,5501,5502,5503,5504], visible=False) # ArrowGuide04
        self.set_effect(trigger_ids=[5300,5301,5302,5303,5304], visible=True) # ArrowGuide02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            # 탑 아래층 도착
            return TowerUnderMobAttack01(self.ctx)


class TowerUnderMobAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039805, text_id=20039805, duration=3000) # 가이드 : 레버를 당기기
        self.spawn_monster(spawn_ids=[920,921,922,923], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return TowerUnderMobAttack01End(self.ctx)


class TowerUnderMobAttack01End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[920,921,922,923]):
            return SwichOn(self.ctx)


class SwichOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002030], state=1) # LeverForLadder01

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002030], state=0):
            return LadderOnToTowerUp01(self.ctx)


class LadderOnToTowerUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039804, text_id=20039804, duration=3000) # 가이드 : 사다리를 타고 위로 올라가기
        self.set_ladder(trigger_ids=[510], visible=True, enable=True, fade=1) # Ladder01
        self.set_ladder(trigger_ids=[511], visible=True, enable=True, fade=2) # Ladder01
        self.set_ladder(trigger_ids=[512], visible=True, enable=True, fade=3) # Ladder01
        self.set_ladder(trigger_ids=[513], visible=True, enable=True, fade=4) # Ladder01
        self.set_ladder(trigger_ids=[514], visible=True, enable=True, fade=5) # Ladder01
        self.set_ladder(trigger_ids=[515], visible=True, enable=True, fade=6) # Ladder01
        self.set_ladder(trigger_ids=[516], visible=True, enable=True, fade=7) # Ladder01
        self.set_ladder(trigger_ids=[517], visible=True, enable=True, fade=8) # Ladder01
        self.set_ladder(trigger_ids=[518], visible=True, enable=True, fade=9) # Ladder01
        self.set_ladder(trigger_ids=[519], visible=True, enable=True, fade=10) # Ladder01
        self.set_ladder(trigger_ids=[520], visible=True, enable=True, fade=11) # Ladder01
        self.set_ladder(trigger_ids=[521], visible=True, enable=True, fade=12) # Ladder01
        self.set_ladder(trigger_ids=[522], visible=True, enable=True, fade=13) # Ladder01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            return GuideMoveToBridge01(self.ctx)


class GuideMoveToBridge01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5400,5401,5402], visible=True) # ArrowGuide03
        self.spawn_monster(spawn_ids=[930,931,932,933,934], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9400]):
            # 다리 끝 도착
            return GuideMoveToBridge01_Guide(self.ctx)


class GuideMoveToBridge01_Guide(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9350]):
            # 다리 끝 도착
            return GuideMoveToBridge01End(self.ctx)


class GuideMoveToBridge01End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20039805, text_id=20039805, duration=3000) # 가이드 : 레버를 당기기

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[930,931,932,933,934]):
            return GuidePullTheLever01(self.ctx)


class GuidePullTheLever01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002031], state=1) # LeverForLadder01
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002031], state=0):
            return LadderOnToNextMap01(self.ctx)


class LadderOnToNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=False, enable=True, minimap_visible=False)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039804, text_id=20039804, duration=3000) # 가이드 : 사다리를 타고 위로 올라가기
        self.set_ladder(trigger_ids=[530], visible=True, enable=True, fade=1) # Ladder02
        self.set_ladder(trigger_ids=[531], visible=True, enable=True, fade=2) # Ladder02
        self.set_ladder(trigger_ids=[532], visible=True, enable=True, fade=3) # Ladder02
        self.set_ladder(trigger_ids=[533], visible=True, enable=True, fade=4) # Ladder02
        self.set_ladder(trigger_ids=[534], visible=True, enable=True, fade=5) # Ladder02


initial_state = Wait
