""" trigger/52010038_qd/mob_1_1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WaveStart', value=1):
            return 생성(self.ctx)

    def on_exit(self) -> None:
        # 최초 3마리
        self.spawn_npc_range(rangeIds=[2001,2002,2003,2004], isAutoTargeting=True)
        self.spawn_npc_range(rangeIds=[2001,2002,2003,2004], isAutoTargeting=True)
        self.spawn_npc_range(rangeIds=[2001,2002,2003,2004], isAutoTargeting=True)
        self.create_monster(spawnIds=[2011], animationEffect=True)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2011], animationEffect=True)
        self.spawn_npc_range(rangeIds=[2001,2002,2003,2004], isAutoTargeting=True, randomPickCount=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 생성(self.ctx)
        if self.user_value(key='WaveSlowDown', value=1):
            return 생성2(self.ctx)
        if self.user_value(key='WaveEnd', value=1):
            return 종료(self.ctx)


class 생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2011], animationEffect=True)
        self.spawn_npc_range(rangeIds=[2001,2002,2003,2004], isAutoTargeting=True, randomPickCount=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=14000):
            return 생성2(self.ctx)
        if self.user_value(key='WaveEnd', value=1):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
