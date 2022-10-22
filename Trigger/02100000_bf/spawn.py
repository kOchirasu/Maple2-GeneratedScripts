""" trigger/02100000_bf/spawn.xml """
from common import *
import state


class 소환(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MonsterSpawn', value=1):
            return 끝_1()

    def on_exit(self):
        create_monster(spawnIds=[81003], arg2=True)
        create_monster(spawnIds=[810031], arg2=True)
        create_monster(spawnIds=[810032], arg2=True)


class 끝_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[82001]):
            return None # Missing State: 성공

    def on_exit(self):
        destroy_monster(spawnIds=[-1])


