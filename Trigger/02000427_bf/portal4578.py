""" trigger/02000427_bf/portal4578.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 4시방향 태엽폭탄 있는 곳의 순간이동 포탈 초기화 하기, 최초에는 모습을 안보임
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)
        # 4시방향 태엽폭탄 있는 곳의 순간이동 포탈 초기화 하기, 최초에는 모습을 안보임
        self.set_portal(portalId=5, visible=False, enable=False, minimapVisible=False)
        # 7시방향 태엽폭탄 있는 곳의 순간이동 포탈 초기화 하기, 최초에는 모습을 안보임
        self.set_portal(portalId=7, visible=False, enable=False, minimapVisible=False)
        # 8시방향 태엽폭탄 있는 곳의 순간이동 포탈 초기화 하기, 최초에는 모습을 안보임
        self.set_portal(portalId=8, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ThirdPhase', value=1):
            # 2페이즈 전투 다 끝나고, ThirdPhase = 1 신호를 받을때까지 여기서 대기, 즉 AI_Papulatus_CN.xml 에서 신호보냄
            return 순간이동포탈생성(self.ctx)


class 순간이동포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 4시방향 태엽폭탄 있는 곳에 순간이동 포탈 등장시킴
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)
        # 4시방향 태엽폭탄 있는 곳에 순간이동 포탈 등장시킴
        self.set_portal(portalId=5, visible=True, enable=True, minimapVisible=True)
        # 7시방향 태엽폭탄 있는 곳에 순간이동 포탈 등장시킴
        self.set_portal(portalId=7, visible=True, enable=True, minimapVisible=True)
        # 8시방향 태엽폭탄 있는 곳에 순간이동 포탈 등장시킴
        self.set_portal(portalId=8, visible=True, enable=True, minimapVisible=True)
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
