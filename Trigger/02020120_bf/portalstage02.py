""" trigger/02020120_bf/portalstage02.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 순간이동 포탈 처음에 감추기
        # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        self.set_user_value(key='DungeonReset', value=0)
        # 어느지점 포탈을 활성화 시킬지 결정하는데 사용하는 변수
        self.set_user_value(key='Stage02', value=0)
        self.set_portal(portal_id=2101, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=2201, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=2301, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3101, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3102, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3103, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3104, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3201, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3202, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3203, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3301, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3302, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3303, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3304, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3305, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=3306, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=4101, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=4102, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=4201, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=4202, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=4301, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=4302, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5101, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5102, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5201, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5202, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5203, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5204, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5205, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5206, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5301, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5302, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5303, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5304, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=5401, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=6101, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=6201, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=6301, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=6302, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=6303, visible=False, enable=False, minimap_visible=False)
        self.set_portal(portal_id=6304, visible=False, enable=False, minimap_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 스테이지2_시작(self.ctx)


class 스테이지2_시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Stage02') >= 11:
            return 스테이지2_왼쪽진행(self.ctx)
        if self.user_value(key='Stage02') >= 21:
            return 스테이지2_가운데진행(self.ctx)
        if self.user_value(key='Stage02') >= 31:
            return 스테이지2_오른쪽진행(self.ctx)


class 스테이지2_왼쪽진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2101, visible=True, enable=True, minimap_visible=True) # 2스테이지로 가는 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지2_가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2201, visible=True, enable=True, minimap_visible=True) # 2스테이지로 가는 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지2_오른쪽진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2301, visible=True, enable=True, minimap_visible=True) # 2스테이지로 가는 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 혹시모를_던전리셋신호_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonReset') >= 1:
            return Ready(self.ctx)


initial_state = Ready
