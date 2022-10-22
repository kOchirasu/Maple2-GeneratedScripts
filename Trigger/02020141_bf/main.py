""" trigger/02020141_bf/main.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 기본셋팅()


class 기본셋팅(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # 나가기 포탈 최초에는 감추기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 보스등장준비()
        if wait_tick(waitTick=2000):
            return 보스등장준비()


class 보스등장준비(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[99], arg2=False) # EventSpawnPointNPC 의 SpawnPointID가 99 번, 즉   arg1="99"

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1100):
            return 클리어성공유무체크시작()
        if dungeon_time_out():
            return 던전실패()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패()


class 클리어성공유무체크시작(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 연출딜레이()
        if dungeon_time_out():
            return 던전실패()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패()


class 던전실패(state.State):
    def on_enter(self):
        dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        dungeon_close_timer()
        destroy_monster(spawnIds=[-1])
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True) # 메인 전투판에 나가기 포탈 생성하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            dungeon_fail()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_enable_give_up(isEnable='0')


class 연출딜레이(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23090000) # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기, 던전 클리어 미션 달성임
        set_achievement(type='trigger', achieve='TurkaDungeonClear') # achieve.xlsx 트로피 투르카던전클리어 조건 체크, arg1을 넣지 않으면 이 맵 전체에 있는 플레이어를 체크함 , 참고로 arg1을 넣으면 트리거 박스 안에 있는 플레이어만 체크하는 것임

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        dungeon_set_end_time() # 보스 죽음과 동시에 자체 60초 늘어나기 때문에,  <state name="연출딜레이"> 단계 끝나고 WaitTick=9초 후에 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        dungeon_close_timer()
        dungeon_clear()
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True) # 메인 전투판에 나가기 포탈 생성하기


