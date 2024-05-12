""" trigger/02010052_bf/invisiblewall01.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[20100,20101,20102,20103,20104,20105,20106,20107,20108,20109,20110,20111,20112], visible=True, interval=0, fade=3) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=710, min_users='1'):
            return 벽면처리(self.ctx)


class 벽면처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[20100,20101,20102,20103,20104,20105,20106,20107,20108,20109,20110,20111,20112], visible=False, interval=0, fade=3) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=710, min_users='1'):
            return 시작(self.ctx)


initial_state = 시작
