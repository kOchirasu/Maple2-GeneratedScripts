""" trigger/02000213_bf/spawncheck.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1099]):
            return 잡몹소멸()


class 잡몹소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001])
        destroy_monster(spawnIds=[1002])
        destroy_monster(spawnIds=[1003])
        destroy_monster(spawnIds=[1004])
        destroy_monster(spawnIds=[1005])
        destroy_monster(spawnIds=[1006])
        destroy_monster(spawnIds=[1007])
        destroy_monster(spawnIds=[1008])
        destroy_monster(spawnIds=[1009])
        destroy_monster(spawnIds=[1010])
        destroy_monster(spawnIds=[1011])
        destroy_monster(spawnIds=[1012])
        destroy_monster(spawnIds=[1013])
        destroy_monster(spawnIds=[1014])
        destroy_monster(spawnIds=[1015])
        destroy_monster(spawnIds=[1016])
        destroy_monster(spawnIds=[1017])
        destroy_monster(spawnIds=[1018])
        destroy_monster(spawnIds=[1019])
        destroy_monster(spawnIds=[1020])
        destroy_monster(spawnIds=[1021])
        destroy_monster(spawnIds=[1022])
        destroy_monster(spawnIds=[1023])
        destroy_monster(spawnIds=[1024])
        destroy_monster(spawnIds=[1025])
        destroy_monster(spawnIds=[1026])
        destroy_monster(spawnIds=[1027])
        destroy_monster(spawnIds=[1028])
        destroy_monster(spawnIds=[1029])
        destroy_monster(spawnIds=[1030])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1099]):
            return 대기()


