""" trigger/02000486_bf/104_clear.xml """
import trigger_api


class 끝1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_skill(trigger_ids=[1000049], enable=False)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9901]):
            return 끝2(self.ctx)


"""
class 끝2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(spawn_id=100000001, compare='lowerEqual', value=5, is_relative=True):
            return 끝3(self.ctx)

"""


class 끝2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(spawn_id=900, compare='lowerEqual', value=5, is_relative=True) and self.check_npc_hp(spawn_id=901, compare='lowerEqual', value=5, is_relative=True):
            return 끝3(self.ctx)


class 끝3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[900], skill_id=50002505, level=1, is_player=True, is_skill_set=False)
        self.add_buff(box_ids=[901], skill_id=50002505, level=1, is_player=True, is_skill_set=False)
        self.set_skill(trigger_ids=[1000049], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            pass


initial_state = 끝1
