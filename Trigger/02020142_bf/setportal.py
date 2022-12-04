""" trigger/02020142_bf/setportal.xml """
import trigger_api


class 전투체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 대기99(self.ctx)


class 대기99(trigger_api.Trigger):
    pass


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=118, visible=False, enable=False, minimapVisible=False) # 1스테이지에서 맨 왼쪽 지점으로 진행하는 포탈
        self.set_portal(portalId=128, visible=False, enable=False, minimapVisible=False) # 1스테이지에서 가운데 지점으로 진행하는 포탈
        self.set_portal(portalId=138, visible=False, enable=False, minimapVisible=False) # 1스테이지에서 맨 오른쪽 지점으로 진행하는 포탈
        self.set_portal(portalId=218, visible=False, enable=False, minimapVisible=False) # 맨 왼쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portalId=228, visible=False, enable=False, minimapVisible=False) # 가운데 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portalId=238, visible=False, enable=False, minimapVisible=False) # 맨 오른쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portalId=318, visible=False, enable=False, minimapVisible=False) # 맨 왼쪽 지점에서 보스 전투판으로 넘어가는 포탈
        self.set_portal(portalId=328, visible=False, enable=False, minimapVisible=False) # 가운데 지점에서 마지막 스테이지로 넘어가는 포탈
        self.set_portal(portalId=338, visible=False, enable=False, minimapVisible=False) # 맨 오른쪽 지점에서 보스 전투판으로 넘어가는 포탈
        self.set_portal(portalId=428, visible=False, enable=False, minimapVisible=False) # 가운데 지점 마지막 스테이지에서 보스 전투판으로 넘어가는 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return 포탈생성(self.ctx)
        if self.user_value(key='SetLight', value=1):
            return 포탈생성(self.ctx)


class 포탈생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=118, visible=True, enable=True, minimapVisible=True) # 1스테이지에서 맨 왼쪽 지점으로 진행하는 포탈
        self.set_portal(portalId=128, visible=True, enable=True, minimapVisible=True) # 1스테이지에서 가운데 지점으로 진행하는 포탈
        self.set_portal(portalId=138, visible=True, enable=True, minimapVisible=True) # 1스테이지에서 맨 오른쪽 지점으로 진행하는 포탈
        self.set_portal(portalId=218, visible=True, enable=True, minimapVisible=True) # 맨 왼쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portalId=228, visible=True, enable=True, minimapVisible=True) # 가운데 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portalId=238, visible=True, enable=True, minimapVisible=True) # 맨 오른쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portalId=318, visible=True, enable=True, minimapVisible=True) # 맨 왼쪽 지점에서 보스 전투판으로 넘어가는 포탈
        self.set_portal(portalId=328, visible=True, enable=True, minimapVisible=True) # 가운데 지점에서 마지막 스테이지로 넘어가는 포탈
        self.set_portal(portalId=338, visible=True, enable=True, minimapVisible=True) # 맨 오른쪽 지점에서 보스 전투판으로 넘어가는 포탈
        self.set_portal(portalId=428, visible=True, enable=True, minimapVisible=True) # 가운데 지점 마지막 스테이지에서 보스 전투판으로 넘어가는 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 전투체크
