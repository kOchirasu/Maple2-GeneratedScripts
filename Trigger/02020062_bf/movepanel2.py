""" trigger/02020062_bf/movepanel2.xml """
import common


class 발판초기화(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], enable=False)
        self.set_visible_breakable_object(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], visible=False)
        self.set_user_value(triggerId=99990025, key='MovePanel02', value=0)
        self.set_interact_object(triggerIds=[12000116], state=2) # 이동발판트리거

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MovePanel02', value=1):
            return 레버생성(self.ctx)


class 레버생성(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000116], state=1) # 이동발판트리거

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000116], stateValue=0):
            return 발판이동(self.ctx)


class 발판이동(common.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], visible=True)
        self.set_interact_object(triggerIds=[12000116], state=2) # 이동발판트리거

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9201]):
            self.set_breakable(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], enable=True)
            return 대기(self.ctx)
        if self.user_detected(boxIds=[9204]):
            self.set_breakable(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], enable=True)
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9204]):
            self.set_breakable(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], enable=False)
            return 발판이동(self.ctx)


initial_state = 발판초기화
