""" trigger/52000040_qd/main_02.xml """
from common import *
import state


#  출연진 : 라오즈(401 : 11001760) 
class ready(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[1]):
            return end()
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[2]):
            return end()
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[3]):
            return end()
        if quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[3]):
            return start_05()
        if quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[2]):
            return start_05()
        if quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[1]):
            set_effect(triggerIds=[6002], visible=True)
            create_monster(spawnIds=[401], arg2=False)
            return start()


class start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=401, script='$52000040_QD__MAIN_02__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_03()


class start_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=401, script='$52000040_QD__MAIN_02__1$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=401, script='$52000040_QD__MAIN_02__2$', arg4=2, arg5=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_npc(spawnId=401, patrolName='MS2PatrolData_4001')
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            return start_04()


class start_04(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=702, spawnIds=[401]):
            return npc_exit_01()


class npc_exit_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True)
        destroy_monster(spawnIds=[401])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return start_05()


class start_05(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='FollowingLaoz') # 퀘스트 목표 체크용 업적이벤트 발생
        create_monster(spawnIds=[501], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[1]):
            return end()


class end(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[501])
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=4, visible=True, enabled=False, minimapVisible=False)


