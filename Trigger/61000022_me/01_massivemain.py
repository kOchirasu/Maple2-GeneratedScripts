""" trigger/61000022_me/01_massivemain.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_sound(triggerId=10000, arg2=False) # Intro
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=40000, arg2=False) # Puzzle
        set_effect(triggerIds=[8000], visible=False) # Scratch
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
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000936], state=2) # 15000ms
        set_user_value(key='Round', value=0)
        set_user_value(key='GambleSuccess', value=0)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return EntryDelay()


class EntryDelay(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=60) # 테스트 수정 가능 지점

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return MusicChange()
        if count_users(boxId=9001, boxId=50):
            return MusicChange()


class MusicChange(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GameGuide01()


class GameGuide01(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='BannerCheckIn', value=1)
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=10000, arg2=True) # Intro
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__0$', arg3='3000', arg4='0') # Voice 02000952
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Notice_01')
        set_achievement(triggerId=9001, type='trigger', achieve='dailyquest_start')
        set_achievement(triggerId=9001, type='trigger', achieve='christmasddstop_start') # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        give_guild_exp(boxId=0, type=2)
        set_mini_game_area_for_hack(boxId=9001) # 해킹 보안용 시작 box 설정
        start_mini_game(boxId=9001, round=5, gameName='christmasdancedancestop')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GameGuide02()


class GameGuide02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__1$', arg3='4000', arg4='0') # Voice 02000981
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Notice_02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GameGuide03()


class GameGuide03(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__2$', arg3='4000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameGuide04()


class GameGuide04(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__3$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return R01Start()

    def on_exit(self):
        set_user_value(key='Round', value=1) # 테스트 수정 가능 지점


#  R01 시작 
class R01Start(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__4$', arg3='3000', arg4='0') # Voice 02000953
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancetime_01')
        set_event_ui(type=0, arg2='1,5') # Round1
        set_sound(triggerId=10000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        start_mini_game_round(boxId=9001, round=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R01DanceTime()


#  R01 DanceTime 패턴 랜덤 
class R01DanceTime(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return R01DancePattern01()
        if random_condition(rate=30):
            return R01DancePattern02()
        if random_condition(rate=30):
            return R01DancePattern03()
        if random_condition(rate=3):
            return R01DancePattern0401()
        if random_condition(rate=3):
            return R01DancePattern0501()
        if random_condition(rate=2):
            return R01DancePattern0601()
        if random_condition(rate=2):
            return R01DancePattern0701()

    def on_exit(self):
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms


#  R01 Dance 9000ms  
class R01DancePattern01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return R01_GameStartDelay()


#  R01 Dance 12000ms
class R01DancePattern02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return R01_GameStartDelay()


#  R01 Dance 15000ms
class R01DancePattern03(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000936], state=1) # 15000ms
        set_user_value(triggerId=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=19000):
            return R01_GameStartDelay()


#  R01 Dance 7000ms+ 9000ms
class R01DancePattern0401(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return R01DancePattern0402()


class R01DancePattern0402(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__9$', arg3='1000') # Voice 02000958
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_01')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R01DancePattern0403()


class R01DancePattern0403(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__10$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R01DancePattern0404()


class R01DancePattern0404(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return R01_GameStartDelay()


#  R01 Dance 9000ms+ 7000ms
class R01DancePattern0501(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return R01DancePattern0502()


class R01DancePattern0502(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__11$', arg3='1000') # Voice 02000982
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_02')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000934], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R01DancePattern0503()


class R01DancePattern0503(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__12$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R01DancePattern0504()


class R01DancePattern0504(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return R01_GameStartDelay()


#  R01 Dance 12000ms+ 7000ms
class R01DancePattern0601(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return R01DancePattern0602()


class R01DancePattern0602(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__13$', arg3='1000') # Voice 02000983
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_03')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000935], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R01DancePattern0603()


class R01DancePattern0603(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__14$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R01DancePattern0604()


class R01DancePattern0604(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return R01_GameStartDelay()


#  R01 Dance 7000ms+ 12000ms
class R01DancePattern0701(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return R01DancePattern0702()


class R01DancePattern0702(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__15$', arg3='1000') # Voice 02000984
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_04')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R01DancePattern0703()


class R01DancePattern0703(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__16$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000935], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R01DancePattern0704()


class R01DancePattern0704(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return R01_GameStartDelay()


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
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000936], state=2) # 15000ms
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__17$', arg3='4000') # Voice 02000959
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R01_GameTimerStart()


class R01_GameTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=30, clearAtZero=True, display=True, arg5=-40) # Round1 / 30sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=1) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=1) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R01G00Check()


#  R01 인원 체크 시작 
#   테스트 수정 가능 지점
class R01G00Check(state.State):
    def on_tick(self) -> state.State:
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
#  패턴 그룹 2개 랜덤 
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


#  G05 패턴 랜덤 
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
        set_user_value(triggerId=7110, key='Color11', value=5) # color reset
        set_user_value(triggerId=7120, key='Color12', value=5) # color reset
        set_user_value(triggerId=7130, key='Color13', value=5) # color reset
        set_user_value(triggerId=7140, key='Color14', value=5) # color reset
        set_user_value(triggerId=7210, key='Color21', value=5) # color reset
        set_user_value(triggerId=7220, key='Color22', value=5) # color reset
        set_user_value(triggerId=7230, key='Color23', value=5) # color reset
        set_user_value(triggerId=7240, key='Color24', value=5) # color reset
        set_user_value(triggerId=7310, key='Color31', value=5) # color reset
        set_user_value(triggerId=7320, key='Color32', value=5) # color reset
        set_user_value(triggerId=7330, key='Color33', value=5) # color reset
        set_user_value(triggerId=7340, key='Color34', value=5) # color reset
        set_user_value(triggerId=7410, key='Color41', value=5) # color reset
        set_user_value(triggerId=7420, key='Color42', value=5) # color reset
        set_user_value(triggerId=7430, key='Color43', value=5) # color reset
        set_user_value(triggerId=7440, key='Color44', value=5) # color reset
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R01End()


class R01End(state.State):
    def on_enter(self):
        write_log(logName='christmasdancedancestop', event='9001', arg3='round_clear', arg4='1')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return R02Ready()
        if not user_detected(boxIds=[9001]):
            return FailAll()


#  R01 종료 후 생존자 인원수에 따른 전체 보상 지급
#  R02 시작
class R02Ready(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=2) # action name="GiveExp" arg1="9001" arg2="5.7"/
        end_mini_game_round(winnerBoxId=9001, expRate=0.2)
        set_achievement(triggerId=9001, type='trigger', achieve='ddstop_pass')
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R02Start()


class R02Start(state.State):
    def on_enter(self):
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
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__5$', arg3='3000', arg4='0') # Voice 02000954
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancetime_02')
        set_sound(triggerId=40000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_event_ui(type=0, arg2='2,5') # Round2
        start_mini_game_round(boxId=9001, round=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R02DanceTime()


#  R02 DanceTime 패턴 랜덤 
class R02DanceTime(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return R02DancePattern01()
        if random_condition(rate=30):
            return R02DancePattern02()
        if random_condition(rate=30):
            return R02DancePattern03()
        if random_condition(rate=3):
            return R02DancePattern0401()
        if random_condition(rate=3):
            return R02DancePattern0501()
        if random_condition(rate=2):
            return R02DancePattern0601()
        if random_condition(rate=2):
            return R02DancePattern0701()


#  R02 Dance 9000ms
class R02DancePattern01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return R02_GameStartDelay()


#  R02 Dance 12000ms
class R02DancePattern02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return R02_GameStartDelay()


#  R02 Dance 15000ms
class R02DancePattern03(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000936], state=1) # 15000ms
        set_user_value(triggerId=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=19000):
            return R02_GameStartDelay()


#  R02 Dance 7000ms+ 9000ms
class R02DancePattern0401(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return R02DancePattern0402()


class R02DancePattern0402(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__9$', arg3='1000') # Voice 02000958
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_01')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R02DancePattern0403()


class R02DancePattern0403(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__10$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R02DancePattern0404()


class R02DancePattern0404(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return R02_GameStartDelay()


#  R02 Dance 9000ms+ 7000ms
class R02DancePattern0501(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return R02DancePattern0502()


class R02DancePattern0502(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__11$', arg3='1000') # Voice 02000982
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_02')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000934], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R02DancePattern0503()


class R02DancePattern0503(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__12$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R02DancePattern0504()


class R02DancePattern0504(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return R02_GameStartDelay()


#  R02 Dance 12000ms+ 7000ms
class R02DancePattern0601(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return R02DancePattern0602()


class R02DancePattern0602(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__13$', arg3='1000') # Voice 02000983
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_03')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000935], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R02DancePattern0603()


class R02DancePattern0603(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__14$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R02DancePattern0604()


class R02DancePattern0604(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return R02_GameStartDelay()


#  R02 Dance 7000ms+ 12000ms
class R02DancePattern0701(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return R02DancePattern0702()


class R02DancePattern0702(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__15$', arg3='1000') # Voice 02000984
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_04')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R02DancePattern0703()


class R02DancePattern0703(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__16$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000935], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R02DancePattern0704()


class R02DancePattern0704(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return R02_GameStartDelay()


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
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000936], state=2) # 15000ms
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__18$', arg3='4000') # Voice 02000960
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_02')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R02_GameTimerStart()


class R02_GameTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=20, clearAtZero=True, display=True, arg5=-40) # Round2 / 20sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=2) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=2) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R02G00Check()


#  R02 인원 체크 시작 
#   테스트 수정 가능 지점
class R02G00Check(state.State):
    def on_tick(self) -> state.State:
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
        set_user_value(triggerId=7110, key='Color11', value=5) # color reset
        set_user_value(triggerId=7120, key='Color12', value=5) # color reset
        set_user_value(triggerId=7130, key='Color13', value=5) # color reset
        set_user_value(triggerId=7140, key='Color14', value=5) # color reset
        set_user_value(triggerId=7210, key='Color21', value=5) # color reset
        set_user_value(triggerId=7220, key='Color22', value=5) # color reset
        set_user_value(triggerId=7230, key='Color23', value=5) # color reset
        set_user_value(triggerId=7240, key='Color24', value=5) # color reset
        set_user_value(triggerId=7310, key='Color31', value=5) # color reset
        set_user_value(triggerId=7320, key='Color32', value=5) # color reset
        set_user_value(triggerId=7330, key='Color33', value=5) # color reset
        set_user_value(triggerId=7340, key='Color34', value=5) # color reset
        set_user_value(triggerId=7410, key='Color41', value=5) # color reset
        set_user_value(triggerId=7420, key='Color42', value=5) # color reset
        set_user_value(triggerId=7430, key='Color43', value=5) # color reset
        set_user_value(triggerId=7440, key='Color44', value=5) # color reset
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R02End()


class R02End(state.State):
    def on_enter(self):
        write_log(logName='christmasdancedancestop', event='9001', arg3='round_clear', arg4='2')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return R03Ready()
        if not user_detected(boxIds=[9001]):
            return FailAll()


#  R02 종료 후 생존자 인원수에 따른 전체 보상 지급
#  R03 시작
class R03Ready(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=3) # action name="GiveExp" arg1="9001" arg2="5.7"/
        end_mini_game_round(winnerBoxId=9001, expRate=0.2)
        set_achievement(triggerId=9001, type='trigger', achieve='ddstop_pass')
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R03Start()


class R03Start(state.State):
    def on_enter(self):
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
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__6$', arg3='3000', arg4='0') # Voice 02000955
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancetime_03')
        set_sound(triggerId=40000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_event_ui(type=0, arg2='3,5') # Round3
        start_mini_game_round(boxId=9001, round=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R03DanceTime()


#  R03 DanceTime 패턴 랜덤 
class R03DanceTime(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return R03DancePattern01()
        if random_condition(rate=30):
            return R03DancePattern02()
        if random_condition(rate=30):
            return R03DancePattern03()
        if random_condition(rate=3):
            return R03DancePattern0401()
        if random_condition(rate=3):
            return R03DancePattern0501()
        if random_condition(rate=2):
            return R03DancePattern0601()
        if random_condition(rate=2):
            return R03DancePattern0701()


#  R03 Dance 9000ms
class R03DancePattern01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return R03_GameStartDelay()


#  R03 Dance 12000ms
class R03DancePattern02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return R03_GameStartDelay()


#  R03 Dance 15000ms
class R03DancePattern03(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000936], state=1) # 15000ms
        set_user_value(triggerId=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=19000):
            return R03_GameStartDelay()


#  R03 Dance 7000ms+ 9000ms
class R03DancePattern0401(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return R03DancePattern0402()


class R03DancePattern0402(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__9$', arg3='1000') # Voice 02000958
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_01')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R03DancePattern0403()


class R03DancePattern0403(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__10$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R03DancePattern0404()


class R03DancePattern0404(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return R03_GameStartDelay()


#  R03 Dance 9000ms+ 7000ms
class R03DancePattern0501(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return R03DancePattern0502()


class R03DancePattern0502(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__11$', arg3='1000') # Voice 02000982
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_02')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000934], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R03DancePattern0503()


class R03DancePattern0503(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__12$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R03DancePattern0504()


class R03DancePattern0504(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return R03_GameStartDelay()


#  R03 Dance 12000ms+ 7000ms
class R03DancePattern0601(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return R03DancePattern0602()


class R03DancePattern0602(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__13$', arg3='1000') # Voice 02000983
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_03')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000935], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R03DancePattern0603()


class R03DancePattern0603(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__14$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R03DancePattern0604()


class R03DancePattern0604(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return R03_GameStartDelay()


#  R03 Dance 7000ms+ 12000ms
class R03DancePattern0701(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return R03DancePattern0702()


class R03DancePattern0702(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__15$', arg3='1000') # Voice 02000984
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_04')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R03DancePattern0703()


class R03DancePattern0703(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__16$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000935], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R03DancePattern0704()


class R03DancePattern0704(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return R03_GameStartDelay()


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
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000936], state=2) # 15000ms
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__19$', arg3='4000') # Voice 02000961
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_03')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R03_GameTimerStart()


class R03_GameTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=15, clearAtZero=True, display=True, arg5=-40) # Round3 / 15sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=3) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=3) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R03G00Check()


#  R03 인원 체크 시작 
#   테스트 수정 가능 지점
class R03G00Check(state.State):
    def on_tick(self) -> state.State:
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
        set_user_value(triggerId=7110, key='Color11', value=5) # color reset
        set_user_value(triggerId=7120, key='Color12', value=5) # color reset
        set_user_value(triggerId=7130, key='Color13', value=5) # color reset
        set_user_value(triggerId=7140, key='Color14', value=5) # color reset
        set_user_value(triggerId=7210, key='Color21', value=5) # color reset
        set_user_value(triggerId=7220, key='Color22', value=5) # color reset
        set_user_value(triggerId=7230, key='Color23', value=5) # color reset
        set_user_value(triggerId=7240, key='Color24', value=5) # color reset
        set_user_value(triggerId=7310, key='Color31', value=5) # color reset
        set_user_value(triggerId=7320, key='Color32', value=5) # color reset
        set_user_value(triggerId=7330, key='Color33', value=5) # color reset
        set_user_value(triggerId=7340, key='Color34', value=5) # color reset
        set_user_value(triggerId=7410, key='Color41', value=5) # color reset
        set_user_value(triggerId=7420, key='Color42', value=5) # color reset
        set_user_value(triggerId=7430, key='Color43', value=5) # color reset
        set_user_value(triggerId=7440, key='Color44', value=5) # color reset
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R03End()


class R03End(state.State):
    def on_enter(self):
        write_log(logName='christmasdancedancestop', event='9001', arg3='round_clear', arg4='3')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return R04Ready()
        if not user_detected(boxIds=[9001]):
            return FailAll()


#  R03 종료 후 생존자 인원수에 따른 전체 보상 지급
#  R04 시작
class R04Ready(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=4) # action name="GiveExp" arg1="9001" arg2="5.7"/
        end_mini_game_round(winnerBoxId=9001, expRate=0.2)
        set_achievement(triggerId=9001, type='trigger', achieve='ddstop_pass')
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R04Start()


class R04Start(state.State):
    def on_enter(self):
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
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__7$', arg3='3000', arg4='0') # Voice 02000956
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancetime_04')
        set_sound(triggerId=40000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_event_ui(type=0, arg2='4,5') # Round4
        start_mini_game_round(boxId=9001, round=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R04DanceTime()


#  R04 DanceTime 패턴 랜덤 
class R04DanceTime(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance

    def on_tick(self) -> state.State:
        if random_condition(rate=2):
            return R04DancePattern01()
        if random_condition(rate=3):
            return R04DancePattern02()
        if random_condition(rate=5):
            return R04DancePattern03()
        if random_condition(rate=25):
            return R04DancePattern0401()
        if random_condition(rate=25):
            return R04DancePattern0501()
        if random_condition(rate=20):
            return R04DancePattern0601()
        if random_condition(rate=20):
            return R04DancePattern0701()


#  R04 Dance 9000ms
class R04DancePattern01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return R04_GameStartDelay()


#  R04 Dance 12000ms
class R04DancePattern02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return R04_GameStartDelay()


#  R04 Dance 15000ms
class R04DancePattern03(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000936], state=1) # 15000ms
        set_user_value(triggerId=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=19000):
            return R04_GameStartDelay()


#  R04 Dance 7000ms+ 9000ms
class R04DancePattern0401(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return R04DancePattern0402()


class R04DancePattern0402(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__9$', arg3='1000') # Voice 02000958
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_01')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R04DancePattern0403()


class R04DancePattern0403(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__10$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R04DancePattern0404()


class R04DancePattern0404(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return R04_GameStartDelay()


#  R04 Dance 9000ms+ 7000ms
class R04DancePattern0501(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return R04DancePattern0502()


class R04DancePattern0502(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__11$', arg3='1000') # Voice 02000982
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_02')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000934], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R04DancePattern0503()


class R04DancePattern0503(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__12$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R04DancePattern0504()


class R04DancePattern0504(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return R04_GameStartDelay()


#  R04 Dance 12000ms+ 7000ms
class R04DancePattern0601(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return R04DancePattern0602()


class R04DancePattern0602(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__13$', arg3='1000') # Voice 02000983
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_03')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000935], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R04DancePattern0603()


class R04DancePattern0603(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__14$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R04DancePattern0604()


class R04DancePattern0604(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return R04_GameStartDelay()


#  R04 Dance 7000ms+ 12000ms
class R04DancePattern0701(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return R04DancePattern0702()


class R04DancePattern0702(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__15$', arg3='1000') # Voice 02000984
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_04')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R04DancePattern0703()


class R04DancePattern0703(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__16$', arg3='1500', arg4='0')
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000935], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R04DancePattern0704()


class R04DancePattern0704(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return R04_GameStartDelay()


class R04_GameStartDelay(state.State):
    def on_enter(self):
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R04_GambleOrNormal00()


#  R04 Gamble Or Normal 00 
#   테스트 수정 가능 지점
class R04_GambleOrNormal00(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=20, operator='GreaterEqual'):
            return R04_GambleOrJackpot()
        if count_users(boxId=9001, boxId=10, operator='GreaterEqual'):
            return R04_GambleOrNormal()
        if count_users(boxId=9001, boxId=10, operator='Less'):
            return R04_GameStart()


#  R04 Gamble Or JackPot 
class R04_GambleOrJackpot(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=75):
            return R04_GambleGuide01()
        if random_condition(rate=25):
            return R04_JackpotGuide01()


#  R04 Gamble Or Normal 
class R04_GambleOrNormal(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return R04_GambleGuide01()
        if random_condition(rate=50):
            return R04_GameStart()


#  R04 Gamble Game 
class R04_GambleGuide01(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=6) # Gamble Round
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=40000, arg2=True) # Game
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000936], state=2) # 15000ms
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__22$', arg3='3000') # Voice 02000964
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_06')
        write_log(logName='christmasdancedancestop', event='9001', arg3='system_event', arg4='4', arg5='gamble')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return R04_GambleGuide02()


class R04_GambleGuide02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__23$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return R04_GambleTimerStart()


class R04_GambleTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=15, clearAtZero=True, display=True, arg5=-40) # Gamble / 15sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=3) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=6) # 가이드 : 붉은색  발판

    def on_tick(self) -> state.State:
        if true():
            return R04GambleCheck()


#  R04 Gamble 인원 체크 시작 
#   테스트 수정 가능 지점
class R04GambleCheck(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=40, operator='Greater'):
            return G06P400_Random()
        if count_users(boxId=9001, boxId=30, operator='Greater'):
            return G06P300_Random()
        if count_users(boxId=9001, boxId=20, operator='Greater'):
            return G06P200_Random()
        if count_users(boxId=9001, boxId=10, operator='Greater'):
            return G06P100_Random()
        if count_users(boxId=9001, boxId=10, operator='LessEqual'):
            return G06P100_Random()


#  R04 Gamble 인원 체크 끝 
#  G06 Gamble Random Pattern 40
class G06P400_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return G06P401_RoundCheckIn()
        if random_condition(rate=10):
            return G06P402_RoundCheckIn()
        if random_condition(rate=10):
            return G06P403_RoundCheckIn()
        if random_condition(rate=10):
            return G06P404_RoundCheckIn()
        if random_condition(rate=10):
            return G06P405_RoundCheckIn()
        if random_condition(rate=10):
            return G06P406_RoundCheckIn()
        if random_condition(rate=10):
            return G06P407_RoundCheckIn()
        if random_condition(rate=10):
            return G06P408_RoundCheckIn()
        if random_condition(rate=10):
            return G06P409_RoundCheckIn()
        if random_condition(rate=10):
            return G06P410_RoundCheckIn()


#  G06 Gamble Random Pattern 30
class G06P300_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return G06P301_RoundCheckIn()
        if random_condition(rate=5):
            return G06P302_RoundCheckIn()
        if random_condition(rate=5):
            return G06P303_RoundCheckIn()
        if random_condition(rate=5):
            return G06P304_RoundCheckIn()
        if random_condition(rate=5):
            return G06P305_RoundCheckIn()
        if random_condition(rate=5):
            return G06P306_RoundCheckIn()
        if random_condition(rate=5):
            return G06P307_RoundCheckIn()
        if random_condition(rate=5):
            return G06P308_RoundCheckIn()
        if random_condition(rate=5):
            return G06P309_RoundCheckIn()
        if random_condition(rate=5):
            return G06P310_RoundCheckIn()
        if random_condition(rate=5):
            return G06P311_RoundCheckIn()
        if random_condition(rate=5):
            return G06P312_RoundCheckIn()
        if random_condition(rate=5):
            return G06P313_RoundCheckIn()
        if random_condition(rate=5):
            return G06P314_RoundCheckIn()
        if random_condition(rate=5):
            return G06P315_RoundCheckIn()
        if random_condition(rate=5):
            return G06P316_RoundCheckIn()
        if random_condition(rate=5):
            return G06P317_RoundCheckIn()
        if random_condition(rate=5):
            return G06P318_RoundCheckIn()
        if random_condition(rate=10):
            return G06P319_RoundCheckIn()
        if random_condition(rate=5):
            return G06P320_RoundCheckIn()


#  G06 Gamble Random Pattern 20
class G06P200_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return G06P201_RoundCheckIn()
        if random_condition(rate=5):
            return G06P202_RoundCheckIn()
        if random_condition(rate=5):
            return G06P203_RoundCheckIn()
        if random_condition(rate=5):
            return G06P204_RoundCheckIn()
        if random_condition(rate=5):
            return G06P205_RoundCheckIn()
        if random_condition(rate=5):
            return G06P206_RoundCheckIn()
        if random_condition(rate=5):
            return G06P207_RoundCheckIn()
        if random_condition(rate=5):
            return G06P208_RoundCheckIn()
        if random_condition(rate=5):
            return G06P209_RoundCheckIn()
        if random_condition(rate=5):
            return G06P210_RoundCheckIn()
        if random_condition(rate=5):
            return G06P211_RoundCheckIn()
        if random_condition(rate=5):
            return G06P212_RoundCheckIn()
        if random_condition(rate=5):
            return G06P213_RoundCheckIn()
        if random_condition(rate=5):
            return G06P214_RoundCheckIn()
        if random_condition(rate=5):
            return G06P215_RoundCheckIn()
        if random_condition(rate=5):
            return G06P216_RoundCheckIn()
        if random_condition(rate=5):
            return G06P217_RoundCheckIn()
        if random_condition(rate=5):
            return G06P218_RoundCheckIn()
        if random_condition(rate=5):
            return G06P219_RoundCheckIn()
        if random_condition(rate=5):
            return G06P220_RoundCheckIn()


#  G06 Gamble Random Pattern 10 
class G06P100_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return G06P101_RoundCheckIn()
        if random_condition(rate=10):
            return G06P102_RoundCheckIn()
        if random_condition(rate=10):
            return G06P103_RoundCheckIn()
        if random_condition(rate=10):
            return G06P104_RoundCheckIn()
        if random_condition(rate=10):
            return G06P105_RoundCheckIn()
        if random_condition(rate=10):
            return G06P106_RoundCheckIn()
        if random_condition(rate=10):
            return G06P107_RoundCheckIn()
        if random_condition(rate=10):
            return G06P108_RoundCheckIn()
        if random_condition(rate=10):
            return G06P109_RoundCheckIn()
        if random_condition(rate=10):
            return G06P110_RoundCheckIn()


#  R04 Jackpot Game 
class R04_JackpotGuide01(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=6) # Gamble Round
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=40000, arg2=True) # Game
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000936], state=2) # 15000ms
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__24$', arg3='3000') # Voice 02000964
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_06')
        write_log(logName='christmasdancedancestop', event='9001', arg3='system_event', arg4='4', arg5='jackpot')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return R04_JackpotGuide02()


class R04_JackpotGuide02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__25$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return R04_JackpotTimerStart()


class R04_JackpotTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=20, clearAtZero=True, display=True, arg5=-40) # Jackpot / 20sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=2) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=7) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R04JackpotCheck()


#  R04 Jackpot 인원 체크 시작 
#   테스트 수정 가능 지점
class R04JackpotCheck(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=40, operator='Greater'):
            return G07P400_Random()
        if count_users(boxId=9001, boxId=30, operator='Greater'):
            return G07P300_Random()
        if count_users(boxId=9001, boxId=20, operator='Greater'):
            return G07P200_Random()
        if count_users(boxId=9001, boxId=20, operator='LessEqual'):
            return G07P200_Random()


#  R04 Jackpot 인원 체크 끝 
#  G07 Jackpot Random Pattern 400
class G07P400_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return G07P401_RoundCheckIn()
        if random_condition(rate=10):
            return G07P402_RoundCheckIn()
        if random_condition(rate=10):
            return G07P403_RoundCheckIn()
        if random_condition(rate=10):
            return G07P404_RoundCheckIn()
        if random_condition(rate=10):
            return G07P405_RoundCheckIn()
        if random_condition(rate=10):
            return G07P406_RoundCheckIn()
        if random_condition(rate=10):
            return G07P407_RoundCheckIn()


#  G07 Jackpot Random Pattern 300
class G07P300_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return G07P301_RoundCheckIn()
        if random_condition(rate=10):
            return G07P302_RoundCheckIn()
        if random_condition(rate=10):
            return G07P303_RoundCheckIn()
        if random_condition(rate=10):
            return G07P304_RoundCheckIn()
        if random_condition(rate=10):
            return G07P305_RoundCheckIn()
        if random_condition(rate=10):
            return G07P306_RoundCheckIn()
        if random_condition(rate=10):
            return G07P307_RoundCheckIn()
        if random_condition(rate=10):
            return G07P308_RoundCheckIn()
        if random_condition(rate=10):
            return G07P309_RoundCheckIn()
        if random_condition(rate=10):
            return G07P310_RoundCheckIn()


#  G07 Jackpot Random Pattern 200
class G07P200_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return G07P201_RoundCheckIn()
        if random_condition(rate=10):
            return G07P202_RoundCheckIn()
        if random_condition(rate=10):
            return G07P203_RoundCheckIn()
        if random_condition(rate=10):
            return G07P204_RoundCheckIn()
        if random_condition(rate=10):
            return G07P205_RoundCheckIn()
        if random_condition(rate=10):
            return G07P206_RoundCheckIn()
        if random_condition(rate=10):
            return G07P207_RoundCheckIn()
        if random_condition(rate=10):
            return G07P208_RoundCheckIn()
        if random_condition(rate=10):
            return G07P209_RoundCheckIn()
        if random_condition(rate=10):
            return G07P210_RoundCheckIn()


#  R04 Gamble End 
class R04GambleEndDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=5) # color reset
        set_user_value(triggerId=7120, key='Color12', value=5) # color reset
        set_user_value(triggerId=7130, key='Color13', value=5) # color reset
        set_user_value(triggerId=7140, key='Color14', value=5) # color reset
        set_user_value(triggerId=7210, key='Color21', value=5) # color reset
        set_user_value(triggerId=7220, key='Color22', value=5) # color reset
        set_user_value(triggerId=7230, key='Color23', value=5) # color reset
        set_user_value(triggerId=7240, key='Color24', value=5) # color reset
        set_user_value(triggerId=7310, key='Color31', value=5) # color reset
        set_user_value(triggerId=7320, key='Color32', value=5) # color reset
        set_user_value(triggerId=7330, key='Color33', value=5) # color reset
        set_user_value(triggerId=7340, key='Color34', value=5) # color reset
        set_user_value(triggerId=7410, key='Color41', value=5) # color reset
        set_user_value(triggerId=7420, key='Color42', value=5) # color reset
        set_user_value(triggerId=7430, key='Color43', value=5) # color reset
        set_user_value(triggerId=7440, key='Color44', value=5) # color reset
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R04GambleEnd()


class R04GambleEnd(state.State):
    def on_enter(self):
        write_log(logName='christmasdancedancestop', event='9001', arg3='round_clear', arg4='4')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return R05ReadyAfterGamble()
        if not user_detected(boxIds=[9001]):
            return FailAll()


#  R05 After Gamble 
class R05ReadyAfterGamble(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=5) # action name="GiveExp" arg1="9001" arg2="5.7"/
        end_mini_game_round(winnerBoxId=9001, expRate=0.2)
        set_achievement(triggerId=9001, type='trigger', achieve='ddstop_pass')
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R05StartAfterGamble()


class R05StartAfterGamble(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='GambleSuccess', value=1):
            return R05StartGamblePass()
        if user_value(key='GambleSuccess', value=0):
            return R05StartGambleFail()


class R05StartGamblePass(state.State):
    def on_enter(self):
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
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__26$', arg3='5000', arg4='0') # Voice 02000966
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_02')
        set_event_ui(type=0, arg2='5,5') # Round5
        start_mini_game_round(boxId=9001, round=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return R05DanceTimeDelay()


class R05StartGambleFail(state.State):
    def on_enter(self):
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
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__27$', arg3='4000', arg4='0') # Voice 02000967
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_03')
        set_event_ui(type=0, arg2='5,5') # Round5
        start_mini_game_round(boxId=9001, round=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R05DanceTimeDelay()


#  R04 Normal Game 
class R04_GameStart(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=40000, arg2=True) # Game
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000936], state=2) # 15000ms
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__20$', arg3='4000') # Voice 02000962
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_04')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R04_GameTimerStart()


class R04_GameTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=10, clearAtZero=True, display=True, arg5=-40) # Round4 / 10sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=4) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=4) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R04G00Check()


#  R04 인원 체크 시작 
#   테스트 수정 가능 지점
class R04G00Check(state.State):
    def on_tick(self) -> state.State:
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
class R05DanceTimeDelay(state.State):
    def on_enter(self):
        set_sound(triggerId=40000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__33$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R05DanceTime()


#  R04 Normal End 
class R04EndDelay(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=5) # color reset
        set_user_value(triggerId=7120, key='Color12', value=5) # color reset
        set_user_value(triggerId=7130, key='Color13', value=5) # color reset
        set_user_value(triggerId=7140, key='Color14', value=5) # color reset
        set_user_value(triggerId=7210, key='Color21', value=5) # color reset
        set_user_value(triggerId=7220, key='Color22', value=5) # color reset
        set_user_value(triggerId=7230, key='Color23', value=5) # color reset
        set_user_value(triggerId=7240, key='Color24', value=5) # color reset
        set_user_value(triggerId=7310, key='Color31', value=5) # color reset
        set_user_value(triggerId=7320, key='Color32', value=5) # color reset
        set_user_value(triggerId=7330, key='Color33', value=5) # color reset
        set_user_value(triggerId=7340, key='Color34', value=5) # color reset
        set_user_value(triggerId=7410, key='Color41', value=5) # color reset
        set_user_value(triggerId=7420, key='Color42', value=5) # color reset
        set_user_value(triggerId=7430, key='Color43', value=5) # color reset
        set_user_value(triggerId=7440, key='Color44', value=5) # color reset
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R04End()


class R04End(state.State):
    def on_enter(self):
        write_log(logName='christmasdancedancestop', event='9001', arg3='round_clear', arg4='4')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return R05Ready()
        if not user_detected(boxIds=[9001]):
            return FailAll()


#  R04 종료 후 생존자 인원수에 따른 전체 보상 지급
#  R05 시작
class R05Ready(state.State):
    def on_enter(self):
        set_user_value(key='Round', value=5) # action name="GiveExp" arg1="9001" arg2="5.7"/
        end_mini_game_round(winnerBoxId=9001, expRate=0.2)
        set_achievement(triggerId=9001, type='trigger', achieve='ddstop_pass')
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R05Start()


class R05Start(state.State):
    def on_enter(self):
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
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__8$', arg3='3000', arg4='0') # Voice 02000957
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancetime_05')
        set_sound(triggerId=40000, arg2=False) # Intro
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_event_ui(type=0, arg2='5,5') # Round5
        start_mini_game_round(boxId=9001, round=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R05DanceTime()


#  R05 DanceTime 패턴 랜덤 
class R05DanceTime(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance

    def on_tick(self) -> state.State:
        if random_condition(rate=2):
            return R05DancePattern01()
        if random_condition(rate=3):
            return R05DancePattern02()
        if random_condition(rate=5):
            return R05DancePattern03()
        if random_condition(rate=20):
            return R05DancePattern0401()
        if random_condition(rate=20):
            return R05DancePattern0501()
        if random_condition(rate=25):
            return R05DancePattern0601()
        if random_condition(rate=25):
            return R05DancePattern0701()


#  R05 Dance 9000ms
class R05DancePattern01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=1) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return R05_GameStartDelay()


#  R05 Dance 12000ms
class R05DancePattern02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=2) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return R05_GameStartDelay()


#  R05 Dance 15000ms
class R05DancePattern03(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000936], state=1) # 15000ms
        set_user_value(triggerId=6, key='DanceGuide', value=3) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=19000):
            return R05_GameStartDelay()


#  R05 Dance 7000ms+ 9000ms
class R05DancePattern0401(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=41) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return R05DancePattern0402()


class R05DancePattern0402(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__34$', arg3='1000')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R05DancePattern0403()


class R05DancePattern0403(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__35$', arg3='1500', arg4='0') # Voice 02000985
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_05')
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R05DancePattern0404()


class R05DancePattern0404(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=42) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return R05_GameStartDelay()


#  R05 Dance 9000ms+ 7000ms
class R05DancePattern0501(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000934], state=1) # 9000ms
        set_user_value(triggerId=6, key='DanceGuide', value=51) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return R05DancePattern0502()


class R05DancePattern0502(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__36$', arg3='1000')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000934], state=0) # 9000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R05DancePattern0503()


class R05DancePattern0503(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__37$', arg3='1500', arg4='0') # Voice 02000985
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_05')
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R05DancePattern0504()


class R05DancePattern0504(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=52) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return R05_GameStartDelay()


#  R05 Dance 12000ms+ 7000ms
class R05DancePattern0601(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=61) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return R05DancePattern0602()


class R05DancePattern0602(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__38$', arg3='1000')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000935], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R05DancePattern0603()


class R05DancePattern0603(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__39$', arg3='1500', arg4='0') # Voice 02000985
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_05')
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R05DancePattern0604()


class R05DancePattern0604(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=62) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return R05_GameStartDelay()


#  R05 Dance 7000ms+ 12000ms
class R05DancePattern0701(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000933], state=1) # 7000ms
        set_user_value(triggerId=6, key='DanceGuide', value=71) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return R05DancePattern0702()


class R05DancePattern0702(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__40$', arg3='1000')
        set_sound(triggerId=20000, arg2=False) # Dance
        set_sound(triggerId=30000, arg2=True) # Silence
        set_effect(triggerIds=[8000], visible=True) # Scratch
        set_interact_object(triggerIds=[10000933], state=0) # 7000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R05DancePattern0703()


class R05DancePattern0703(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__41$', arg3='1500', arg4='0') # Voice 02000985
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancerandom_05')
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000935], state=0) # 12000ms

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return R05DancePattern0704()


class R05DancePattern0704(state.State):
    def on_enter(self):
        set_sound(triggerId=30000, arg2=False) # Silence
        set_sound(triggerId=20000, arg2=True) # Dance
        play_system_sound_in_box(boxIds=[9001], sound='DDStop_Stage_Ready_01')
        set_interact_object(triggerIds=[10000935], state=1) # 12000ms
        set_user_value(triggerId=6, key='DanceGuide', value=72) # 춤추기 가이드

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return R05_GameStartDelay()


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
        set_interact_object(triggerIds=[10000933], state=2) # 7000ms
        set_interact_object(triggerIds=[10000934], state=2) # 9000ms
        set_interact_object(triggerIds=[10000935], state=2) # 12000ms
        set_interact_object(triggerIds=[10000936], state=2) # 15000ms
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__21$', arg3='4000') # Voice 02000963
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Round_05')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R05_GameTimerStart()


class R05_GameTimerStart(state.State):
    def on_enter(self):
        set_timer(timerId='11111', seconds=10, clearAtZero=True, display=True, arg5=-40) # Round5 / 10sec  / UI 표시
        set_user_value(triggerId=8, key='CheerUpTimer', value=4) # 이속 증가 버프
        set_user_value(triggerId=7, key='GameGuide', value=5) # 가이드 : 숫자 발판

    def on_tick(self) -> state.State:
        if true():
            return R05G05Check()


#  R05 인원 체크 시작 
#   테스트 수정 가능 지점
class R05G05Check(state.State):
    def on_tick(self) -> state.State:
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
        set_user_value(triggerId=7110, key='Color11', value=5) # color reset
        set_user_value(triggerId=7120, key='Color12', value=5) # color reset
        set_user_value(triggerId=7130, key='Color13', value=5) # color reset
        set_user_value(triggerId=7140, key='Color14', value=5) # color reset
        set_user_value(triggerId=7210, key='Color21', value=5) # color reset
        set_user_value(triggerId=7220, key='Color22', value=5) # color reset
        set_user_value(triggerId=7230, key='Color23', value=5) # color reset
        set_user_value(triggerId=7240, key='Color24', value=5) # color reset
        set_user_value(triggerId=7310, key='Color31', value=5) # color reset
        set_user_value(triggerId=7320, key='Color32', value=5) # color reset
        set_user_value(triggerId=7330, key='Color33', value=5) # color reset
        set_user_value(triggerId=7340, key='Color34', value=5) # color reset
        set_user_value(triggerId=7410, key='Color41', value=5) # color reset
        set_user_value(triggerId=7420, key='Color42', value=5) # color reset
        set_user_value(triggerId=7430, key='Color43', value=5) # color reset
        set_user_value(triggerId=7440, key='Color44', value=5) # color reset
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R05End()


class R05End(state.State):
    def on_enter(self):
        write_log(logName='christmasdancedancestop', event='9001', arg3='round_clear', arg4='5')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return GameWrapUp()
        if not user_detected(boxIds=[9001]):
            return FailAll()


#  R05 종료 후 생존자 인원수에 따른 전체 보상 지급
class GameWrapUp(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=9001, expRate=0.2) # win
        set_achievement(triggerId=9001, type='trigger', achieve='ddstop_pass')
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier
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

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MiniGameCameraDirection()


#  완료 카메라 연출 : 내부 규칙에 따라 가장 캐릭터 외모 점수가 높은 타겟을 비주는 카메라 
class MiniGameCameraDirection(state.State):
    def on_enter(self):
        mini_game_camera_direction(boxId=9001, cameraId=910) # LocalTargetCamera

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GameOver()


#  완료 보상 
class GameOver(state.State):
    def on_enter(self):
        move_user(mapId=61000022, portalId=3, boxId=9002)
        set_event_ui(type=3, arg2='$61000008_ME__01_MASSIVEMAIN__29$', arg3='3000', arg4='9001') # Voice 02000968
        set_event_ui(type=4, arg2='$61000008_ME__01_MASSIVEMAIN__30$', arg3='3000', arg4='!9001') # Voice 02000969
        play_system_sound_in_box(boxIds=[9001], sound='DJDD_Ending_01')
        play_system_sound_in_box(boxIds=[9010,9011,9012,9013], sound='DJDD_Ending_02')
        set_achievement(triggerId=9001, type='trigger', achieve='ddstop_win')
        set_achievement(triggerId=9001, type='trigger', achieve='christmasddstop_win')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return GiveReward()


class GiveReward(state.State):
    def on_enter(self):
        mini_game_give_reward(winnerBoxId=9001, contentType='miniGame')
        end_mini_game(winnerBoxId=9001, gameName='christmasdancedancestop') # action name="아이템을생성한다" arg1="7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036,7037,7038,7039,7040,7041,7042,7043,7044,7045,7046,7047,7048,7049,7050,7051,7052,7053,7054,7055,7056,7057,7058,7059,7060,7061,7062,7063,7064,7065,7066,7067,7068,7069,7070,7071,7072,7073,7074,7075,7076,7077,7078,7079,7080,7081,7082,7083,7084"/
        add_buff(boxIds=[9001], skillId=70000019, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return LeaveAll()


class FailAll(state.State):
    def on_enter(self):
        end_mini_game(winnerBoxId=9001, gameName='christmasdancedancestop')
        set_event_ui(type=0, arg2='0,0')
        set_event_ui(type=5, arg2='$61000008_ME__01_MASSIVEMAIN__28$', arg3='5000') # Voice 02000969
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Ending_02')
        set_mesh(triggerIds=[8900,8901,8902,8903,8904,8905,8906,8907,8908,8909,8910,8911,8912,8913,8914], visible=False, arg3=400, arg4=0, arg5=0) # Barrier
        set_user_value(triggerId=4, key='BannerCheckIn', value=1)
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
        set_user_value(triggerId=7110, key='Color11', value=5) # color reset
        set_user_value(triggerId=7120, key='Color12', value=5) # color reset
        set_user_value(triggerId=7130, key='Color13', value=5) # color reset
        set_user_value(triggerId=7140, key='Color14', value=5) # color reset
        set_user_value(triggerId=7210, key='Color21', value=5) # color reset
        set_user_value(triggerId=7220, key='Color22', value=5) # color reset
        set_user_value(triggerId=7230, key='Color23', value=5) # color reset
        set_user_value(triggerId=7240, key='Color24', value=5) # color reset
        set_user_value(triggerId=7310, key='Color31', value=5) # color reset
        set_user_value(triggerId=7320, key='Color32', value=5) # color reset
        set_user_value(triggerId=7330, key='Color33', value=5) # color reset
        set_user_value(triggerId=7340, key='Color34', value=5) # color reset
        set_user_value(triggerId=7410, key='Color41', value=5) # color reset
        set_user_value(triggerId=7420, key='Color42', value=5) # color reset
        set_user_value(triggerId=7430, key='Color43', value=5) # color reset
        set_user_value(triggerId=7440, key='Color44', value=5) # color reset
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=True, arg3=400, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LeaveAll()

    def on_exit(self):
        reset_timer(timerId='10004')


class LeaveAll(state.State):
    def on_enter(self):
        set_local_camera(cameraId=910, enable=False) # LocalTargetCamera
        unset_mini_game_area_for_hack() # 해킹 보안 종료
        set_sound(triggerId=40000, arg2=False) # Game
        set_user_value(triggerId=5, key='BannerNumber', value=0)
        set_event_ui(type=1, arg2='$61000008_ME__01_MASSIVEMAIN__31$', arg3='10000') # Voice 02000970
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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


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
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
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
            return RoundCheckOut()


#  GambleGame Pattern
#  G06 P101 
class G06P101_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P101Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P101_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P101_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P101_Check()


class G06P101_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P101TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P101_End()


class G06P101_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P101End', value=1):
            return RoundCheckOut()


#  G06 P102 
class G06P102_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P102Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P102_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P102_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P102_Check()


class G06P102_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P102TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P102_End()


class G06P102_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P102End', value=1):
            return RoundCheckOut()


#  G06 P103 
class G06P103_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P103Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P103_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P103_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P103_Check()


class G06P103_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P103TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P103_End()


class G06P103_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P103End', value=1):
            return RoundCheckOut()


#  G06 P104 
class G06P104_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P104Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P104_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P104_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P104_Check()


class G06P104_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P104TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P104_End()


class G06P104_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P104End', value=1):
            return RoundCheckOut()


#  G06 P105 
class G06P105_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P105Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P105_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P105_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P105_Check()


class G06P105_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P105TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P105_End()


class G06P105_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P105End', value=1):
            return RoundCheckOut()


#  G06 P106 
class G06P106_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P106Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P106_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P106_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P106_Check()


class G06P106_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P106TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P106_End()


class G06P106_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P106End', value=1):
            return RoundCheckOut()


#  G06 P107 
class G06P107_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P107Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P107_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P107_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P107_Check()


class G06P107_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P107TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P107_End()


class G06P107_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P107End', value=1):
            return RoundCheckOut()


#  G06 P108 
class G06P108_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P108Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P108_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P108_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P108_Check()


class G06P108_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P108TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P108_End()


class G06P108_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P108End', value=1):
            return RoundCheckOut()


#  G06 P109 
class G06P109_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P109Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P109_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P109_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P109_Check()


class G06P109_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P109TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P109_End()


class G06P109_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P109End', value=1):
            return RoundCheckOut()


#  G06 P110 
class G06P110_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P110Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P110_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P110_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P110_Check()


class G06P110_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P110TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P110_End()


class G06P110_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P110End', value=1):
            return RoundCheckOut()


#  G06 P201 
class G06P201_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P201Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P201_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P201_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P201_Check()


class G06P201_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P201TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P201_End()


class G06P201_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P201End', value=1):
            return RoundCheckOut()


#  G06 P202 
class G06P202_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P202Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P202_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P202_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P202_Check()


class G06P202_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P202TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P202_End()


class G06P202_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P202End', value=1):
            return RoundCheckOut()


#  G06 P203 
class G06P203_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P203Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P203_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P203_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P203_Check()


class G06P203_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P203TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P203_End()


class G06P203_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P203End', value=1):
            return RoundCheckOut()


#  G06 P204 
class G06P204_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P204Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P204_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P204_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P204_Check()


class G06P204_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P204TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P204_End()


class G06P204_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P204End', value=1):
            return RoundCheckOut()


#  G06 P205 
class G06P205_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P205Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P205_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P205_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P205_Check()


class G06P205_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P205TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P205_End()


class G06P205_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P205End', value=1):
            return RoundCheckOut()


#  G06 P206 
class G06P206_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P206Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P206_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P206_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P206_Check()


class G06P206_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P206TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P206_End()


class G06P206_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P206End', value=1):
            return RoundCheckOut()


#  G06 P207 
class G06P207_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P207Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P207_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P207_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P207_Check()


class G06P207_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P207TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P207_End()


class G06P207_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P207End', value=1):
            return RoundCheckOut()


#  G06 P208 
class G06P208_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P208Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P208_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P208_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P208_Check()


class G06P208_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P208TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P208_End()


class G06P208_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P208End', value=1):
            return RoundCheckOut()


#  G06 P209 
class G06P209_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P209Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P209_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P209_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P209_Check()


class G06P209_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P209TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P209_End()


class G06P209_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P209End', value=1):
            return RoundCheckOut()


#  G06 P210 
class G06P210_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P210Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P210_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P210_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P210_Check()


class G06P210_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P210TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P210_End()


class G06P210_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P210End', value=1):
            return RoundCheckOut()


#  G06 P211 
class G06P211_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P211Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P211_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P211_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P211_Check()


class G06P211_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P211TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P211_End()


class G06P211_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P211End', value=1):
            return RoundCheckOut()


#  G06 P212 
class G06P212_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P212Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P212_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P212_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P212_Check()


class G06P212_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P212TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P212_End()


class G06P212_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P212End', value=1):
            return RoundCheckOut()


#  G06 P213 
class G06P213_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P213Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P213_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P213_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P213_Check()


class G06P213_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P213TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P213_End()


class G06P213_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P213End', value=1):
            return RoundCheckOut()


#  G06 P214 
class G06P214_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P214Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P214_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P214_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P214_Check()


class G06P214_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P214TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P214_End()


class G06P214_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P214End', value=1):
            return RoundCheckOut()


#  G06 P215 
class G06P215_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P215Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P215_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P215_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P215_Check()


class G06P215_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P215TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P215_End()


class G06P215_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P215End', value=1):
            return RoundCheckOut()


#  G06 P216 
class G06P216_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P216Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P216_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P216_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P216_Check()


class G06P216_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P216TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P216_End()


class G06P216_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P216End', value=1):
            return RoundCheckOut()


#  G06 P217 
class G06P217_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P217Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P217_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P217_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P217_Check()


class G06P217_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P217TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P217_End()


class G06P217_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P217End', value=1):
            return RoundCheckOut()


#  G06 P218 
class G06P218_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P218Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P218_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P218_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P218_Check()


class G06P218_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P218TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P218_End()


class G06P218_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P218End', value=1):
            return RoundCheckOut()


#  G06 P219 
class G06P219_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P219Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P219_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P219_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P219_Check()


class G06P219_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P219TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P219_End()


class G06P219_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P219End', value=1):
            return RoundCheckOut()


#  G06 P220 
class G06P220_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P220Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P220_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P220_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P220_Check()


class G06P220_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P220TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P220_End()


class G06P220_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P220End', value=1):
            return RoundCheckOut()


#  G06 P301 
class G06P301_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P301Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P301_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P301_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P301_Check()


class G06P301_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P301TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P301_End()


class G06P301_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P301End', value=1):
            return RoundCheckOut()


#  G06 P302 
class G06P302_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P302Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P302_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P302_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P302_Check()


class G06P302_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P302TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P302_End()


class G06P302_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P302End', value=1):
            return RoundCheckOut()


#  G06 P303 
class G06P303_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P303Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P303_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P303_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P303_Check()


class G06P303_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P303TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P303_End()


class G06P303_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P303End', value=1):
            return RoundCheckOut()


#  G06 P304 
class G06P304_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P304Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P304_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P304_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P304_Check()


class G06P304_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P304TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P304_End()


class G06P304_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P304End', value=1):
            return RoundCheckOut()


#  G06 P305 
class G06P305_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P305Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P305_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P305_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P305_Check()


class G06P305_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P305TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P305_End()


class G06P305_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P305End', value=1):
            return RoundCheckOut()


#  G06 P306 
class G06P306_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P306Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P306_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P306_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P306_Check()


class G06P306_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P306TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P306_End()


class G06P306_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P306End', value=1):
            return RoundCheckOut()


#  G06 P307 
class G06P307_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P307Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P307_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P307_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P307_Check()


class G06P307_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P307TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P307_End()


class G06P307_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P307End', value=1):
            return RoundCheckOut()


#  G06 P308 
class G06P308_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P308Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P308_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P308_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P308_Check()


class G06P308_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P308TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P308_End()


class G06P308_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P308End', value=1):
            return RoundCheckOut()


#  G06 P309 
class G06P309_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P309Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P309_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P309_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P309_Check()


class G06P309_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P309TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P309_End()


class G06P309_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P309End', value=1):
            return RoundCheckOut()


#  G06 P310 
class G06P310_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P310Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P310_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P310_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P310_Check()


class G06P310_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P310TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P310_End()


class G06P310_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P310End', value=1):
            return RoundCheckOut()


#  G06 P311 
class G06P311_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P311Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P311_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P311_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P311_Check()


class G06P311_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P311TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P311_End()


class G06P311_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P311End', value=1):
            return RoundCheckOut()


#  G06 P312 
class G06P312_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P312Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P312_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P312_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P312_Check()


class G06P312_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P312TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P312_End()


class G06P312_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P312End', value=1):
            return RoundCheckOut()


#  G06 P313 
class G06P313_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P313Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P313_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P313_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P313_Check()


class G06P313_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P313TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P313_End()


class G06P313_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P313End', value=1):
            return RoundCheckOut()


#  G06 P314 
class G06P314_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P314Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P314_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P314_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P314_Check()


class G06P314_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P314TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P314_End()


class G06P314_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P314End', value=1):
            return RoundCheckOut()


#  G06 P315 
class G06P315_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P315Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P315_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P315_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P315_Check()


class G06P315_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P315TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P315_End()


class G06P315_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P315End', value=1):
            return RoundCheckOut()


#  G06 P316 
class G06P316_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P316Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P316_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P316_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P316_Check()


class G06P316_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P316TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P316_End()


class G06P316_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P316End', value=1):
            return RoundCheckOut()


#  G06 P317 
class G06P317_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P317Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P317_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P317_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P317_Check()


class G06P317_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P317TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P317_End()


class G06P317_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P317End', value=1):
            return RoundCheckOut()


#  G06 P318 
class G06P318_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P318Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P318_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P318_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P318_Check()


class G06P318_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P318TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P318_End()


class G06P318_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P318End', value=1):
            return RoundCheckOut()


#  G06 P319 
class G06P319_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P319Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P319_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P319_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P319_Check()


class G06P319_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P319TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P319_End()


class G06P319_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P319End', value=1):
            return RoundCheckOut()


#  G06 P320 
class G06P320_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P320Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P320_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P320_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P320_Check()


class G06P320_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P320TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P320_End()


class G06P320_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P320End', value=1):
            return RoundCheckOut()


#  G06 P401 
class G06P401_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P401Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P401_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P401_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P401_Check()


class G06P401_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P401TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P401_End()


class G06P401_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P401End', value=1):
            return RoundCheckOut()


#  G06 P402 
class G06P402_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P402Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P402_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P402_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P402_Check()


class G06P402_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P402TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P402_End()


class G06P402_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P402End', value=1):
            return RoundCheckOut()


#  G06 P403 
class G06P403_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P403Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P403_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P403_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P403_Check()


class G06P403_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P403TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P403_End()


class G06P403_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P403End', value=1):
            return RoundCheckOut()


#  G06 P404 
class G06P404_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P404Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P404_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P404_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P404_Check()


class G06P404_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P404TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P404_End()


class G06P404_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P404End', value=1):
            return RoundCheckOut()


#  G06 P405 
class G06P405_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P405Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P405_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P405_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P405_Check()


class G06P405_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P405TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P405_End()


class G06P405_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P405End', value=1):
            return RoundCheckOut()


#  G06 P406 
class G06P406_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P406Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P406_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P406_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P406_Check()


class G06P406_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P406TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P406_End()


class G06P406_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P406End', value=1):
            return RoundCheckOut()


#  G06 P407 
class G06P407_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P407Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P407_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P407_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P407_Check()


class G06P407_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P407TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P407_End()


class G06P407_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P407End', value=1):
            return RoundCheckOut()


#  G06 P408 
class G06P408_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P408Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P408_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P408_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P408_Check()


class G06P408_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P408TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P408_End()


class G06P408_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P408End', value=1):
            return RoundCheckOut()


#  G06 P409 
class G06P409_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P409Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P409_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P409_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P409_Check()


class G06P409_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P409TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P409_End()


class G06P409_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P409End', value=1):
            return RoundCheckOut()


#  G06 P410 
class G06P410_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P410Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G06P410_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G06P410_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G06P410_Check()


class G06P410_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=600, key='G06P410TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G06P410_End()


class G06P410_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G06P410End', value=1):
            return RoundCheckOut()


#  JackpotGame Pattern
#  G07 P201 
class G07P201_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P201Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P201_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P201_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P201_Check()


class G07P201_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P201TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P201_End()


class G07P201_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P201End', value=1):
            return RoundCheckOut()


#  G07 P202 
class G07P202_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P202Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P202_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P202_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P202_Check()


class G07P202_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P202TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P202_End()


class G07P202_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P202End', value=1):
            return RoundCheckOut()


#  G07 P203 
class G07P203_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P203Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P203_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P203_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P203_Check()


class G07P203_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P203TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P203_End()


class G07P203_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P203End', value=1):
            return RoundCheckOut()


#  G07 P204 
class G07P204_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P204Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P204_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P204_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P204_Check()


class G07P204_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P204TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P204_End()


class G07P204_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P204End', value=1):
            return RoundCheckOut()


#  G07 P205 
class G07P205_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P205Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P205_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P205_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P205_Check()


class G07P205_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P205TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P205_End()


class G07P205_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P205End', value=1):
            return RoundCheckOut()


#  G07 P206 
class G07P206_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P206Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P206_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P206_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P206_Check()


class G07P206_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P206TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P206_End()


class G07P206_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P206End', value=1):
            return RoundCheckOut()


#  G07 P207 
class G07P207_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P207Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P207_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P207_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P207_Check()


class G07P207_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P207TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P207_End()


class G07P207_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P207End', value=1):
            return RoundCheckOut()


#  G07 P208 
class G07P208_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P208Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P208_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P208_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P208_Check()


class G07P208_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P208TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P208_End()


class G07P208_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P208End', value=1):
            return RoundCheckOut()


#  G07 P209 
class G07P209_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P209Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P209_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P209_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P209_Check()


class G07P209_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P209TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P209_End()


class G07P209_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P209End', value=1):
            return RoundCheckOut()


#  G07 P210 
class G07P210_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P210Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P210_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P210_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P210_Check()


class G07P210_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P210TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P210_End()


class G07P210_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P210End', value=1):
            return RoundCheckOut()


#  G07 P301 
class G07P301_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P301Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P301_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P301_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P301_Check()


class G07P301_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P301TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P301_End()


class G07P301_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P301End', value=1):
            return RoundCheckOut()


#  G07 P302 
class G07P302_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P302Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P302_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P302_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P302_Check()


class G07P302_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P302TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P302_End()


class G07P302_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P302End', value=1):
            return RoundCheckOut()


#  G07 P303 
class G07P303_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P303Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P303_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P303_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P303_Check()


class G07P303_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P303TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P303_End()


class G07P303_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P303End', value=1):
            return RoundCheckOut()


#  G07 P304 
class G07P304_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P304Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P304_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P304_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P304_Check()


class G07P304_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P304TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P304_End()


class G07P304_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P304End', value=1):
            return RoundCheckOut()


#  G07 P305 
class G07P305_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P305Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P305_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P305_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P305_Check()


class G07P305_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P305TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P305_End()


class G07P305_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P305End', value=1):
            return RoundCheckOut()


#  G07 P306 
class G07P306_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P306Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P306_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P306_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P306_Check()


class G07P306_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P306TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P306_End()


class G07P306_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P306End', value=1):
            return RoundCheckOut()


#  G07 P307 
class G07P307_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P307Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P307_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P307_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P307_Check()


class G07P307_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P307TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P307_End()


class G07P307_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P307End', value=1):
            return RoundCheckOut()


#  G07 P308 
class G07P308_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P308Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P308_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P308_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P308_Check()


class G07P308_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P308TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P308_End()


class G07P308_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P308End', value=1):
            return RoundCheckOut()


#  G07 P309 
class G07P309_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P309Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P309_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P309_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P309_Check()


class G07P309_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P309TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P309_End()


class G07P309_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P309End', value=1):
            return RoundCheckOut()


#  G07 P310 
class G07P310_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P310Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P310_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P310_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P310_Check()


class G07P310_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P310TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P310_End()


class G07P310_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P310End', value=1):
            return RoundCheckOut()


#  G07 P401 
class G07P401_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P401Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P401_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P401_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P401_Check()


class G07P401_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P401TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P401_End()


class G07P401_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P401End', value=1):
            return RoundCheckOut()


#  G07 P402 
class G07P402_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P402Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P402_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P402_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P402_Check()


class G07P402_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P402TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P402_End()


class G07P402_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P402End', value=1):
            return RoundCheckOut()


#  G07 P403 
class G07P403_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P403Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P403_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P403_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P403_Check()


class G07P403_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P403TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P403_End()


class G07P403_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P403End', value=1):
            return RoundCheckOut()


#  G07 P404 
class G07P404_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P404Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P404_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P404_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P404_Check()


class G07P404_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P404TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P404_End()


class G07P404_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P404End', value=1):
            return RoundCheckOut()


#  G07 P405 
class G07P405_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P405Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P405_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P405_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P405_Check()


class G07P405_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P405TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P405_End()


class G07P405_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P405End', value=1):
            return RoundCheckOut()


#  G07 P406 
class G07P406_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P406Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P406_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P406_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P406_Check()


class G07P406_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P406TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P406_End()


class G07P406_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P406End', value=1):
            return RoundCheckOut()


#  G07 P407 
class G07P407_RoundCheckIn(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P407Set', value=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11111'):
            return G07P407_CleanUp()

    def on_exit(self):
        reset_timer(timerId='11111')


class G07P407_CleanUp(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        select_camera(triggerId=901, enable=True)
        set_cinematic_ui(type=3, script='$61000008_ME__01_MASSIVEMAIN__32$') # Voice 02000965
        play_system_sound_in_box(boxIds=[9000], sound='DJDD_Dancing_01')
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633], visible=False, arg3=2000, arg4=0, arg5=2) # 스테이지 정리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return G07P407_Check()


class G07P407_Check(state.State):
    def on_enter(self):
        set_user_value(triggerId=700, key='G07P407TimeLimit', value=1)
        play_system_sound_in_box(boxIds=[6901,6902,6903,6904,6905,6906], sound='DDStop_Stage_Fail_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return G07P407_End()


class G07P407_End(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='G07P407End', value=1):
            return RoundCheckOut()


class RoundCheckOut(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='BannerCheckIn', value=1)
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
        if user_value(key='Round', value=6):
            return R04GambleEndDelay()
        if user_value(key='Round', value=5):
            return R05EndDelay()

    def on_exit(self):
        set_user_value(key='Round', value=0)


