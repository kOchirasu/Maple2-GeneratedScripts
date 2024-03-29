""" trigger/82000012_survival/01_survival.xml """
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
        self.set_interact_object(triggerIds=[11000037], state=1) # Normal Box
        self.set_interact_object(triggerIds=[11000039], state=1) # Normal Box
        self.set_sound(triggerId=20000, enable=False) # BGM Intro
        self.set_sound(triggerId=20001, enable=False) # BGM Loop
        self.set_local_camera(cameraId=100, enable=False)
        self.sight_range(enable=True, range=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return Wait_Talk01(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[4000,4100,4200,4300,4400,4500,4600,4700,4800], visible=True) # SafeZone Barrier Effect


class Wait_Talk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=90, startDelay=1, interval=1, vOffset=-80) # test용 수정 가능 지점 arg2="60" / arg2="5"
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__0$')
        self.write_log(logName='Survival', event='Waiting_Start') # 서바이벌 대기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait_Talk02(self.ctx)
        if self.time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st(self.ctx)


class Wait_Talk02(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait_Talk03(self.ctx)
        if self.time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st(self.ctx)


class Wait_Talk03(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait_Talk04(self.ctx)
        if self.time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st(self.ctx)


class Wait_Talk04(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait_Talk05(self.ctx)
        if self.time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st(self.ctx)


class Wait_Talk05(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait_Talk06(self.ctx)
        if self.time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st(self.ctx)


class Wait_Talk06(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Wait_Talk01(self.ctx)
        if self.time_expired(timerId='1'):
            return CheckTheNumberOfPlayers_1st(self.ctx)


class CheckTheNumberOfPlayers_1st(trigger_api.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, boxId=25, operator='GreaterEqual'):
            return MatchingSuccessDelay(self.ctx)
        if self.count_users(boxId=9000, boxId=25, operator='Less'):
            return MatchingFailDelay(self.ctx)


class MatchingSuccessDelay(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7, key='HidePartyUI', value=1)
        self.play_system_sound_in_box(sound='GuildBattle_Enter')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return MatchingSuccess(self.ctx)


class MatchingSuccess(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__17$') # 충분히 모였군!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ReadyToMoveStartPosition(self.ctx)


class ReadyToMoveStartPosition(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=3000, script='$82000012_survival__01_SURVIVAL__11$') # 시작 지점으로 이동할까?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return StartPositionRandomPick(self.ctx)


class StartPositionRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=12.5):
            return PCRemap01_North(self.ctx)
        if self.random_condition(rate=12.5):
            return PCRemap02_South(self.ctx)
        if self.random_condition(rate=12.5):
            return PCRemap03_East(self.ctx)
        if self.random_condition(rate=12.5):
            return PCRemap04_West(self.ctx)
        if self.random_condition(rate=12.5):
            return PCRemap05_NorthWest(self.ctx)
        if self.random_condition(rate=12.5):
            return PCRemap06_NorthEast(self.ctx)
        if self.random_condition(rate=12.5):
            return PCRemap07_SouthWest(self.ctx)
        if self.random_condition(rate=12.5):
            return PCRemap08_SouthEast(self.ctx)


class PCRemap01_North(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='BattleField_Event')
        self.set_sound(triggerId=20000, enable=True) # BGM Intro
        self.move_user(mapId=82000012, portalId=101, boxId=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return StartGameExplain(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=1)


class PCRemap02_South(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='BattleField_Event')
        self.set_sound(triggerId=20000, enable=True) # BGM Intro
        self.move_user(mapId=82000012, portalId=102, boxId=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return StartGameExplain(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=2)


class PCRemap03_East(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='BattleField_Event')
        self.set_sound(triggerId=20000, enable=True) # BGM Intro
        self.move_user(mapId=82000012, portalId=103, boxId=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return StartGameExplain(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=3)


class PCRemap04_West(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='BattleField_Event')
        self.set_sound(triggerId=20000, enable=True) # BGM Intro
        self.move_user(mapId=82000012, portalId=104, boxId=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return StartGameExplain(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=4)


class PCRemap05_NorthWest(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='BattleField_Event')
        self.set_sound(triggerId=20000, enable=True) # BGM Intro
        self.move_user(mapId=82000012, portalId=105, boxId=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return StartGameExplain(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=5)


class PCRemap06_NorthEast(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='BattleField_Event')
        self.set_sound(triggerId=20000, enable=True) # BGM Intro
        self.move_user(mapId=82000012, portalId=106, boxId=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return StartGameExplain(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=6)


class PCRemap07_SouthWest(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='BattleField_Event')
        self.set_sound(triggerId=20000, enable=True) # BGM Intro
        self.move_user(mapId=82000012, portalId=107, boxId=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return StartGameExplain(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=7)


class PCRemap08_SouthEast(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='BattleField_Event')
        self.set_sound(triggerId=20000, enable=True) # BGM Intro
        self.move_user(mapId=82000012, portalId=108, boxId=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return StartGameExplain(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=2, key='SetRide', value=8)


class StartGameExplain(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=6000, script='$82000012_survival__01_SURVIVAL__6$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return GameExplain01(self.ctx)


class GameExplain01(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=6000, script='$82000012_survival__01_SURVIVAL__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return GameExplain02(self.ctx)


class GameExplain02(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=3500, script='$82000012_survival__01_SURVIVAL__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return GameExplain03(self.ctx)


class GameExplain03(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=3500, script='$82000012_survival__01_SURVIVAL__9$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return GameExplain04(self.ctx)


class GameExplain04(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=5000, script='$82000012_survival__01_SURVIVAL__10$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return GameExplain05(self.ctx)


class GameExplain05(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=5000, script='$82000012_survival__01_SURVIVAL__12$') # 버섯 열기구 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return PVPReady(self.ctx)


class PVPReady(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__13$') # 누가 우승할지 보자

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CheckTheNumberOfPlayers_2nd(self.ctx)


class CheckTheNumberOfPlayers_2nd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, boxId=20, operator='GreaterEqual'):
            return RideRiseUp(self.ctx)
        if self.count_users(boxId=9000, boxId=20, operator='Less'):
            return MatchingFailDelay(self.ctx)


class RideRiseUp(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2, key='StartPatrol', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Countdown(self.ctx)


class Countdown(trigger_api.Trigger):
    def on_enter(self):
        self.create_field_game(type='MapleSurvival')
        self.show_count_ui(text='$82000012_survival__01_SURVIVAL__14$', stage=0, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return AreaOpen(self.ctx)


class AreaOpen(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159], isStart=True) # 나태 버섯 Normal Mob
        self.set_user_value(triggerId=5, key='RareBoxOnCount', value=1)
        self.set_user_value(triggerId=8, key='RareMobOnCount', value=1)
        self.set_user_value(triggerId=9, key='NormaBoxOnCount', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_user_value(triggerId=4, key='InvincibleOff', value=1)
        self.add_buff(boxIds=[9000], skillId=71000053, level=1, isPlayer=False, isSkillSet=False) # 31초 무적
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
        self.set_user_value(triggerId=3, key='StormStart', value=1) # test용 수정 지점
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
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__15$') # 인원 부족

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return GameCancel(self.ctx)


class GameCancel(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23500110, illust='Mushking_normal', duration=4000, script='$82000012_survival__01_SURVIVAL__16$') # 경기 취소

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ReadyToKickOut(self.ctx)


class ReadyToKickOut(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$82000012_survival__01_SURVIVAL__18$', arg3='4000', arg4='0') # 잠시 후 원래 있던 곳으로 돌아갑니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class GameEnd(trigger_api.Trigger):
    def on_enter(self):
        self.sight_range(enable=False, range=3) # 우승자 카메라 (LocalTargetCamera 호출) 연출 시, 비석 상태인 유저의 위치 기준으로 우승자가 멀리 있어도 우승자가 보이도록 워포그 해제

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9000]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=5, key='RareBoxOff', value=1)
        self.set_user_value(triggerId=8, key='RareMobOff', value=1)
        self.set_user_value(triggerId=9, key='NormaBoxOff', value=1)
        self.set_interact_object(triggerIds=[11000037], state=0) # Normal Box
        self.set_interact_object(triggerIds=[11000039], state=0) # Normal Box
        self.destroy_monster(spawnIds=[-1])
        self.move_user(mapId=0, portalId=0)
        self.start_combine_spawn(groupId=[37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159], isStart=False) # 나태 버섯 Normal Mob


initial_state = Setting
