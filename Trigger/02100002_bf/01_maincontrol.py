""" trigger/02100002_bf/01_maincontrol.xml """
from common import *
import state

from dungeon_common.checkuser10_guildraid import *

class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False) # RainbowSlime_Sound
        set_effect(triggerIds=[5002], visible=False) # PoopSlime_Sound
        limit_spawn_npc_count(limitCount=0, desc='몬스터 스폰 제한을 끕니다.') # 공장 가동하기 반응 오브젝트
        set_interact_object(triggerIds=[10001239], state=0) # 결과 출력하기 반응 오브젝트
        set_interact_object(triggerIds=[10001240], state=0) # 용광로 바닥 TOK always off
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419,3420,3421,3422,3423], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521,3522,3523], visible=False, arg3=0, arg4=0, arg5=0) # 용광로 더미 몬스터 : 슬라임 죽이기
        destroy_monster(spawnIds=[900]) # 결과 몬스터
        destroy_monster(spawnIds=[1000,2000]) # 무지개 슬라임 공장 전용 위젯
        create_widget(type='RainbowMonster') # 입구 포탈
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True) # 출구 포탈
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False) # 아래층에서 위 층으로 올라갈 수 있는 일방 포탈
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716,3717,3718,3719,3720,3721,3722,3723,3724,3725,3726,3727,3728,3729,3730,3731,3732,3733,3734,3735,3736,3737,3738,3739,3740,3741,3742,3743,3744,3745,3746,3747,3748,3749,3750,3751,3752,3753,3754,3755,3756,3757,3758,3759,3760,3761,3762,3763,3764,3765,3766,3767,3768,3769,3770,3771,3772,3773,3774,3775,3776,3777,3778,3779,3780,3781,3782,3783,3784,3785,3786,3787,3788,3789,3790,3791,3792,3793,3794,3795,3796,3797,3798,3799], visible=True, arg3=0, arg4=0, arg5=0) # 빨강 게이지 샘플
        set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816,3817,3818,3819], visible=True, arg3=0, arg4=0, arg5=0) # 용광로 더미 몬스터 : 슬라임 죽이기
        create_monster(spawnIds=[900], arg2=False) # 해당 필드에 몬스터의 수가  limitCount를 넘어가면 스폰을 중단한다.
        limit_spawn_npc_count(limitCount=200) # 정상 슬라임 몬스터 id 그룹 할당
        widget_action(type='RainbowMonster', func='CreateGroup', widgetArgNum=1, widgetArg='34000122,34000123,34000124,34000142')
        widget_action(type='RainbowMonster', func='CreateGroup', widgetArgNum=2, widgetArg='34000128,34000129,34000130,34000143')
        widget_action(type='RainbowMonster', func='CreateGroup', widgetArgNum=3, widgetArg='34000125,34000126,34000127,34000144')
        widget_action(type='RainbowMonster', func='CreateGroup', widgetArgNum=4, widgetArg='34000131,34000132,34000133,34000145')
        widget_action(type='RainbowMonster', func='CreateGroup', widgetArgNum=5, widgetArg='34000134,34000135,34000136,34000146') # 용광로 더미 몬스터에게 죽임을 당한 정상 슬라임만 점수로 체크
        widget_action(type='RainbowMonster', func='SetKillerNpc', widgetArg='34000141', desc='34000141 npc가 죽인 몬스터만 스코어에 반영') # 일정 시간 동안 용광로에 유입된 정상 슬라임이 없으면 게이지 감소 패널티
        widget_action(type='RainbowMonster', func='SetLoseScoreTick', widgetArgNum=60000, desc='60초마다 감점') # 용광로에 불량 슬라임이 들어가면 전체 게이지 랜덤 감소 패널티 / 34000138,34000139 두 종류 몬스터 미구현항목으로 제외 시킴(기획상 BigMom과 소환된 꼬마)
        widget_action(type='RainbowMonster', func='SetBadNpc', widgetArg='34000121,34000137', desc='해당 NPC가 킬러에게 죽으면 모든 게이지 감소')
        widget_action(type='RainbowMonster', func='SetBadNpcScore', widgetArg='2-5', desc='2~5칸 게이지가 떨어진다')
        widget_action(type='RainbowMonster', func='SetBadNpcSoundKey', widgetArg='GuildRaid_RainbowSlimeFactory_ScreenWarning_01', desc='게이지가 떨어질때 플레이할 사운드')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MaxGaugePattern_Random()


