""" trigger/02020027_bf/battle_4.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 전투시작_2(self.ctx)


class 전투시작_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='summon_2_2', value=1):
            return 몬스터소환(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[401,402,403,404,405,406])
        self.set_conversation(type=1, spawnId=401, script='$02020027_BF__battle_1__1$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=403, script='$02020027_BF__battle_1__2$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=405, script='$02020027_BF__battle_1__3$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[401,402,403,404,405,406]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[201], skillId=62000002, level=1, isPlayer=True)
        self.add_buff(boxIds=[201], skillId=51200002, level=1, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return None


initial_state = 전투시작
