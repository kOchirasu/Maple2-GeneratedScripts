""" trigger/02000420_bf/left201.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[201]):
            return 왼쪽지점견제(self.ctx)


class 왼쪽지점견제(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='LeftPositionCheck', value=1) # 플레이어가 왼쪽지점 태엽폭탄 있는 곳에 들어서면, 파풀라투스가 사용하는 이 변수를 1로 만들어서 파풀라투스가 왼쪽 태엽폭탄 지점 플레이어 견제하도록 함

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[201]):
            return 왼쪽지점견제풀기(self.ctx)


class 왼쪽지점견제풀기(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='LeftPositionCheck', value=0) # 플레이어가 왼쪽지점 태엽폭탄 있는 곳에 벗어나면 , 파풀라투스가 사용하는 이 변수를 0로 만들어 초기화 하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 시작(self.ctx)


initial_state = 시작
