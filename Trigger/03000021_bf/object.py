""" trigger/03000021_bf/object.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[11000008], state=2)
        self.set_interact_object(triggerIds=[11000009], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            self.create_monster(spawnIds=[2001], animationEffect=False)
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=23000004, textId=23000004, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 몬스터생성(self.ctx)
        if self.monster_dead(boxIds=[2001]):
            self.hide_guide_summary(entityId=23000004)
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
