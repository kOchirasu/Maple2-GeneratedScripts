""" trigger/82000001_survival/01_survival.xml """
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
        sight_range(enable=True, range=3, rangeZ=300, border=75)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Wait_Talk01()

    def on_exit(self):
        set_effect(triggerIds=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=True) # SafeZone Barrier Effect
        set_timer(timerId='1', seconds=59, clearAtZero=True, display=True, arg5=-80) # test용 수정 가능 지점 / arg2="30" / arg2 시간 더 짧게 가능  arg2="10"
        write_log(logName='Survival', arg3='Waiting_Start') # 서바이벌 대기 시작


class Wait_Talk01(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000000_survival__01_SURVIVAL__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait_Talk02()
        if time_expired(timerId='1'):
            return ChangeBGM()


class Wait_Talk02(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000000_survival__01_SURVIVAL__1$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait_Talk03()
        if time_expired(timerId='1'):
            return ChangeBGM()


class Wait_Talk03(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000000_survival__01_SURVIVAL__2$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Wait_Talk01()
        if time_expired(timerId='1'):
            return ChangeBGM()


class ChangeBGM(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='BattleField_Event')
        set_sound(triggerId=20000, arg2=True) # BGM Intro

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return StartGameExplain()


class StartGameExplain(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=5000, script='$82000000_survival__01_SURVIVAL__3$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GameExplain01()


class GameExplain01(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=6000, script='$82000000_survival__01_SURVIVAL__4$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return GameExplain02()


class GameExplain02(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000000_survival__01_SURVIVAL__5$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return GameExplain03()


class GameExplain03(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000000_survival__01_SURVIVAL__6$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return GameExplain04()


class GameExplain04(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=5000, script='$82000000_survival__01_SURVIVAL__7$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CheckPCLocation()


class CheckPCLocation(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return StartPoint01_North()
        if user_detected(boxIds=[9002]):
            return StartPoint02_South()
        if user_detected(boxIds=[9003]):
            return StartPoint03_East()
        if user_detected(boxIds=[9004]):
            return StartPoint04_West()
        if user_detected(boxIds=[9005]):
            return StartPoint05_NorthWest()
        if user_detected(boxIds=[9006]):
            return StartPoint06_NorthEast()
        if user_detected(boxIds=[9007]):
            return StartPoint07_SouthWest()
        if user_detected(boxIds=[9008]):
            return StartPoint08_SouthEast()


class StartPoint01_North(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=1)


class StartPoint02_South(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=2)


class StartPoint03_East(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=3)


class StartPoint04_West(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=4)


class StartPoint05_NorthWest(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=5)


class StartPoint06_NorthEast(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=6)


class StartPoint07_SouthWest(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=7)


class StartPoint08_SouthEast(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PVPReady()

    def on_exit(self):
        set_user_value(triggerId=2, key='SetRide', value=8)


class PVPReady(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000000_survival__01_SURVIVAL__8$') # 누가 우승할지 보자

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CheckTheNumberOfPlayers()


class CheckTheNumberOfPlayers(state.State):
    def on_enter(self):
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=20, operator='GreaterEqual'):
            return MatchingSuccessDelay()
        if count_users(boxId=9000, boxId=20, operator='Less'):
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
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000000_survival__01_SURVIVAL__9$') # 충분히 모였군!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return RideRiseUp()


class RideRiseUp(state.State):
    def on_enter(self):
        set_user_value(triggerId=2, key='StartPatrol', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Countdown()


class Countdown(state.State):
    def on_enter(self):
        create_field_game(type='MapleSurvival')
        show_count_ui(text='$82000000_survival__01_SURVIVAL__10$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return AreaOpen()


class AreaOpen(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318], isStart=True) # 나태 버섯 Normal Mob
        set_user_value(triggerId=5, key='RareBoxOnCount', value=1)
        set_user_value(triggerId=8, key='RareMobOnCount', value=1)
        set_user_value(triggerId=9, key='NormaBoxOnCount', value=1)
        set_user_value(triggerId=10, key='BattleRidingOnCount', value=1)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_user_value(triggerId=4, key='InvincibleOff', value=1)
        add_buff(boxIds=[9000], skillId=71000053, level=1, arg4=False, arg5=False) # 31초 무적 버프
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
        set_user_value(triggerId=3, key='StormStart', value=1) # test용 수정 가능 지점 : 스톰 생성 안하려면 주석 처리
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
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000000_survival__01_SURVIVAL__11$') # 인원 부족

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameCancel()


class GameCancel(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000000_survival__01_SURVIVAL__12$') # 경기 취소

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReadyToKickOut()


class ReadyToKickOut(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$82000000_survival__01_SURVIVAL__13$', arg3='4000', arg4='0') # 잠시 후 원래 있던 곳으로 돌아갑니다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class GameEnd(state.State):
    def on_enter(self):
        add_buff(boxIds=[9000], skillId=70001101, level=1, arg4=False, arg5=False) # 변신 탈 것 해제용 버프
        sight_range(enable=False, range=3) # 우승자 카메라 (LocalTargetCamera 호출) 연출 시, 비석 상태인 유저의 위치 기준으로 우승자가 멀리 있어도 우승자가 보이도록 워포그 해제

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9000]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_user_value(triggerId=5, key='RareBoxOff', value=1)
        set_user_value(triggerId=8, key='RareMobOff', value=1)
        set_user_value(triggerId=9, key='NormaBoxOff', value=1)
        set_user_value(triggerId=10, key='BattleRidingOff', value=1)
        destroy_monster(spawnIds=[-1])
        move_user(mapId=0, portalId=0)
        start_combine_spawn(groupId=[196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318], isStart=False) # 나태 버섯 Normal Mob


