""" trigger/99999913/01_survival.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_effect(triggerIds=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=False) # SafeZone Barrier Effect
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007], visible=True, arg3=0, arg4=0, arg5=0) # Barrier Center
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=True, arg3=0, arg4=0, arg5=0) # Barrier North
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207], visible=True, arg3=0, arg4=0, arg5=0) # Barrier South
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307], visible=True, arg3=0, arg4=0, arg5=0) # Barrier East
        set_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407], visible=True, arg3=0, arg4=0, arg5=0) # Barrier West
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507], visible=True, arg3=0, arg4=0, arg5=0) # Barrier SouthEast
        set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607], visible=True, arg3=0, arg4=0, arg5=0) # Barrier SouthWest
        set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707], visible=True, arg3=0, arg4=0, arg5=0) # Barrier NorthEast
        set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807], visible=True, arg3=0, arg4=0, arg5=0) # Barrier NorthWest
        set_interact_object(triggerIds=[11000037], state=1) # Normal Box
        set_interact_object(triggerIds=[11000039], state=1) # Normal Box
        set_sound(triggerId=20000, arg2=False) # BGM Intro
        set_sound(triggerId=20001, arg2=False) # BGM Loop
        sight_range(enable=True, range=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Wait01()

    def on_exit(self):
        set_effect(triggerIds=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=True) # SafeZone Barrier Effect


class Wait01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=60, clearAtZero=True, display=True, arg5=-80) # test용 수정 가능 지점
        set_event_ui(type=1, arg2='잠시 기다려주세요.\n잠시 후 경기 시작점이 결정됩니다.', arg3='4000', arg4='0')
        write_log(logName='Survival', arg3='Waiting_Start') # 서바이벌 대기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait02()
        if time_expired(timerId='1'):
            return CheckTheNumberOfPlayers()


class Wait02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Wait01()
        if time_expired(timerId='1'):
            return CheckTheNumberOfPlayers()


class CheckTheNumberOfPlayers(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=20, operator='Less'):
            return GameCancel01()
        if count_users(boxId=9000, boxId=20, operator='GreaterEqual'):
            return StartPositionRandomPick()


class StartPositionRandomPick(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        set_event_ui(type=1, arg2='시작점으로 이동합니다.', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if random_condition(rate=12.5):
            return PCRemap01_North()
        if random_condition(rate=12.5):
            return PCRemap02_South()
        if random_condition(rate=12.5):
            return PCRemap03_East()
        if random_condition(rate=12.5):
            return PCRemap04_West()
        if random_condition(rate=12.5):
            return PCRemap05_NorthWest()
        if random_condition(rate=12.5):
            return PCRemap06_NorthEast()
        if random_condition(rate=12.5):
            return PCRemap07_SouthWest()
        if random_condition(rate=12.5):
            return PCRemap08_SouthEast()


class PCRemap01_North(state.State):
    def on_enter(self):
        move_user(mapId=82000001, portalId=101, boxId=9000)
        write_log(logName='Survival', arg3='Waiting_PositionPick') # 위치 이동 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=1)


class PCRemap02_South(state.State):
    def on_enter(self):
        move_user(mapId=82000001, portalId=102, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=2)


class PCRemap03_East(state.State):
    def on_enter(self):
        move_user(mapId=82000001, portalId=103, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=3)


class PCRemap04_West(state.State):
    def on_enter(self):
        move_user(mapId=82000001, portalId=104, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=4)


class PCRemap05_NorthWest(state.State):
    def on_enter(self):
        move_user(mapId=82000001, portalId=105, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=5)


class PCRemap06_NorthEast(state.State):
    def on_enter(self):
        move_user(mapId=82000001, portalId=106, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=6)


class PCRemap07_SouthWest(state.State):
    def on_enter(self):
        move_user(mapId=82000001, portalId=107, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=7)


class PCRemap08_SouthEast(state.State):
    def on_enter(self):
        move_user(mapId=82000001, portalId=108, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=8)


class PVPReady(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='space 키를 누르면  수레에 탈 수 있습니다.\nspace 키를 다시 누르면 수레에서 내립니다.', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PVPStart()


class PVPStart(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='경기를 곧 시작합니다!\n경기 시작과 함께 수레가 출발합니다!', arg3='4000', arg4='0')
        create_field_game(type='MapleSurvive')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Countdown()


class Countdown(state.State):
    def on_enter(self):
        show_count_ui(text='경기 시작!', count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return AreaOpen()


class AreaOpen(state.State):
    def on_enter(self):
        set_user_value(triggerId=5, key='RareBoxOnCount', value=1)
        set_user_value(triggerId=2, key='StartPatrol', value=1)
        set_sound(triggerId=20000, arg2=True) # BGM Intro
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_user_value(triggerId=4, key='InvincibleOff', value=1)
        add_buff(boxIds=[9000], skillId=71000053, level=1, arg4=False, arg5=False) # 31초 무적
        set_effect(triggerIds=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=False) # SafeZone Barrier Effect
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007], visible=False, arg3=1000, arg4=0, arg5=2) # Barrier Center
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=False, arg3=1000, arg4=0, arg5=2) # Barrier_North
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207], visible=False, arg3=1000, arg4=0, arg5=2) # Barrier_South
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307], visible=False, arg3=1000, arg4=0, arg5=2) # Barrier_East
        set_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407], visible=False, arg3=1000, arg4=0, arg5=2) # Barrier_West
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507], visible=False, arg3=1000, arg4=0, arg5=2) # Barrier_SouthEast
        set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607], visible=False, arg3=1000, arg4=0, arg5=2) # Barrier_SouthWest
        set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707], visible=False, arg3=1000, arg4=0, arg5=2) # Barrier_NorthEast
        set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807], visible=False, arg3=1000, arg4=0, arg5=2) # Barrier_NorthWest
        write_log(logName='Survival', arg3='Start') # 서바이벌 시작 로그 남김

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return GameStart()


class GameStart(state.State):
    def on_enter(self):
        set_sound(triggerId=20000, arg2=False) # BGM Intro
        set_sound(triggerId=20001, arg2=True) # BGM Loop
        set_user_value(triggerId=3, key='StormStart', value=1)
        write_log(logName='Survival', arg3='StormStart') # 서바이벌 스톰 시작 로그 남김

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9000]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000037], state=0) # Normal Box
        set_interact_object(triggerIds=[11000039], state=0) # Normal Box
        set_user_value(triggerId=5, key='RareBoxOff', value=1)
        write_log(logName='Survival', arg3='Trigger_End') # 서바이벌 트리거 종료 로그 남김
        destroy_monster(spawnIds=[-1])


#  인원 미만으로 인한 경기 취소 
class GameCancel01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='참가자 부족으로 인해 경기를 취소합니다.', arg3='4000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameCancel02()


class GameCancel02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='잠시 후 원래 있던 곳으로 돌아갑니다.', arg3='4000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return GameCancel03()


class GameCancel03(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000037], state=0) # Normal Box
        set_interact_object(triggerIds=[11000039], state=0) # Normal Box
        destroy_monster(spawnIds=[-1])
        move_user(mapId=0, portalId=0)


