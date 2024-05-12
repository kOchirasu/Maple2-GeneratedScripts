""" trigger/99999985_plantest_08/ia_105.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='환경음 테스트 트리거 입니다. 환경음을 켭니다. (HeavyRain)')
        self.set_sound(trigger_id=10001, enable=True)
        self.weather(weather_type='HeavyRain')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='환경음이 꺼집니다.')
        self.set_sound(trigger_id=10001, enable=False)
        self.weather(weather_type='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
