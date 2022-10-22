""" trigger/02020130_bf/skilldebuff_1phase.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_user_value(key='SkillDebuffCheck_1Phase', value=0) # SkillDebuffCheck_1Phase 변수 0으로 초기 세팅, 보스가 저주디버프스킬 사용할 때 이 트리거에거 이 변수 1 신호를 보냄
        set_user_value(key='MonsterMany', value=0) # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함
        set_user_value(key='FirstBattleEnd', value=0) # FirstBattleEnd변수 0으로 초기 셋팅, 첫번째 전투판에서 전투가 끝나면 이 변수 1 신호를 보냄

    def on_tick(self) -> state.State:
        if count_users(boxId=601, boxId=1):
            return 보스의저주디버프사용신호대기()


class 보스의저주디버프사용신호대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SkillDebuffCheck_1Phase', value=1):
            return 소환몹활성화될때까지잠시기다리기()
        if user_value(key='FirstBattleEnd', value=1):
            return 폭발저주디버프제거잠시대기()
        if user_value(key='FirstBattleEnd', value=99):
            return 폭발저주디버프제거하고종료()


class 소환몹활성화될때까지잠시기다리기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5200):
            return 소환몹전멸할때까지대기()


class 소환몹전멸할때까지대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MonsterMany', value=0):
            return 폭발저주디버프제거잠시대기()
        if user_value(key='FirstBattleEnd', value=1):
            return 폭발저주디버프제거잠시대기()
        if user_value(key='FirstBattleEnd', value=99):
            return 폭발저주디버프제거하고종료()


class 폭발저주디버프제거잠시대기(state.State):
    def on_enter(self):
        set_user_value(key='SkillDebuffCheck_1Phase', value=0) # 중요:  여기 단계 끝나면 다시 처음인 <state name="보스의저주디버프사용신호대기"> 단계로 넘어가는데, 거기서의  SkillDebuffCheck_1Phase =  1 진행되지 않도록 이 변수 꼭 0 초기화 하기
        set_user_value(key='FirstBattleEnd', value=0) # FirstBattleEnd변수 0으로 초기 셋팅

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 폭발저주디버프제거()


class 폭발저주디버프제거(state.State):
    def on_enter(self):
        add_buff(boxIds=[601], skillId=50001413, level=1, arg4=False) # 50001413은 보스한테 걸린 폭발 저주 디버프 제거해주는 애디셔널임, MS2TriggerBox  ID = 601 트리거 박스 크기는 1셋트 3개 전투판과 스타팅 지점까지 포함되는 넓은 범위임

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1800):
            return 보스의저주디버프사용신호대기()


class 폭발저주디버프제거하고종료(state.State):
    def on_enter(self):
        add_buff(boxIds=[601], skillId=50001413, level=1, arg4=False) # 50001413은 보스한테 걸린 폭발 저주 디버프 제거해주는 애디셔널임, MS2TriggerBox  ID = 601 트리거 박스 크기는 1셋트 3개 전투판과 스타팅 지점까지 포함되는 넓은 범위임

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 종료()


class 종료(state.State):
    pass