# MaxGaugePatter_RandomPick 
#  5개의 그룹에서 100, 120, 140, 160, 180, 200 값 중 중복 없이 5개  Pick : 조합 
class MaxGaugePattern_Random(state.State):
    def on_enter(self):
        widget_action(type='RainbowMonster', func='InitRandomMaxScore', widgetArg='120,120,140,140,160,160')
        # <action name="WidgetAction" arg1="RainbowMonster" arg2="ShowMaxScore" />
        widget_action(type='RainbowMonster', func='InitScoreMesh', widgetArgNum=1, widgetArg='3100')
        widget_action(type='RainbowMonster', func='InitScoreMesh', widgetArgNum=2, widgetArg='3200')
        widget_action(type='RainbowMonster', func='InitScoreMesh', widgetArgNum=3, widgetArg='3300')
        widget_action(type='RainbowMonster', func='InitScoreMesh', widgetArgNum=4, widgetArg='3500')
        widget_action(type='RainbowMonster', func='InitScoreMesh', widgetArgNum=5, widgetArg='3400')

    def on_tick(self) -> state.State:
        if true():
            return CheckUser10_GuildRaid()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_intro()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ShowCaption01()

state.DungeonStart = DungeonStart


#  설명문 출력 
class ShowCaption01(state.State):
    def on_enter(self):
        set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__0$')
        set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return ShowCaption01Skip()


