""" trigger/02000486_bf/104_clear.xml """
import trigger_api


class 끝1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_skill(triggerIds=[1000049], enable=False)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9901]):
            return 끝2(self.ctx)


"""
class 끝2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(spawnId=100000001, compare='lowerEqual', value=5, isRelative=True):
            return 끝3(self.ctx)

"""


class 끝2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(spawnId=900, compare='lowerEqual', value=5, isRelative=True) and self.check_npc_hp(spawnId=901, compare='lowerEqual', value=5, isRelative=True):
            return 끝3(self.ctx)


class 끝3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[900], skillId=50002505, level=1, isPlayer=True, isSkillSet=False)
        self.add_buff(boxIds=[901], skillId=50002505, level=1, isPlayer=True, isSkillSet=False)
        self.set_skill(triggerIds=[1000049], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            pass


initial_state = 끝1
