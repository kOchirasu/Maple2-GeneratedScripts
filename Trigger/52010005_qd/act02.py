""" trigger/52010005_qd/act02.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            set_interact_object(triggerIds=[10000872], state=0)
            return 퀘스트조건02()


class 퀘스트조건02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002821], questStates=[2]):
            return Q2_미카등장01()


#   2nd Quest  
class Q2_미카등장01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return Q2_딜레이01()


class Q2_딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=2)
        select_camera(triggerId=3001, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return Q2_미카대화01()


class Q2_미카대화01(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=3)
        set_conversation(type=2, spawnId=11001285, script='$52010005_QD__ACT02__0$', arg4=3)
        set_skip(state=Q2_미카대화02대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return Q2_미카대화02대기()


class Q2_미카대화02대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return Q2_미카대화02()


class Q2_미카대화02(state.State):
    def on_enter(self):
        set_timer(timerId='13', seconds=3)
        set_conversation(type=2, spawnId=11001285, script='$52010005_QD__ACT02__1$', arg4=3)
        set_skip(state=Q2_미카대화종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='13'):
            return Q2_미카대화종료()


class Q2_미카대화종료(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        select_camera(triggerId=3001, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


