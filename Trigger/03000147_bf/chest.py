""" trigger/03000147_bf/chest.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[11000023], state=1)
        self.set_interact_object(triggerIds=[11000008], state=2)
        self.set_interact_object(triggerIds=[11000009], state=2)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            self.set_interact_object(triggerIds=[11000023], state=2)
            return 차웨이브대기1(self.ctx)


class 차웨이브대기1(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=23000003, textId=23000003, duration=5000)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[603], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차웨이브시작1(self.ctx)


class 차웨이브시작1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001,1002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1001,1002]):
            return 차웨이브대기2(self.ctx)


class 차웨이브대기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차웨이브시작2(self.ctx)


class 차웨이브시작2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 차웨이브대기3(self.ctx)


class 차웨이브대기3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차웨이브시작3(self.ctx)


class 차웨이브시작3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[3001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[3001]):
            self.set_event_ui(type=7, arg3='2000', arg4='0')
            return 상자확률(self.ctx)


class 상자확률(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=90):
            self.set_interact_object(triggerIds=[11000008], state=1)
            return 종료(self.ctx)
        if self.random_condition(rate=10):
            self.set_interact_object(triggerIds=[11000009], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
