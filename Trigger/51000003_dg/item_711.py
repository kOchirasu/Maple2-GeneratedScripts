""" trigger/51000003_dg/item_711.xml """
from common import *
import state


#  포그 이펙트 
class Spawn_check(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7711], visible=False)
        set_effect(triggerIds=[7721], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='item_711_spawn', value=1):
            return SpawnItem()


class SpawnItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7711], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[721]):
            return GetItem_Random()
        if user_value(key='item_711_spawn', value=0):
            return Spawn_check()


class Disable(state.State):
    def on_enter(self):
        set_user_value(triggerId=991118, key='item_711_spawn', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Spawn_check()


class GetItem_Random(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='random_buff_box') # 큐브 안에 뭐가 들었을까? (트로피)
        set_effect(triggerIds=[7711], visible=False)
        set_effect(triggerIds=[7721], visible=True)

    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return Buff_01()
        if random_condition(rate=1):
            return Buff_02()
        if random_condition(rate=1):
            return Buff_03()
        if random_condition(rate=10):
            return Buff_04()
        if random_condition(rate=1):
            return Buff_05()


class Buff_01(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=70000080, level=1, arg5=False) # 이속증가

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Spawn_check()

    def on_exit(self):
        set_user_value(triggerId=991118, key='item_711_spawn', value=0)


class Buff_02(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=70000081, level=1, arg5=False) # 이속감소

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Spawn_check()

    def on_exit(self):
        set_user_value(triggerId=991118, key='item_711_spawn', value=0)


class Buff_03(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=70000082, level=1, arg5=False) # 키 커짐

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Spawn_check()

    def on_exit(self):
        set_user_value(triggerId=991118, key='item_711_spawn', value=0)


class Buff_04(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=70000083, level=1, arg5=False) # 키 작아짐

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Spawn_check()

    def on_exit(self):
        set_user_value(triggerId=991118, key='item_711_spawn', value=0)


class Buff_05(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=70000085, level=1, arg5=False) # 무적

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Spawn_check()

    def on_exit(self):
        set_user_value(triggerId=991118, key='item_711_spawn', value=0)


