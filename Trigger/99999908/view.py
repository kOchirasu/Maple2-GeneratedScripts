""" trigger/99999908/view.xml """
from common import *
import state


#  에디셔널 이펙트를 계속 걸어줌 
class idle(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return buff_01()


class buff_01(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=99910221, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return buff_02()


class buff_02(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=99910221, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return buff_03()


class buff_03(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=99910221, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return buff_04()


class buff_04(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=99910221, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return buff_05()


class buff_05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120])
        spawn_npc_range(rangeIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120], isAutoTargeting=False, randomPickCount=3, score=100)
        add_buff(boxIds=[701], skillId=99910221, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return idle()


