""" trigger/02020061_bf/battle_2.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='ObjectClear', value=0)
        self.set_user_value(triggerId=99990004, key='ObjectStart', value=0)
        self.set_user_value(triggerId=99990005, key='ObjectStart', value=0)
        self.set_user_value(triggerId=99990006, key='ObjectStart', value=0)
        self.set_user_value(triggerId=99990007, key='ObjectStart', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ObjectPhase', value=1):
            return 오브젝트소환(self.ctx)


class 오브젝트소환(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[711,712,713,714], animationEffect=False)
        self.set_user_value(triggerId=99990004, key='ObjectStart', value=1)
        self.set_user_value(triggerId=99990005, key='ObjectStart', value=1)
        self.set_user_value(triggerId=99990006, key='ObjectStart', value=1)
        self.set_user_value(triggerId=99990007, key='ObjectStart', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ObjectPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[701]):
            return 오브젝트소환_클리어(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대사용_1(self.ctx)


class 대사용_1(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020061_BF__BATTLE_2__0$')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ObjectPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[701]):
            return 오브젝트소환_클리어(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대사용_2(self.ctx)


class 대사용_2(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020061_BF__BATTLE_2__1$')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ObjectPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[701]):
            return 오브젝트소환_클리어(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대사용_3(self.ctx)


class 대사용_3(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020061_BF__BATTLE_2__2$')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ObjectPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[701]):
            return 오브젝트소환_클리어(self.ctx)


class 오브젝트소환_클리어(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='ObjectClear', value=1)
        self.set_user_value(triggerId=99990004, key='ObjectStart', value=0)
        self.set_user_value(triggerId=99990005, key='ObjectStart', value=0)
        self.set_user_value(triggerId=99990006, key='ObjectStart', value=0)
        self.set_user_value(triggerId=99990007, key='ObjectStart', value=0)


initial_state = 대기
