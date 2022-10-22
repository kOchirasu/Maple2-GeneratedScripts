""" trigger/52000090_qd/52000090_trigger.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9100], questIds=[50100470], questStates=[1]):
            return 진행중일때20002272()
        if quest_user_detected(boxIds=[9100], questIds=[20002272], questStates=[1]):
            return 진행중일때20002272()


class 진행중일때20002272(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], isAutoTargeting=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 진행중일때02_20002272()


class 진행중일때02_20002272(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[1011,1012,1013,1014,1015], isAutoTargeting=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 진행중일때03_20002272()


class 진행중일때03_20002272(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[1016,1017,1018,1019,1020], isAutoTargeting=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 진행중일때04_20002272()


class 진행중일때04_20002272(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[1021,1022,1023,1024,1025,1026,1027,1028,1029], isAutoTargeting=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


