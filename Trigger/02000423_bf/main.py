""" trigger/02000423_bf/main.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 기본셋팅시작(self.ctx)


class 기본셋팅시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        # 100번 MS2RegionSpawn 에서 등장한 몬스터가 101번 트리거영역에 감지 되었으면
        if self.user_value(key='PortalHidden', value=1):
            return 보스사냥후포탈생성(self.ctx)
        # 100번 MS2RegionSpawn 에서 등장한 몬스터가 101번 트리거영역에 없으면
        if self.npc_detected(boxId=101, spawnIds=[100]):
            return 포탈감추기(self.ctx)
        if not self.npc_detected(boxId=101, spawnIds=[100]):
            return 디폴트포탈생성(self.ctx)


class 디폴트포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 머쉬킹이 없을 때는 편한 빠른 이동을 위해 존재하는 순간이동 포탈을 생성시킴
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=6, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=7, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=8, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=9, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=12, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=14, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 포탈다시체크대기(self.ctx)


class 보스사냥후포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 머쉬킹이 없을 때는 편한 빠른 이동을 위해 존재하는 순간이동 포탈을 생성시킴
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=6, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=7, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=8, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=9, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=12, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=14, visible=True, enable=True, minimapVisible=True)
        # PortalHidden 변수 0으로 초기하 하여 무한루프 도는 상황을 방지
        self.set_user_value(key='PortalHidden', value=0)
        # 포탈이 생성되었고, 머쉬킹이 등장하면 곧 사라진다는 메시지를 보여줌
        self.show_guide_summary(entityId=20043001, textId=20043001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # 메시지 6초 뒤에 제거해야 하기 때문에 어쩔수 없이 "포탈다시체크대기이전" 스테이트를 더 끼워 넣음
            return 포탈다시체크대기이전(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20043001)


class 포탈감추기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 머쉬킹 보스와 전투를 하게 되면 순간이동 포탈 감추기
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=7, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=8, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=9, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=14, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 포탈다시체크대기(self.ctx)


class 포탈다시체크대기이전(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return 시작대기중(self.ctx)


class 포탈다시체크대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
