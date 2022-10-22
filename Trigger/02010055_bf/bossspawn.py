""" trigger/02010055_bf/bossspawn.xml """
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
            return 룸체크()


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 난이도체크()
        if not is_dungeon_room():
            return 퀘스트던전()


class 난이도체크(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True) # 포탈ID 1: 던전 입구에 있는 나가기 포탈 작동 활성화

    def on_tick(self) -> state.State:
        if dungeon_level(level=2):
            return 레이드()
        if dungeon_level(level=3):
            return 카오스레이드()


class 퀘스트던전(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=70000118, level=1, arg4=False, arg5=False)
        create_monster(spawnIds=[2299], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2299]):
            return 종료딜레이()


class 레이드(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2099], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099]):
            return 종료딜레이()


class 카오스레이드(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2199], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2199]):
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


