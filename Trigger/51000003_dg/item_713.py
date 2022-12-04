""" trigger/51000003_dg/item_713.xml """
import trigger_api


# 포그 이펙트
class Spawn_check(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7713], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='item_713_spawn', value=1):
            return SpawnItem(self.ctx)


class SpawnItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7713], visible=True)
        self.set_effect(triggerIds=[7723], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[723]):
            return GetItem_Random(self.ctx)
        if self.user_value(key='item_713_spawn', value=0):
            return Spawn_check(self.ctx)


class Disable(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991116, key='item_713_spawn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Spawn_check(self.ctx)


class GetItem_Random(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='random_buff_box') # 큐브 안에 뭐가 들었을까? (트로피)
        self.set_effect(triggerIds=[7713], visible=False)
        self.set_effect(triggerIds=[7723], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return Buff_01(self.ctx)
        if self.random_condition(rate=1):
            return Buff_02(self.ctx)
        if self.random_condition(rate=1):
            return Buff_03(self.ctx)
        if self.random_condition(rate=10):
            return Buff_04(self.ctx)
        if self.random_condition(rate=1):
            return Buff_05(self.ctx)


class Buff_01(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000080, level=1, isSkillSet=False) # 이속증가

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=991116, key='item_713_spawn', value=0)


class Buff_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000081, level=1, isSkillSet=False) # 이속감소

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=991116, key='item_713_spawn', value=0)


class Buff_03(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000082, level=1, isSkillSet=False) # 키 커짐

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=991116, key='item_713_spawn', value=0)


class Buff_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000083, level=1, isSkillSet=False) # 키 작아짐

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=991116, key='item_713_spawn', value=0)


class Buff_05(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000085, level=1, isSkillSet=False) # 무적

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=991116, key='item_713_spawn', value=0)


initial_state = Spawn_check
