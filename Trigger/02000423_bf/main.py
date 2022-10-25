""" trigger/02000423_bf/main.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return 기본셋팅시작(self.ctx)


class 기본셋팅시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='PortalHidden', value=1): # 100번 MS2RegionSpawn 에서 등장한 몬스터가 101번 트리거영역에 감지 되었으면
            return 보스사냥후포탈생성(self.ctx)
        if self.npc_detected(boxId=101, spawnIds=[100]): # 100번 MS2RegionSpawn 에서 등장한 몬스터가 101번 트리거영역에 없으면
            return 포탈감추기(self.ctx)
        if not self.npc_detected(boxId=101, spawnIds=[100]):
            return 디폴트포탈생성(self.ctx)


class 디폴트포탈생성(common.Trigger):
    def on_enter(self):
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

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 포탈다시체크대기(self.ctx)


class 보스사냥후포탈생성(common.Trigger):
    def on_enter(self):
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
        self.set_user_value(key='PortalHidden', value=0) # PortalHidden 변수 0으로 초기하 하여 무한루프 도는 상황을 방지
        self.show_guide_summary(entityId=20043001, textId=20043001) # 포탈이 생성되었고, 머쉬킹이 등장하면 곧 사라진다는 메시지를 보여줌

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 포탈다시체크대기이전(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20043001)


class 포탈감추기(common.Trigger):
    def on_enter(self):
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

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 포탈다시체크대기(self.ctx)


class 포탈다시체크대기이전(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11000):
            return 시작대기중(self.ctx)


class 포탈다시체크대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
