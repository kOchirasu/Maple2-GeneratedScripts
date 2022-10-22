""" trigger/99999926/main.xml """
from common import *
import state


class DungeonStart(state.DungeonStart):
    pass

state.DungeonStart = DungeonStart


class Battle01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[421,422,423,424,425], arg2=False) # action name="스킬을설정한다" arg1="501" arg2="1" /

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[421,422,423,424,425]):
            return Battle02()


class Battle02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[411,412,413,414,415], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[411,412,413,414,415]):
            return Battle03Random()


class Battle03Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return Battle03A()
        if random_condition(rate=25):
            return Battle03B()


class Battle03A(state.State):
    def on_enter(self):
        create_monster(spawnIds=[421,422,423,424,425], arg2=False)
        create_monster(spawnIds=[441], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[421,422,423,424,425]):
            return MevidicCinematic()


class Battle03B(state.State):
    def on_enter(self):
        create_monster(spawnIds=[411,412,413,414,415], arg2=False)
        create_monster(spawnIds=[441], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[411,412,413,414,415]):
            return MevidicCinematic()


class MevidicCinematic(state.State):
    def on_enter(self):
        create_monster(spawnIds=[451], arg2=False)
        move_npc(spawnId=451, patrolName='MS2PatrolData_701')

    def on_tick(self) -> state.State:
        if count_users(boxId=402, boxId=1):
            return None # Missing State: LoadingStart


