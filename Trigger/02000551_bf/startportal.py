""" trigger/02000551_bf/startportal.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 기본셋팅()


class 기본셋팅(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False) # 최초 입구에 있는 전투판으로 가는  포탈 최초에는 감추기
        set_effect(triggerIds=[8101,8102,8103,8104,8105], visible=False) # 최초 시작 지점에 나오는 화살표 표시 끄기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 포탈활성화()


class 포탈활성화(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True) # 최초 입구에 있는 전투판으로 가는  포탈 활성화
        dungeon_enable_give_up(isEnable='1')
        set_event_ui(type=1, arg2='$02020140_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if dungeon_time_out():
            return 던전실패종료()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패종료()
        if wait_tick(waitTick=30000):
            return 포탈감추기()


class 포탈감추기(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False) # 전투판으로 가는  포탈  감추기

    def on_tick(self) -> state.State:
        if dungeon_time_out():
            return 던전실패종료()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패종료()


class 던전실패종료(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True) # 최초 입구에 있는 전투판으로 가는  포탈 활성화


