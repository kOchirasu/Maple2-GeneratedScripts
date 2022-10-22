""" trigger/02020097_bf/message.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10]):
            return 대기상태()


class 대기상태(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[12]): # 2페이즈 전투 다 끝나고 , AI_Balrog_Kritias.xml 발록에게   StairsOk2nd = 1 신호를 받으면 이 부분 실행, 2페이즈 건너띄기가 되었기 때문에 경비병 도움 메시지 출력 안함
            return 경비병도움안내()
        if user_value(key='StairsOk2nd', value=1):
            return 트리거종료()


class 경비병도움안내(state.State):
    def on_enter(self):
        show_guide_summary(entityId=29200001, textId=29200001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 트리거종료()

    def on_exit(self):
        hide_guide_summary(entityId=29200001)


class 트리거종료(state.State):
    pass


