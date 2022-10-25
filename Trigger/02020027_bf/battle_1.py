""" trigger/02020027_bf/battle_1.xml """
import common


class 전투시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return 전투시작_2(self.ctx)


class 전투시작_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='summon_1_1', value=1):
            return 몬스터소환(self.ctx)


class 몬스터소환(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301,302,303,304,305,306])
        self.set_event_ui(type=1, arg2='$02020027_BF__battle_1__0$', arg3='4000')
        self.set_conversation(type=1, spawnId=301, script='$02020027_BF__battle_1__1$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=303, script='$02020027_BF__battle_1__2$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=305, script='$02020027_BF__battle_1__3$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[301,302,303,304,305,306]):
            return 버프(self.ctx)


class 버프(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[201], skillId=62000002, level=1, isPlayer=True)
        self.add_buff(boxIds=[201], skillId=51200002, level=1, isPlayer=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return None


initial_state = 전투시작
