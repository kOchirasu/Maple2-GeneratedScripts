""" trigger/02000543_bf/mob_1_1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WaveStart', value=1):
            return 생성(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[101,102], animationEffect=True)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 생성(self.ctx)
        if self.user_value(key='WaveEnd', value=1):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
