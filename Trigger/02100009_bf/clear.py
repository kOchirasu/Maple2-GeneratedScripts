""" trigger/02100009_bf/clear.xml """
import trigger_api


class 끝1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[1000049], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 끝2(self.ctx)


"""
class 끝2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(spawnId=100000001, compare='lowerEqual', value=5, isRelative=True):
            return 끝3(self.ctx)

"""


class 끝2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(spawnId=100000001, compare='lowerEqual', value=5, isRelative=True) and self.check_npc_hp(spawnId=100000002, compare='lowerEqual', value=5, isRelative=True):
            return 끝3(self.ctx)


class 끝3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[100000002], skillId=50000217, level=1, isPlayer=True, isSkillSet=False)
        self.set_skill(triggerIds=[1000049], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            pass


initial_state = 끝1
