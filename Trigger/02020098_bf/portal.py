""" trigger/02020098_bf/portal.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False) # 졸구간 전투판에 있는 던전 나가기 포탈 최초에 감추기
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False) # 1페이지 전투판에 있는 던전 나가기 포탈 최초에 감추기
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False) # 2페이지 7시 전투판에 있는 던전 나가기 포탈 최초에 감추기
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False) # 2페이지 5시 전투판에 있는 던전 나가기 포탈 최초에 감추기
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False) # 2페이지 12시 전투판에 있는 던전 나가기 포탈 최초에 감추기
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False) # 3페이지 마지막 전투판에 있는 던전 나가기 포탈 최초에 감추기
        set_user_value(key='BossOnePhaseEnd', value=0) # 변수 초기화, 보스AI로 부터 이 변수 1 신호를 받으면 이 트리거 작동시켜 1페이지 순간이동 포탈 Off 상태로 만들기
        set_portal(portalId=40, visible=True, enabled=True, minimapVisible=True) # 1페이지의 왼쪽 순간이동 포탈 최초에 On 설정 하기
        set_portal(portalId=50, visible=True, enabled=True, minimapVisible=True) # 1페이지의 오른쪽 순간이동 포탈 최초에 On 설정 하기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10]):
            return 포탈체크시작()


class 포탈체크시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 포탈체크대기중()


class 포탈체크대기중(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BossOnePhaseEnd', value=1): # 인페르녹 보스가 죽으면 BossDead =  1, 신호를 보내서 전투 끝났음을 알림
            return 순간이동포탈OFF()
        if user_value(key='BossDead', value=1):
            return 나가기포탈생성잠시대기()
        """
        중요: 보스 죽음 체크를 <condition name="몬스터가죽어있으면" arg1="98">   <condition name="몬스터가죽어있으면" arg1="99"> 방식을 사용하지 않는 이유는 
                이 맵은 한맵에 2개 난이도가 존재하는데, 만약 스폰포인트 99로 보스가 등장할 하여 트리거가 이 단계에 오면 98 스폰 포인트의 보스가 죽은 것으로 처리해 버리기 때문에 
                 보스AI에서 죽을때 변수 신호 보내는 방식을 사용하였음
        """


class 순간이동포탈OFF(state.State):
    def on_enter(self):
        set_portal(portalId=40, visible=False, enabled=False, minimapVisible=False) # 1페이지의 왼쪽 순간이동 포탈 Off 설정 하기
        set_portal(portalId=50, visible=False, enabled=False, minimapVisible=False) # 1페이지의 오른쪽 순간이동 포탈 Off 설정 하기
        set_user_value(key='BossOnePhaseEnd', value=0) # 변수 초기화, 이거 안하면 무한루프에 빠짐

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 포탈체크대기중()


class 나가기포탈생성잠시대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9500):
            return 나가기포탈생성()


class 나가기포탈생성(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='PhasePortar', value=0):
            return 졸구간만포탈생성()
        if user_value(key='PhasePortar', value=1):
            return 페이지전투판포탈생성1()
        if user_value(key='PhasePortar', value=2):
            return 페이지전투판포탈생성2()
        if user_value(key='PhasePortar', value=3):
            return 페이지전투판포탈생성3()


class 졸구간만포탈생성(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트리거종료()


class 페이지전투판포탈생성1(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 1페이지 전투판에서 나가기 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트리거종료()


class 페이지전투판포탈생성2(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 2페이지 7시 전투판에서 나가기 포탈
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 2페이지 5시 전투판에서 나가기 포탈
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 2페이지 12시 전투판에서 나가기 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트리거종료()


class 페이지전투판포탈생성3(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 마지막 전투판에서 나가기 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트리거종료()


class 트리거종료(state.State):
    pass


