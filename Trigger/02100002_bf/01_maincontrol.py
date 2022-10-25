""" trigger/02100002_bf/01_maincontrol.xml """
import common

#include dungeon_common/checkuser10_guildraid.py
from dungeon_common.checkuser10_guildraid import *


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False) # RainbowSlime_Sound
        self.set_effect(triggerIds=[5002], visible=False) # PoopSlime_Sound
        self.limit_spawn_npc_count(limitCount=0, desc='몬스터 스폰 제한을 끕니다.') # 공장 가동하기 반응 오브젝트
        self.set_interact_object(triggerIds=[10001239], state=0) # 결과 출력하기 반응 오브젝트
        self.set_interact_object(triggerIds=[10001240], state=0) # 용광로 바닥 TOK always off
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419,3420,3421,3422,3423], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520,3521,3522,3523], visible=False, arg3=0, delay=0, scale=0) # 용광로 더미 몬스터 : 슬라임 죽이기
        self.destroy_monster(spawnIds=[900]) # 결과 몬스터
        self.destroy_monster(spawnIds=[1000,2000]) # 무지개 슬라임 공장 전용 위젯
        self.create_widget(type='RainbowMonster') # 입구 포탈
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 출구 포탈
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False) # 아래층에서 위 층으로 올라갈 수 있는 일방 포탈
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716,3717,3718,3719,3720,3721,3722,3723,3724,3725,3726,3727,3728,3729,3730,3731,3732,3733,3734,3735,3736,3737,3738,3739,3740,3741,3742,3743,3744,3745,3746,3747,3748,3749,3750,3751,3752,3753,3754,3755,3756,3757,3758,3759,3760,3761,3762,3763,3764,3765,3766,3767,3768,3769,3770,3771,3772,3773,3774,3775,3776,3777,3778,3779,3780,3781,3782,3783,3784,3785,3786,3787,3788,3789,3790,3791,3792,3793,3794,3795,3796,3797,3798,3799], visible=True, arg3=0, delay=0, scale=0) # 빨강 게이지 샘플
        self.set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816,3817,3818,3819], visible=True, arg3=0, delay=0, scale=0) # 용광로 더미 몬스터 : 슬라임 죽이기
        self.create_monster(spawnIds=[900], animationEffect=False) # 해당 필드에 몬스터의 수가  limitCount를 넘어가면 스폰을 중단한다.
        self.limit_spawn_npc_count(limitCount=200) # 정상 슬라임 몬스터 id 그룹 할당
        self.widget_action(type='RainbowMonster', func='CreateGroup', widgetArgNum=1, widgetArg='34000122,34000123,34000124,34000142')
        self.widget_action(type='RainbowMonster', func='CreateGroup', widgetArgNum=2, widgetArg='34000128,34000129,34000130,34000143')
        self.widget_action(type='RainbowMonster', func='CreateGroup', widgetArgNum=3, widgetArg='34000125,34000126,34000127,34000144')
        self.widget_action(type='RainbowMonster', func='CreateGroup', widgetArgNum=4, widgetArg='34000131,34000132,34000133,34000145')
        self.widget_action(type='RainbowMonster', func='CreateGroup', widgetArgNum=5, widgetArg='34000134,34000135,34000136,34000146') # 용광로 더미 몬스터에게 죽임을 당한 정상 슬라임만 점수로 체크
        self.widget_action(type='RainbowMonster', func='SetKillerNpc', widgetArg='34000141', desc='34000141 npc가 죽인 몬스터만 스코어에 반영') # 일정 시간 동안 용광로에 유입된 정상 슬라임이 없으면 게이지 감소 패널티
        self.widget_action(type='RainbowMonster', func='SetLoseScoreTick', widgetArgNum=60000, desc='60초마다 감점') # 용광로에 불량 슬라임이 들어가면 전체 게이지 랜덤 감소 패널티 / 34000138,34000139 두 종류 몬스터 미구현항목으로 제외 시킴(기획상 BigMom과 소환된 꼬마)
        self.widget_action(type='RainbowMonster', func='SetBadNpc', widgetArg='34000121,34000137', desc='해당 NPC가 킬러에게 죽으면 모든 게이지 감소')
        self.widget_action(type='RainbowMonster', func='SetBadNpcScore', widgetArg='2-5', desc='2~5칸 게이지가 떨어진다')
        self.widget_action(type='RainbowMonster', func='SetBadNpcSoundKey', widgetArg='GuildRaid_RainbowSlimeFactory_ScreenWarning_01', desc='게이지가 떨어질때 플레이할 사운드')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return MaxGaugePattern_Random(self.ctx)


