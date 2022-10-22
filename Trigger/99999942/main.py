""" trigger/99999942/main.xml """
from common import *
import state


class StateNone(state.State):
    def on_enter(self):
        create_field_game(type='WaterGunBattle', reset=True) # 데이터 셋팅
        field_game_constant(key='WaitUserTick', value='15000') # 유저이동의 arg2와 같도록
        field_game_constant(key='WaitPlayTick', value='5000')
        field_game_constant(key='ResizeWaitTick', value='15000,15000,15000,15000')
        field_game_constant(key='ResizeWarningTick', value='5000,5000,5000,5000')
        field_game_constant(key='SkillSetID', value='99930047')
        field_game_constant(key='MinPlayer', value='2') # 포탈 셋팅
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_value(key='WaitUser', value=1):
            return 유저대기중()


class 유저대기중(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=15, clearAtZero=False, display=True)

    def on_tick(self) -> state.State:
        if user_value(key='MoveUser', value=1):
            return 유저이동()
        if user_value(key='End', value=1):
            return 종료()


class 유저이동(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5, clearAtZero=False, display=True)
        move_user(mapId=99999942, portalId=2)

    def on_tick(self) -> state.State:
        if user_value(key='Play', value=1):
            return 게임시작()


class 게임시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='PlayRound1', value=1):
            return 라운드1()


class 라운드1(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='PlayRound2', value=1):
            return 라운드2()
        if user_value(key='End', value=1):
            return 종료()


class 라운드2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], visible=False, arg3=2, arg4=2)

    def on_tick(self) -> state.State:
        if user_value(key='PlayRound3', value=1):
            return 라운드3()
        if user_value(key='End', value=1):
            return 종료()


class 라운드3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48], visible=False, arg3=2, arg4=2)

    def on_tick(self) -> state.State:
        if user_value(key='PlayRound4', value=1):
            return 라운드4()
        if user_value(key='End', value=1):
            return 종료()


class 라운드4(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[49,50,51,52,53,54,55,56,57,58,59,60], visible=False, arg3=2, arg4=2)

    def on_tick(self) -> state.State:
        if user_value(key='End', value=1):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64], visible=True, arg3=0, arg4=0)
        # <action name="SetPortal" arg1="1" arg2="1" arg3="1" arg4="0"/>
        move_user(mapId=99999942, portalId=1)


