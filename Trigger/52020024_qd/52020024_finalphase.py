""" trigger/52020024_qd/52020024_finalphase.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FinalPhase', value=1):
            return 스폰(self.ctx)


class 스폰(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[131,132,133,134,135,136], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=20000):
            return 스폰(self.ctx)
        if self.monster_dead(boxIds=[131,132,133,134,135,136]):
            return 스폰(self.ctx)
        if self.user_value(key='FinalPhase', value=2):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
