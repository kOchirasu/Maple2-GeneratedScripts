""" trigger/02020112_bf/safezone1.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990002, key='Safe', value=0)
        self.set_interact_object(triggerIds=[10002117], state=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[902], jobCode=0):
            return 감지(self.ctx)


class 감지(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102,103], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101,102,103]):
            return 안전장치_활성화(self.ctx)


class 안전장치_활성화(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002117], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002117], stateValue=0):
            return 안전장치_작동(self.ctx)


class 안전장치_작동(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020112_BF__SAFEZONE1__0$', arg3='5000')
        self.set_user_value(triggerId=99990002, key='Safe', value=1)


initial_state = 대기
