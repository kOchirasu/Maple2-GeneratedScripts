""" trigger/03000084_bf/boss.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[11000009], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            self.create_monster(spawnIds=[2001], animationEffect=False)
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=23000001, textId=23000001, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 보스등장(self.ctx)
        if self.monster_dead(boxIds=[2001]):
            self.hide_guide_summary(entityId=23000001)
            self.set_interact_object(triggerIds=[11000009], state=1)
            self.set_event_ui(type=7, arg3='2000', arg4='0')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