class ShowCaption01Skip(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ShowCaption02()


class ShowCaption02(state.State):
    def on_enter(self):
        set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__1$')
        set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return ShowCaption02Skip()


class ShowCaption02Skip(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ShowCaption03()


class ShowCaption03(state.State):
    def on_enter(self):
        select_camera(triggerId=900, enable=True)
        set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__2$')
        set_skip(state=ShowCaption03Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return ShowCaption03Skip()


class ShowCaption03Skip(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ShowCaption04()


class ShowCaption04(state.State):
    def on_enter(self):
        select_camera(triggerId=901, enable=True)
        set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__3$')
        set_skip(state=ShowCaption04Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return ShowCaption04Skip()


class ShowCaption04Skip(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ShowCaption05()


class ShowCaption05(state.State):
    def on_enter(self):
        select_camera(triggerId=902, enable=True)
        set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__4$')
        set_skip(state=ShowCaption05Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return ShowCaption05Skip()


class ShowCaption05Skip(state.State):
    def on_enter(self):
        set_skip()
        reset_camera(interpolationTime=1)
        set_user_value(triggerId=2, key='GuideNpcSpawn', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CloseCaptionSetting()


class CloseCaptionSetting(state.State):
    def on_enter(self):
        close_cinematic() # 컬러 게이지 샘플
        set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716,3717,3718,3719,3720,3721,3722,3723,3724,3725,3726,3727,3728,3729,3730,3731,3732,3733,3734,3735,3736,3737,3738,3739,3740,3741,3742,3743,3744,3745,3746,3747,3748,3749,3750,3751,3752,3753,3754,3755,3756,3757,3758,3759,3760,3761,3762,3763,3764,3765,3766,3767,3768,3769,3770,3771,3772,3773,3774,3775,3776,3777,3778,3779,3780,3781,3782,3783,3784,3785,3786,3787,3788,3789,3790,3791,3792,3793,3794,3795,3796,3797,3798,3799], visible=False, arg3=0, arg4=0, arg5=0) # 빨강 게이지 샘플
        set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816,3817,3818,3819], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Guide01()


class Guide01(state.State):
    def on_enter(self):
        set_user_value(triggerId=99, key='PortalOn', value=1)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__5$', arg3='5000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Guide02()


class Guide02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__6$', arg3='3000') # 공장 가동하기
        set_interact_object(triggerIds=[10001239], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001239], arg2=0):
            return Guide03()


class Guide03(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='GuildRaid_RainbowSlimeFactory_MachineOn_01')
        set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__7$', arg3='2000')
        set_interact_object(triggerIds=[10001239], state=0) # 슬라임 생성 신호
        set_user_value(triggerId=11, key='ActivateTank', value=1)
        set_user_value(triggerId=12, key='ActivateTank', value=1)
        set_user_value(triggerId=13, key='ActivateTank', value=1)
        set_user_value(triggerId=14, key='ActivateTank', value=1)
        set_user_value(triggerId=15, key='ActivateTank', value=1) # 홀더 활성화 신호
        set_user_value(triggerId=21, key='ActivateHolder', value=1)
        set_user_value(triggerId=22, key='ActivateHolder', value=1)
        set_user_value(triggerId=23, key='ActivateHolder', value=1)
        set_user_value(triggerId=24, key='ActivateHolder', value=1)
        set_user_value(triggerId=25, key='ActivateHolder', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TimmerStart()


class TimmerStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=99, key='MissionStart', value=1)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01') # 제한 시간 10분
        set_timer(timerId='10000', seconds=600, clearAtZero=True, display=True, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=60000):
            return EnableCheckOutput()


class EnableCheckOutput(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__8$', arg3='3000') # 결과 출력하기 반응 오브젝트
        set_interact_object(triggerIds=[10001240], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001240], arg2=0):
            return CheckSuccess()
        if time_expired(timerId='10000'):
            return MissionFail()

    def on_exit(self):
        set_user_value(triggerId=11, key='DungeonQuit', value=1)
        set_user_value(triggerId=12, key='DungeonQuit', value=1)
        set_user_value(triggerId=13, key='DungeonQuit', value=1)
        set_user_value(triggerId=14, key='DungeonQuit', value=1)
        set_user_value(triggerId=15, key='DungeonQuit', value=1)
        set_user_value(triggerId=21, key='DungeonQuit', value=1)
        set_user_value(triggerId=22, key='DungeonQuit', value=1)
        set_user_value(triggerId=23, key='DungeonQuit', value=1)
        set_user_value(triggerId=24, key='DungeonQuit', value=1)
        set_user_value(triggerId=25, key='DungeonQuit', value=1) # 용광로 소멸
        destroy_monster(spawnIds=[900]) # 입구 포탈
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10001234], state=0)


class CheckSuccess(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if widget_condition(type='RainbowMonster', name='IsMissionSuccess', condition='19-21'):
            return HappyEndingStart()
        if not widget_condition(type='RainbowMonster', name='IsMissionSuccess', condition='19-21'):
            return BadEndingStart()


#  BadEnding 연출 
class BadEndingStart(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=909, enable=True)
        play_system_sound_in_box(sound='GuildRaid_RainbowSlimeFactory_Result_01')
        move_user(mapId=2100002, portalId=2, boxId=9901) # 용광로 안에 있는 PC 안전한 곳으로 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BadEndingSpawn()


class BadEndingSpawn(state.State):
    def on_enter(self):
        select_camera(triggerId=908, enable=True)
        set_effect(triggerIds=[5002], visible=True) # PoopSlime_Sound
        create_monster(spawnIds=[2000], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return BadEndingEnd()


class BadEndingEnd(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return MissionFail()

    def on_exit(self):
        set_achievement(triggerId=9902, type='trigger', achieve='MakeMutantKingSlime')


#  HappyEnding 연출 
class HappyEndingStart(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=909, enable=True)
        play_system_sound_in_box(sound='GuildRaid_RainbowSlimeFactory_Result_01')
        move_user(mapId=2100002, portalId=2, boxId=9901) # 용광로 안에 있는 PC 안전한 곳으로 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return HappyEndingSpawn()


class HappyEndingSpawn(state.State):
    def on_enter(self):
        select_camera(triggerId=908, enable=True)
        set_effect(triggerIds=[5001], visible=True) # RainbowSlime_Sound
        create_monster(spawnIds=[1000], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return HappyEndingEnd()


class HappyEndingEnd(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return DungeonSuccess()

    def on_exit(self):
        set_achievement(triggerId=9902, type='trigger', achieve='MakeRainbowKingSlime')


#  던전 클리어 선언 
class DungeonSuccess(state.State):
    def on_enter(self):
        dungeon_clear()
        set_achievement(triggerId=9902, type='trigger', achieve='Find02100002')
        set_event_ui(type=7, arg2='$02100002_BF__01_MAINCONTROL__10$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ExitPortalOn()


class MissionFail(state.State):
    def on_enter(self):
        reset_timer(timerId='10000')
        set_event_ui(type=5, arg2='$02100002_BF__01_MAINCONTROL__9$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return DungeonFail()


#  던전 실패 선언 
class DungeonFail(state.State):
    def on_enter(self):
        dungeon_fail() # 아래층에서 위 층으로 올라갈 수 있는 일방 포탈
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ExitPortalOn()


class ExitPortalOn(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_user_value(triggerId=99, key='DungeonClear', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    pass


