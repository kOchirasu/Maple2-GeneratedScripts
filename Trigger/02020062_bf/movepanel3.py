""" trigger/02020062_bf/movepanel3.xml """
import trigger_api


class 발판초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[2200,2201,2202,2203,2204,2205,2206,2207,2208], enable=False)
        self.set_visible_breakable_object(triggerIds=[2200,2201,2202,2203,2204,2205,2206,2207,2208], visible=False)
        self.set_user_value(triggerId=99990026, key='MovePanel03', value=0)
        self.set_interact_object(triggerIds=[12000117], state=2) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MovePanel03', value=1):
            # 이동발판 삭제 후 대기
            return 레버생성(self.ctx)


class 레버생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[12000117], state=1) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000117], stateValue=0):
            return 발판이동(self.ctx)


class 발판이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(triggerIds=[2200,2201,2202,2203,2204,2205,2206,2207,2208], visible=True)
        self.set_interact_object(triggerIds=[12000117], state=2) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9202]):
            self.set_breakable(triggerIds=[2200,2201,2202,2203,2204,2205,2206,2207,2208], enable=True)
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[2200,2201,2202,2203,2204,2205,2206,2207,2208], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 발판이동(self.ctx)


initial_state = 발판초기화
