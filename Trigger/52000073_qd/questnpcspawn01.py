""" trigger/52000073_qd/questnpcspawn01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # 카트반

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[3]): # 조사대원
            return NpcRemove01()
        if quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002666], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002666], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002666], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002665], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002665], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002665], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002664], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002664], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002664], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002663], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002663], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002663], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002662], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002662], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002662], questStates=[1]):
            return NpcChange01()


class NpcChange01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[201], arg2=False)


class NpcRemove01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])


