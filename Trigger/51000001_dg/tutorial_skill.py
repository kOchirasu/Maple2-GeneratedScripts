""" trigger/51000001_dg/tutorial_skill.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 지역랜덤()


class 지역랜덤(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[100]):
            return 종료()
        if random_condition(rate=50):
            set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0)
            return A지역()
        if random_condition(rate=50):
            set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0)
            return B지역()


class A지역(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10001]):
            return 스킬랜덤()


class B지역(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10002]):
            return 스킬랜덤()


class 스킬랜덤(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[100]):
            return 종료()
        if random_condition(rate=40):
            add_buff(boxIds=[199], skillId=49179051, level=1, arg4=False, arg5=False)
            return 대기시간()
        """
        <condition name="랜덤조건" arg1="20">    소형화 사용 안함
                    <action name="버프를걸어준다" arg1="199" arg2="49179081" arg3="1" arg4="0" arg5="0"/>
                    <transition state="대기시간" />
                </condition>
        """
        if random_condition(rate=30):
            add_buff(boxIds=[199], skillId=70000085, level=1, arg5=False)
            return 대기시간()
        if random_condition(rate=15):
            add_buff(boxIds=[199], skillId=49179061, level=1, arg4=False, arg5=False)
            return 대기시간()
        if random_condition(rate=15):
            add_buff(boxIds=[199], skillId=49179071, level=1, arg4=False, arg5=False)
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작대기중()


class 종료(state.State):
    pass


