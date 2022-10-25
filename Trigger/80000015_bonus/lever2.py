""" trigger/80000015_bonus/lever2.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7102], enable=False)
        self.set_interact_object(triggerIds=[10001315], state=1)
        self.set_mesh(triggerIds=[3006,3007,3008,3009,3010,3011], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 반응대기(self.ctx)


class 반응대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            return 안내(self.ctx)
        if self.object_interacted(interactIds=[10001315], stateValue=0):
            return 문열림(self.ctx)


class 안내(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$80000015_bonus__lever2__0$', arg3='2000', arg4='102')

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001315], stateValue=0):
            return 문열림(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 반응대기(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True)
        self.spawn_npc_range(rangeIds=[2002], isAutoTargeting=False, score=1500)
        self.set_mesh(triggerIds=[3006,3007,3008,3009,3010,3011], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2002]):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999101, key='Dead_B', value=1)
        self.set_effect(triggerIds=[6000], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_skill(triggerIds=[7102], enable=True)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
