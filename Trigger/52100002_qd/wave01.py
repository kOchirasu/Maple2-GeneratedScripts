""" trigger/52100002_qd/wave01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='wave01', value=1):
            return 소환(self.ctx)
        if self.user_value(key='EndDungeon', value=1):
            return 종료(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(rangeIds=[1901,1902,1903,1904,1905,1906,1907,1908,1909], isAutoTargeting=True, randomPickCount=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 대기(self.ctx)
        if self.user_value(key='EndDungeon', value=1):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
