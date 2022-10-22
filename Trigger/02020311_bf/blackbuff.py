""" trigger/02020311_bf/blackbuff.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000406], state=0)
        set_interact_object(triggerIds=[12000406], state=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[801]):
            return 오브젝트체크()
        """
        <condition  name="WaitTick" waitTick="3000"  >
            <action name="오브젝트반응설정한다" arg1="12000406" arg2="1" />
            <transition state="대기이"/>
        </condition>
        """


class 대기이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대기()
        if user_detected(boxIds=[801]):
            return 오브젝트체크()


class 오브젝트체크(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000406], arg2=0):
            return 오브젝트재생성()


class 오브젝트재생성(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_interact_object(triggerIds=[12000406], state=1)
            return 오브젝트체크()


