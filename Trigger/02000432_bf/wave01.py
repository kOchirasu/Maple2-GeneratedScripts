""" trigger/02000432_bf/wave01.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='wave01', value=1):
            return 소환(self.ctx)
        if self.user_value(key='EndDungeon', value=1):
            return 종료(self.ctx)


class 소환(common.Trigger):
    def on_enter(self):
        self.spawn_npc_range(rangeIds=[1901,1902,1903,1904,1905,1906,1907,1908,1909], isAutoTargeting=True, randomPickCount=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 대기(self.ctx)
        if self.user_value(key='EndDungeon', value=1):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
