""" trigger/82000006_survival/01_survival.xml """
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
        set_sound(triggerId=20000, arg2=False) # BGM Intro
        set_sound(triggerId=20001, arg2=False) # BGM Loop
        set_local_camera(cameraId=100, enable=False)
        sight_range(enable=True, range=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Wait_Talk01()

    def on_exit(self):
        set_effect(triggerIds=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=True) # SafeZone Barrier Effect


class Wait_Talk01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=90, clearAtZero=True, display=True, arg5=-80) # test용 수정 가능 지점 arg2="60" / arg2="5"
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__0$')
        write_log(logName='Survival', arg3='Waiting_Start') # 서바이벌 대기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait_Talk02()
        if time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st()


class Wait_Talk02(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__1$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait_Talk03()
        if time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st()


class Wait_Talk03(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__2$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait_Talk04()
        if time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st()


class Wait_Talk04(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__3$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait_Talk05()
        if time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st()


class Wait_Talk05(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__4$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait_Talk06()
        if time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st()


class Wait_Talk06(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__5$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait_Talk01()
        if time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st()


class CheckTheNumberOfPlayers_1st(state.State):
    def on_enter(self):
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=25, operator='GreaterEqual'):
            return MatchingSuccessDelay()
        if count_users(boxId=9000, boxId=25, operator='Less'):
            return MatchingFailDelay()


class MatchingSuccessDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=7, key='HidePartyUI', value=1)
        play_system_sound_in_box(sound='GuildBattle_Enter')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return MatchingSuccess()


class MatchingSuccess(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__17$') # 충분히 모였군!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ReadyToMoveStartPosition()


class ReadyToMoveStartPosition(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=3000, script='$82000012_survival__01_SURVIVAL__11$') # 시작 지점으로 이동할까?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return StartPositionRandomPick()


class StartPositionRandomPick(state.State):
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
        play_system_sound_in_box(sound='BattleField_Event')
        set_sound(triggerId=20000, arg2=True) # BGM Intro
        move_user(mapId=82000012, portalId=101, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return StartGameExplain()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=1)


class PCRemap02_South(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='BattleField_Event')
        set_sound(triggerId=20000, arg2=True) # BGM Intro
        move_user(mapId=82000012, portalId=102, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return StartGameExplain()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=2)


class PCRemap03_East(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='BattleField_Event')
        set_sound(triggerId=20000, arg2=True) # BGM Intro
        move_user(mapId=82000012, portalId=103, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return StartGameExplain()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=3)


class PCRemap04_West(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='BattleField_Event')
        set_sound(triggerId=20000, arg2=True) # BGM Intro
        move_user(mapId=82000012, portalId=104, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return StartGameExplain()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=4)


class PCRemap05_NorthWest(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='BattleField_Event')
        set_sound(triggerId=20000, arg2=True) # BGM Intro
        move_user(mapId=82000012, portalId=105, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return StartGameExplain()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=5)


class PCRemap06_NorthEast(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='BattleField_Event')
        set_sound(triggerId=20000, arg2=True) # BGM Intro
        move_user(mapId=82000012, portalId=106, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return StartGameExplain()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=6)


class PCRemap07_SouthWest(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='BattleField_Event')
        set_sound(triggerId=20000, arg2=True) # BGM Intro
        move_user(mapId=82000012, portalId=107, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return StartGameExplain()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=7)


class PCRemap08_SouthEast(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='BattleField_Event')
        set_sound(triggerId=20000, arg2=True) # BGM Intro
        move_user(mapId=82000012, portalId=108, boxId=9000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return StartGameExplain()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=8)


class StartGameExplain(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=6000, script='$82000012_survival__01_SURVIVAL__6$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return GameExplain01()


class GameExplain01(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=6000, script='$82000012_survival__01_SURVIVAL__7$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return GameExplain02()


class GameExplain02(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=3500, script='$82000012_survival__01_SURVIVAL__8$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return GameExplain03()


class GameExplain03(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=3500, script='$82000012_survival__01_SURVIVAL__9$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return GameExplain04()


class GameExplain04(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=5000, script='$82000012_survival__01_SURVIVAL__10$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameExplain05()


class GameExplain05(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=5000, script='$82000012_survival__01_SURVIVAL__12$') # 버섯 열기구 안내

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PVPReady()


class PVPReady(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__13$') # 누가 우승할지 보자

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CheckTheNumberOfPlayers_2nd()


class CheckTheNumberOfPlayers_2nd(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=20, operator='GreaterEqual'):
            return RideRiseUp()
        if count_users(boxId=9000, boxId=20, operator='Less'):
            return MatchingFailDelay()


class RideRiseUp(state.State):
    def on_enter(self):
        set_user_value(triggerId=2, key='StartPatrol', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Countdown()


class Countdown(state.State):
    def on_enter(self):
        create_field_game(type='MapleSurvival')
        show_count_ui(text='$82000012_survival__01_SURVIVAL__14$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return AreaOpen()


class AreaOpen(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159], isStart=True) # 나태 버섯 Normal Mob
        set_user_value(triggerId=5, key='RareBoxOnCount', value=1)
        set_user_value(triggerId=8, key='RareMobOnCount', value=1)
        set_user_value(triggerId=9, key='NormaBoxOnCount', value=1)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_user_value(triggerId=4, key='InvincibleOff', value=1)
        add_buff(boxIds=[9000], skillId=71000053, level=1, arg4=False, arg5=False) # 31초 무적
        set_effect(triggerIds=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=False) # SafeZone Barrier Effect
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007], visible=False, arg3=1000, arg4=0, arg5=1) # Barrier Center
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=False, arg3=1000, arg4=0, arg5=1) # Barrier_North
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207], visible=False, arg3=1000, arg4=0, arg5=1) # Barrier_South
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307], visible=False, arg3=1000, arg4=0, arg5=1) # Barrier_East
        set_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407], visible=False, arg3=1000, arg4=0, arg5=1) # Barrier_West
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507], visible=False, arg3=1000, arg4=0, arg5=1) # Barrier_SouthEast
        set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607], visible=False, arg3=1000, arg4=0, arg5=1) # Barrier_SouthWest
        set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707], visible=False, arg3=1000, arg4=0, arg5=1) # Barrier_NorthEast
        set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807], visible=False, arg3=1000, arg4=0, arg5=1) # Barrier_NorthWest
        set_sound(triggerId=20000, arg2=False) # BGM Intro
        set_sound(triggerId=20001, arg2=True) # BGM Loop
        write_log(logName='Survival', arg3='Start') # 서바이벌 시작 로그 남김

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return GameStart()


class GameStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=3, key='StormStart', value=1) # test용 수정 지점
        write_log(logName='Survival', arg3='StormStart') # 서바이벌 스톰 시작 로그 남김

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9000]):
            return Quit()
        if not is_playing_maple_survival():
            return GameEnd()


#  인원 미만으로 인한 경기 취소 
class MatchingFailDelay(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='guildBattle_MatchingFail')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return MatchingFail()


class MatchingFail(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__15$') # 인원 부족

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameCancel()


class GameCancel(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__16$') # 경기 취소

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReadyToKickOut()


class ReadyToKickOut(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$82000012_survival__01_SURVIVAL__18$', arg3='4000', arg4='0') # 잠시 후 원래 있던 곳으로 돌아갑니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class GameEnd(state.State):
    def on_enter(self):
        sight_range(enable=False, range=3) # 우승자 카메라 (LocalTargetCamera 호출) 연출 시, 비석 상태인 유저의 위치 기준으로 우승자가 멀리 있어도 우승자가 보이도록 워포그 해제

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9000]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_user_value(triggerId=5, key='RareBoxOff', value=1)
        set_user_value(triggerId=8, key='RareMobOff', value=1)
        set_user_value(triggerId=9, key='NormaBoxOff', value=1)
        destroy_monster(spawnIds=[-1])
        move_user(mapId=0, portalId=0)
        start_combine_spawn(groupId=[37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159], isStart=False) # 나태 버섯 Normal Mob

