""" trigger/02000290_bf/ladder.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310], visible=True, start_delay=0, interval=0, fade=0) # WaterDisApp
        self.set_ladder(trigger_ids=[511], visible=False, enable=False) # LadderTheFall
        self.set_ladder(trigger_ids=[512], visible=False, enable=False) # LadderTheFall
        self.set_ladder(trigger_ids=[513], visible=False, enable=False) # LadderTheFall
        self.set_ladder(trigger_ids=[514], visible=False, enable=False) # LadderTheFall
        self.set_ladder(trigger_ids=[515], visible=False, enable=False) # LadderTheFall
        self.set_ladder(trigger_ids=[516], visible=False, enable=False) # LadderTheFall
        self.set_ladder(trigger_ids=[517], visible=False, enable=False) # LadderTheFall
        self.set_ladder(trigger_ids=[518], visible=False, enable=False) # LadderTheFall
        self.set_ladder(trigger_ids=[519], visible=False, enable=False) # LadderTheFall
        self.set_ladder(trigger_ids=[520], visible=False, enable=False) # LadderTheFall
        self.set_effect(trigger_ids=[5100], visible=False) # LadderAppear
        self.set_effect(trigger_ids=[5102], visible=False) # WaterDisApp
        self.set_effect(trigger_ids=[5200], visible=False) # LeverArrow
        self.set_interact_object(trigger_ids=[10000429], state=0) # Lever

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 폭포안내(self.ctx)


class 폭포안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000429], state=1) # Lever
        self.set_effect(trigger_ids=[5200], visible=True) # LeverArrow
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
        self.show_guide_summary(entity_id=20002902, text_id=20002902) # 레버를 당겨 보세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000429], state=0):
            return 폭포갈라짐(self.ctx)


class 폭포갈라짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002902)
        self.set_effect(trigger_ids=[5102], visible=True) # WaterDisApp
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310], visible=False, start_delay=0, interval=200, fade=2)
        self.set_effect(trigger_ids=[5200], visible=False) # LeverArrow

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 사다리생김(self.ctx)


class 사다리생김(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 폭포 위로 올라갈 수 있는 사다리가 나타났어요.
        self.show_guide_summary(entity_id=20002907, text_id=20002907, duration=5000)
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
        self.set_effect(trigger_ids=[5100], visible=True) # LadderAppear
        self.set_ladder(trigger_ids=[511], visible=True, enable=True)
        self.set_ladder(trigger_ids=[512], visible=True, enable=True)
        self.set_ladder(trigger_ids=[513], visible=True, enable=True)
        self.set_ladder(trigger_ids=[514], visible=True, enable=True)
        self.set_ladder(trigger_ids=[515], visible=True, enable=True)
        self.set_ladder(trigger_ids=[516], visible=True, enable=True)
        self.set_ladder(trigger_ids=[517], visible=True, enable=True)
        self.set_ladder(trigger_ids=[518], visible=True, enable=True)
        self.set_ladder(trigger_ids=[519], visible=True, enable=True)
        self.set_ladder(trigger_ids=[520], visible=True, enable=True)


initial_state = 대기
