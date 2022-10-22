""" trigger/52000057_qd/guidescene_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1003], arg2=False)
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[90000611], questStates=[2]):
            return 오필리아리젠()
        if quest_user_detected(boxIds=[199], questIds=[90000611], questStates=[1]):
            return 오필리아리젠()
        if quest_user_detected(boxIds=[199], questIds=[90000610], questStates=[3]):
            return 오필리아리젠상시()
        if quest_user_detected(boxIds=[199], questIds=[90000610], questStates=[2]):
            return 오필리아리젠상시()
        if quest_user_detected(boxIds=[199], questIds=[90000610], questStates=[1]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001], arg2=False)
        set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 말풍선대사01()


class 말풍선대사01(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=198, spawnIds=[1001]):
            return 시네마틱대사01()


class 시네마틱대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001871, script='$52000057_QD__GUIDESCENE_01__0$', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=11001871, script='$52000057_QD__GUIDESCENE_01__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 연퀘감지()


class 연퀘감지(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[90000611], questStates=[1]):
            return 오필리아대사연출01()


class 오필리아리젠(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 오필리아대사연출01()


class 오필리아대사연출01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001871, script='$52000057_QD__GUIDESCENE_01__2$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return SendSignalToGuide01()


#  트리거 To가이드  
class SendSignalToGuide01(state.State):
    def on_enter(self):
        guide_event(eventId=60660)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 종료()


class 오필리아리젠상시(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[90000611], questStates=[1]):
            return 오필리아대사연출01()


class 종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


