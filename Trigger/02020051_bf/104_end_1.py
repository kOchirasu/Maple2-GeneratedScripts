""" trigger/02020051_bf/104_end_1.xml """
import common


class 사망조건(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='End', value=1):
            return 준비(self.ctx)


class 준비(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=103, key='Main', value=2)
        self.set_user_value(triggerId=107, key='Text', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 준비_2(self.ctx)


class 준비_2(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', script='$02020051_BF__104_END_1__0$', duration=5684, voice='ko/Npc/00002201')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 몬스터사망_1(self.ctx)


class 몬스터사망_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.any_one():
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=102, key='Timmer', value=3)
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료_2(self.ctx)


class 종료_2(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=103, key='Main', value=2)
        self.set_user_value(triggerId=102, key='Timmer', value=2)
        self.set_user_value(triggerId=102, key='Timmer', value=3)
        self.set_user_value(triggerId=101, key='Potion', value=2)
        self.set_user_value(triggerId=105, key='Summon_monster', value=2)
        self.set_user_value(triggerId=106, key='Summon_monster_2', value=2)
        self.set_user_value(triggerId=107, key='Text', value=2)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='End', value=2):
            return 사망조건(self.ctx)


initial_state = 사망조건
