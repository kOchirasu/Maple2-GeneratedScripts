""" trigger/02000207_bf/lavaflow.xml """
from common import *
import state


#  현재 이거 사용 안함, 만약을 위해 남겨두었음, 이 부분은  999102_Lavaflow.xml   999108_Lavaflow.xml    999109_Lavaflow.xml   3개 xml 파일로 나누어서 분할 설정 했음 
class 전투체크(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2001]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='LavaflowHigh', value=1):
            return 칸분기3()
        if user_value(key='LavaflowLow', value=1):
            return 칸분기2()
        if user_value(key='LavaflowLeft', value=1):
            return 왼쪽용암생성()
        if user_value(key='LavaflowRight', value=1):
            return 오른쪽용암생성()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


class 칸분기3(state.State):
    def on_enter(self):
        set_user_value(triggerId=999102, key='LavaflowHigh', value=0)
        set_effect(triggerIds=[600], visible=True)
        create_monster(spawnIds=[1001], arg2=False)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A') # MS2PatrolData_1001A  이것이 용암 2층까지 올라오게 하는 설정값

    def on_tick(self) -> state.State:
        if random_condition(rate=52):
            return 칸이동3()
        if random_condition(rate=48):
            return 리턴()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


class 칸이동3(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=28000):
            return 리턴()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


class 칸분기2(state.State):
    def on_enter(self):
        set_user_value(triggerId=999102, key='LavaflowLow', value=0)
        set_effect(triggerIds=[600], visible=True)
        create_monster(spawnIds=[1001], arg2=False)
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A') # MS2PatrolData_1001B  이것이 용암 1층까지 올라오게 하는 설정값

    def on_tick(self) -> state.State:
        if random_condition(rate=99):
            return 칸이동2()
        if random_condition(rate=1):
            return 리턴()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


class 칸이동2(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 리턴()
        if user_value(key='BattleEnd2', value=1):
            return 종료()


class 리턴(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            destroy_monster(spawnIds=[1001])
            return 대기()


# 왼쪽담당 계약의 토템을 소환하면서 자쿰몸체한테 신호 받아 용암 올라오는 경우임
class 왼쪽용암생성(state.State):
    def on_enter(self):
        set_user_value(triggerId=999102, key='LavaflowLeft', value=0) # LavaflowLeft 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        set_user_value(triggerId=999102, key='LavaflowLeftStop', value=0) # ### 올라온 용암 내려가게 할 때 사용하는 LavaflowLeftStop 변수 이전에 이미 사용했을 수 있으므로 여기서  0으로 꼭 초기화 해야함
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
        set_user_value(triggerId=999102, key='LavaflowLeft', value=0) # ### 왼쪽용암내려가기  신호받는 대기 상태에서 이 변수가 1이 되는 상황이 생길수도 있기 때문에 만약을 대비해 여기서도 다시한번 0으로 초기화 함
        set_user_value(triggerId=999102, key='LavaflowLeftStop', value=0) # LavaflowLeftStop 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            destroy_monster(spawnIds=[1002])
            return 대기()


# 오른쪽담당 계약의 토템을 소환하면서 자쿰몸체한테 신호 받아 용암 올라오는 경우임
class 오른쪽용암생성(state.State):
    def on_enter(self):
        set_user_value(triggerId=999102, key='LavaflowRight', value=0) # LavaflowRight 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        set_user_value(triggerId=999102, key='LavaflowRightStop', value=0) # ### 올라온 용암 내려가게 할 때 사용하는 LavaflowRightStop 변수 이전에 이미 사용했을 수 있으므로 여기서  0으로 꼭 초기화 해야함
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
        set_user_value(triggerId=999102, key='LavaflowRight', value=0) # ### 오른쪽용암내려가기  신호받는 대기 상태에서 이 변수가 1이 되는 상황이 생길수도 있기 때문에 만약을 대비해 여기서도 다시한번 0으로 초기화 함
        set_user_value(triggerId=999102, key='LavaflowRightStop', value=0) # LavaflowRightStop 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            destroy_monster(spawnIds=[1003])
            return 대기()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001])
        destroy_monster(spawnIds=[1002])
        destroy_monster(spawnIds=[1003])


