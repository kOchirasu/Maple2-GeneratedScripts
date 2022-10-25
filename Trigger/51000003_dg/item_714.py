""" trigger/51000003_dg/item_714.xml """
import common


# 포그 이펙트
class Spawn_check(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7714], visible=False)
        self.set_effect(triggerIds=[7724], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='item_714_spawn', value=1):
            return SpawnItem(self.ctx)


class SpawnItem(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7714], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[724]):
            return GetItem_Random(self.ctx)
        if self.user_value(key='item_714_spawn', value=0):
            return Spawn_check(self.ctx)


class Disable(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991114, key='item_715_spawn', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Spawn_check(self.ctx)


class GetItem_Random(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='random_buff_box') # 큐브 안에 뭐가 들었을까? (트로피)
        self.set_effect(triggerIds=[7714], visible=False)
        self.set_effect(triggerIds=[7724], visible=True)

    def on_tick(self) -> common.Trigger:
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


class Buff_01(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000080, level=1, isSkillSet=False) # 이속증가

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=991115, key='item_714_spawn', value=0)


class Buff_02(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000081, level=1, isSkillSet=False) # 이속감소

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=991115, key='item_714_spawn', value=0)


class Buff_03(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000082, level=1, isSkillSet=False) # 키 커짐

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=991115, key='item_714_spawn', value=0)


class Buff_04(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000083, level=1, isSkillSet=False) # 키 작아짐

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=991115, key='item_714_spawn', value=0)


class Buff_05(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=70000085, level=1, isSkillSet=False) # 무적

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=991115, key='item_714_spawn', value=0)


initial_state = Spawn_check
