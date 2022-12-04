""" trigger/02000290_bf/ladder.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310], visible=True, arg3=0, delay=0, scale=0) # WaterDisApp
        self.set_ladder(triggerIds=[511], visible=False, animationEffect=False) # LadderTheFall
        self.set_ladder(triggerIds=[512], visible=False, animationEffect=False) # LadderTheFall
        self.set_ladder(triggerIds=[513], visible=False, animationEffect=False) # LadderTheFall
        self.set_ladder(triggerIds=[514], visible=False, animationEffect=False) # LadderTheFall
        self.set_ladder(triggerIds=[515], visible=False, animationEffect=False) # LadderTheFall
        self.set_ladder(triggerIds=[516], visible=False, animationEffect=False) # LadderTheFall
        self.set_ladder(triggerIds=[517], visible=False, animationEffect=False) # LadderTheFall
        self.set_ladder(triggerIds=[518], visible=False, animationEffect=False) # LadderTheFall
        self.set_ladder(triggerIds=[519], visible=False, animationEffect=False) # LadderTheFall
        self.set_ladder(triggerIds=[520], visible=False, animationEffect=False) # LadderTheFall
        self.set_effect(triggerIds=[5100], visible=False) # LadderAppear
        self.set_effect(triggerIds=[5102], visible=False) # WaterDisApp
        self.set_effect(triggerIds=[5200], visible=False) # LeverArrow
        self.set_interact_object(triggerIds=[10000429], state=0) # Lever

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return 폭포안내(self.ctx)


class 폭포안내(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000429], state=1) # Lever
        self.set_effect(triggerIds=[5200], visible=True) # LeverArrow
        self.set_effect(triggerIds=[5000], visible=True) # GuideUI
        self.show_guide_summary(entityId=20002902, textId=20002902) # 레버를 당겨 보세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000429], stateValue=0):
            return 폭포갈라짐(self.ctx)


class 폭포갈라짐(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002902)
        self.set_effect(triggerIds=[5102], visible=True) # WaterDisApp
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310], visible=False, arg3=0, delay=200, scale=2)
        self.set_effect(triggerIds=[5200], visible=False) # LeverArrow

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 사다리생김(self.ctx)


class 사다리생김(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20002907, textId=20002907, duration=5000) # 폭포 위로 올라갈 수 있는 사다리가 나타났어요.
        self.set_effect(triggerIds=[5000], visible=True) # GuideUI
        self.set_effect(triggerIds=[5100], visible=True) # LadderAppear
        self.set_ladder(triggerIds=[511], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[512], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[513], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[514], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[515], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[516], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[517], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[518], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[519], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[520], visible=True, animationEffect=True)


initial_state = 대기
