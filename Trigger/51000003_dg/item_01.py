""" trigger/51000003_dg/item_01.xml """
from common import *
import state


#  포그 이펙트 
class Round_check(state.State):
    def on_enter(self):
        set_user_value(triggerId=991119, key='item_710_spawn', value=0) # 모든 아이템 초기화
        set_user_value(triggerId=991118, key='item_711_spawn', value=0)
        set_user_value(triggerId=991117, key='item_712_spawn', value=0)
        set_user_value(triggerId=991116, key='item_713_spawn', value=0)
        set_user_value(triggerId=991115, key='item_714_spawn', value=0)
        set_user_value(triggerId=991114, key='item_715_spawn', value=0)
        set_user_value(triggerId=991113, key='item_716_spawn', value=0)
        set_user_value(triggerId=991112, key='item_717_spawn', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Round_01', value=1):
            return Round_01_Ready()


class Round_01_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round_01_Start()


class Round_01_Start(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return item_710()
        if random_condition(rate=1):
            return item_711()
        if random_condition(rate=1):
            return item_712()
        if random_condition(rate=1):
            return item_713()
        if random_condition(rate=1):
            return item_714()
        if random_condition(rate=1):
            return item_715()
        if random_condition(rate=1):
            return item_716()
        if random_condition(rate=1):
            return item_717()
        if user_value(key='Round_01', value=0):
            return Round_check()


class NextSpawn(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round_01_Start()
        if user_value(key='Round_01', value=0):
            return Round_check()


class item_710(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[710]):
            return item_710_spawn()
        if wait_tick(waitTick=1000):
            return Round_01_Start()


class item_711(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[711]):
            return item_711_spawn()
        if wait_tick(waitTick=1000):
            return Round_01_Start()


class item_712(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[712]):
            return item_712_spawn()
        if wait_tick(waitTick=1000):
            return Round_01_Start()


class item_713(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[713]):
            return item_713_spawn()
        if wait_tick(waitTick=1000):
            return Round_01_Start()


class item_714(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[714]):
            return item_714_spawn()
        if wait_tick(waitTick=1000):
            return Round_01_Start()


class item_715(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[715]):
            return item_715_spawn()
        if wait_tick(waitTick=1000):
            return Round_01_Start()


class item_716(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[716]):
            return item_716_spawn()
        if wait_tick(waitTick=1000):
            return Round_01_Start()


class item_717(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[717]):
            return item_717_spawn()
        if wait_tick(waitTick=1000):
            return Round_01_Start()


class item_710_spawn(state.State):
    def on_enter(self):
        set_user_value(triggerId=991119, key='item_710_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> state.State:
        if true():
            return NextSpawn()


class item_711_spawn(state.State):
    def on_enter(self):
        set_user_value(triggerId=991118, key='item_711_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> state.State:
        if true():
            return NextSpawn()


class item_712_spawn(state.State):
    def on_enter(self):
        set_user_value(triggerId=991117, key='item_712_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> state.State:
        if true():
            return NextSpawn()


class item_713_spawn(state.State):
    def on_enter(self):
        set_user_value(triggerId=991116, key='item_713_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> state.State:
        if true():
            return NextSpawn()


class item_714_spawn(state.State):
    def on_enter(self):
        set_user_value(triggerId=991115, key='item_714_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> state.State:
        if true():
            return NextSpawn()


class item_715_spawn(state.State):
    def on_enter(self):
        set_user_value(triggerId=991114, key='item_715_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> state.State:
        if true():
            return NextSpawn()


class item_716_spawn(state.State):
    def on_enter(self):
        set_user_value(triggerId=991113, key='item_716_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> state.State:
        if true():
            return NextSpawn()


class item_717_spawn(state.State):
    def on_enter(self):
        set_user_value(triggerId=991112, key='item_717_spawn', value=1) # 아이템 생성 스위치

    def on_tick(self) -> state.State:
        if true():
            return NextSpawn()


