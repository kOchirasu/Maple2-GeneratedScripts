""" trigger/80000015_bonus/spawn.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001326], state=2)
        set_interact_object(triggerIds=[10001327], state=2)
        set_interact_object(triggerIds=[10001328], state=2)
        set_interact_object(triggerIds=[10001329], state=2)
        set_interact_object(triggerIds=[10001330], state=2)
        set_interact_object(triggerIds=[10001331], state=2)
        set_interact_object(triggerIds=[10001332], state=2)
        set_interact_object(triggerIds=[10001333], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 랜덤A()


class 랜덤A(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_interact_object(triggerIds=[10001326], state=1)
            return 랜덤B()
        if random_condition(rate=50):
            create_monster(spawnIds=[1501], arg2=False)
            return 랜덤B()


class 랜덤B(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_interact_object(triggerIds=[10001327], state=1)
            return 랜덤C()
        if random_condition(rate=50):
            create_monster(spawnIds=[1502], arg2=False)
            return 랜덤C()


class 랜덤C(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_interact_object(triggerIds=[10001328], state=1)
            return 랜덤D()
        if random_condition(rate=50):
            create_monster(spawnIds=[1503], arg2=False)
            return 랜덤D()


class 랜덤D(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_interact_object(triggerIds=[10001329], state=1)
            return 랜덤E()
        if random_condition(rate=50):
            create_monster(spawnIds=[1504], arg2=False)
            return 랜덤E()


class 랜덤E(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_interact_object(triggerIds=[10001330], state=1)
            return 랜덤F()
        if random_condition(rate=50):
            create_monster(spawnIds=[1505], arg2=False)
            return 랜덤F()


class 랜덤F(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_interact_object(triggerIds=[10001331], state=1)
            return 랜덤G()
        if random_condition(rate=50):
            create_monster(spawnIds=[1506], arg2=False)
            return 랜덤G()


class 랜덤G(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_interact_object(triggerIds=[10001332], state=1)
            return 랜덤H()
        if random_condition(rate=50):
            create_monster(spawnIds=[1507], arg2=False)
            return 랜덤H()


class 랜덤H(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_interact_object(triggerIds=[10001333], state=1)
            return 스폰1()
        if random_condition(rate=50):
            create_monster(spawnIds=[1508], arg2=False)
            return 스폰1()


class 스폰1(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021], isAutoTargeting=False, score=100)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[112]):
            return 스폰2()


class 스폰2(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038], isAutoTargeting=False, score=100)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[113]):
            return 스폰3()


class 스폰3(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061], isAutoTargeting=False, score=100)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[114]):
            return 스폰4()


class 스폰4(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083], isAutoTargeting=False, score=100)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


