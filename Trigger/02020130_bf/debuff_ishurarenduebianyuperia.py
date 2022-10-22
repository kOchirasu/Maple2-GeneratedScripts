""" trigger/02020130_bf/debuff_ishurarenduebianyuperia.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_user_value(key='IshuraFirstSetEnd', value=0)
        set_user_value(key='RenduebianFirstSetEnd', value=0)
        set_user_value(key='YuperiaFirstSetEnd', value=0)

    def on_tick(self) -> state.State:
        if count_users(boxId=601, boxId=1):
            return 셋트전투판스킬트리거셋팅1()


class 셋트전투판스킬트리거셋팅1(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1301], isEnable=True) # 이슈라 전투판 디버프 스킬 On으로 초기 셋팅하기
        set_skill(triggerIds=[1302], isEnable=True) # 렌듀비앙 전투판 디버프 스킬 On으로 초기 셋팅하기
        set_skill(triggerIds=[1303], isEnable=True) # 유페리아 전투판 디버프 스킬 On으로 초기 셋팅하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=310):
            return 셋트전투판마무리신호대기1()


class 셋트전투판마무리신호대기1(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='IshuraFirstSetEnd', value=1): # 레듀비앙 보스 AI에게 변수 신호 받을때까지 대기하기
            return 이슈라_디버프스킬끄기()
        if user_value(key='RenduebianFirstSetEnd', value=1): # 유페리아 보스 AI에게 변수 신호 받을때까지 대기하기
            return 렌듀비앙_디버프스킬끄기()
        if user_value(key='YuperiaFirstSetEnd', value=1):
            return 유페리아_디버프스킬끄기()


class 이슈라_디버프스킬끄기(state.State):
    def on_enter(self):
        set_user_value(key='IshuraFirstSetEnd', value=0) # IshuraFirstSetEnd 변수 0으로 초기화
        set_skill(triggerIds=[1301], isEnable=False) # 이슈라 전투판 디버프 스킬 끄기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=370):
            return 셋트전투판마무리신호대기1()


class 렌듀비앙_디버프스킬끄기(state.State):
    def on_enter(self):
        set_user_value(key='RenduebianFirstSetEnd', value=0) # RenduebianFirstSetEnd 변수 0으로 초기화
        set_skill(triggerIds=[1302], isEnable=False) # 렌듀비앙 전투판 디버프 스킬 끄기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=370):
            return 셋트전투판마무리신호대기1()


class 유페리아_디버프스킬끄기(state.State):
    def on_enter(self):
        set_user_value(key='YuperiaFirstSetEnd', value=0) # YuperiaFirstSetEnd 변수 0으로 초기화
        set_skill(triggerIds=[1303], isEnable=False) # 유페리아 전투판 디버프 스킬 끄기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=370):
            return 셋트전투판마무리신호대기1()


class 종료(state.State):
    pass


