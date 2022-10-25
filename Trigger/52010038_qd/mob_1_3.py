""" trigger/52010038_qd/mob_1_3.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='bombStart', value=1):
            return 생성(self.ctx)


class 생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2097], animationEffect=False)
        self.spawn_npc_range(rangeIds=[2008,2009,2010], isAutoTargeting=True)
        self.spawn_npc_range(rangeIds=[2101,2102,2103,2104,2105,2106,2107], isAutoTargeting=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2097]):
            self.set_user_value(triggerId=999001, key='CoreIsDead', value=1)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