# MaxGaugePatter_RandomPick
# 5개의 그룹에서 100, 120, 140, 160, 180, 200 값 중 중복 없이 5개  Pick : 조합
class MaxGaugePattern_Random(common.Trigger):
    def on_enter(self):
        self.widget_action(type='RainbowMonster', func='InitRandomMaxScore', widgetArg='120,120,140,140,160,160')
        # <action name="WidgetAction" arg1="RainbowMonster" arg2="ShowMaxScore" />
        self.widget_action(type='RainbowMonster', func='InitScoreMesh', widgetArgNum=1, widgetArg='3100')
        self.widget_action(type='RainbowMonster', func='InitScoreMesh', widgetArgNum=2, widgetArg='3200')
        self.widget_action(type='RainbowMonster', func='InitScoreMesh', widgetArgNum=3, widgetArg='3300')
        self.widget_action(type='RainbowMonster', func='InitScoreMesh', widgetArgNum=4, widgetArg='3500')
        self.widget_action(type='RainbowMonster', func='InitScoreMesh', widgetArgNum=5, widgetArg='3400')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CheckUser10_GuildRaid(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_cinematic_intro()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ShowCaption01(self.ctx)


# 설명문 출력
class ShowCaption01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__0$')
        self.set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return ShowCaption01Skip(self.ctx)


class ShowCaption01Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return ShowCaption02(self.ctx)


class ShowCaption02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__1$')
        self.set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return ShowCaption02Skip(self.ctx)


class ShowCaption02Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return ShowCaption03(self.ctx)


class ShowCaption03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=900, enable=True)
        self.set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__2$')
        self.set_skip(state=ShowCaption03Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return ShowCaption03Skip(self.ctx)


class ShowCaption03Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ShowCaption04(self.ctx)


class ShowCaption04(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=901, enable=True)
        self.set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__3$')
        self.set_skip(state=ShowCaption04Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return ShowCaption04Skip(self.ctx)


class ShowCaption04Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return ShowCaption05(self.ctx)


class ShowCaption05(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=902, enable=True)
        self.set_cinematic_intro(text='$02100002_BF__01_MAINCONTROL__4$')
        self.set_skip(state=ShowCaption05Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return ShowCaption05Skip(self.ctx)


class ShowCaption05Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.reset_camera(interpolationTime=1)
        self.set_user_value(triggerId=2, key='GuideNpcSpawn', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CloseCaptionSetting(self.ctx)


class CloseCaptionSetting(common.Trigger):
    def on_enter(self):
        self.close_cinematic() # 컬러 게이지 샘플
        self.set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716,3717,3718,3719,3720,3721,3722,3723,3724,3725,3726,3727,3728,3729,3730,3731,3732,3733,3734,3735,3736,3737,3738,3739,3740,3741,3742,3743,3744,3745,3746,3747,3748,3749,3750,3751,3752,3753,3754,3755,3756,3757,3758,3759,3760,3761,3762,3763,3764,3765,3766,3767,3768,3769,3770,3771,3772,3773,3774,3775,3776,3777,3778,3779,3780,3781,3782,3783,3784,3785,3786,3787,3788,3789,3790,3791,3792,3793,3794,3795,3796,3797,3798,3799], visible=False, arg3=0, delay=0, scale=0) # 빨강 게이지 샘플
        self.set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816,3817,3818,3819], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Guide01(self.ctx)


class Guide01(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99, key='PortalOn', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__5$', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Guide02(self.ctx)


class Guide02(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__6$', arg3='3000') # 공장 가동하기
        self.set_interact_object(triggerIds=[10001239], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001239], stateValue=0):
            return Guide03(self.ctx)


class Guide03(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='GuildRaid_RainbowSlimeFactory_MachineOn_01')
        self.set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__7$', arg3='2000')
        self.set_interact_object(triggerIds=[10001239], state=0) # 슬라임 생성 신호
        self.set_user_value(triggerId=11, key='ActivateTank', value=1)
        self.set_user_value(triggerId=12, key='ActivateTank', value=1)
        self.set_user_value(triggerId=13, key='ActivateTank', value=1)
        self.set_user_value(triggerId=14, key='ActivateTank', value=1)
        self.set_user_value(triggerId=15, key='ActivateTank', value=1) # 홀더 활성화 신호
        self.set_user_value(triggerId=21, key='ActivateHolder', value=1)
        self.set_user_value(triggerId=22, key='ActivateHolder', value=1)
        self.set_user_value(triggerId=23, key='ActivateHolder', value=1)
        self.set_user_value(triggerId=24, key='ActivateHolder', value=1)
        self.set_user_value(triggerId=25, key='ActivateHolder', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return TimmerStart(self.ctx)


class TimmerStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99, key='MissionStart', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01') # 제한 시간 10분
        self.set_timer(timerId='10000', seconds=600, startDelay=1, interval=1, vOffset=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=60000):
            return EnableCheckOutput(self.ctx)


class EnableCheckOutput(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02100002_BF__01_MAINCONTROL__8$', arg3='3000') # 결과 출력하기 반응 오브젝트
        self.set_interact_object(triggerIds=[10001240], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001240], stateValue=0):
            return CheckSuccess(self.ctx)
        if self.time_expired(timerId='10000'):
            return MissionFail(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=11, key='DungeonQuit', value=1)
        self.set_user_value(triggerId=12, key='DungeonQuit', value=1)
        self.set_user_value(triggerId=13, key='DungeonQuit', value=1)
        self.set_user_value(triggerId=14, key='DungeonQuit', value=1)
        self.set_user_value(triggerId=15, key='DungeonQuit', value=1)
        self.set_user_value(triggerId=21, key='DungeonQuit', value=1)
        self.set_user_value(triggerId=22, key='DungeonQuit', value=1)
        self.set_user_value(triggerId=23, key='DungeonQuit', value=1)
        self.set_user_value(triggerId=24, key='DungeonQuit', value=1)
        self.set_user_value(triggerId=25, key='DungeonQuit', value=1) # 용광로 소멸
        self.destroy_monster(spawnIds=[900]) # 입구 포탈
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10001234], state=0)


class CheckSuccess(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='RainbowMonster', name='IsMissionSuccess', condition='19-21'):
            return HappyEndingStart(self.ctx)
        if not self.widget_condition(type='RainbowMonster', name='IsMissionSuccess', condition='19-21'):
            return BadEndingStart(self.ctx)


# BadEnding 연출
class BadEndingStart(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=909, enable=True)
        self.play_system_sound_in_box(sound='GuildRaid_RainbowSlimeFactory_Result_01')
        self.move_user(mapId=2100002, portalId=2, boxId=9901) # 용광로 안에 있는 PC 안전한 곳으로 이동

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return BadEndingSpawn(self.ctx)


class BadEndingSpawn(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=908, enable=True)
        self.set_effect(triggerIds=[5002], visible=True) # PoopSlime_Sound
        self.create_monster(spawnIds=[2000], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return BadEndingEnd(self.ctx)


class BadEndingEnd(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return MissionFail(self.ctx)

    def on_exit(self):
        self.set_achievement(triggerId=9902, type='trigger', achieve='MakeMutantKingSlime')


# HappyEnding 연출
class HappyEndingStart(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=909, enable=True)
        self.play_system_sound_in_box(sound='GuildRaid_RainbowSlimeFactory_Result_01')
        self.move_user(mapId=2100002, portalId=2, boxId=9901) # 용광로 안에 있는 PC 안전한 곳으로 이동

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return HappyEndingSpawn(self.ctx)


class HappyEndingSpawn(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=908, enable=True)
        self.set_effect(triggerIds=[5001], visible=True) # RainbowSlime_Sound
        self.create_monster(spawnIds=[1000], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return HappyEndingEnd(self.ctx)


class HappyEndingEnd(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return DungeonSuccess(self.ctx)

    def on_exit(self):
        self.set_achievement(triggerId=9902, type='trigger', achieve='MakeRainbowKingSlime')


# 던전 클리어 선언
class DungeonSuccess(common.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.set_achievement(triggerId=9902, type='trigger', achieve='Find02100002')
        self.set_event_ui(type=7, arg2='$02100002_BF__01_MAINCONTROL__10$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ExitPortalOn(self.ctx)


class MissionFail(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='10000')
        self.set_event_ui(type=5, arg2='$02100002_BF__01_MAINCONTROL__9$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return DungeonFail(self.ctx)


# 던전 실패 선언
class DungeonFail(common.Trigger):
    def on_enter(self):
        self.dungeon_fail() # 아래층에서 위 층으로 올라갈 수 있는 일방 포탈
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ExitPortalOn(self.ctx)


class ExitPortalOn(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_user_value(triggerId=99, key='DungeonClear', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
