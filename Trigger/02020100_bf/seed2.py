""" trigger/02020100_bf/seed2.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='Seed2interact', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Seed2start', value=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[221,222,223,224])
        self.set_mesh(triggerIds=[1303], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002110], state=1, arg3=True)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Seed2start', value=2):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002110], stateValue=0):
            return 씨앗2_대기(self.ctx)


class 씨앗2_대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[221,222,223,224], animationEffect=False)
        self.set_mesh(triggerIds=[1303], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10002110], state=0, arg3=True)
        self.set_user_value(triggerId=99990001, key='Seed2interact', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Seed2start', value=2):
            return 종료(self.ctx)
        if not self.check_any_user_additional_effect(boxId=0, additionalEffectId=70002109, level=1):
            return 시작(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002110], state=0)


initial_state = 대기
