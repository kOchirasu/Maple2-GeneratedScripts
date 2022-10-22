""" trigger/02000426_bf/999108_lavaflow.xml """
from common import *
import state


# 계약의 토템에 의해 왼쪽 지점에 용암파도 생성
class 전투체크(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='LavaflowLeft', value=1):
            return 왼쪽용암생성()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


# 왼쪽담당 계약의 토템을 소환하면서 자쿰몸체한테 신호 받아 용암 올라오는 경우임
class 왼쪽용암생성(state.State):
    def on_enter(self):
        set_user_value(triggerId=999108, key='LavaflowLeft', value=0) # LavaflowLeft 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        set_user_value(triggerId=999108, key='LavaflowLeftStop', value=0) # ### 올라온 용암 내려가게 할 때 사용하는 LavaflowLeftStop 변수 이전에 이미 사용했을 수 있으므로 여기서  0으로 꼭 초기화 해야함
        set_effect(triggerIds=[600], visible=True)
        create_monster(spawnIds=[1002], arg2=False)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002A')

    def on_tick(self) -> state.State:
        if user_value(key='LavaflowLeftStop', value=1): # 보스가 죽으면 보스 스폰시키는 트리거 xml 에서 BattleEnd2 = 1 신호를 보내서 올라와 있는 용암을 여기서 바로 제거 시키게 함
            return 왼쪽용암내려가기()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


class 왼쪽용암내려가기(state.State):
    def on_enter(self):
        set_user_value(triggerId=999108, key='LavaflowLeft', value=0) # ### 왼쪽용암내려가기  신호받는 대기 상태에서 이 변수가 1이 되는 상황이 생길수도 있기 때문에 만약을 대비해 여기서도 다시한번 0으로 초기화 함
        set_user_value(triggerId=999108, key='LavaflowLeftStop', value=0) # LavaflowLeftStop 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            destroy_monster(spawnIds=[1002])
            return 대기()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1002])

