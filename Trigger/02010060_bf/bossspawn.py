""" trigger/02010060_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # 포탈ID 1: 던전 입구에 있는 나가기 포탈 셋팅 초기화
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False) # 포탈ID 2: 3페이즈 전투 장소에 나가기 포탈 셋팅 초기화
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False) # 포탈ID 8: 1페이즈 전투 장소에 나가기 포탈 셋팅 초기화, 보스가 1페이즈에서 순삭 당할 수 있기 때문에 1페이즈 전투 장소에도 나가기 포탈 생성함
        set_portal(portalId=9, visible=False, enabled=False, minimapVisible=False) # 포탈ID 9: 2페이즈 전투 장소에 나가기 포탈 셋팅 초기화, 보스가 2페이즈에서 순삭 당할 수 있기 때문에 1페이즈 전투 장소에도 나가기 포탈 생성함

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 몬스터등장()


class 몬스터등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2099], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099]):
            return 종료딜레이()


class 종료딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=9, visible=True, enabled=True, minimapVisible=True)
            dungeon_clear()
            return 종료()


class 종료(state.State):
    pass


