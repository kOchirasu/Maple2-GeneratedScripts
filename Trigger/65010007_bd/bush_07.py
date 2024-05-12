""" trigger/65010007_bd/bush_07.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=1001007, skill_id=70000075)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=1001007, min_users='1', operator='Equal'):
            return 버프발동(self.ctx)


class 버프발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[1001007], skill_id=70000075, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 버프발동(self.ctx)
        if self.count_users(box_id=1001007, min_users='1', operator='Greater'):
            return 대기(self.ctx)
        if not self.user_detected(box_ids=[1001007]):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
