""" trigger/02020062_bf/movepanel2.xml """
import trigger_api


class 발판초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[2100,2101,2102,2103,2104,2105,2106,2107,2108])
        self.set_visible_breakable_object(trigger_ids=[2100,2101,2102,2103,2104,2105,2106,2107,2108])
        self.set_user_value(trigger_id=99990025, key='MovePanel02', value=0)
        self.set_interact_object(trigger_ids=[12000116], state=2) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MovePanel02') >= 1:
            # 이동발판 삭제 후 대기
            return 레버생성(self.ctx)


class 레버생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000116], state=1) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000116], state=0):
            return 발판이동(self.ctx)


class 발판이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[2100,2101,2102,2103,2104,2105,2106,2107,2108], visible=True)
        self.set_interact_object(trigger_ids=[12000116], state=2) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9201]):
            self.set_breakable(trigger_ids=[2100,2101,2102,2103,2104,2105,2106,2107,2108], enable=True)
            return 대기(self.ctx)
        if self.user_detected(box_ids=[9204]):
            self.set_breakable(trigger_ids=[2100,2101,2102,2103,2104,2105,2106,2107,2108], enable=True)
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9204]):
            self.set_breakable(trigger_ids=[2100,2101,2102,2103,2104,2105,2106,2107,2108])
            return 발판이동(self.ctx)


initial_state = 발판초기화
