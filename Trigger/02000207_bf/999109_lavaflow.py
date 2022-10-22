""" trigger/02000207_bf/999109_lavaflow.xml """
from common import *
import state


# 계약의 토템에 의해 오른쪽 지점에 용암파도 생성
class 전투체크(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2001]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='LavaflowRight', value=1):
            return 오른쪽용암생성()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


# 오른쪽담당 계약의 토템을 소환하면서 자쿰몸체한테 신호 받아 용암 올라오는 경우임
class 오른쪽용암생성(state.State):
    def on_enter(self):
        set_user_value(triggerId=999109, key='LavaflowRight', value=0) # LavaflowRight 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        set_user_value(triggerId=999109, key='LavaflowRightStop', value=0) # ### 올라온 용암 내려가게 할 때 사용하는 LavaflowRightStop 변수 이전에 이미 사용했을 수 있으므로 여기서  0으로 꼭 초기화 해야함
        set_effect(triggerIds=[600], visible=True)
        create_monster(spawnIds=[1003], arg2=False)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003A')

    def on_tick(self) -> state.State:
        if user_value(key='LavaflowRightStop', value=1): # 보스가 죽으면 보스 스폰시키는 트리거 xml 에서 BattleEnd2 = 1 신호를 보내서 올라와 있는 용암을 여기서 바로 제거 시키게 함
            return 오른쪽용암내려가기()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


class 오른쪽용암내려가기(state.State):
    def on_enter(self):
        set_user_value(triggerId=999109, key='LavaflowRight', value=0) # ### 오른쪽용암내려가기  신호받는 대기 상태에서 이 변수가 1이 되는 상황이 생길수도 있기 때문에 만약을 대비해 여기서도 다시한번 0으로 초기화 함
        set_user_value(triggerId=999109, key='LavaflowRightStop', value=0) # LavaflowRightStop 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            destroy_monster(spawnIds=[1003])
            return 대기()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1003])


