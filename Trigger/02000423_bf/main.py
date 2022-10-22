""" trigger/02000423_bf/main.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 기본셋팅시작()


class 기본셋팅시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='PortalHidden', value=1): # 100번 MS2RegionSpawn 에서 등장한 몬스터가 101번 트리거영역에 감지 되었으면
            return 보스사냥후포탈생성()
        if npc_detected(boxId=101, spawnIds=[100]): # 100번 MS2RegionSpawn 에서 등장한 몬스터가 101번 트리거영역에 없으면
            return 포탈감추기()
        if not npc_detected(boxId=101, spawnIds=[100]):
            return 디폴트포탈생성()


class 디폴트포탈생성(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=9, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=12, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=14, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 포탈다시체크대기()


class 보스사냥후포탈생성(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=9, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=12, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=14, visible=True, enabled=True, minimapVisible=True)
        set_user_value(key='PortalHidden', value=0) # PortalHidden 변수 0으로 초기하 하여 무한루프 도는 상황을 방지
        show_guide_summary(entityId=20043001, textId=20043001) # 포탈이 생성되었고, 머쉬킹이 등장하면 곧 사라진다는 메시지를 보여줌

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 포탈다시체크대기이전()

    def on_exit(self):
        hide_guide_summary(entityId=20043001)


class 포탈감추기(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=9, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=14, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if true():
            return 포탈다시체크대기()


class 포탈다시체크대기이전(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 시작대기중()


class 포탈다시체크대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 시작대기중()


