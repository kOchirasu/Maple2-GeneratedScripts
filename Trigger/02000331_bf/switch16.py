""" trigger/02000331_bf/switch16.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000802], state=2) # 첫번째 다리 재생성레버 감춤
        self.set_effect(triggerIds=[4100], visible=False) # 아랫방향 화살표
        self.set_user_value(key='FirstBridgeOff', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 첫번째전투종료(self.ctx)


class 첫번째전투종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FirstBridgeOff', value=1):
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 유저재시작(self.ctx)


class 유저재시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 딜레이02(self.ctx)


class 딜레이02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이동안내(self.ctx)


class 이동안내(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_interact_object(triggerIds=[10000802], state=0) # 첫번째 다리 재생성레버 나타남
        self.set_interact_object(triggerIds=[10000802], state=1) # 첫번째 다리 재생성레버 활성화
        self.set_effect(triggerIds=[4100], visible=True) # 아랫방향 화살표

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 스위치켜기(self.ctx)


class 스위치켜기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000802]):
            return 다리재생성(self.ctx)


class 다리재생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016], visible=True, meshCount=16, arg4=100, delay=100) # 없어졌던 다리 재생성
        self.set_effect(triggerIds=[777701], visible=True) # 길 나타남01 사운드 / 첫 번째 다리
        self.set_mesh(triggerIds=[90000], visible=False, arg3=0, delay=0, scale=0) # 1st barrier OFF
        self.set_mesh(triggerIds=[90001], visible=False, arg3=0, delay=0, scale=0) # 2nd barrier OFF
        self.set_effect(triggerIds=[4100], visible=False) # 아랫방향 화살표

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
