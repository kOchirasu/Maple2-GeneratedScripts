""" trigger/99999926/main.xml """
import common


class DungeonStart(common.Trigger):
    pass


class Battle01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[421,422,423,424,425], animationEffect=False)
        # action name="스킬을설정한다" arg1="501" arg2="1" /

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[421,422,423,424,425]):
            return Battle02(self.ctx)


class Battle02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[411,412,413,414,415], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[411,412,413,414,415]):
            return Battle03Random(self.ctx)


class Battle03Random(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=25):
            return Battle03A(self.ctx)
        if self.random_condition(rate=25):
            return Battle03B(self.ctx)


class Battle03A(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[421,422,423,424,425], animationEffect=False)
        self.create_monster(spawnIds=[441], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[421,422,423,424,425]):
            return MevidicCinematic(self.ctx)


class Battle03B(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[411,412,413,414,415], animationEffect=False)
        self.create_monster(spawnIds=[441], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[411,412,413,414,415]):
            return MevidicCinematic(self.ctx)


class MevidicCinematic(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[451], animationEffect=False)
        self.move_npc(spawnId=451, patrolName='MS2PatrolData_701')

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=402, boxId=1):
            return None # Missing State: LoadingStart


initial_state = DungeonStart
