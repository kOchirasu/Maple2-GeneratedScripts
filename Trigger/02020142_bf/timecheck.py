""" trigger/02020142_bf/timecheck.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 던전시간체크()


class 던전시간체크(state.State):
    def on_enter(self):
        set_portal(portalId=41, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=42, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=43, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=44, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=45, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=46, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=47, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=48, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=49, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if dungeon_time_out():
            return 던전실패()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패()


class 던전실패(state.State):
    def on_enter(self):
        dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        dungeon_close_timer()
        destroy_monster(spawnIds=[-1]) # 던전 Fail 처리, 던전 나가기 포탈 생성하기
        set_portal(portalId=41, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=42, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=43, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=44, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=45, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=46, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=47, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=48, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=49, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            dungeon_fail()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_enable_give_up(isEnable='0')


