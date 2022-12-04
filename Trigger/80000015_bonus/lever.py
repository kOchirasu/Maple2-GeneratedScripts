""" trigger/80000015_bonus/lever.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7101], enable=False)
        self.set_interact_object(triggerIds=[10001314], state=1)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 안내(self.ctx)
        if self.object_interacted(interactIds=[10001314], stateValue=0):
            return 문열림(self.ctx)


class 안내(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$80000015_bonus__lever__0$', arg3='2000', arg4='101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001314], stateValue=0):
            return 문열림(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 반응대기(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True)
        self.spawn_npc_range(rangeIds=[2001], isAutoTargeting=False, score=1500)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999101, key='Dead_A', value=1)
        self.set_effect(triggerIds=[6000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_skill(triggerIds=[7101], enable=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
