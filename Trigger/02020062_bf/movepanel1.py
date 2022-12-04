""" trigger/02020062_bf/movepanel1.xml """
import trigger_api


class 발판초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008], enable=False)
        self.set_visible_breakable_object(triggerIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008], visible=False)
        self.set_user_value(triggerId=99990024, key='MovePanel01', value=0)
        self.set_interact_object(triggerIds=[12000115], state=2) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MovePanel01', value=1):
            return 레버생성(self.ctx)


class 레버생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000115], state=1) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000115], stateValue=0):
            return 발판이동(self.ctx)


class 발판이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008], visible=True)
        self.set_interact_object(triggerIds=[12000115], state=2) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9200]):
            self.set_breakable(triggerIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008], enable=True)
            return 대기(self.ctx)
        if self.user_detected(boxIds=[9204]):
            self.set_breakable(triggerIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008], enable=True)
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9204]):
            self.set_breakable(triggerIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008], enable=False)
            return 발판이동(self.ctx)


initial_state = 발판초기화
