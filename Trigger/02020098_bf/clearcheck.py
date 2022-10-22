""" trigger/02020098_bf/clearcheck.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10]):
            return 클리어성공유무체크시작()


class 클리어성공유무체크시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BossDead', value=1):
            return 연출딜레이()
        """
        중요: 보스 죽음 체크를 <condition name="몬스터가죽어있으면" arg1="98">   <condition name="몬스터가죽어있으면" arg1="99"> 방식을 사용하지 않는 이유는 
                이 맵은 한맵에 2개 난이도가 존재하는데, 만약 스폰포인트 99로 보스가 등장할 하여 트리거가 이 단계에 오면 98 스폰 포인트의 보스가 죽은 것으로 처리해 버리기 때문에 
                 보스AI에서 죽을때 변수 신호 보내는 방식을 사용하였음
        """
        if dungeon_time_out():
            return 던전실패()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패()


class 연출딜레이(state.State):
    def on_enter(self):
        set_achievement(achieve='BalrogMagicBursterKritiasClear') # arg3="BalrogMagicBursterKritiasClear" 는 퀘스트와 트로피 업적 당설 완료 조건 처리 키값임, arg1="??" arg2="trigger" 은 해당 트리거 안에 만 있으면 클리어 처리 할때 사용하는 것인데, 이거 생략하면 맵 안에만 있으면 무조건 퀘스트와 트로피 업적을 완료 처리함
        dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        dungeon_close_timer()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        dungeon_clear()
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311], visible=False, arg3=0, arg4=0, arg5=0) # 스타트포인트 지점의 칸막이 트리거메쉬 제거하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 종료()


class 던전실패(state.State):
    def on_enter(self):
        dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        dungeon_close_timer()
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311], visible=False, arg3=0, arg4=0, arg5=0) # 스타트포인트 지점의 칸막이 트리거메쉬 제거하기
        destroy_monster(spawnIds=[-1]) # 모든 구간에 나가기 포탈 생성하기
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 1페이지 전투판에서 나가기 포탈
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 2페이지 7시 전투판에서 나가기 포탈
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 2페이지 5시 전투판에서 나가기 포탈
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 2페이지 12시 전투판에서 나가기 포탈
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 마지막 전투판에서 나가기 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            dungeon_fail()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_enable_give_up(isEnable='0')


