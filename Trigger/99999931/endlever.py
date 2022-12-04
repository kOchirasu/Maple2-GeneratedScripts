""" trigger/99999931/endlever.xml """
import trigger_api


class 게임종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[211,212], visible=True) # 닫힌 문이 보인다 (arg2=1)
        self.set_mesh(triggerIds=[551,552], visible=False) # 열린 문을 가린다 (arg2=0)
        self.set_interact_object(triggerIds=[10000216], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000216], stateValue=0):
            return 종료안내(self.ctx)


class 종료안내(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)
        self.set_event_ui(type=5, arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 문열기(self.ctx)


class 문열기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=7)
        self.set_mesh(triggerIds=[211,212], visible=False) # 닫힌 문을 가린다
        self.set_mesh(triggerIds=[551,552], visible=True) # 열린 문을 보인다

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 문닫기(self.ctx)


class 문닫기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_mesh(triggerIds=[211,212], visible=True) # 닫힌 문을 가린다
        self.set_mesh(triggerIds=[551,552], visible=False) # 열린 문을 보인다
        self.set_mesh(triggerIds=[201,202,203,204,205,206,207,208], visible=True) # 순간 이동 발판이 보인다 (arg2=1)
        self.set_portal(portalId=101, visible=False, enable=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portalId=102, visible=False, enable=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portalId=103, visible=False, enable=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portalId=104, visible=False, enable=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portalId=115, visible=False, enable=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portalId=116, visible=False, enable=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portalId=117, visible=False, enable=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portalId=118, visible=False, enable=True) # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 게임종료(self.ctx)


initial_state = 게임종료
