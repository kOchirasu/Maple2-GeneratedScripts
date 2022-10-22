""" trigger/02020147_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 기본셋팅()


class 기본셋팅(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # 던전맵 나가는 포탈, 시작 지점에 위치
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False) # 던전맵 나가는 포탈, 전투판에 위치
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False) # 시작지점에서 전투판으로 가기위한 포탈

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[601]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[701,702,703], arg2=False) # 이슈라 렌듀비아 유페리아  등장

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 클리어체크시작()


class 클리어체크시작(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True) # 시작지점에서 전투판으로 가기위한 포탈

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[701,702,703]):
            return 종료딜레이()


class 종료딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_achievement(achieve='IshuraFinalDungeonClear_Quest')
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True) # 던전맵 나가는 포탈, 시작 지점에 위치
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 던전맵 나가는 포탈, 전투판에 위치


