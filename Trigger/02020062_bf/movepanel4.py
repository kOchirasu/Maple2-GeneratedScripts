""" trigger/02020062_bf/movepanel4.xml """
import common


class 발판초기화(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[2300,2301,2302,2303,2304,2305,2306,2307,2308], enable=False)
        self.set_visible_breakable_object(triggerIds=[2300,2301,2302,2303,2304,2305,2306,2307,2308], visible=False)
        self.set_user_value(triggerId=99990027, key='MovePanel04', value=0)
        self.set_interact_object(triggerIds=[12000118], state=2) # 이동발판트리거

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MovePanel04', value=1):
            return 레버생성(self.ctx)


class 레버생성(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000118], state=1) # 이동발판트리거

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000118], stateValue=0):
            return 발판이동(self.ctx)


class 발판이동(common.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[2300,2301,2302,2303,2304,2305,2306,2307,2308], visible=True)
        self.set_interact_object(triggerIds=[12000118], state=2) # 이동발판트리거

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9203]):
            self.set_breakable(triggerIds=[2300,2301,2302,2303,2304,2305,2306,2307,2308], enable=True)
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[2300,2301,2302,2303,2304,2305,2306,2307,2308], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 발판이동(self.ctx)


initial_state = 발판초기화
