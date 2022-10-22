""" trigger/52000064_qd/90000650.xml """
from common import *
import state


class 시작대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[1001,1002,1003], arg2=False)
        create_monster(spawnIds=[1101,1102,1103], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 아이템생성()


class 아이템생성(state.State):
    def on_enter(self):
        create_item(spawnIds=[9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 완료대기()


class 완료대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 완료()


class 완료(state.State):
    def on_enter(self):
        create_item(spawnIds=[9011,9012,9013,9014,9015])
        set_event_ui(type=7, arg3='3000', arg4='0')
        set_achievement(triggerId=199, type='trigger', achieve='ArrivedFlyBalloon')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[90000650], questStates=[3]):
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            return 종료()


class 종료(state.State):
    pass


