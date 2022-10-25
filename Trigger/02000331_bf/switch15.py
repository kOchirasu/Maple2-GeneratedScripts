""" trigger/02000331_bf/switch15.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000801], state=2) # 외다리 재생성레버 감춤
        self.set_effect(triggerIds=[4200], visible=False) # 아랫방향 화살표
        self.set_user_value(key='SecondBridgeOff', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[99993]):
            return 전투체크(self.ctx)


class 전투체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SecondBridgeOff', value=1):
            return 스위치준비(self.ctx)


class 스위치준비(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[777703], visible=False) # 길 나타남02 사운드 / 외다리
        self.set_effect(triggerIds=[777804], visible=False) # 길 없어짐02 사운드 /  외다리

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[99995]):
            return 스위치켜기(self.ctx)


class 스위치켜기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_interact_object(triggerIds=[10000801], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(triggerIds=[10000801], state=1) # 외다리 생성하는 레버01 나타남
        self.set_effect(triggerIds=[4200], visible=True) # 아랫방향 화살표

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000801]):
            return 외다리재생성(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[7775], visible=True) # 레버 작동 사운드


class 외다리재생성(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[90008], visible=False, arg3=0, delay=0, scale=0) # 9th barrier OFF
        self.set_random_mesh(triggerIds=[10040,10041,10042,10043,10044], visible=True, meshCount=5, arg4=100, delay=100)
        self.set_effect(triggerIds=[777703], visible=True) # 길 나타남02 사운드 / 외다리
        self.set_effect(triggerIds=[4200], visible=False) # 아랫방향 화살표

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[99992]):
            return 이동안내(self.ctx)


class 이동안내(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_mesh(triggerIds=[90008], visible=False, arg3=0, delay=0, scale=0) # 9th barrier OFF
        self.set_random_mesh(triggerIds=[10040,10041,10042,10043,10044], visible=True, meshCount=5, arg4=150, delay=150) # 3rd bridge ON

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
