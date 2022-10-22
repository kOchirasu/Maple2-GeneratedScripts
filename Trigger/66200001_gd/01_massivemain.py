""" trigger/66200001_gd/01_massivemain.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_field_game(type='GuildVsGame')
        user_tag_symbol(symbol1='guild_game_blue', symbol2='guild_game_red')
        set_sound(triggerId=10000, arg2=False) # Intro
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=40000, arg2=False) # Puzzle
        set_effect(triggerIds=[8000], visible=False) # Scratch
        set_effect(triggerIds=[8002], visible=False) # BlueTeamBox
        set_effect(triggerIds=[8003], visible=False) # BlueTeamArrow
        set_effect(triggerIds=[8004], visible=False) # RedTeamBox
        set_effect(triggerIds=[8005], visible=False) # RedTeamArrow
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=0, arg4=0, arg5=0) # Dance
        set_mesh(triggerIds=[511,512,513,514], visible=True, arg3=0, arg4=0, arg5=0) # Row1
        set_mesh(triggerIds=[521,522,523,524], visible=True, arg3=0, arg4=0, arg5=0) # Row2
        set_mesh(triggerIds=[531,532,533,534], visible=True, arg3=0, arg4=0, arg5=0) # Row3
        set_mesh(triggerIds=[541,542,543,544], visible=True, arg3=0, arg4=0, arg5=0) # Row4
        set_mesh(triggerIds=[110,111,112,113,114,115], visible=False, arg3=0, arg4=0, arg5=0) # 1,1 / 0 to 5
        set_mesh(triggerIds=[120,121,122,123,124,125], visible=False, arg3=0, arg4=0, arg5=0) # 1,2 / 0 to 5
        set_mesh(triggerIds=[130,131,132,133,134,135], visible=False, arg3=0, arg4=0, arg5=0) # 1,3 / 0 to 5
        set_mesh(triggerIds=[140,141,142,143,144,145], visible=False, arg3=0, arg4=0, arg5=0) # 1,4 / 0 to 5
        set_mesh(triggerIds=[210,211,212,213,214,215], visible=False, arg3=0, arg4=0, arg5=0) # 2,1 / 0 to 5
        set_mesh(triggerIds=[220,221,222,223,224,225], visible=False, arg3=0, arg4=0, arg5=0) # 2,2 / 0 to 5
        set_mesh(triggerIds=[230,231,232,233,234,235], visible=False, arg3=0, arg4=0, arg5=0) # 2,3 / 0 to 5
        set_mesh(triggerIds=[240,241,242,243,244,245], visible=False, arg3=0, arg4=0, arg5=0) # 2,4 / 0 to 5
        set_mesh(triggerIds=[310,311,312,313,314,315], visible=False, arg3=0, arg4=0, arg5=0) # 3,1 / 0 to 5
        set_mesh(triggerIds=[320,321,322,323,324,325], visible=False, arg3=0, arg4=0, arg5=0) # 3,2 / 0 to 5
        set_mesh(triggerIds=[330,331,332,333,334,335], visible=False, arg3=0, arg4=0, arg5=0) # 3,3 / 0 to 5
        set_mesh(triggerIds=[340,341,342,343,344,345], visible=False, arg3=0, arg4=0, arg5=0) # 3,4 / 0 to 5
        set_mesh(triggerIds=[410,411,412,413,414,415], visible=False, arg3=0, arg4=0, arg5=0) # 4,1 / 0 to 5
        set_mesh(triggerIds=[420,421,422,423,424,425], visible=False, arg3=0, arg4=0, arg5=0) # 4,2 / 0 to 5
        set_mesh(triggerIds=[430,431,432,433,434,435], visible=False, arg3=0, arg4=0, arg5=0) # 4,3 / 0 to 5
        set_mesh(triggerIds=[440,441,442,443,444,445], visible=False, arg3=0, arg4=0, arg5=0) # 4,4 / 0 to 5
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=0, arg4=0, arg5=0) # Barrier
        set_interact_object(triggerIds=[10001180], state=0) # 7000ms
        set_interact_object(triggerIds=[10001181], state=2) # 9000ms
        set_interact_object(triggerIds=[10001182], state=2) # 12000ms
        set_interact_object(triggerIds=[10001183], state=2) # 15000ms
        set_user_value(key='Round', value=0)
        set_user_value(key='DanceTime', value=0)
        set_user_value(key='WinnerTeam', value=0)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False) # LeavePortal_EndGame
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False) # LeavePortal_EndGame
        set_portal(portalId=9, visible=False, enabled=False, minimapVisible=False) # LeavePortal_EndGame
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False) # LeavePortal_EndGame

    def on_tick(self) -> state.State:
        if check_user():
            return EntryDelay()


class EntryDelay(state.State):
    def on_enter(self):
        set_mini_game_area_for_hack(boxId=9001) # 해킹 보안용 시작 box 설정
        set_user_value(triggerId=9, key='MoveToTeamPortal', value=1) # 팀 대기 공간으로 이동 시작
        set_user_value(triggerId=10, key='BannerCheckIn', value=1) # 대기 공간 인원 체크 시작
        set_user_value(triggerId=11, key='BannerCheckIn', value=1) # 게임판 위 인원수 배너 표시
        set_timer(timerId='1', seconds=90) # 테스트 수정 가능 지점

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return IsGameStartOrNot()


#  유효 게임 판정 (팀별 인원수 체크) 
class IsGameStartOrNot(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=10, operator='GreaterEqual', userTagId=1):
            return IsGameStart_True01()
        if count_users(boxId=9000, boxId=10, operator='GreaterEqual', userTagId=2):
            return IsGameStart_Ture02()
        if count_users(boxId=9000, boxId=10, operator='Less', userTagId=1):
            return IsGameStart_False()


class IsGameStart_True01(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=10, operator='GreaterEqual', userTagId=2):
            return MoveToTeamCamp()
        if count_users(boxId=9000, boxId=10, operator='Less', userTagId=2):
            return DefaultbyWin_BlueTeam()


class IsGameStart_Ture02(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=10, operator='GreaterEqual', userTagId=1):
            return MoveToTeamCamp()
        if count_users(boxId=9000, boxId=10, operator='Less', userTagId=1):
            return DefaultbyWin_RedTeam()


class IsGameStart_False(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=10, operator='Less', userTagId=2):
            return GameCancel()


#  팀 대기 공간으로 이동 
class MoveToTeamCamp(state.State):
    def on_enter(self):
        set_user_value(triggerId=9, key='MoveToTeamPortal', value=2) # 팀 대기 공간으로 이동 종료 = 입장 종료
        move_to_portal(userTagId=1, portalId=21) # Tag1=Blue
        move_to_portal(userTagId=2, portalId=22) # Tag2=Red
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return GameGuide01()


#  길드 미니게임 대전 게임 진행 방식 안내 
class GameGuide01(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='0,0')
        set_user_value(triggerId=10, key='BannerCheckIn', value=0) # 대기 공간 인원 체크 종료
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=10000, arg2=True) # Intro
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__0$', arg3='5000', arg4='0')
        set_achievement(triggerId=9000, type='trigger', achieve='guildminigame_start') # 이벤트 퀘스트 관련

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameGuide02()


class GameGuide02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__1$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameGuide03()


class GameGuide03(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__2$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameGuide04()


class GameGuide04(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__3$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return R01Ready()


class R01Ready(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=1) # 테스트 수정 가능 지점
        set_event_ui(type=0, arg2='1,5') # Round1

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R01PlayerRandomPick01()


#  무작위 이동 안내 전 안내 / 1 라운드 전용
class R01PlayerRandomPick01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__67$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PlayerRandomPick02()


class PlayerRandomPick02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='BattleField_Event')
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__5$', arg3='5000', arg4='0')
        set_effect(triggerIds=[8002], visible=True) # BlueTeamBox
        set_effect(triggerIds=[8003], visible=True) # BlueTeamArrow
        set_effect(triggerIds=[8004], visible=True) # RedTeamBox
        set_effect(triggerIds=[8005], visible=True) # RedTeamArrow

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return PlayerRandomPickStartCount()


#  무작위 이동 안내 / 라운드 공용
class PlayerRandomPickStartCount(state.State):
    def on_enter(self):
        show_count_ui(text='$66200001_GD__01_MASSIVEMAIN__6$', stage=0, count=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PlayerRandomPickMove()


class PlayerRandomPickMove(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8002], visible=False) # BlueTeamBox
        set_effect(triggerIds=[8003], visible=False) # BlueTeamArrow
        set_effect(triggerIds=[8004], visible=False) # RedTeamBox
        set_effect(triggerIds=[8005], visible=False) # RedTeamArrow
        move_random_user(mapId=66200001, portalId=1, triggerId=9031, count=30) # 1번 포탈로 블루팀 최대 30명 이동
        move_random_user(mapId=66200001, portalId=2, triggerId=9032, count=30) # 2번 포탈로 블루팀 최대 30명 이동
        play_system_sound_in_box(boxIds=[9000], sound='GuildBattle_MemberPick')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CheckTheNumberOfPlayer()
        if not user_detected(boxIds=[9000]):
            return LeaveAll()


class CheckTheNumberOfPlayer(state.State):
    def on_enter(self):
        set_user_value(triggerId=11, key='BannerCheckIn', value=1) # 게임판 위 인원수 배너 표시
        play_system_sound_in_box(boxIds=[9000], sound='BattleField_Event')

    def on_tick(self) -> state.State:
        if user_value(key='Round', value=1):
            return R01Start()
        if user_value(key='Round', value=2):
            return R02Start()
        if user_value(key='Round', value=3):
            return R03Start()
        if user_value(key='Round', value=4):
            return R04Start()
        if user_value(key='Round', value=5):
            return R05Start()


#  R01 시작 
class R01Start(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__7$', arg3='3000', arg4='0') # Voice 02000953
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancetime_01')
        set_sound(triggerId=10000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R01DanceTime()


#  댄스 패턴 / 라운드 공용 
#  R01 DanceTime 패턴 랜덤 
class R01DanceTime(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        set_user_value(key='DanceTime', value=1)

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return DancePattern01()
        if random_condition(rate=30):
            return DancePattern02()
        if random_condition(rate=30):
            return DancePattern03()
        if random_condition(rate=3):
            return DancePattern0401()
        if random_condition(rate=3):
            return DancePattern0501()
        if random_condition(rate=2):
            return DancePattern0601()
        if random_condition(rate=2):
            return DancePattern0701()

    def on_exit(self):
        set_interact_object(triggerIds=[10001180], state=2) # 7000ms


#  Dance 9000ms  
class DancePattern01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001181], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return CheckDanceRound()


#  Dance 12000ms
class DancePattern02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001182], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return CheckDanceRound()


#  Dance 15000ms
class DancePattern03(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001183], state=1) # 15000ms
        set_user_value(triggerId=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=19000):
            return CheckDanceRound()


#  Dance 7000ms+ 9000ms
class DancePattern0401(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001180], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return DancePattern0402()


class DancePattern0402(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__8$', arg3='1000') # Voice 02000958
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_01')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10001180], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DancePattern0403()


class DancePattern0403(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__9$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10001180], state=2) # 7000ms
        set_interact_object(triggerIds=[10001181], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return DancePattern0404()


class DancePattern0404(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001181], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return CheckDanceRound()


#  Dance 9000ms+ 7000ms
class DancePattern0501(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001181], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return DancePattern0502()


class DancePattern0502(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__10$', arg3='1000') # Voice 02000982
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_02')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10001181], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DancePattern0503()


class DancePattern0503(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__11$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10001181], state=2) # 9000ms
        set_interact_object(triggerIds=[10001180], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return DancePattern0504()


class DancePattern0504(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001180], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return CheckDanceRound()


#  Dance 12000ms+ 7000ms
class DancePattern0601(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001182], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return DancePattern0602()


class DancePattern0602(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__12$', arg3='1000') # Voice 02000983
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_03')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10001182], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DancePattern0603()


class DancePattern0603(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__13$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10001182], state=2) # 12000ms
        set_interact_object(triggerIds=[10001180], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return DancePattern0604()


class DancePattern0604(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001180], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return CheckDanceRound()


#  Dance 7000ms+ 12000ms
class DancePattern0701(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001180], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return DancePattern0702()


class DancePattern0702(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__14$', arg3='1000') # Voice 02000984
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_04')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10001180], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DancePattern0703()


class DancePattern0703(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__15$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10001180], state=2) # 7000ms
        set_interact_object(triggerIds=[10001182], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return DancePattern0704()


class DancePattern0704(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10001182], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return CheckDanceRound()


class CheckDanceRound(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='DanceTime', value=1):
            return R01_GameStartDelay()
        if user_value(key='DanceTime', value=2):
            return R02_GameStartDelay()
        if user_value(key='DanceTime', value=3):
            return R03_GameStartDelay()
        if user_value(key='DanceTime', value=4):
            return R04_GameStartDelay()
        if user_value(key='DanceTime', value=5):
            return R05_GameStartDelay()

    def on_exit(self):
        set_user_value(key='DanceTime', value=0)


class R01_GameStartDelay(state.State):
    def on_enter(self):
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R01_GameStart()


class R01_GameStart(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=40000, arg2=True) # Game
        set_interact_object(triggerIds=[10001180], state=2) # 7000ms
        set_interact_object(triggerIds=[10001181], state=2) # 9000ms
        set_interact_object(triggerIds=[10001182], state=2) # 12000ms
        set_interact_object(triggerIds=[10001183], state=2) # 15000ms
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__16$', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R01_GameTimerStart()


class R01_GameTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=20, clearAtZero=True, display=True, arg5=-40) # Round1 / 20sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R01G00Check()


#  R01 인원 체크 시작 
#   테스트 수정 가능 지점
class R01G00Check(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=50, operator='Greater'):
            return G05P00_Random()
        if count_users(boxId=9001, boxId=40, operator='Greater'):
            return G05orG04()
        if count_users(boxId=9001, boxId=30, operator='Greater'):
            return G03orG04orG05()
        if count_users(boxId=9001, boxId=20, operator='Greater'):
            return G02orG03orG04()
        if count_users(boxId=9001, boxId=10, operator='Greater'):
            return G02orG03()
        if count_users(boxId=9001, boxId=10, operator='LessEqual'):
            return G01orG02()


#  R01  인원 체크 끝 
#  패턴 그룹 2개 랜덤 / 라운드 공용 
class G05orG04(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=80):
            return G05P00_Random()
        if random_condition(rate=20):
            return G04P00_Random()


class G03orG04orG05(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return G03P00_Random()
        if random_condition(rate=60):
            return G04P00_Random()
        if random_condition(rate=30):
            return G05P00_Random()


class G02orG03orG04(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return G02P00_Random()
        if random_condition(rate=60):
            return G03P00_Random()
        if random_condition(rate=30):
            return G04P00_Random()


class G02orG03(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=60):
            return G02P00_Random()
        if random_condition(rate=40):
            return G03P00_Random()


class G01orG02(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=70):
            return G01P00_Random()
        if random_condition(rate=30):
            return G02P00_Random()


#  G05 패턴 랜덤 / 라운드 공용 
class G05P00_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=2):
            return G05P01_RoundCheckIn()
        if random_condition(rate=2):
            return G05P02_RoundCheckIn()
        if random_condition(rate=2):
            return G05P03_RoundCheckIn()
        if random_condition(rate=2):
            return G05P04_RoundCheckIn()
        if random_condition(rate=2):
            return G05P05_RoundCheckIn()
        if random_condition(rate=2):
            return G05P06_RoundCheckIn()
        if random_condition(rate=2):
            return G05P07_RoundCheckIn()
        if random_condition(rate=2):
            return G05P08_RoundCheckIn()
        if random_condition(rate=2):
            return G05P09_RoundCheckIn()
        if random_condition(rate=2):
            return G05P10_RoundCheckIn()
        if random_condition(rate=2):
            return G05P11_RoundCheckIn()
        if random_condition(rate=2):
            return G05P12_RoundCheckIn()
        if random_condition(rate=2):
            return G05P13_RoundCheckIn()
        if random_condition(rate=2):
            return G05P14_RoundCheckIn()
        if random_condition(rate=2):
            return G05P15_RoundCheckIn()
        if random_condition(rate=2):
            return G05P16_RoundCheckIn()
        if random_condition(rate=2):
            return G05P17_RoundCheckIn()
        if random_condition(rate=2):
            return G05P18_RoundCheckIn()
        if random_condition(rate=2):
            return G05P19_RoundCheckIn()
        if random_condition(rate=2):
            return G05P20_RoundCheckIn()
        if random_condition(rate=2):
            return G05P21_RoundCheckIn()
        if random_condition(rate=2):
            return G05P22_RoundCheckIn()
        if random_condition(rate=2):
            return G05P23_RoundCheckIn()
        if random_condition(rate=2):
            return G05P24_RoundCheckIn()
        if random_condition(rate=2):
            return G05P25_RoundCheckIn()
        if random_condition(rate=2):
            return G05P26_RoundCheckIn()
        if random_condition(rate=2):
            return G05P27_RoundCheckIn()
        if random_condition(rate=2):
            return G05P28_RoundCheckIn()
        if random_condition(rate=2):
            return G05P29_RoundCheckIn()
        if random_condition(rate=2):
            return G05P30_RoundCheckIn()
        if random_condition(rate=2):
            return G05P31_RoundCheckIn()
        if random_condition(rate=2):
            return G05P32_RoundCheckIn()
        if random_condition(rate=2):
            return G05P33_RoundCheckIn()
        if random_condition(rate=2):
            return G05P34_RoundCheckIn()
        if random_condition(rate=2):
            return G05P35_RoundCheckIn()
        if random_condition(rate=2):
            return G05P36_RoundCheckIn()
        if random_condition(rate=2):
            return G05P37_RoundCheckIn()
        if random_condition(rate=2):
            return G05P38_RoundCheckIn()
        if random_condition(rate=2):
            return G05P39_RoundCheckIn()
        if random_condition(rate=2):
            return G05P40_RoundCheckIn()
        if random_condition(rate=2):
            return G05P41_RoundCheckIn()
        if random_condition(rate=2):
            return G05P42_RoundCheckIn()
        if random_condition(rate=2):
            return G05P43_RoundCheckIn()
        if random_condition(rate=2):
            return G05P44_RoundCheckIn()
        if random_condition(rate=2):
            return G05P45_RoundCheckIn()
        if random_condition(rate=2):
            return G05P46_RoundCheckIn()
        if random_condition(rate=2):
            return G05P47_RoundCheckIn()
        if random_condition(rate=2):
            return G05P48_RoundCheckIn()
        if random_condition(rate=2):
            return G05P49_RoundCheckIn()
        if random_condition(rate=2):
            return G05P50_RoundCheckIn()


#  G04 패턴 랜덤 
class G04P00_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return G04P01_RoundCheckIn()
        if random_condition(rate=5):
            return G04P02_RoundCheckIn()
        if random_condition(rate=5):
            return G04P03_RoundCheckIn()
        if random_condition(rate=5):
            return G04P04_RoundCheckIn()
        if random_condition(rate=5):
            return G04P05_RoundCheckIn()
        if random_condition(rate=5):
            return G04P06_RoundCheckIn()
        if random_condition(rate=5):
            return G04P07_RoundCheckIn()
        if random_condition(rate=5):
            return G04P08_RoundCheckIn()
        if random_condition(rate=5):
            return G04P09_RoundCheckIn()
        if random_condition(rate=5):
            return G04P10_RoundCheckIn()
        if random_condition(rate=5):
            return G04P11_RoundCheckIn()
        if random_condition(rate=5):
            return G04P12_RoundCheckIn()
        if random_condition(rate=5):
            return G04P13_RoundCheckIn()
        if random_condition(rate=5):
            return G04P14_RoundCheckIn()
        if random_condition(rate=5):
            return G04P15_RoundCheckIn()
        if random_condition(rate=5):
            return G04P16_RoundCheckIn()
        if random_condition(rate=5):
            return G04P17_RoundCheckIn()
        if random_condition(rate=5):
            return G04P18_RoundCheckIn()
        if random_condition(rate=5):
            return G04P19_RoundCheckIn()
        if random_condition(rate=5):
            return G04P20_RoundCheckIn()
        if random_condition(rate=5):
            return G04P21_RoundCheckIn()
        if random_condition(rate=5):
            return G04P22_RoundCheckIn()
        if random_condition(rate=5):
            return G04P23_RoundCheckIn()
        if random_condition(rate=5):
            return G04P24_RoundCheckIn()
        if random_condition(rate=5):
            return G04P25_RoundCheckIn()
        if random_condition(rate=5):
            return G04P26_RoundCheckIn()
        if random_condition(rate=5):
            return G04P27_RoundCheckIn()
        if random_condition(rate=5):
            return G04P28_RoundCheckIn()
        if random_condition(rate=5):
            return G04P29_RoundCheckIn()
        if random_condition(rate=5):
            return G04P30_RoundCheckIn()
        if random_condition(rate=5):
            return G04P31_RoundCheckIn()
        if random_condition(rate=5):
            return G04P32_RoundCheckIn()
        if random_condition(rate=5):
            return G04P33_RoundCheckIn()
        if random_condition(rate=5):
            return G04P34_RoundCheckIn()
        if random_condition(rate=5):
            return G04P35_RoundCheckIn()
        if random_condition(rate=5):
            return G04P36_RoundCheckIn()
        if random_condition(rate=5):
            return G04P37_RoundCheckIn()
        if random_condition(rate=5):
            return G04P38_RoundCheckIn()
        if random_condition(rate=5):
            return G04P39_RoundCheckIn()
        if random_condition(rate=5):
            return G04P40_RoundCheckIn()


#  G03 패턴 랜덤 
class G03P00_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return G03P01_RoundCheckIn()
        if random_condition(rate=5):
            return G03P02_RoundCheckIn()
        if random_condition(rate=5):
            return G03P03_RoundCheckIn()
        if random_condition(rate=5):
            return G03P04_RoundCheckIn()
        if random_condition(rate=5):
            return G03P05_RoundCheckIn()
        if random_condition(rate=5):
            return G03P06_RoundCheckIn()
        if random_condition(rate=5):
            return G03P07_RoundCheckIn()
        if random_condition(rate=5):
            return G03P08_RoundCheckIn()
        if random_condition(rate=5):
            return G03P09_RoundCheckIn()
        if random_condition(rate=5):
            return G03P10_RoundCheckIn()
        if random_condition(rate=5):
            return G03P11_RoundCheckIn()
        if random_condition(rate=5):
            return G03P12_RoundCheckIn()
        if random_condition(rate=5):
            return G03P13_RoundCheckIn()
        if random_condition(rate=5):
            return G03P14_RoundCheckIn()
        if random_condition(rate=5):
            return G03P15_RoundCheckIn()
        if random_condition(rate=5):
            return G03P16_RoundCheckIn()
        if random_condition(rate=5):
            return G03P17_RoundCheckIn()
        if random_condition(rate=5):
            return G03P18_RoundCheckIn()
        if random_condition(rate=5):
            return G03P19_RoundCheckIn()
        if random_condition(rate=5):
            return G03P20_RoundCheckIn()
        if random_condition(rate=5):
            return G03P21_RoundCheckIn()
        if random_condition(rate=5):
            return G03P22_RoundCheckIn()
        if random_condition(rate=5):
            return G03P23_RoundCheckIn()
        if random_condition(rate=5):
            return G03P24_RoundCheckIn()
        if random_condition(rate=5):
            return G03P25_RoundCheckIn()
        if random_condition(rate=5):
            return G03P26_RoundCheckIn()
        if random_condition(rate=5):
            return G03P27_RoundCheckIn()
        if random_condition(rate=5):
            return G03P28_RoundCheckIn()
        if random_condition(rate=5):
            return G03P29_RoundCheckIn()
        if random_condition(rate=5):
            return G03P30_RoundCheckIn()


#  G02 패턴 랜덤 
class G02P00_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return G02P01_RoundCheckIn()
        if random_condition(rate=5):
            return G02P02_RoundCheckIn()
        if random_condition(rate=5):
            return G02P03_RoundCheckIn()
        if random_condition(rate=5):
            return G02P04_RoundCheckIn()
        if random_condition(rate=5):
            return G02P05_RoundCheckIn()
        if random_condition(rate=5):
            return G02P06_RoundCheckIn()
        if random_condition(rate=5):
            return G02P07_RoundCheckIn()
        if random_condition(rate=5):
            return G02P08_RoundCheckIn()
        if random_condition(rate=5):
            return G02P09_RoundCheckIn()
        if random_condition(rate=5):
            return G02P10_RoundCheckIn()
        if random_condition(rate=5):
            return G02P11_RoundCheckIn()
        if random_condition(rate=5):
            return G02P12_RoundCheckIn()
        if random_condition(rate=5):
            return G02P13_RoundCheckIn()
        if random_condition(rate=5):
            return G02P14_RoundCheckIn()
        if random_condition(rate=5):
            return G02P15_RoundCheckIn()
        if random_condition(rate=5):
            return G02P16_RoundCheckIn()
        if random_condition(rate=5):
            return G02P17_RoundCheckIn()
        if random_condition(rate=5):
            return G02P18_RoundCheckIn()
        if random_condition(rate=5):
            return G02P19_RoundCheckIn()
        if random_condition(rate=5):
            return G02P20_RoundCheckIn()
        if random_condition(rate=5):
            return G02P21_RoundCheckIn()
        if random_condition(rate=5):
            return G02P22_RoundCheckIn()
        if random_condition(rate=5):
            return G02P23_RoundCheckIn()
        if random_condition(rate=5):
            return G02P24_RoundCheckIn()
        if random_condition(rate=5):
            return G02P25_RoundCheckIn()
        if random_condition(rate=5):
            return G02P26_RoundCheckIn()
        if random_condition(rate=5):
            return G02P27_RoundCheckIn()
        if random_condition(rate=5):
            return G02P28_RoundCheckIn()
        if random_condition(rate=5):
            return G02P29_RoundCheckIn()
        if random_condition(rate=5):
            return G02P30_RoundCheckIn()


#  G01 패턴 랜덤 
class G01P00_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return G01P01_RoundCheckIn()
        if random_condition(rate=5):
            return G01P02_RoundCheckIn()
        if random_condition(rate=5):
            return G01P03_RoundCheckIn()
        if random_condition(rate=5):
            return G01P04_RoundCheckIn()
        if random_condition(rate=5):
            return G01P05_RoundCheckIn()
        if random_condition(rate=5):
            return G01P06_RoundCheckIn()
        if random_condition(rate=5):
            return G01P07_RoundCheckIn()
        if random_condition(rate=5):
            return G01P08_RoundCheckIn()
        if random_condition(rate=5):
            return G01P09_RoundCheckIn()
        if random_condition(rate=5):
            return G01P10_RoundCheckIn()
        if random_condition(rate=5):
            return G01P11_RoundCheckIn()
        if random_condition(rate=5):
            return G01P12_RoundCheckIn()
        if random_condition(rate=5):
            return G01P13_RoundCheckIn()
        if random_condition(rate=5):
            return G01P14_RoundCheckIn()
        if random_condition(rate=5):
            return G01P15_RoundCheckIn()
        if random_condition(rate=5):
            return G01P16_RoundCheckIn()
        if random_condition(rate=5):
            return G01P17_RoundCheckIn()
        if random_condition(rate=5):
            return G01P18_RoundCheckIn()
        if random_condition(rate=5):
            return G01P19_RoundCheckIn()
        if random_condition(rate=5):
            return G01P20_RoundCheckIn()
        if random_condition(rate=5):
            return G01P21_RoundCheckIn()
        if random_condition(rate=5):
            return G01P22_RoundCheckIn()
        if random_condition(rate=5):
            return G01P23_RoundCheckIn()
        if random_condition(rate=5):
            return G01P24_RoundCheckIn()
        if random_condition(rate=5):
            return G01P25_RoundCheckIn()
        if random_condition(rate=5):
            return G01P26_RoundCheckIn()
        if random_condition(rate=5):
            return G01P27_RoundCheckIn()
        if random_condition(rate=5):
            return G01P28_RoundCheckIn()
        if random_condition(rate=5):
            return G01P29_RoundCheckIn()
        if random_condition(rate=5):
            return G01P30_RoundCheckIn()


#  R01 종료 
class R01EndDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7120, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7130, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7140, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7210, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7220, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7230, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7240, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7310, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7320, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7330, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7340, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7410, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7420, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7430, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7440, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=4, key='RoundScoreRecord', value=1) # 스코어 배너 기록
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R01End()


class R01End(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)
        set_user_value(triggerId=8110, key='Barrier11', value=10)
        set_user_value(triggerId=8120, key='Barrier12', value=10)
        set_user_value(triggerId=8130, key='Barrier13', value=10)
        set_user_value(triggerId=8140, key='Barrier14', value=10)
        set_user_value(triggerId=8210, key='Barrier21', value=10)
        set_user_value(triggerId=8220, key='Barrier22', value=10)
        set_user_value(triggerId=8230, key='Barrier23', value=10)
        set_user_value(triggerId=8240, key='Barrier24', value=10)
        set_user_value(triggerId=8310, key='Barrier31', value=10)
        set_user_value(triggerId=8320, key='Barrier32', value=10)
        set_user_value(triggerId=8330, key='Barrier33', value=10)
        set_user_value(triggerId=8340, key='Barrier34', value=10)
        set_user_value(triggerId=8410, key='Barrier41', value=10)
        set_user_value(triggerId=8420, key='Barrier42', value=10)
        set_user_value(triggerId=8430, key='Barrier43', value=10)
        set_user_value(triggerId=8440, key='Barrier44', value=10)
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return RoundResultNotice01()


class RoundResultNotice01(state.State):
    def on_tick(self) -> state.State:
        if guild_vs_game_scored_team(teamId=1):
            return RoundResult_BlueTeamWin01()
        if guild_vs_game_scored_team(teamId=2):
            return RoundResult_RedTeamWin01()
        if guild_vs_game_scored_team(teamId=0):
            return RoundResult_Draw01()


class RoundResult_BlueTeamWin01(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__17$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__18$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R01RoundScoreRecord()


class RoundResult_RedTeamWin01(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__19$', duration=4000, userTagId=2)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__20$', duration=4000, userTagId=1)
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R01RoundScoreRecord()


class RoundResult_Draw01(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__21$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__22$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_Draw_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_Draw_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R01RoundScoreRecord()


#  R01 라운드 승패 판정 
class R01RoundScoreRecord(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='WinnerTeam', value=0):
            return EveryPlayerVacuumGuide()
        if user_value(key='WinnerTeam', value=1):
            return BlueTeamWinAlreadyNotice()
        if user_value(key='WinnerTeam', value=2):
            return RedTeamWinAlreadyNotice()


#  라운드 종료 멤버 리셋 / 라운드 공용
class EveryPlayerVacuumGuide(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__23$', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EveryPlayerVacuumExecute()


class EveryPlayerVacuumExecute(state.State):
    def on_enter(self):
        move_to_portal(boxId=9001, userTagId=1, portalId=21) # Tag1=Blue 통과자들 진영으로
        move_to_portal(boxId=9001, userTagId=2, portalId=22) # Tag2=Red 통과자들 진영으로

    def on_tick(self) -> state.State:
        if user_value(key='Round', value=1):
            return R02Ready()
        if user_value(key='Round', value=2):
            return R03Ready()
        if user_value(key='Round', value=3):
            return R04Ready()
        if user_value(key='Round', value=4):
            return R05Ready()

    def on_exit(self):
        set_user_value(triggerId=11, key='BannerCheckIn', value=1) # 게임판 위 인원수 배너 표시


#  R02 시작
class R02Ready(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=2)
        set_event_ui(type=0, arg2='2,5') # Round2

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R02PlayerRandomPick01()


#  무작위 이동 안내 전 안내 / 2,3,4 라운드 전용
class R02PlayerRandomPick01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__4$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PlayerRandomPick02()


#  무작위 이동 안내 / 라운드 공용 
class R02Start(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__24$', arg3='3000', arg4='0') # Voice 02000954
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancetime_02')
        set_sound(triggerId=40000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R02DanceTime()


#  R02 DanceTime 패턴 랜덤 
class R02DanceTime(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        set_user_value(key='DanceTime', value=2)

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return DancePattern01()
        if random_condition(rate=30):
            return DancePattern02()
        if random_condition(rate=30):
            return DancePattern03()
        if random_condition(rate=3):
            return DancePattern0401()
        if random_condition(rate=3):
            return DancePattern0501()
        if random_condition(rate=2):
            return DancePattern0601()
        if random_condition(rate=2):
            return DancePattern0701()


#  DancePattern & CheckDanceRound 
class R02_GameStartDelay(state.State):
    def on_enter(self):
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R02_GameStart()


class R02_GameStart(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=40000, arg2=True) # Game
        set_interact_object(triggerIds=[10001180], state=2) # 7000ms
        set_interact_object(triggerIds=[10001181], state=2) # 9000ms
        set_interact_object(triggerIds=[10001182], state=2) # 12000ms
        set_interact_object(triggerIds=[10001183], state=2) # 15000ms
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__25$', arg3='4000') # Voice 02000960
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R02_GameTimerStart()


class R02_GameTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=20, clearAtZero=True, display=True, arg5=-40) # Round2 / 20sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R02G00Check()


#  R02 인원 체크 시작 
#   테스트 수정 가능 지점
class R02G00Check(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=50, operator='Greater'):
            return G05P00_Random()
        if count_users(boxId=9001, boxId=40, operator='Greater'):
            return G05orG04()
        if count_users(boxId=9001, boxId=30, operator='Greater'):
            return G03orG04orG05()
        if count_users(boxId=9001, boxId=20, operator='Greater'):
            return G02orG03orG04()
        if count_users(boxId=9001, boxId=10, operator='Greater'):
            return G02orG03()
        if count_users(boxId=9001, boxId=10, operator='LessEqual'):
            return G01orG02()


#  R02 인원 체크 끝 
class R02EndDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7120, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7130, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7140, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7210, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7220, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7230, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7240, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7310, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7320, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7330, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7340, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7410, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7420, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7430, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7440, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=4, key='RoundScoreRecord', value=2) # 스코어 배너 기록
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R02End()


class R02End(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)
        set_user_value(triggerId=8110, key='Barrier11', value=10)
        set_user_value(triggerId=8120, key='Barrier12', value=10)
        set_user_value(triggerId=8130, key='Barrier13', value=10)
        set_user_value(triggerId=8140, key='Barrier14', value=10)
        set_user_value(triggerId=8210, key='Barrier21', value=10)
        set_user_value(triggerId=8220, key='Barrier22', value=10)
        set_user_value(triggerId=8230, key='Barrier23', value=10)
        set_user_value(triggerId=8240, key='Barrier24', value=10)
        set_user_value(triggerId=8310, key='Barrier31', value=10)
        set_user_value(triggerId=8320, key='Barrier32', value=10)
        set_user_value(triggerId=8330, key='Barrier33', value=10)
        set_user_value(triggerId=8340, key='Barrier34', value=10)
        set_user_value(triggerId=8410, key='Barrier41', value=10)
        set_user_value(triggerId=8420, key='Barrier42', value=10)
        set_user_value(triggerId=8430, key='Barrier43', value=10)
        set_user_value(triggerId=8440, key='Barrier44', value=10)
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return RoundResultNotice02()


class RoundResultNotice02(state.State):
    def on_tick(self) -> state.State:
        if guild_vs_game_scored_team(teamId=1):
            return RoundResult_BlueTeamWin02()
        if guild_vs_game_scored_team(teamId=2):
            return RoundResult_RedTeamWin02()
        if guild_vs_game_scored_team(teamId=0):
            return RoundResult_Draw02()


class RoundResult_BlueTeamWin02(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__26$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__27$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R02RoundScoreRecord()


class RoundResult_RedTeamWin02(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__28$', duration=4000, userTagId=2)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__29$', duration=4000, userTagId=1)
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R02RoundScoreRecord()


class RoundResult_Draw02(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__30$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__31$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_Draw_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_Draw_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R02RoundScoreRecord()


#  R02 라운드 승패 판정 
class R02RoundScoreRecord(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='WinnerTeam', value=0):
            return EveryPlayerVacuumGuide()
        if user_value(key='WinnerTeam', value=1):
            return BlueTeamWinAlreadyNotice()
        if user_value(key='WinnerTeam', value=2):
            return RedTeamWinAlreadyNotice()


#  라운드 종료 멤버 리셋 / 라운드 공용
#  R03 시작
class R03Ready(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=3)
        set_event_ui(type=0, arg2='3,5') # Round3

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R02PlayerRandomPick01()


class R03Start(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__32$', arg3='3000', arg4='0') # Voice 02000955
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancetime_03')
        set_sound(triggerId=40000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R03DanceTime()


#  R03 DanceTime 패턴 랜덤 
class R03DanceTime(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        set_user_value(key='DanceTime', value=3)

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return DancePattern01()
        if random_condition(rate=30):
            return DancePattern02()
        if random_condition(rate=30):
            return DancePattern03()
        if random_condition(rate=3):
            return DancePattern0401()
        if random_condition(rate=3):
            return DancePattern0501()
        if random_condition(rate=2):
            return DancePattern0601()
        if random_condition(rate=2):
            return DancePattern0701()


#  DancePattern & CheckDanceRound 
class R03_GameStartDelay(state.State):
    def on_enter(self):
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R03_GameStart()


class R03_GameStart(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=40000, arg2=True) # Game
        set_interact_object(triggerIds=[10001180], state=2) # 7000ms
        set_interact_object(triggerIds=[10001181], state=2) # 9000ms
        set_interact_object(triggerIds=[10001182], state=2) # 12000ms
        set_interact_object(triggerIds=[10001183], state=2) # 15000ms
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__33$', arg3='4000') # Voice 02000961
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_03')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R03_GameTimerStart()


class R03_GameTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=20, clearAtZero=True, display=True, arg5=-40) # Round3 / 20sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R03G00Check()


#  R03 인원 체크 시작 
#   테스트 수정 가능 지점
class R03G00Check(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=50, operator='Greater'):
            return G05P00_Random()
        if count_users(boxId=9001, boxId=40, operator='Greater'):
            return G05orG04()
        if count_users(boxId=9001, boxId=30, operator='Greater'):
            return G03orG04orG05()
        if count_users(boxId=9001, boxId=20, operator='Greater'):
            return G02orG03orG04()
        if count_users(boxId=9001, boxId=10, operator='Greater'):
            return G02orG03()
        if count_users(boxId=9001, boxId=10, operator='LessEqual'):
            return G01orG02()


#  R03 인원 체크 끝 
class R03EndDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7120, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7130, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7140, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7210, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7220, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7230, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7240, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7310, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7320, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7330, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7340, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7410, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7420, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7430, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7440, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=4, key='RoundScoreRecord', value=3) # 스코어 배너 기록
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R03End()


class R03End(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)
        set_user_value(triggerId=8110, key='Barrier11', value=10)
        set_user_value(triggerId=8120, key='Barrier12', value=10)
        set_user_value(triggerId=8130, key='Barrier13', value=10)
        set_user_value(triggerId=8140, key='Barrier14', value=10)
        set_user_value(triggerId=8210, key='Barrier21', value=10)
        set_user_value(triggerId=8220, key='Barrier22', value=10)
        set_user_value(triggerId=8230, key='Barrier23', value=10)
        set_user_value(triggerId=8240, key='Barrier24', value=10)
        set_user_value(triggerId=8310, key='Barrier31', value=10)
        set_user_value(triggerId=8320, key='Barrier32', value=10)
        set_user_value(triggerId=8330, key='Barrier33', value=10)
        set_user_value(triggerId=8340, key='Barrier34', value=10)
        set_user_value(triggerId=8410, key='Barrier41', value=10)
        set_user_value(triggerId=8420, key='Barrier42', value=10)
        set_user_value(triggerId=8430, key='Barrier43', value=10)
        set_user_value(triggerId=8440, key='Barrier44', value=10)
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return RoundResultNotice03()


class RoundResultNotice03(state.State):
    def on_tick(self) -> state.State:
        if guild_vs_game_scored_team(teamId=1):
            return RoundResult_BlueTeamWin03()
        if guild_vs_game_scored_team(teamId=2):
            return RoundResult_RedTeamWin03()
        if guild_vs_game_scored_team(teamId=0):
            return RoundResult_Draw03()


class RoundResult_BlueTeamWin03(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__34$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__35$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R03RoundScoreRecord()


class RoundResult_RedTeamWin03(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__36$', duration=4000, userTagId=2)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__37$', duration=4000, userTagId=1)
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R03RoundScoreRecord()


class RoundResult_Draw03(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__38$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__39$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_Draw_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_Draw_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R03RoundScoreRecord()


#  R03 라운드 승패 판정 
class R03RoundScoreRecord(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='WinnerTeam', value=0):
            return EveryPlayerVacuumGuide()
        if user_value(key='WinnerTeam', value=1):
            return BlueTeamWinAlreadyNotice()
        if user_value(key='WinnerTeam', value=2):
            return RedTeamWinAlreadyNotice()


#  라운드 종료 멤버 리셋 / 라운드 공용
#  R04 시작
class R04Ready(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=4)
        set_event_ui(type=0, arg2='4,5') # Round4

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R02PlayerRandomPick01()


class R04Start(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__40$', arg3='3000', arg4='0') # Voice 02000956
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancetime_04')
        set_sound(triggerId=40000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R04DanceTime()


#  R04 DanceTime 패턴 랜덤 
class R04DanceTime(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        set_user_value(key='DanceTime', value=4)

    def on_tick(self) -> state.State:
        if random_condition(rate=2):
            return DancePattern01()
        if random_condition(rate=3):
            return DancePattern02()
        if random_condition(rate=5):
            return DancePattern03()
        if random_condition(rate=25):
            return DancePattern0401()
        if random_condition(rate=25):
            return DancePattern0501()
        if random_condition(rate=20):
            return DancePattern0601()
        if random_condition(rate=20):
            return DancePattern0701()


#  DancePattern & CheckDanceRound 
class R04_GameStartDelay(state.State):
    def on_enter(self):
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R04_GameStart()


#  R04 Normal Game 
class R04_GameStart(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=40000, arg2=True) # Game
        set_interact_object(triggerIds=[10001180], state=2) # 7000ms
        set_interact_object(triggerIds=[10001181], state=2) # 9000ms
        set_interact_object(triggerIds=[10001182], state=2) # 12000ms
        set_interact_object(triggerIds=[10001183], state=2) # 15000ms
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__41$', arg3='4000') # Voice 02000962
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_04')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R04_GameTimerStart()


class R04_GameTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=20, clearAtZero=True, display=True, arg5=-40) # Round4 / 20sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R04G00Check()


#  R04 인원 체크 시작 
#   테스트 수정 가능 지점
class R04G00Check(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=50, operator='Greater'):
            return G05P00_Random()
        if count_users(boxId=9001, boxId=40, operator='Greater'):
            return G05orG04()
        if count_users(boxId=9001, boxId=30, operator='Greater'):
            return G03orG04orG05()
        if count_users(boxId=9001, boxId=20, operator='Greater'):
            return G02orG03orG04()
        if count_users(boxId=9001, boxId=10, operator='Greater'):
            return G02orG03()
        if count_users(boxId=9001, boxId=10, operator='LessEqual'):
            return G01orG02()


#  R04 인원 체크 끝 
#  R04 Normal End 
class R04EndDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7120, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7130, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7140, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7210, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7220, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7230, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7240, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7310, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7320, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7330, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7340, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7410, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7420, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7430, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7440, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=4, key='RoundScoreRecord', value=4) # 스코어 배너 기록
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R04End()


class R04End(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)
        set_user_value(triggerId=8110, key='Barrier11', value=10)
        set_user_value(triggerId=8120, key='Barrier12', value=10)
        set_user_value(triggerId=8130, key='Barrier13', value=10)
        set_user_value(triggerId=8140, key='Barrier14', value=10)
        set_user_value(triggerId=8210, key='Barrier21', value=10)
        set_user_value(triggerId=8220, key='Barrier22', value=10)
        set_user_value(triggerId=8230, key='Barrier23', value=10)
        set_user_value(triggerId=8240, key='Barrier24', value=10)
        set_user_value(triggerId=8310, key='Barrier31', value=10)
        set_user_value(triggerId=8320, key='Barrier32', value=10)
        set_user_value(triggerId=8330, key='Barrier33', value=10)
        set_user_value(triggerId=8340, key='Barrier34', value=10)
        set_user_value(triggerId=8410, key='Barrier41', value=10)
        set_user_value(triggerId=8420, key='Barrier42', value=10)
        set_user_value(triggerId=8430, key='Barrier43', value=10)
        set_user_value(triggerId=8440, key='Barrier44', value=10)
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return RoundResultNotice04()


class RoundResultNotice04(state.State):
    def on_tick(self) -> state.State:
        if guild_vs_game_scored_team(teamId=1):
            return RoundResult_BlueTeamWin04()
        if guild_vs_game_scored_team(teamId=2):
            return RoundResult_RedTeamWin04()
        if guild_vs_game_scored_team(teamId=0):
            return RoundResult_Draw04()


class RoundResult_BlueTeamWin04(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__42$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__43$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R04RoundScoreRecord()


class RoundResult_RedTeamWin04(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__44$', duration=4000, userTagId=2)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__45$', duration=4000, userTagId=1)
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R04RoundScoreRecord()


class RoundResult_Draw04(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__46$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__47$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_Draw_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_Draw_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return R04RoundScoreRecord()


#  R04 라운드 승패 판정 
class R04RoundScoreRecord(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='WinnerTeam', value=0):
            return EveryPlayerVacuumGuide()
        if user_value(key='WinnerTeam', value=1):
            return BlueTeamWinAlreadyNotice()
        if user_value(key='WinnerTeam', value=2):
            return RedTeamWinAlreadyNotice()


#  라운드 종료 멤버 리셋 / 라운드 공용
#  R05 시작
class R05Ready(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=5)
        set_event_ui(type=0, arg2='5,5') # Round5

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R05PlayerRandomPick01()


#  무작위 이동 안내 전 안내 / 5 라운드 전용
class R05PlayerRandomPick01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__68$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PlayerRandomPick02()


class R05Start(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__48$', arg3='3000', arg4='0') # Voice 02000957
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancetime_05')
        set_sound(triggerId=40000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R05DanceTime()


#  R05 DanceTime 패턴 랜덤 
class R05DanceTime(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        set_user_value(key='DanceTime', value=5)

    def on_tick(self) -> state.State:
        if random_condition(rate=2):
            return DancePattern01()
        if random_condition(rate=3):
            return DancePattern02()
        if random_condition(rate=5):
            return DancePattern03()
        if random_condition(rate=20):
            return DancePattern0401()
        if random_condition(rate=20):
            return DancePattern0501()
        if random_condition(rate=25):
            return DancePattern0601()
        if random_condition(rate=25):
            return DancePattern0701()


#  DancePattern & CheckDanceRound 
class R05_GameStartDelay(state.State):
    def on_enter(self):
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R05_GameStart()


class R05_GameStart(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=40000, arg2=True) # Game
        set_interact_object(triggerIds=[10001180], state=2) # 7000ms
        set_interact_object(triggerIds=[10001181], state=2) # 9000ms
        set_interact_object(triggerIds=[10001182], state=2) # 12000ms
        set_interact_object(triggerIds=[10001183], state=2) # 15000ms
        set_event_ui(type=1, arg2='$66200001_GD__01_MASSIVEMAIN__49$', arg3='4000') # Voice 02000963
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_05')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R05_GameTimerStart()


class R05_GameTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=20, clearAtZero=True, display=True, arg5=-40) # Round5 / 20sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R05G05Check()


#  R05 인원 체크 시작 
#   테스트 수정 가능 지점
class R05G05Check(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=50, operator='Greater'):
            return G05P00_Random()
        if count_users(boxId=9001, boxId=40, operator='Greater'):
            return G05orG04()
        if count_users(boxId=9001, boxId=30, operator='Greater'):
            return G03orG04orG05()
        if count_users(boxId=9001, boxId=20, operator='Greater'):
            return G02orG03orG04()
        if count_users(boxId=9001, boxId=10, operator='Greater'):
            return G02orG03()
        if count_users(boxId=9001, boxId=10, operator='LessEqual'):
            return G01orG02()


#  R05 인원 체크 끝 
class R05EndDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7120, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7130, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7140, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7210, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7220, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7230, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7240, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7310, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7320, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7330, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7340, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7410, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7420, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7430, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=7440, key='ColorEnd', value=1) # color reset
        set_user_value(triggerId=4, key='RoundScoreRecord', value=5) # 스코어 배너 기록
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R05End()


class R05End(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)
        set_user_value(triggerId=8110, key='Barrier11', value=10)
        set_user_value(triggerId=8120, key='Barrier12', value=10)
        set_user_value(triggerId=8130, key='Barrier13', value=10)
        set_user_value(triggerId=8140, key='Barrier14', value=10)
        set_user_value(triggerId=8210, key='Barrier21', value=10)
        set_user_value(triggerId=8220, key='Barrier22', value=10)
        set_user_value(triggerId=8230, key='Barrier23', value=10)
        set_user_value(triggerId=8240, key='Barrier24', value=10)
        set_user_value(triggerId=8310, key='Barrier31', value=10)
        set_user_value(triggerId=8320, key='Barrier32', value=10)
        set_user_value(triggerId=8330, key='Barrier33', value=10)
        set_user_value(triggerId=8340, key='Barrier34', value=10)
        set_user_value(triggerId=8410, key='Barrier41', value=10)
        set_user_value(triggerId=8420, key='Barrier42', value=10)
        set_user_value(triggerId=8430, key='Barrier43', value=10)
        set_user_value(triggerId=8440, key='Barrier44', value=10)
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return RoundResultNotice05()


class RoundResultNotice05(state.State):
    def on_tick(self) -> state.State:
        if guild_vs_game_scored_team(teamId=1):
            return RoundResult_BlueTeamWin05()
        if guild_vs_game_scored_team(teamId=2):
            return RoundResult_RedTeamWin05()
        if guild_vs_game_scored_team(teamId=0):
            return RoundResult_Draw05()


class RoundResult_BlueTeamWin05(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__50$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__51$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameWrapUp_EveryPlayerVacuumExecute()


class RoundResult_RedTeamWin05(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__52$', duration=4000, userTagId=2)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__53$', duration=4000, userTagId=1)
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameWrapUp_EveryPlayerVacuumExecute()


class RoundResult_Draw05(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__54$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__55$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_Draw_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_Draw_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameWrapUp_EveryPlayerVacuumExecute()


#  게임 종료 모든 팀원 각 진영으로 
class GameWrapUp_EveryPlayerVacuumExecute(state.State):
    def on_enter(self):
        move_to_portal(boxId=9001, userTagId=1, portalId=21) # Tag1=Blue 통과자들 진영으로
        move_to_portal(boxId=9001, userTagId=2, portalId=22) # Tag2=Red 통과자들 진영으로

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return R05RoundScoreRecord()

    def on_exit(self):
        set_user_value(triggerId=11, key='BannerCheckIn', value=1) # 게임판 위 인원수 배너 표시


#  최종 라운드 승패 판정 
class R05RoundScoreRecord(state.State):
    def on_tick(self) -> state.State:
        if guild_vs_game_winner_team(teamId=1):
            return BlueTeamWin_GiveReward()
        if guild_vs_game_winner_team(teamId=2):
            return RedTeamWin_GiveReward()
        if guild_vs_game_winner_team(teamId=0):
            return DrawGame_GiveReward()


#  5 라운드 이전 승패 판정 
class BlueTeamWinAlreadyNotice(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__56$', duration=3000, userTagId=1) # BlueTeam 승리
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__57$', duration=3000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return BlueTeamWinWinAlready_VacuumExecute()


class BlueTeamWinWinAlready_VacuumExecute(state.State):
    def on_enter(self):
        move_to_portal(boxId=9001, userTagId=1, portalId=21) # Tag1=Blue 통과자들 진영으로
        move_to_portal(boxId=9001, userTagId=2, portalId=22) # Tag2=Red 통과자들 진영으로

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BlueTeamWin_GiveReward()


class RedTeamWinAlreadyNotice(state.State):
    def on_enter(self):
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__58$', duration=3000, userTagId=2) # RedTeam 승리
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__59$', duration=3000, userTagId=1)
        play_system_sound_by_user_tag(userTagId=2, soundKey='System_YouWin_01')
        play_system_sound_by_user_tag(userTagId=1, soundKey='System_YouLose_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return RedTeamWinAlready_VacuumExecute()


class RedTeamWinAlready_VacuumExecute(state.State):
    def on_enter(self):
        move_to_portal(boxId=9001, userTagId=1, portalId=21) # Tag1=Blue 통과자들 진영으로
        move_to_portal(boxId=9001, userTagId=2, portalId=22) # Tag2=Red 통과자들 진영으로

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return RedTeamWin_GiveReward()


#  정상 게임 1팀 블루팀 승리 
class BlueTeamWin_GiveReward(state.State):
    def on_enter(self):
        guild_vs_game_give_reward(type='fund', teamId=1, isWin=True) # BlueTeam 승리
        guild_vs_game_give_reward(type='exp', teamId=1, isWin=True) # BlueTeam 승리
        guild_vs_game_give_reward(type='guildCoin', teamId=1, isWin=True) # BlueTeam 승리
        guild_vs_game_give_contribution(teamId=1, isWin=True) # BlueTeam 승리
        guild_vs_game_give_reward(type='fund', teamId=2, isWin=False) # RedTeam 패배
        guild_vs_game_give_reward(type='exp', teamId=2, isWin=False) # RedTeam 패배
        guild_vs_game_give_reward(type='guildCoin', teamId=2, isWin=False) # RedTeam 패배
        guild_vs_game_give_contribution(teamId=2, isWin=False) # RedTeam 패배

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ResultPopUp_BlueTeamWin()


#  정상 게임 2팀 레드팀 승리 
class RedTeamWin_GiveReward(state.State):
    def on_enter(self):
        guild_vs_game_give_reward(type='fund', teamId=2, isWin=True) # RedTeam 승리
        guild_vs_game_give_reward(type='exp', teamId=2, isWin=True) # RedTeam 승리
        guild_vs_game_give_reward(type='guildCoin', teamId=2, isWin=True) # RedTeam 승리
        guild_vs_game_give_contribution(teamId=2, isWin=True) # RedTeam 승리
        guild_vs_game_give_reward(type='fund', teamId=1, isWin=False) # BlueTeam 패배
        guild_vs_game_give_reward(type='exp', teamId=1, isWin=False) # BlueTeam 패배
        guild_vs_game_give_reward(type='guildCoin', teamId=1, isWin=False) # BlueTeam 패배
        guild_vs_game_give_contribution(teamId=1, isWin=False) # BlueTeam 패배

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ResultPopUp_RedTeamWin()


#  정상 게임 무승부 
class DrawGame_GiveReward(state.State):
    def on_enter(self):
        guild_vs_game_give_reward(type='fund', teamId=1, isWin=False) # BlueTeam 무승부
        guild_vs_game_give_reward(type='exp', teamId=1, isWin=False) # BlueTeam 무승부
        guild_vs_game_give_reward(type='guildCoin', teamId=1, isWin=False) # BlueTeam 무승부
        guild_vs_game_give_contribution(teamId=1, isWin=False) # BlueTeam 무승부
        guild_vs_game_give_reward(type='fund', teamId=2, isWin=False) # RedTeam 무승부
        guild_vs_game_give_reward(type='exp', teamId=2, isWin=False) # RedTeam 무승부
        guild_vs_game_give_reward(type='guildCoin', teamId=2, isWin=False) # RedTeam 무승부
        guild_vs_game_give_contribution(teamId=2, isWin=False) # RedTeam 무승부

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ResultPopUp_Draw()


#  블루팀 승리 결과창 팝업 
class ResultPopUp_BlueTeamWin(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='0,0')
        guild_vs_game_result()
        guild_vs_game_log_result()
        play_system_sound_by_user_tag(userTagId=1, soundKey='massive_success')
        play_system_sound_by_user_tag(userTagId=2, soundKey='massive_fail')
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return LeaveAll()


#  레드팀 승리 결과창 팝업 
class ResultPopUp_RedTeamWin(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='0,0')
        guild_vs_game_result()
        guild_vs_game_log_result()
        play_system_sound_by_user_tag(userTagId=2, soundKey='massive_success')
        play_system_sound_by_user_tag(userTagId=1, soundKey='massive_fail')
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return LeaveAll()


#  무승부 결과창 팝업 
class ResultPopUp_Draw(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='0,0')
        guild_vs_game_result()
        guild_vs_game_log_result()
        play_system_sound_by_user_tag(userTagId=2, soundKey='massive_fail')
        play_system_sound_by_user_tag(userTagId=1, soundKey='massive_fail')
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return LeaveAll()


#  1팀=블루팀 부전승 
class DefaultbyWin_BlueTeam(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='0,0')
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__60$', duration=4000, userTagId=1)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__61$', duration=4000, userTagId=2)
        play_system_sound_by_user_tag(userTagId=1, soundKey='massive_success')
        play_system_sound_by_user_tag(userTagId=2, soundKey='massive_fail')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefaultbyWin_BlueTeam_GiveReward()


class DefaultbyWin_BlueTeam_GiveReward(state.State):
    def on_enter(self):
        guild_vs_game_give_reward(type='fund', teamId=1, isWin=False) # BlueTeam 부전승
        guild_vs_game_give_reward(type='exp', teamId=1, isWin=False) # BlueTeam 부전승
        guild_vs_game_give_reward(type='guildCoin', teamId=1, isWin=False) # BlueTeam 부전승
        guild_vs_game_give_contribution(teamId=1, isWin=False) # BlueTeam 부전승
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        guild_vs_game_log_won_by_default(teamId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LeaveAll()


#  2팀=레드팀 부전승 
class DefaultbyWin_RedTeam(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='0,0')
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__62$', duration=4000, userTagId=2)
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__63$', duration=4000, userTagId=1)
        play_system_sound_by_user_tag(userTagId=2, soundKey='massive_success')
        play_system_sound_by_user_tag(userTagId=1, soundKey='massive_fail')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefaultbyWin_RedTeam_GiveReward()


class DefaultbyWin_RedTeam_GiveReward(state.State):
    def on_enter(self):
        guild_vs_game_give_reward(type='fund', teamId=2, isWin=False) # RedTeam 부전승
        guild_vs_game_give_reward(type='exp', teamId=2, isWin=False) # RedTeam 부전승
        guild_vs_game_give_reward(type='guildCoin', teamId=2, isWin=False) # BlueTeam 부전승
        guild_vs_game_give_contribution(teamId=2, isWin=False) # RedTeam 부전승
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        guild_vs_game_log_won_by_default(teamId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LeaveAll()


#  인원 미달 게임 취소 
class GameCancel(state.State):
    def on_enter(self):
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_portal(portalId=9, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True) # LeavePortal_EndGame
        set_event_ui(type=0, arg2='0,0')
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__64$', duration=4000, triggerBoxId=9000, isOutside=False)
        play_system_sound_in_box(boxIds=[9000], sound='massive_fail')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return LeaveAll()


class LeaveAll(state.State):
    def on_enter(self):
        guild_vs_game_end_game()
        unset_mini_game_area_for_hack() # 해킹 보안 종료
        set_sound(triggerId=40000, arg2=False) # Game
        show_event_result(type='notice', text='$66200001_GD__01_MASSIVEMAIN__65$', duration=10000, triggerBoxId=9000, isOutside=False)
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Ending_03')
        set_sound(triggerId=10000, arg2=False) # Intro

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)


#  그룹별패턴 모음 
#  G01 P01 
class G01P01_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P01Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P01_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P01_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P01_Check()


class G01P01_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P01TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P01_End()


class G01P01_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P01End', value=1):
            return RoundCheckOutDelay()


#  G01 P02 
class G01P02_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P02Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P02_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P02_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P02_Check()


class G01P02_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P02TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P02_End()


class G01P02_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P02End', value=1):
            return RoundCheckOutDelay()


#  G01 P03 
class G01P03_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P03Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P03_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P03_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P03_Check()


class G01P03_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P03TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P03_End()


class G01P03_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P03End', value=1):
            return RoundCheckOutDelay()


#  G01 P04 
class G01P04_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P04Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P04_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P04_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P04_Check()


class G01P04_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P04TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P04_End()


class G01P04_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P04End', value=1):
            return RoundCheckOutDelay()


#  G01 P05 
class G01P05_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P05Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P05_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P05_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P05_Check()


class G01P05_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P05TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P05_End()


class G01P05_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P05End', value=1):
            return RoundCheckOutDelay()


#  G01 P06 
class G01P06_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P06Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P06_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P06_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P06_Check()


class G01P06_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P06TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P06_End()


class G01P06_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P06End', value=1):
            return RoundCheckOutDelay()


#  G01 P07 
class G01P07_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P07Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P07_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P07_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P07_Check()


class G01P07_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P07TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P07_End()


class G01P07_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P07End', value=1):
            return RoundCheckOutDelay()


#  G01 P08 
class G01P08_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P08Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P08_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P08_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P08_Check()


class G01P08_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P08TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P08_End()


class G01P08_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P08End', value=1):
            return RoundCheckOutDelay()


#  G01 P09 
class G01P09_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P09Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P09_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P09_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P09_Check()


class G01P09_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P09TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P09_End()


class G01P09_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P09End', value=1):
            return RoundCheckOutDelay()


#  G01 P10 
class G01P10_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P10Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P10_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P10_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P10_Check()


class G01P10_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P10TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P10_End()


class G01P10_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P10End', value=1):
            return RoundCheckOutDelay()


#  G01 P11 
class G01P11_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P11Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P11_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P11_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P11_Check()


class G01P11_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P11TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P11_End()


class G01P11_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P11End', value=1):
            return RoundCheckOutDelay()


#  G01 P12 
class G01P12_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P12Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P12_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P12_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P12_Check()


class G01P12_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P12TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P12_End()


class G01P12_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P12End', value=1):
            return RoundCheckOutDelay()


#  G01 P13 
class G01P13_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P13Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P13_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P13_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P13_Check()


class G01P13_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P13TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P13_End()


class G01P13_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P13End', value=1):
            return RoundCheckOutDelay()


#  G01 P14 
class G01P14_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P14Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P14_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P14_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P14_Check()


class G01P14_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P14TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P14_End()


class G01P14_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P14End', value=1):
            return RoundCheckOutDelay()


#  G01 P15 
class G01P15_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P15Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P15_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P15_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P15_Check()


class G01P15_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P15TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P15_End()


class G01P15_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P15End', value=1):
            return RoundCheckOutDelay()


#  G01 P16 
class G01P16_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P16Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P16_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P16_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P16_Check()


class G01P16_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P16TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P16_End()


class G01P16_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P16End', value=1):
            return RoundCheckOutDelay()


#  G01 P17 
class G01P17_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P17Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P17_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P17_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P17_Check()


class G01P17_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P17TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P17_End()


class G01P17_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P17End', value=1):
            return RoundCheckOutDelay()


#  G01 P18 
class G01P18_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P18Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P18_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P18_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P18_Check()


class G01P18_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P18TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P18_End()


class G01P18_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P18End', value=1):
            return RoundCheckOutDelay()


#  G01 P19 
class G01P19_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P19Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P19_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P19_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P19_Check()


class G01P19_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P19TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P19_End()


class G01P19_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P19End', value=1):
            return RoundCheckOutDelay()


#  G01 P20 
class G01P20_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P20Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P20_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P20_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P20_Check()


class G01P20_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P20TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P20_End()


class G01P20_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P20End', value=1):
            return RoundCheckOutDelay()


#  G01 P21 
class G01P21_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P21Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P21_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P21_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P21_Check()


class G01P21_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P21TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P21_End()


class G01P21_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P21End', value=1):
            return RoundCheckOutDelay()


#  G01 P22 
class G01P22_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P22Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P22_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P22_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P22_Check()


class G01P22_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P22TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P22_End()


class G01P22_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P22End', value=1):
            return RoundCheckOutDelay()


#  G01 P23 
class G01P23_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P23Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P23_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P23_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P23_Check()


class G01P23_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P23TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P23_End()


class G01P23_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P23End', value=1):
            return RoundCheckOutDelay()


#  G01 P24 
class G01P24_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P24Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P24_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P24_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P24_Check()


class G01P24_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P24TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P24_End()


class G01P24_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P24End', value=1):
            return RoundCheckOutDelay()


#  G01 P25 
class G01P25_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P25Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P25_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P25_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P25_Check()


class G01P25_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P25TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P25_End()


class G01P25_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P25End', value=1):
            return RoundCheckOutDelay()


#  G01 P26 
class G01P26_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P26Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P26_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P26_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P26_Check()


class G01P26_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P26TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P26_End()


class G01P26_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P26End', value=1):
            return RoundCheckOutDelay()


#  G01 P27 
class G01P27_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P27Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P27_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P27_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P27_Check()


class G01P27_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P27TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P27_End()


class G01P27_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P27End', value=1):
            return RoundCheckOutDelay()


#  G01 P28 
class G01P28_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P28Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P28_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P28_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P28_Check()


class G01P28_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P28TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P28_End()


class G01P28_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P28End', value=1):
            return RoundCheckOutDelay()


#  G01 P29 
class G01P29_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P29Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P29_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P29_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P29_Check()


class G01P29_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P29TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P29_End()


class G01P29_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P29End', value=1):
            return RoundCheckOutDelay()


#  G01 P30 
class G01P30_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P30Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G01P30_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G01P30_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G01P30_Check()


class G01P30_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=100, key='G01P30TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G01P30_End()


class G01P30_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G01P30End', value=1):
            return RoundCheckOutDelay()


#  G02 P01 
class G02P01_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P01Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P01_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P01_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P01_Check()


class G02P01_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P01TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P01_End()


class G02P01_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P01End', value=1):
            return RoundCheckOutDelay()


#  G02 P02 
class G02P02_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P02Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P02_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P02_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P02_Check()


class G02P02_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P02TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P02_End()


class G02P02_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P02End', value=1):
            return RoundCheckOutDelay()


#  G02 P03 
class G02P03_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P03Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P03_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P03_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P03_Check()


class G02P03_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P03TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P03_End()


class G02P03_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P03End', value=1):
            return RoundCheckOutDelay()


#  G02 P04 
class G02P04_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P04Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P04_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P04_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P04_Check()


class G02P04_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P04TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P04_End()


class G02P04_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P04End', value=1):
            return RoundCheckOutDelay()


#  G02 P05 
class G02P05_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P05Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P05_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P05_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P05_Check()


class G02P05_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P05TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P05_End()


class G02P05_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P05End', value=1):
            return RoundCheckOutDelay()


#  G02 P06 
class G02P06_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P06Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P06_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P06_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P06_Check()


class G02P06_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P06TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P06_End()


class G02P06_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P06End', value=1):
            return RoundCheckOutDelay()


#  G02 P07 
class G02P07_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P07Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P07_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P07_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P07_Check()


class G02P07_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P07TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P07_End()


class G02P07_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P07End', value=1):
            return RoundCheckOutDelay()


#  G02 P08 
class G02P08_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P08Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P08_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P08_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P08_Check()


class G02P08_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P08TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P08_End()


class G02P08_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P08End', value=1):
            return RoundCheckOutDelay()


#  G02 P09 
class G02P09_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P09Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P09_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P09_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P09_Check()


class G02P09_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P09TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P09_End()


class G02P09_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P09End', value=1):
            return RoundCheckOutDelay()


#  G02 P10 
class G02P10_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P10Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P10_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P10_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P10_Check()


class G02P10_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P10TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P10_End()


class G02P10_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P10End', value=1):
            return RoundCheckOutDelay()


#  G02 P11 
class G02P11_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P11Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P11_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P11_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P11_Check()


class G02P11_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P11TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P11_End()


class G02P11_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P11End', value=1):
            return RoundCheckOutDelay()


#  G02 P12 
class G02P12_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P12Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P12_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P12_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P12_Check()


class G02P12_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P12TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P12_End()


class G02P12_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P12End', value=1):
            return RoundCheckOutDelay()


#  G02 P13 
class G02P13_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P13Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P13_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P13_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P13_Check()


class G02P13_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P13TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P13_End()


class G02P13_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P13End', value=1):
            return RoundCheckOutDelay()


#  G02 P14 
class G02P14_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P14Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P14_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P14_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P14_Check()


class G02P14_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P14TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P14_End()


class G02P14_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P14End', value=1):
            return RoundCheckOutDelay()


#  G02 P15 
class G02P15_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P15Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P15_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P15_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P15_Check()


class G02P15_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P15TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P15_End()


class G02P15_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P15End', value=1):
            return RoundCheckOutDelay()


#  G02 P16 
class G02P16_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P16Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P16_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P16_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P16_Check()


class G02P16_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P16TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P16_End()


class G02P16_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P16End', value=1):
            return RoundCheckOutDelay()


#  G02 P17 
class G02P17_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P17Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P17_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P17_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P17_Check()


class G02P17_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P17TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P17_End()


class G02P17_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P17End', value=1):
            return RoundCheckOutDelay()


#  G02 P18 
class G02P18_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P18Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P18_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P18_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P18_Check()


class G02P18_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P18TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P18_End()


class G02P18_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P18End', value=1):
            return RoundCheckOutDelay()


#  G02 P19 
class G02P19_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P19Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P19_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P19_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P19_Check()


class G02P19_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P19TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P19_End()


class G02P19_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P19End', value=1):
            return RoundCheckOutDelay()


#  G02 P20 
class G02P20_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P20Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P20_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P20_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P20_Check()


class G02P20_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P20TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P20_End()


class G02P20_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P20End', value=1):
            return RoundCheckOutDelay()


#  G02 P21 
class G02P21_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P21Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P21_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P21_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P21_Check()


class G02P21_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P21TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P21_End()


class G02P21_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P21End', value=1):
            return RoundCheckOutDelay()


#  G02 P22 
class G02P22_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P22Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P22_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P22_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P22_Check()


class G02P22_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P22TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P22_End()


class G02P22_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P22End', value=1):
            return RoundCheckOutDelay()


#  G02 P23 
class G02P23_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P23Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P23_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P23_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P23_Check()


class G02P23_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P23TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P23_End()


class G02P23_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P23End', value=1):
            return RoundCheckOutDelay()


#  G02 P24 
class G02P24_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P24Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P24_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P24_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P24_Check()


class G02P24_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P24TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P24_End()


class G02P24_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P24End', value=1):
            return RoundCheckOutDelay()


#  G02 P25 
class G02P25_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P25Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P25_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P25_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P25_Check()


class G02P25_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P25TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P25_End()


class G02P25_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P25End', value=1):
            return RoundCheckOutDelay()


#  G02 P26 
class G02P26_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P26Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P26_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P26_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P26_Check()


class G02P26_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P26TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P26_End()


class G02P26_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P26End', value=1):
            return RoundCheckOutDelay()


#  G02 P27 
class G02P27_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P27Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P27_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P27_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P27_Check()


class G02P27_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P27TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P27_End()


class G02P27_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P27End', value=1):
            return RoundCheckOutDelay()


#  G02 P28 
class G02P28_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P28Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P28_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P28_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P28_Check()


class G02P28_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P28TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P28_End()


class G02P28_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P28End', value=1):
            return RoundCheckOutDelay()


#  G02 P29 
class G02P29_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P29Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P29_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P29_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P29_Check()


class G02P29_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P29TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P29_End()


class G02P29_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P29End', value=1):
            return RoundCheckOutDelay()


#  G02 P30 
class G02P30_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P30Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G02P30_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G02P30_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G02P30_Check()


class G02P30_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=200, key='G02P30TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G02P30_End()


class G02P30_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G02P30End', value=1):
            return RoundCheckOutDelay()


#  G03 P01 
class G03P01_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P01Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P01_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P01_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P01_Check()


class G03P01_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P01TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P01_End()


class G03P01_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P01End', value=1):
            return RoundCheckOutDelay()


#  G03 P02 
class G03P02_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P02Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P02_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P02_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P02_Check()


class G03P02_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P02TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P02_End()


class G03P02_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P02End', value=1):
            return RoundCheckOutDelay()


#  G03 P03 
class G03P03_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P03Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P03_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P03_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P03_Check()


class G03P03_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P03TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P03_End()


class G03P03_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P03End', value=1):
            return RoundCheckOutDelay()


#  G03 P04 
class G03P04_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P04Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P04_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P04_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P04_Check()


class G03P04_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P04TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P04_End()


class G03P04_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P04End', value=1):
            return RoundCheckOutDelay()


#  G03 P05 
class G03P05_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P05Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P05_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P05_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P05_Check()


class G03P05_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P05TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P05_End()


class G03P05_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P05End', value=1):
            return RoundCheckOutDelay()


#  G03 P06 
class G03P06_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P06Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P06_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P06_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P06_Check()


class G03P06_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P06TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P06_End()


class G03P06_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P06End', value=1):
            return RoundCheckOutDelay()


#  G03 P07 
class G03P07_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P07Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P07_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P07_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P07_Check()


class G03P07_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P07TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P07_End()


class G03P07_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P07End', value=1):
            return RoundCheckOutDelay()


#  G03 P08 
class G03P08_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P08Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P08_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P08_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P08_Check()


class G03P08_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P08TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P08_End()


class G03P08_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P08End', value=1):
            return RoundCheckOutDelay()


#  G03 P09 
class G03P09_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P09Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P09_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P09_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P09_Check()


class G03P09_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P09TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P09_End()


class G03P09_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P09End', value=1):
            return RoundCheckOutDelay()


#  G03 P10 
class G03P10_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P10Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P10_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P10_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P10_Check()


class G03P10_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P10TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P10_End()


class G03P10_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P10End', value=1):
            return RoundCheckOutDelay()


#  G03 P11 
class G03P11_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P11Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P11_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P11_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P11_Check()


class G03P11_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P11TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P11_End()


class G03P11_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P11End', value=1):
            return RoundCheckOutDelay()


#  G03 P12 
class G03P12_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P12Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P12_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P12_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P12_Check()


class G03P12_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P12TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P12_End()


class G03P12_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P12End', value=1):
            return RoundCheckOutDelay()


#  G03 P13 
class G03P13_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P13Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P13_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P13_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P13_Check()


class G03P13_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P13TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P13_End()


class G03P13_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P13End', value=1):
            return RoundCheckOutDelay()


#  G03 P14 
class G03P14_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P14Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P14_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P14_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P14_Check()


class G03P14_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P14TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P14_End()


class G03P14_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P14End', value=1):
            return RoundCheckOutDelay()


#  G03 P15 
class G03P15_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P15Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P15_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P15_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P15_Check()


class G03P15_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P15TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P15_End()


class G03P15_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P15End', value=1):
            return RoundCheckOutDelay()


#  G03 P16 
class G03P16_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P16Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P16_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P16_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P16_Check()


class G03P16_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P16TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P16_End()


class G03P16_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P16End', value=1):
            return RoundCheckOutDelay()


#  G03 P17 
class G03P17_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P17Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P17_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P17_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P17_Check()


class G03P17_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P17TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P17_End()


class G03P17_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P17End', value=1):
            return RoundCheckOutDelay()


#  G03 P18 
class G03P18_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P18Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P18_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P18_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P18_Check()


class G03P18_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P18TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P18_End()


class G03P18_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P18End', value=1):
            return RoundCheckOutDelay()


#  G03 P19 
class G03P19_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P19Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P19_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P19_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P19_Check()


class G03P19_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P19TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P19_End()


class G03P19_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P19End', value=1):
            return RoundCheckOutDelay()


#  G03 P20 
class G03P20_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P20Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P20_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P20_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P20_Check()


class G03P20_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P20TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P20_End()


class G03P20_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P20End', value=1):
            return RoundCheckOutDelay()


#  G03 P21 
class G03P21_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P21Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P21_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P21_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P21_Check()


class G03P21_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P21TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P21_End()


class G03P21_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P21End', value=1):
            return RoundCheckOutDelay()


#  G03 P22 
class G03P22_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P22Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P22_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P22_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P22_Check()


class G03P22_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P22TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P22_End()


class G03P22_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P22End', value=1):
            return RoundCheckOutDelay()


#  G03 P23 
class G03P23_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P23Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P23_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P23_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P23_Check()


class G03P23_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P23TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P23_End()


class G03P23_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P23End', value=1):
            return RoundCheckOutDelay()


#  G03 P24 
class G03P24_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P24Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P24_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P24_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P24_Check()


class G03P24_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P24TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P24_End()


class G03P24_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P24End', value=1):
            return RoundCheckOutDelay()


#  G03 P25 
class G03P25_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P25Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P25_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P25_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P25_Check()


class G03P25_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P25TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P25_End()


class G03P25_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P25End', value=1):
            return RoundCheckOutDelay()


#  G03 P26 
class G03P26_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P26Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P26_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P26_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P26_Check()


class G03P26_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P26TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P26_End()


class G03P26_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P26End', value=1):
            return RoundCheckOutDelay()


#  G03 P27 
class G03P27_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P27Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P27_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P27_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P27_Check()


class G03P27_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P27TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P27_End()


class G03P27_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P27End', value=1):
            return RoundCheckOutDelay()


#  G03 P28 
class G03P28_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P28Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P28_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P28_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P28_Check()


class G03P28_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P28TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P28_End()


class G03P28_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P28End', value=1):
            return RoundCheckOutDelay()


#  G03 P29 
class G03P29_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P29Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P29_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P29_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P29_Check()


class G03P29_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P29TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P29_End()


class G03P29_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P29End', value=1):
            return RoundCheckOutDelay()


#  G03 P30 
class G03P30_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P30Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G03P30_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G03P30_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G03P30_Check()


class G03P30_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=300, key='G03P30TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G03P30_End()


class G03P30_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G03P30End', value=1):
            return RoundCheckOutDelay()


#  G04 P01 
class G04P01_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P01Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P01_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P01_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P01_Check()


class G04P01_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P01TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P01_End()


class G04P01_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P01End', value=1):
            return RoundCheckOutDelay()


#  G04 P02 
class G04P02_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P02Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P02_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P02_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P02_Check()


class G04P02_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P02TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P02_End()


class G04P02_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P02End', value=1):
            return RoundCheckOutDelay()


#  G04 P03 
class G04P03_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P03Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P03_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P03_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P03_Check()


class G04P03_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P03TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P03_End()


class G04P03_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P03End', value=1):
            return RoundCheckOutDelay()


#  G04 P04 
class G04P04_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P04Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P04_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P04_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P04_Check()


class G04P04_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P04TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P04_End()


class G04P04_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P04End', value=1):
            return RoundCheckOutDelay()


#  G04 P05 
class G04P05_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P05Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P05_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P05_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P05_Check()


class G04P05_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P05TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P05_End()


class G04P05_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P05End', value=1):
            return RoundCheckOutDelay()


#  G04 P06 
class G04P06_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P06Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P06_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P06_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P06_Check()


class G04P06_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P06TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P06_End()


class G04P06_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P06End', value=1):
            return RoundCheckOutDelay()


#  G04 P07 
class G04P07_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P07Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P07_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P07_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P07_Check()


class G04P07_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P07TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P07_End()


class G04P07_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P07End', value=1):
            return RoundCheckOutDelay()


#  G04 P08 
class G04P08_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P08Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P08_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P08_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P08_Check()


class G04P08_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P08TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P08_End()


class G04P08_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P08End', value=1):
            return RoundCheckOutDelay()


#  G04 P09 
class G04P09_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P09Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P09_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P09_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P09_Check()


class G04P09_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P09TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P09_End()


class G04P09_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P09End', value=1):
            return RoundCheckOutDelay()


#  G04 P10 
class G04P10_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P10Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P10_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P10_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P10_Check()


class G04P10_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P10TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P10_End()


class G04P10_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P10End', value=1):
            return RoundCheckOutDelay()


#  G04 P11 
class G04P11_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P11Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P11_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P11_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P11_Check()


class G04P11_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P11TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P11_End()


class G04P11_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P11End', value=1):
            return RoundCheckOutDelay()


#  G04 P12 
class G04P12_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P12Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P12_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P12_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P12_Check()


class G04P12_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P12TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P12_End()


class G04P12_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P12End', value=1):
            return RoundCheckOutDelay()


#  G04 P13 
class G04P13_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P13Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P13_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P13_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P13_Check()


class G04P13_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P13TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P13_End()


class G04P13_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P13End', value=1):
            return RoundCheckOutDelay()


#  G04 P14 
class G04P14_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P14Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P14_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P14_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P14_Check()


class G04P14_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P14TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P14_End()


class G04P14_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P14End', value=1):
            return RoundCheckOutDelay()


#  G04 P15 
class G04P15_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P15Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P15_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P15_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P15_Check()


class G04P15_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P15TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P15_End()


class G04P15_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P15End', value=1):
            return RoundCheckOutDelay()


#  G04 P16 
class G04P16_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P16Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P16_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P16_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P16_Check()


class G04P16_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P16TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P16_End()


class G04P16_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P16End', value=1):
            return RoundCheckOutDelay()


#  G04 P17 
class G04P17_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P17Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P17_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P17_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P17_Check()


class G04P17_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P17TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P17_End()


class G04P17_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P17End', value=1):
            return RoundCheckOutDelay()


#  G04 P18 
class G04P18_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P18Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P18_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P18_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P18_Check()


class G04P18_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P18TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P18_End()


class G04P18_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P18End', value=1):
            return RoundCheckOutDelay()


#  G04 P19 
class G04P19_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P19Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P19_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P19_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P19_Check()


class G04P19_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P19TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P19_End()


class G04P19_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P19End', value=1):
            return RoundCheckOutDelay()


#  G04 P20 
class G04P20_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P20Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P20_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P20_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P20_Check()


class G04P20_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P20TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P20_End()


class G04P20_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P20End', value=1):
            return RoundCheckOutDelay()


#  G04 P21 
class G04P21_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P21Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P21_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P21_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P21_Check()


class G04P21_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P21TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P21_End()


class G04P21_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P21End', value=1):
            return RoundCheckOutDelay()


#  G04 P22 
class G04P22_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P22Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P22_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P22_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P22_Check()


class G04P22_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P22TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P22_End()


class G04P22_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P22End', value=1):
            return RoundCheckOutDelay()


#  G04 P23 
class G04P23_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P23Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P23_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P23_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P23_Check()


class G04P23_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P23TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P23_End()


class G04P23_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P23End', value=1):
            return RoundCheckOutDelay()


#  G04 P24 
class G04P24_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P24Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P24_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P24_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P24_Check()


class G04P24_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P24TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P24_End()


class G04P24_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P24End', value=1):
            return RoundCheckOutDelay()


#  G04 P25 
class G04P25_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P25Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P25_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P25_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P25_Check()


class G04P25_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P25TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P25_End()


class G04P25_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P25End', value=1):
            return RoundCheckOutDelay()


#  G04 P26 
class G04P26_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P26Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P26_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P26_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P26_Check()


class G04P26_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P26TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P26_End()


class G04P26_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P26End', value=1):
            return RoundCheckOutDelay()


#  G04 P27 
class G04P27_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P27Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P27_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P27_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P27_Check()


class G04P27_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P27TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P27_End()


class G04P27_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P27End', value=1):
            return RoundCheckOutDelay()


#  G04 P28 
class G04P28_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P28Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P28_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P28_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P28_Check()


class G04P28_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P28TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P28_End()


class G04P28_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P28End', value=1):
            return RoundCheckOutDelay()


#  G04 P29 
class G04P29_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P29Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P29_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P29_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P29_Check()


class G04P29_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P29TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P29_End()


class G04P29_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P29End', value=1):
            return RoundCheckOutDelay()


#  G04 P30 
class G04P30_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P30Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P30_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P30_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P30_Check()


class G04P30_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P30TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P30_End()


class G04P30_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P30End', value=1):
            return RoundCheckOutDelay()


#  G04 P31 
class G04P31_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P31Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P31_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P31_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P31_Check()


class G04P31_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P31TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P31_End()


class G04P31_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P31End', value=1):
            return RoundCheckOutDelay()


#  G04 P32 
class G04P32_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P32Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P32_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P32_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P32_Check()


class G04P32_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P32TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P32_End()


class G04P32_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P32End', value=1):
            return RoundCheckOutDelay()


#  G04 P33 
class G04P33_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P33Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P33_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P33_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P33_Check()


class G04P33_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P33TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P33_End()


class G04P33_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P33End', value=1):
            return RoundCheckOutDelay()


#  G04 P34 
class G04P34_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P34Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P34_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P34_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P34_Check()


class G04P34_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P34TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P34_End()


class G04P34_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P34End', value=1):
            return RoundCheckOutDelay()


#  G04 P35 
class G04P35_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P35Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P35_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P35_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P35_Check()


class G04P35_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P35TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P35_End()


class G04P35_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P35End', value=1):
            return RoundCheckOutDelay()


#  G04 P36 
class G04P36_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P36Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P36_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P36_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P36_Check()


class G04P36_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P36TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P36_End()


class G04P36_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P36End', value=1):
            return RoundCheckOutDelay()


#  G04 P37 
class G04P37_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P37Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P37_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P37_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P37_Check()


class G04P37_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P37TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P37_End()


class G04P37_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P37End', value=1):
            return RoundCheckOutDelay()


#  G04 P38 
class G04P38_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P38Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P38_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P38_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P38_Check()


class G04P38_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P38TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P38_End()


class G04P38_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P38End', value=1):
            return RoundCheckOutDelay()


#  G04 P39 
class G04P39_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P39Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P39_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P39_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P39_Check()


class G04P39_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P39TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P39_End()


class G04P39_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P39End', value=1):
            return RoundCheckOutDelay()


#  G04 P40 
class G04P40_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P40Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G04P40_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G04P40_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G04P40_Check()


class G04P40_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=400, key='G04P40TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G04P40_End()


class G04P40_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G04P40End', value=1):
            return RoundCheckOutDelay()


#  G05 P01 
class G05P01_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P01Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P01_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P01_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P01_Check()


class G05P01_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P01TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P01_End()


class G05P01_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P01End', value=1):
            return RoundCheckOutDelay()


#  G05 P02 
class G05P02_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P02Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P02_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P02_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P02_Check()


class G05P02_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P02TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P02_End()


class G05P02_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P02End', value=1):
            return RoundCheckOutDelay()


#  G05 P03 
class G05P03_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P03Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P03_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P03_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P03_Check()


class G05P03_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P03TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P03_End()


class G05P03_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P03End', value=1):
            return RoundCheckOutDelay()


#  G05 P04 
class G05P04_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P04Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P04_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P04_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P04_Check()


class G05P04_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P04TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P04_End()


class G05P04_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P04End', value=1):
            return RoundCheckOutDelay()


#  G05 P05 
class G05P05_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P05Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P05_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P05_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P05_Check()


class G05P05_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P05TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P05_End()


class G05P05_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P05End', value=1):
            return RoundCheckOutDelay()


#  G05 P06 
class G05P06_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P06Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P06_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P06_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P06_Check()


class G05P06_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P06TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P06_End()


class G05P06_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P06End', value=1):
            return RoundCheckOutDelay()


#  G05 P07 
class G05P07_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P07Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P07_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P07_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P07_Check()


class G05P07_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P07TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P07_End()


class G05P07_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P07End', value=1):
            return RoundCheckOutDelay()


#  G05 P08 
class G05P08_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P08Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P08_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P08_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P08_Check()


class G05P08_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P08TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P08_End()


class G05P08_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P08End', value=1):
            return RoundCheckOutDelay()


#  G05 P09 
class G05P09_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P09Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P09_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P09_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P09_Check()


class G05P09_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P09TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P09_End()


class G05P09_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P09End', value=1):
            return RoundCheckOutDelay()


#  G05 P10 
class G05P10_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P10Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P10_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P10_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P10_Check()


class G05P10_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P10TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P10_End()


class G05P10_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P10End', value=1):
            return RoundCheckOutDelay()


#  G05 P11 
class G05P11_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P11Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P11_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P11_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P11_Check()


class G05P11_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P11TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P11_End()


class G05P11_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P11End', value=1):
            return RoundCheckOutDelay()


#  G05 P12 
class G05P12_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P12Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P12_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P12_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P12_Check()


class G05P12_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P12TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P12_End()


class G05P12_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P12End', value=1):
            return RoundCheckOutDelay()


#  G05 P13 
class G05P13_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P13Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P13_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P13_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P13_Check()


class G05P13_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P13TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P13_End()


class G05P13_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P13End', value=1):
            return RoundCheckOutDelay()


#  G05 P14 
class G05P14_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P14Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P14_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P14_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P14_Check()


class G05P14_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P14TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P14_End()


class G05P14_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P14End', value=1):
            return RoundCheckOutDelay()


#  G05 P15 
class G05P15_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P15Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P15_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P15_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P15_Check()


class G05P15_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P15TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P15_End()


class G05P15_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P15End', value=1):
            return RoundCheckOutDelay()


#  G05 P16 
class G05P16_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P16Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P16_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P16_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P16_Check()


class G05P16_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P16TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P16_End()


class G05P16_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P16End', value=1):
            return RoundCheckOutDelay()


#  G05 P17 
class G05P17_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P17Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P17_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P17_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P17_Check()


class G05P17_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P17TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P17_End()


class G05P17_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P17End', value=1):
            return RoundCheckOutDelay()


#  G05 P18 
class G05P18_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P18Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P18_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P18_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P18_Check()


class G05P18_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P18TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P18_End()


class G05P18_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P18End', value=1):
            return RoundCheckOutDelay()


#  G05 P19 
class G05P19_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P19Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P19_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P19_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P19_Check()


class G05P19_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P19TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P19_End()


class G05P19_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P19End', value=1):
            return RoundCheckOutDelay()


#  G05 P20 
class G05P20_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P20Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P20_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P20_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P20_Check()


class G05P20_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P20TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P20_End()


class G05P20_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P20End', value=1):
            return RoundCheckOutDelay()


#  G05 P21 
class G05P21_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P21Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P21_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P21_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P21_Check()


class G05P21_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P21TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P21_End()


class G05P21_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P21End', value=1):
            return RoundCheckOutDelay()


#  G05 P22 
class G05P22_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P22Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P22_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P22_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P22_Check()


class G05P22_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P22TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P22_End()


class G05P22_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P22End', value=1):
            return RoundCheckOutDelay()


#  G05 P23 
class G05P23_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P23Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P23_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P23_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P23_Check()


class G05P23_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P23TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P23_End()


class G05P23_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P23End', value=1):
            return RoundCheckOutDelay()


#  G05 P24 
class G05P24_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P24Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P24_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P24_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P24_Check()


class G05P24_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P24TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P24_End()


class G05P24_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P24End', value=1):
            return RoundCheckOutDelay()


#  G05 P25 
class G05P25_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P25Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P25_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P25_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P25_Check()


class G05P25_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P25TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P25_End()


class G05P25_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P25End', value=1):
            return RoundCheckOutDelay()


#  G05 P26 
class G05P26_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P26Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P26_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P26_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P26_Check()


class G05P26_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P26TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P26_End()


class G05P26_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P26End', value=1):
            return RoundCheckOutDelay()


#  G05 P27 
class G05P27_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P27Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P27_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P27_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P27_Check()


class G05P27_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P27TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P27_End()


class G05P27_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P27End', value=1):
            return RoundCheckOutDelay()


#  G05 P28 
class G05P28_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P28Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P28_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P28_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P28_Check()


class G05P28_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P28TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P28_End()


class G05P28_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P28End', value=1):
            return RoundCheckOutDelay()


#  G05 P29 
class G05P29_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P29Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P29_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P29_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P29_Check()


class G05P29_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P29TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P29_End()


class G05P29_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P29End', value=1):
            return RoundCheckOutDelay()


#  G05 P30 
class G05P30_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P30Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P30_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P30_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P30_Check()


class G05P30_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P30TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P30_End()


class G05P30_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P30End', value=1):
            return RoundCheckOutDelay()


#  G05 P31 
class G05P31_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P31Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P31_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P31_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P31_Check()


class G05P31_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P31TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P31_End()


class G05P31_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P31End', value=1):
            return RoundCheckOutDelay()


#  G05 P32 
class G05P32_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P32Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P32_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P32_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P32_Check()


class G05P32_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P32TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P32_End()


class G05P32_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P32End', value=1):
            return RoundCheckOutDelay()


#  G05 P33 
class G05P33_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P33Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P33_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P33_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P33_Check()


class G05P33_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P33TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P33_End()


class G05P33_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P33End', value=1):
            return RoundCheckOutDelay()


#  G05 P34 
class G05P34_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P34Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P34_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P34_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P34_Check()


class G05P34_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P34TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P34_End()


class G05P34_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P34End', value=1):
            return RoundCheckOutDelay()


#  G05 P35 
class G05P35_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P35Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P35_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P35_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P35_Check()


class G05P35_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P35TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P35_End()


class G05P35_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P35End', value=1):
            return RoundCheckOutDelay()


#  G05 P36 
class G05P36_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P36Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P36_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P36_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P36_Check()


class G05P36_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P36TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P36_End()


class G05P36_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P36End', value=1):
            return RoundCheckOutDelay()


#  G05 P37 
class G05P37_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P37Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P37_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P37_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P37_Check()


class G05P37_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P37TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P37_End()


class G05P37_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P37End', value=1):
            return RoundCheckOutDelay()


#  G05 P38 
class G05P38_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P38Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P38_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P38_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P38_Check()


class G05P38_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P38TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P38_End()


class G05P38_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P38End', value=1):
            return RoundCheckOutDelay()


#  G05 P39 
class G05P39_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P39Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P39_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P39_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P39_Check()


class G05P39_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P39TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P39_End()


class G05P39_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P39End', value=1):
            return RoundCheckOutDelay()


#  G05 P40 
class G05P40_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P40Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P40_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P40_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P40_Check()


class G05P40_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P40TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P40_End()


class G05P40_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P40End', value=1):
            return RoundCheckOutDelay()


#  G05 P41 
class G05P41_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P41Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P41_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P41_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P41_Check()


class G05P41_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P41TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P41_End()


class G05P41_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P41End', value=1):
            return RoundCheckOutDelay()


#  G05 P42 
class G05P42_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P42Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P42_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P42_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P42_Check()


class G05P42_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P42TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P42_End()


class G05P42_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P42End', value=1):
            return RoundCheckOutDelay()


#  G05 P43 
class G05P43_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P43Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P43_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P43_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P43_Check()


class G05P43_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P43TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P43_End()


class G05P43_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P43End', value=1):
            return RoundCheckOutDelay()


#  G05 P44 
class G05P44_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P44Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P44_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P44_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P44_Check()


class G05P44_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P44TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P44_End()


class G05P44_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P44End', value=1):
            return RoundCheckOutDelay()


#  G05 P45 
class G05P45_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P45Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P45_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P45_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P45_Check()


class G05P45_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P45TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P45_End()


class G05P45_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P45End', value=1):
            return RoundCheckOutDelay()


#  G05 P46 
class G05P46_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P46Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P46_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P46_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P46_Check()


class G05P46_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P46TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P46_End()


class G05P46_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P46End', value=1):
            return RoundCheckOutDelay()


#  G05 P47 
class G05P47_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P47Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P47_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P47_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P47_Check()


class G05P47_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P47TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P47_End()


class G05P47_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P47End', value=1):
            return RoundCheckOutDelay()


#  G05 P48 
class G05P48_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P48Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P48_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P48_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P48_Check()


class G05P48_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P48TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P48_End()


class G05P48_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P48End', value=1):
            return RoundCheckOutDelay()


#  G05 P49 
class G05P49_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P49Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P49_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P49_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P49_Check()


class G05P49_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P49TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P49_End()


class G05P49_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P49End', value=1):
            return RoundCheckOutDelay()


#  G05 P50 
class G05P50_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P50Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G05P50_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G05P50_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$66200001_GD__01_MASSIVEMAIN__66$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G05P50_Check()


class G05P50_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=500, key='G05P50TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G05P50_End()


class G05P50_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G05P50End', value=1):
            return RoundCheckOutDelay()


class RoundCheckOutDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return RoundCheckOut()


class RoundCheckOut(state.State):
    def on_enter(self):
        set_user_value(triggerId=11, key='BannerCheckIn', value=1) # 게임판 위 인원수 배너 표시
        guild_vs_game_score_by_user(boxId=9001, score=1) # 이긴팀에게 라운드 스코어 1점 부여
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=True, arg3=0, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckNextRound()


class CheckNextRound(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Round', value=1):
            return R01EndDelay()
        if user_value(key='Round', value=2):
            return R02EndDelay()
        if user_value(key='Round', value=3):
            return R03EndDelay()
        if user_value(key='Round', value=4):
            return R04EndDelay()
        if user_value(key='Round', value=5):
            return R05EndDelay()


