""" trigger/51000003_dg/item_01.xml """
import common


# 포그 이펙트
class Round_check(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991119, key='item_710_spawn', value=0) # 모든 아이템 초기화
        self.set_user_value(triggerId=991118, key='item_711_spawn', value=0)
        self.set_user_value(triggerId=991117, key='item_712_spawn', value=0)
        self.set_user_value(triggerId=991116, key='item_713_spawn', value=0)
        self.set_user_value(triggerId=991115, key='item_714_spawn', value=0)
        self.set_user_value(triggerId=991114, key='item_715_spawn', value=0)
        self.set_user_value(triggerId=991113, key='item_716_spawn', value=0)
        self.set_user_value(triggerId=991112, key='item_717_spawn', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Round_01', value=1):
            return Round_01_Ready(self.ctx)


class Round_01_Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round_01_Start(self.ctx)


class Round_01_Start(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=1):
            return item_710(self.ctx)
        if self.random_condition(rate=1):
            return item_711(self.ctx)
        if self.random_condition(rate=1):
            return item_712(self.ctx)
        if self.random_condition(rate=1):
            return item_713(self.ctx)
        if self.random_condition(rate=1):
            return item_714(self.ctx)
        if self.random_condition(rate=1):
            return item_715(self.ctx)
        if self.random_condition(rate=1):
            return item_716(self.ctx)
        if self.random_condition(rate=1):
            return item_717(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)


class NextSpawn(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round_01_Start(self.ctx)
        if self.user_value(key='Round_01', value=0):
            return Round_check(self.ctx)


class item_710(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[710]):
            return item_710_spawn(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Round_01_Start(self.ctx)


class item_711(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[711]):
            return item_711_spawn(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Round_01_Start(self.ctx)


class item_712(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[712]):
            return item_712_spawn(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Round_01_Start(self.ctx)


class item_713(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[713]):
            return item_713_spawn(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Round_01_Start(self.ctx)


class item_714(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[714]):
            return item_714_spawn(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Round_01_Start(self.ctx)


class item_715(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[715]):
            return item_715_spawn(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Round_01_Start(self.ctx)


class item_716(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[716]):
            return item_716_spawn(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Round_01_Start(self.ctx)


class item_717(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[717]):
            return item_717_spawn(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Round_01_Start(self.ctx)


class item_710_spawn(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991119, key='item_710_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NextSpawn(self.ctx)


class item_711_spawn(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991118, key='item_711_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NextSpawn(self.ctx)


class item_712_spawn(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991117, key='item_712_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NextSpawn(self.ctx)


class item_713_spawn(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991116, key='item_713_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NextSpawn(self.ctx)


class item_714_spawn(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991115, key='item_714_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NextSpawn(self.ctx)


class item_715_spawn(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991114, key='item_715_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NextSpawn(self.ctx)


class item_716_spawn(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991113, key='item_716_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NextSpawn(self.ctx)


class item_717_spawn(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=991112, key='item_717_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NextSpawn(self.ctx)


initial_state = Round_check
