""" trigger/82000002_survival/01_survival.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=False) # SafeZone Barrier Effect
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007], visible=True, arg3=0, delay=0, scale=0) # Barrier Center
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=True, arg3=0, delay=0, scale=0) # Barrier North
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207], visible=True, arg3=0, delay=0, scale=0) # Barrier South
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307], visible=True, arg3=0, delay=0, scale=0) # Barrier East
        self.set_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407], visible=True, arg3=0, delay=0, scale=0) # Barrier West
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507], visible=True, arg3=0, delay=0, scale=0) # Barrier SouthEast
        self.set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607], visible=True, arg3=0, delay=0, scale=0) # Barrier SouthWest
        self.set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707], visible=True, arg3=0, delay=0, scale=0) # Barrier NorthEast
        self.set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807], visible=True, arg3=0, delay=0, scale=0) # Barrier NorthWest
        self.set_sound(triggerId=20000, enable=False) # BGM Intro
        self.set_sound(triggerId=20001, enable=False) # BGM Loop
        self.set_local_camera(cameraId=100, enable=False)
        self.sight_range(enable=True, range=3, rangeZ=300, border=75)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return Wait_Talk01(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=True) # SafeZone Barrier Effect
        self.set_timer(timerId='1', seconds=59, startDelay=1, interval=1, vOffset=-80) # test용 수정 가능 지점 / arg2="30" / arg2 시간 더 짧게 가능  arg2="10"
        self.write_log(logName='Survival', event='Waiting_Start') # 서바이벌 대기 시작


class Wait_Talk01(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait_Talk02(self.ctx)
        if self.time_expired(timerId='1'):
            return ChangeBGM(self.ctx)


class Wait_Talk02(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait_Talk03(self.ctx)
        if self.time_expired(timerId='1'):
            return ChangeBGM(self.ctx)


class Wait_Talk03(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait_Talk01(self.ctx)
        if self.time_expired(timerId='1'):
            return ChangeBGM(self.ctx)


class ChangeBGM(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='BattleField_Event')
        self.set_sound(triggerId=20000, enable=True) # BGM Intro

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return StartGameExplain(self.ctx)


class StartGameExplain(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return GameExplain01(self.ctx)


class GameExplain01(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=6000, script='$82000002_survival__01_SURVIVAL__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return GameExplain02(self.ctx)


class GameExplain02(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=3000, script='$82000002_survival__01_SURVIVAL__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return GameExplain03(self.ctx)


class GameExplain03(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=3000, script='$82000002_survival__01_SURVIVAL__6$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return GameExplain04(self.ctx)


class GameExplain04(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return GameExplain05(self.ctx)


class GameExplain05(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__14$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return CheckPCLocation(self.ctx)


class CheckPCLocation(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return StartPoint01_North(self.ctx)
        if self.user_detected(boxIds=[9002]):
            return StartPoint02_South(self.ctx)
        if self.user_detected(boxIds=[9003]):
            return StartPoint03_East(self.ctx)
        if self.user_detected(boxIds=[9004]):
            return StartPoint04_West(self.ctx)
        if self.user_detected(boxIds=[9005]):
            return StartPoint05_NorthWest(self.ctx)
        if self.user_detected(boxIds=[9006]):
            return StartPoint06_NorthEast(self.ctx)
        if self.user_detected(boxIds=[9007]):
            return StartPoint07_SouthWest(self.ctx)
        if self.user_detected(boxIds=[9008]):
            return StartPoint08_SouthEast(self.ctx)


class StartPoint01_North(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PVPReady(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=1)


class StartPoint02_South(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PVPReady(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=2)


class StartPoint03_East(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PVPReady(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=3)


class StartPoint04_West(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PVPReady(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=4)


class StartPoint05_NorthWest(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PVPReady(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=5)


class StartPoint06_NorthEast(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PVPReady(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=6)


class StartPoint07_SouthWest(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PVPReady(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=7)


class StartPoint08_SouthEast(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PVPReady(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=8)


class PVPReady(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__8$') # 누가 우승할지 보자

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CheckTheNumberOfPlayers(self.ctx)


class CheckTheNumberOfPlayers(trigger_api.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, boxId=20, operator='GreaterEqual'):
            return MatchingSuccessDelay(self.ctx)
        if self.count_users(boxId=9000, boxId=20, operator='Less'):
            return MatchingFailDelay(self.ctx)


class MatchingSuccessDelay(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='GuildBattle_Enter')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return MatchingSuccess(self.ctx)


class MatchingSuccess(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__9$') # 충분히 모였군!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return RideRiseUp(self.ctx)


class RideRiseUp(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2, key='StartPatrol', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Countdown(self.ctx)


class Countdown(trigger_api.Trigger):
    def on_enter(self):
        self.create_field_game(type='MapleSurvivalTeam')
        self.show_count_ui(text='$82000002_survival__01_SURVIVAL__10$', stage=0, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return AreaOpen(self.ctx)


class AreaOpen(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477], isStart=True) # 나태 버섯 Normal Mob
        self.set_user_value(triggerId=5, key='RareBoxOnCount', value=1)
        self.set_user_value(triggerId=8, key='RareMobOnCount', value=1)
        self.set_user_value(triggerId=9, key='NormaBoxOnCount', value=1)
        self.set_user_value(triggerId=16, key='ExtraEventCheck', value=1)
        # <action name="SetUserValue" triggerID="16" key="ExtraEventTestOn" value="1" />	 test용 수정 가능 지점 : 이벤트 즉시 발동
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_user_value(triggerId=4, key='InvincibleOff', value=1)
        self.add_buff(boxIds=[9000], skillId=71000053, level=1, isPlayer=False, isSkillSet=False) # 31초 무적 버프
        self.set_effect(triggerIds=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=False) # SafeZone Barrier Effect
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007], visible=False, arg3=1000, delay=0, scale=1) # Barrier Center
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107], visible=False, arg3=1000, delay=0, scale=1) # Barrier_North
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207], visible=False, arg3=1000, delay=0, scale=1) # Barrier_South
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307], visible=False, arg3=1000, delay=0, scale=1) # Barrier_East
        self.set_mesh(triggerIds=[3400,3401,3402,3403,3404,3405,3406,3407], visible=False, arg3=1000, delay=0, scale=1) # Barrier_West
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507], visible=False, arg3=1000, delay=0, scale=1) # Barrier_SouthEast
        self.set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607], visible=False, arg3=1000, delay=0, scale=1) # Barrier_SouthWest
        self.set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707], visible=False, arg3=1000, delay=0, scale=1) # Barrier_NorthEast
        self.set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807], visible=False, arg3=1000, delay=0, scale=1) # Barrier_NorthWest
        self.set_sound(triggerId=20000, enable=False) # BGM Intro
        self.set_sound(triggerId=20001, enable=True) # BGM Loop
        self.write_log(logName='Survival', event='Start') # 서바이벌 시작 로그 남김

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return GameStart(self.ctx)


class GameStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=3, key='StormStart', value=1) # test용 수정 가능 지점 : 스톰 생성 안하려면 주석 처리
        self.write_log(logName='Survival', event='StormStart') # 서바이벌 스톰 시작 로그 남김

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9000]):
            return Quit(self.ctx)
        if not self.is_playing_maple_survival():
            return GameEnd(self.ctx)


# 인원 미만으로 인한 경기 취소
class MatchingFailDelay(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='guildBattle_MatchingFail')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return MatchingFail(self.ctx)


class MatchingFail(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__11$') # 인원 부족

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return GameCancel(self.ctx)


class GameCancel(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000002_survival__01_SURVIVAL__12$') # 경기 취소

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ReadyToKickOut(self.ctx)


class ReadyToKickOut(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$82000002_survival__01_SURVIVAL__13$', arg3='4000', arg4='0') # 잠시 후 원래 있던 곳으로 돌아갑니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class GameEnd(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9000], skillId=70001101, level=1, isPlayer=False, isSkillSet=False) # 변신 탈 것 해제용 버프
        self.sight_range(enable=False, range=3) # 우승자 카메라 (LocalTargetCamera 호출) 연출 시, 워포그 해제

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9000]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=5, key='RareBoxOff', value=1)
        self.set_user_value(triggerId=8, key='RareMobOff', value=1)
        self.set_user_value(triggerId=9, key='NormaBoxOff', value=1)
        self.set_user_value(triggerId=16, key='ExtraEventOff', value=1)
        self.destroy_monster(spawnIds=[-1])
        self.move_user(mapId=0, portalId=0)
        self.start_combine_spawn(groupId=[355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477], isStart=False) # 나태 버섯 Normal Mob


initial_state = Setting
