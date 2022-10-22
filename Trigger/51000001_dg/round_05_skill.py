""" trigger/51000001_dg/round_05_skill.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3501], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3503], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 지역랜덤()


class 지역랜덤(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[105]):
            return 종료()
        if random_condition(rate=33):
            set_mesh(triggerIds=[3501], visible=True, arg3=0, arg4=0, arg5=0)
            return A지역()
        if random_condition(rate=33):
            set_mesh(triggerIds=[3502], visible=True, arg3=0, arg4=0, arg5=0)
            return B지역()
        if random_condition(rate=34):
            set_mesh(triggerIds=[3503], visible=True, arg3=0, arg4=0, arg5=0)
            return C지역()


class A지역(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10501]):
            return 스킬랜덤()


class B지역(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10502]):
            return 스킬랜덤()


class C지역(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10503]):
            return 스킬랜덤()


class 스킬랜덤(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='random_buff_box')

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[105]):
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
        set_mesh(triggerIds=[3501], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3502], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3503], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 시작대기중()


class 종료(state.State):
    pass


