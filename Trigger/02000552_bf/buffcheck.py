""" trigger/02000552_bf/buffcheck.xml """
from common import *
import state


#  TriggerModelID =  553 
class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 기본셋팅()


class 기본셋팅(state.State):
    def on_enter(self):
        set_user_value(key='MonsterMany', value=0) # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함, 몬스터 등장 이전에 이 변수 0 초기화 하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 트리거작동시작()


class 트리거작동시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MonsterMany', value=1, operator='GreaterEqual'):
            return 블랙빈에게버프부여()


class 블랙빈에게버프부여(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=50003307, level=2, arg4=True) # 공격반사 버프 부여하기 ,   arg1="101" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨
        add_buff(boxIds=[102], skillId=50003307, level=2, arg4=True) # 공격반사 버프 부여하기 ,   arg1="102" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 블랙빈에게버프삭제체크()


class 블랙빈에게버프삭제체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MonsterMany', value=0):
            return 블랙빈에게버프삭제대기()


class 블랙빈에게버프삭제대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return 블랙빈에게버프삭제실시()


class 블랙빈에게버프삭제실시(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=50003309, level=1, arg4=True) # 공격반사 버프 버프 제거 ,   arg1="101" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨
        add_buff(boxIds=[102], skillId=50003309, level=1, arg4=True) # 공격반사 버프 버프 제거 ,   arg1="102" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 트리거작동시작()


