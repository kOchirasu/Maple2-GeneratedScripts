from typing import List


class Trigger:
    def __init__(self, ctx: ...):
        self.ctx = ctx

    def on_enter(self) -> 'Trigger':
        """Invoked after transitioning to this state."""
        pass

    def on_tick(self) -> 'Trigger':
        """Periodically invoked while in this state."""
        pass

    def on_exit(self) -> None:
        """Invoked before transitioning to another state."""
        pass

    """ Actions """
    def add_balloon_talk(self, spawnId: int=0, msg: str=None, duration: int=0, delayTick: int=0, npcID: int=0):
        """AddBalloonTalk

        Args:
            spawnId (int): _description_. Defaults to 0.
            msg (str): _description_. Defaults to None.
            duration (int): _description_. Defaults to 0.
            delayTick (int): _description_. Defaults to 0.
            npcID (int): _description_. Defaults to 0.
        """
        pass

    def add_buff(self, boxIds: List[int]=[], skillId: int=0, level: int=0, isPlayer: bool=True, isSkillSet: bool=True, feature: str=None):
        """버프를걸어준다

        Args:
            boxIds (List[int]): _description_. Defaults to [].
            skillId (int): _description_. Defaults to 0.
            level (int): _description_. Defaults to 0.
            isPlayer (bool): _description_. Defaults to True.
            isSkillSet (bool): _description_. Defaults to True.
            feature (str): _description_. Defaults to None.
        """
        pass

    def add_cinematic_talk(self, npcId: int=0, illustId: str=None, msg: str=None, duration: int=0, align: str=None, delayTick: int=0, illust: str=None):
        """AddCinematicTalk

        Args:
            npcId (int): _description_. Defaults to 0.
            illustId (str): _description_. Defaults to None.
            msg (str): _description_. Defaults to None.
            duration (int): _description_. Defaults to 0.
            align (str): _description_. Defaults to None.
            delayTick (int): _description_. Defaults to 0.
            illust (str): _description_. Defaults to None.
        """
        pass

    def add_effect_nif(self, spawnId: int=0, nifPath: str=None, isOutline: bool=False, scale: float=0.0, rotateZ: int=0):
        """AddEffectNif

        Args:
            spawnId (int): _description_. Defaults to 0.
            nifPath (str): _description_. Defaults to None.
            isOutline (bool): _description_. Defaults to False.
            scale (float): _description_. Defaults to 0.0.
            rotateZ (int): _description_. Defaults to 0.
        """
        pass

    def add_user_value(self, key: str=None, value: int=0):
        """AddUserValue

        Args:
            key (str): _description_. Defaults to None.
            value (int): _description_. Defaults to 0.
        """
        pass

    def arcade_boom_boom_ocean(self, type: str=None, lifeCount: int=0, id: int=0, score: int=0, round: int=0, roundDuration: int=0, timeScoreRate: int=0):
        """ArcadeBoomBoomOcean

        Args:
            type (str): _description_. Defaults to None.
            lifeCount (int): _description_. Defaults to 0.
            id (int): _description_. Defaults to 0.
            score (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            roundDuration (int): _description_. Defaults to 0.
            timeScoreRate (int): _description_. Defaults to 0.
        """
        pass

    def arcade_spring_farm(self, type: str=None, lifeCount: int=0, id: int=0, score: int=0, spawnIds: List[int]=[], uiDuration: int=0, round: int=0, timeScoreType: str=None, timeScoreRate: str=None, roundDuration: str=None):
        """ArcadeSpringFarm

        Args:
            type (str): _description_. Defaults to None.
            lifeCount (int): _description_. Defaults to 0.
            id (int): _description_. Defaults to 0.
            score (int): _description_. Defaults to 0.
            spawnIds (List[int]): _description_. Defaults to [].
            uiDuration (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            timeScoreType (str): _description_. Defaults to None.
            timeScoreRate (str): _description_. Defaults to None.
            roundDuration (str): _description_. Defaults to None.
        """
        pass

    def arcade_three_two_one(self, type: str=None, lifeCount: int=0, initScore: int=0, uiDuration: int=0, round: int=0, resultDirection: int=0):
        """ArcadeThreeTwoOne

        Args:
            type (str): _description_. Defaults to None.
            lifeCount (int): _description_. Defaults to 0.
            initScore (int): _description_. Defaults to 0.
            uiDuration (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            resultDirection (int): _description_. Defaults to 0.
        """
        pass

    def arcade_three_two_one2(self, type: str=None, lifeCount: int=0, initScore: int=0, uiDuration: int=0, round: int=0, resultDirection: int=0):
        """ArcadeThreeTwoOne2

        Args:
            type (str): _description_. Defaults to None.
            lifeCount (int): _description_. Defaults to 0.
            initScore (int): _description_. Defaults to 0.
            uiDuration (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            resultDirection (int): _description_. Defaults to 0.
        """
        pass

    def arcade_three_two_one3(self, type: str=None, lifeCount: int=0, initScore: int=0, uiDuration: int=0, round: int=0, resultDirection: int=0):
        """ArcadeThreeTwoOne3

        Args:
            type (str): _description_. Defaults to None.
            lifeCount (int): _description_. Defaults to 0.
            initScore (int): _description_. Defaults to 0.
            uiDuration (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            resultDirection (int): _description_. Defaults to 0.
        """
        pass

    def change_background(self, dds: str=None):
        """ChangeBackground

        Args:
            dds (str): _description_. Defaults to None.
        """
        pass

    def change_monster(self, removeSpawnId: int=0, addSpawnId: int=0):
        """몬스터를변경한다

        Args:
            removeSpawnId (int): _description_. Defaults to 0.
            addSpawnId (int): _description_. Defaults to 0.
        """
        pass

    def close_cinematic(self):
        """CloseCinematic"""
        pass

    def create_field_game(self, type: str=None, reset: bool=False):
        """CreateFieldGame

        Args:
            type (str): _description_. Defaults to None.
            reset (bool): _description_. Defaults to False.
        """
        pass

    def create_item(self, spawnIds: List[int]=[], triggerId: int=0, itemId: int=0, arg5: int=0):
        """아이템을생성한다

        Args:
            spawnIds (List[int]): _description_. Defaults to [].
            triggerId (int): _description_. Defaults to 0.
            itemId (int): _description_. Defaults to 0.
            arg5 (int): _description_. Defaults to 0.
        """
        pass

    def create_monster(self, spawnIds: List[int]=[], animationEffect: bool=True, animationDelay: int=0):
        """몬스터를생성한다

        Args:
            spawnIds (List[int]): _description_. Defaults to [].
            animationEffect (bool): _description_. Defaults to True.
            animationDelay (int): _description_. Defaults to 0.
        """
        pass

    def create_widget(self, type: str=None):
        """CreateWidget

        Args:
            type (str): _description_. Defaults to None.
        """
        pass

    def dark_stream(self, type: str=None, round: int=0, uiDuration: int=0, damagePenalty: int=0, spawnIds: List[int]=[], score: int=0):
        """DarkStream

        Args:
            type (str): _description_. Defaults to None.
            round (int): _description_. Defaults to 0.
            uiDuration (int): _description_. Defaults to 0.
            damagePenalty (int): _description_. Defaults to 0.
            spawnIds (List[int]): _description_. Defaults to [].
            score (int): _description_. Defaults to 0.
        """
        pass

    def debug_string(self, value: str=None, feature: str=None, string: str=None):
        """DebugString

        Args:
            value (str): _description_. Defaults to None.
            feature (str): _description_. Defaults to None.
            string (str): _description_. Defaults to None.
        """
        pass

    def destroy_monster(self, spawnIds: List[int]=[], arg2: bool=True):
        """몬스터소멸시킨다

        Args:
            spawnIds (List[int]): _description_. Defaults to [].
            arg2 (bool): _description_. Defaults to True.
        """
        pass

    def dungeon_clear(self, uiType: str=None):
        """DungeonClear

        Args:
            uiType (str): _description_. Defaults to None.
        """
        pass

    def dungeon_clear_round(self, round: int=0):
        """DungeonClearRound

        Args:
            round (int): _description_. Defaults to 0.
        """
        pass

    def dungeon_close_timer(self):
        """DungeonCloseTimer"""
        pass

    def dungeon_disable_ranking(self):
        """DungeonDisableRanking"""
        pass

    def dungeon_enable_give_up(self, isEnable: str=None):
        """DungeonEnableGiveUp

        Args:
            isEnable (str): _description_. Defaults to None.
        """
        pass

    def dungeon_fail(self):
        """DungeonFail"""
        pass

    def dungeon_mission_complete(self, feature: str=None, missionId: int=0):
        """DungeonMissionComplete

        Args:
            feature (str): _description_. Defaults to None.
            missionId (int): _description_. Defaults to 0.
        """
        pass

    def dungeon_move_lap_time_to_now(self, id: int=0):
        """DungeonMoveLapTimeToNow

        Args:
            id (int): _description_. Defaults to 0.
        """
        pass

    def dungeon_reset_time(self, seconds: int=0):
        """DungeonResetTime

        Args:
            seconds (int): _description_. Defaults to 0.
        """
        pass

    def dungeon_set_end_time(self):
        """DungeonSetEndTime"""
        pass

    def dungeon_set_lap_time(self, id: int=0, lapTime: int=0):
        """DungeonSetLapTime

        Args:
            id (int): _description_. Defaults to 0.
            lapTime (int): _description_. Defaults to 0.
        """
        pass

    def dungeon_stop_timer(self):
        """DungeonStopTimer"""
        pass

    def dungeon_variable(self, varId: int=0, value: int=0):
        """DungeonVariable

        Args:
            varId (int): _description_. Defaults to 0.
            value (int): _description_. Defaults to 0.
        """
        pass

    def enable_local_camera(self, isEnable: bool=False):
        """EnableLocalCamera

        Args:
            isEnable (bool): _description_. Defaults to False.
        """
        pass

    def enable_spawn_point_pc(self, spawnId: int=0, isEnable: bool=False):
        """EnableSpawnPointPC

        Args:
            spawnId (int): _description_. Defaults to 0.
            isEnable (bool): _description_. Defaults to False.
        """
        pass

    def end_mini_game(self, winnerBoxId: int=0, gameName: str=None, isOnlyWinner: str=None):
        """EndMiniGame

        Args:
            winnerBoxId (int): _description_. Defaults to 0.
            gameName (str): _description_. Defaults to None.
            isOnlyWinner (str): _description_. Defaults to None.
        """
        pass

    def end_mini_game_round(self, winnerBoxId: int=0, expRate: float=0.0, meso: float=0.0, isOnlyWinner: bool=False, isGainLoserBonus: bool=False, gameName: str=None):
        """EndMiniGameRound

        Args:
            winnerBoxId (int): _description_. Defaults to 0.
            expRate (float): _description_. Defaults to 0.0.
            meso (float): _description_. Defaults to 0.0.
            isOnlyWinner (bool): _description_. Defaults to False.
            isGainLoserBonus (bool): _description_. Defaults to False.
            gameName (str): _description_. Defaults to None.
        """
        pass

    def face_emotion(self, spawnId: int=0, emotionName: str=None):
        """FaceEmotion

        Args:
            spawnId (int): _description_. Defaults to 0.
            emotionName (str): _description_. Defaults to None.
        """
        pass

    def field_game_constant(self, key: str=None, value: str=None, feature: str=None, locale: str=None):
        """FieldGameConstant

        Args:
            key (str): _description_. Defaults to None.
            value (str): _description_. Defaults to None.
            feature (str): _description_. Defaults to None.
            locale (str): _description_. Defaults to None.
        """
        pass

    def field_game_message(self, custom: int=0, type: str=None, script: str=None, duration: int=0):
        """FieldGameMessage

        Args:
            custom (int): _description_. Defaults to 0.
            type (str): _description_. Defaults to None.
            script (str): _description_. Defaults to None.
            duration (int): _description_. Defaults to 0.
        """
        pass

    def field_war_end(self, isClear: bool=False):
        """FieldWarEnd

        Args:
            isClear (bool): _description_. Defaults to False.
        """
        pass

    def give_exp(self, boxId: int=0, amount: int=0, arg3: str=None):
        """GiveExp

        Args:
            boxId (int): _description_. Defaults to 0.
            amount (int): _description_. Defaults to 0.
            arg3 (str): _description_. Defaults to None.
        """
        pass

    def give_guild_exp(self, boxId: int=0, type: int=0):
        """GiveGuildExp

        Args:
            boxId (int): _description_. Defaults to 0.
            type (int): _description_. Defaults to 0.
        """
        pass

    def give_reward_content(self, rewardId: int=0):
        """GiveRewardContent

        Args:
            rewardId (int): _description_. Defaults to 0.
        """
        pass

    def guide_event(self, eventId: int=0):
        """GuideEvent

        Args:
            eventId (int): _description_. Defaults to 0.
        """
        pass

    def guild_vs_game_end_game(self):
        """GuildVsGameEndGame"""
        pass

    def guild_vs_game_give_contribution(self, teamId: int=0, isWin: bool=False, desc: str=None):
        """GuildVsGameGiveContribution

        Args:
            teamId (int): _description_. Defaults to 0.
            isWin (bool): _description_. Defaults to False.
            desc (str): _description_. Defaults to None.
        """
        pass

    def guild_vs_game_give_reward(self, type: str=None, teamId: int=0, isWin: bool=False, desc: str=None):
        """GuildVsGameGiveReward

        Args:
            type (str): _description_. Defaults to None.
            teamId (int): _description_. Defaults to 0.
            isWin (bool): _description_. Defaults to False.
            desc (str): _description_. Defaults to None.
        """
        pass

    def guild_vs_game_log_result(self, desc: str=None):
        """GuildVsGameLogResult

        Args:
            desc (str): _description_. Defaults to None.
        """
        pass

    def guild_vs_game_log_won_by_default(self, teamId: int=0, desc: str=None):
        """GuildVsGameLogWonByDefault

        Args:
            teamId (int): _description_. Defaults to 0.
            desc (str): _description_. Defaults to None.
        """
        pass

    def guild_vs_game_result(self, desc: str=None):
        """GuildVsGameResult

        Args:
            desc (str): _description_. Defaults to None.
        """
        pass

    def guild_vs_game_score_by_user(self, boxId: int=0, score: int=0, desc: str=None):
        """GuildVsGameScoreByUser

        Args:
            boxId (int): _description_. Defaults to 0.
            score (int): _description_. Defaults to 0.
            desc (str): _description_. Defaults to None.
        """
        pass

    def hide_guide_summary(self, entityId: int=0, textId: int=0):
        """HideGuideSummary

        Args:
            entityId (int): _description_. Defaults to 0.
            textId (int): _description_. Defaults to 0.
        """
        pass

    def init_npc_rotation(self, spawnIds: List[int]=[]):
        """InitNpcRotation

        Args:
            spawnIds (List[int]): _description_. Defaults to [].
        """
        pass

    def kick_music_audience(self, boxId: int=0, portalId: int=0):
        """KickMusicAudience

        Args:
            boxId (int): _description_. Defaults to 0.
            portalId (int): _description_. Defaults to 0.
        """
        pass

    def limit_spawn_npc_count(self, limitCount: int=0, desc: str=None):
        """LimitSpawnNpcCount

        Args:
            limitCount (int): _description_. Defaults to 0.
            desc (str): _description_. Defaults to None.
        """
        pass

    def lock_my_pc(self, isLock: bool=False):
        """LockMyPC

        Args:
            isLock (bool): _description_. Defaults to False.
        """
        pass

    def mini_game_camera_direction(self, boxId: int=0, cameraId: int=0):
        """MiniGameCameraDirection

        Args:
            boxId (int): _description_. Defaults to 0.
            cameraId (int): _description_. Defaults to 0.
        """
        pass

    def mini_game_give_exp(self, boxId: int=0, expRate: float=1.0, isOutside: bool=False):
        """MiniGameGiveExp

        Args:
            boxId (int): _description_. Defaults to 0.
            expRate (float): _description_. Defaults to 1.0.
            isOutside (bool): _description_. Defaults to False.
        """
        pass

    def mini_game_give_reward(self, winnerBoxId: int=0, contentType: str=None, gameName: str=None):
        """MiniGameGiveReward

        Args:
            winnerBoxId (int): _description_. Defaults to 0.
            contentType (str): _description_. Defaults to None.
            gameName (str): _description_. Defaults to None.
        """
        pass

    def move_npc(self, spawnId: int=0, patrolName: str=None):
        """NPC를이동시킨다

        Args:
            spawnId (int): _description_. Defaults to 0.
            patrolName (str): _description_. Defaults to None.
        """
        pass

    def move_npc_to_pos(self, spawnId: int=0, pos: List[float]=[0,0,0], rot: List[float]=[0,0,0]):
        """MoveNpcToPos

        Args:
            spawnId (int): _description_. Defaults to 0.
            pos (List[float]): _description_. Defaults to [0,0,0].
            rot (List[float]): _description_. Defaults to [0,0,0].
        """
        pass

    def move_random_user(self, mapId: int=0, portalId: int=0, triggerId: int=0, count: int=0):
        """무작위유저를이동시킨다

        Args:
            mapId (int): _description_. Defaults to 0.
            portalId (int): _description_. Defaults to 0.
            triggerId (int): _description_. Defaults to 0.
            count (int): _description_. Defaults to 0.
        """
        pass

    def move_to_portal(self, userTagId: int=0, portalId: int=0, boxId: int=0):
        """MoveToPortal

        Args:
            userTagId (int): _description_. Defaults to 0.
            portalId (int): _description_. Defaults to 0.
            boxId (int): _description_. Defaults to 0.
        """
        pass

    def move_user(self, mapId: int=0, portalId: int=0, boxId: int=0):
        """유저를이동시킨다

        Args:
            mapId (int): _description_. Defaults to 0.
            portalId (int): _description_. Defaults to 0.
            boxId (int): _description_. Defaults to 0.
        """
        pass

    def move_user_path(self, patrolName: str=None):
        """유저를경로이동시킨다

        Args:
            patrolName (str): _description_. Defaults to None.
        """
        pass

    def move_user_to_box(self, boxId: int=0, portalId: int=0):
        """MoveUserToBox

        Args:
            boxId (int): _description_. Defaults to 0.
            portalId (int): _description_. Defaults to 0.
        """
        pass

    def move_user_to_pos(self, pos: List[float]=[0,0,0], rot: List[float]=[0,0,0]):
        """MoveUserToPos

        Args:
            pos (List[float]): _description_. Defaults to [0,0,0].
            rot (List[float]): _description_. Defaults to [0,0,0].
        """
        pass

    def notice(self, arg1: bool=False, script: str=None, arg3: bool=False):
        """Notice

        Args:
            arg1 (bool): _description_. Defaults to False.
            script (str): _description_. Defaults to None.
            arg3 (bool): _description_. Defaults to False.
        """
        pass

    def npc_remove_additional_effect(self, spawnId: int=0, additionalEffectId: int=0):
        """NpcRemoveAdditionalEffect

        Args:
            spawnId (int): _description_. Defaults to 0.
            additionalEffectId (int): _description_. Defaults to 0.
        """
        pass

    def npc_to_patrol_in_box(self, boxId: int=0, npcId: int=0, spawnId: str=None, patrolName: str=None):
        """NpcToPatrolInBox

        Args:
            boxId (int): _description_. Defaults to 0.
            npcId (int): _description_. Defaults to 0.
            spawnId (str): _description_. Defaults to None.
            patrolName (str): _description_. Defaults to None.
        """
        pass

    def patrol_condition_user(self, patrolName: str=None, patrolIndex: int=0, additionalEffectId: int=0):
        """PatrolConditionUser

        Args:
            patrolName (str): _description_. Defaults to None.
            patrolIndex (int): _description_. Defaults to 0.
            additionalEffectId (int): _description_. Defaults to 0.
        """
        pass

    def play_scene_movie(self, fileName: str=None, movieId: int=0, skipType: str=None):
        """PlaySceneMovie

        Args:
            fileName (str): _description_. Defaults to None.
            movieId (int): _description_. Defaults to 0.
            skipType (str): _description_. Defaults to None.
        """
        pass

    def play_system_sound_by_user_tag(self, userTagId: int=0, soundKey: str=None):
        """PlaySystemSoundByUserTag

        Args:
            userTagId (int): _description_. Defaults to 0.
            soundKey (str): _description_. Defaults to None.
        """
        pass

    def play_system_sound_in_box(self, sound: str=None, boxIds: List[int]=[]):
        """PlaySystemSoundInBox

        Args:
            sound (str): _description_. Defaults to None.
            boxIds (List[int]): _description_. Defaults to [].
        """
        pass

    def random_additional_effect(self, target: str=None, boxId: int=0, spawnId: int=0, targetCount: int=0, tick: int=0, waitTick: int=0, targetEffect: str=None, additionalEffectId: int=0):
        """RandomAdditionalEffect

        Args:
            target (str): _description_. Defaults to None.
            boxId (int): _description_. Defaults to 0.
            spawnId (int): _description_. Defaults to 0.
            targetCount (int): _description_. Defaults to 0.
            tick (int): _description_. Defaults to 0.
            waitTick (int): _description_. Defaults to 0.
            targetEffect (str): _description_. Defaults to None.
            additionalEffectId (int): _description_. Defaults to 0.
        """
        pass

    def remove_balloon_talk(self, spawnId: int=0):
        """RemoveBalloonTalk

        Args:
            spawnId (int): _description_. Defaults to 0.
        """
        pass

    def remove_buff(self, boxId: int=0, skillId: int=0, isPlayer: bool=False):
        """버프를삭제한다

        Args:
            boxId (int): _description_. Defaults to 0.
            skillId (int): _description_. Defaults to 0.
            isPlayer (bool): _description_. Defaults to False.
        """
        pass

    def remove_cinematic_talk(self):
        """RemoveCinematicTalk"""
        pass

    def remove_effect_nif(self, spawnId: int=0):
        """RemoveEffectNif

        Args:
            spawnId (int): _description_. Defaults to 0.
        """
        pass

    def reset_camera(self, interpolationTime: float=0.0):
        """카메라리셋

        Args:
            interpolationTime (float): _description_. Defaults to 0.0.
        """
        pass

    def reset_timer(self, timerId: str=None):
        """타이머를초기화한다

        Args:
            timerId (str): _description_. Defaults to None.
        """
        pass

    def room_expire(self):
        """RoomExpire"""
        pass

    def score_board_create(self, type: str=None, title: str=None, maxScore: int=0):
        """ScoreBoardCreate

        Args:
            type (str): _description_. Defaults to None.
            title (str): _description_. Defaults to None.
            maxScore (int): _description_. Defaults to 0.
        """
        pass

    def score_board_remove(self):
        """ScoreBoardRemove"""
        pass

    def score_board_set_score(self, score: int=0):
        """ScoreBoardSetScore

        Args:
            score (int): _description_. Defaults to 0.
        """
        pass

    def select_camera(self, triggerId: int=0, enable: bool=True):
        """카메라를선택한다

        Args:
            triggerId (int): _description_. Defaults to 0.
            enable (bool): _description_. Defaults to True.
        """
        pass

    def select_camera_path(self, pathIds: List[int]=[], returnView: bool=True):
        """카메라경로를선택한다

        Args:
            pathIds (List[int]): _description_. Defaults to [].
            returnView (bool): _description_. Defaults to True.
        """
        pass

    def set_achievement(self, triggerId: int=0, type: str=None, achieve: str=None):
        """업적이벤트를발생시킨다

        Args:
            triggerId (int): _description_. Defaults to 0.
            type (str): _description_. Defaults to None.
            achieve (str): _description_. Defaults to None.
        """
        pass

    def set_actor(self, triggerId: int=0, visible: bool=False, initialSequence: str=None, arg4: bool=False, arg5: bool=False):
        """액터를설정한다

        Args:
            triggerId (int): _description_. Defaults to 0.
            visible (bool): _description_. Defaults to False.
            initialSequence (str): _description_. Defaults to None.
            arg4 (bool): _description_. Defaults to False.
            arg5 (bool): _description_. Defaults to False.
        """
        pass

    def set_agent(self, triggerIds: List[int]=[], visible: bool=False):
        """AGENT를설정한다

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
        """
        pass

    def set_ai_extra_data(self, key: str=None, value: int=0, isModify: bool=False, boxId: int=0):
        """SetAiExtraData

        Args:
            key (str): _description_. Defaults to None.
            value (int): _description_. Defaults to 0.
            isModify (bool): _description_. Defaults to False.
            boxId (int): _description_. Defaults to 0.
        """
        pass

    def set_ambient_light(self, primary: List[float]=[0,0,0], secondary: List[float]=[0,0,0], tertiary: List[float]=[0,0,0]):
        """SetAmbientLight

        Args:
            primary (List[float]): _description_. Defaults to [0,0,0].
            secondary (List[float]): _description_. Defaults to [0,0,0].
            tertiary (List[float]): _description_. Defaults to [0,0,0].
        """
        pass

    def set_breakable(self, triggerIds: List[int]=[], enable: bool=False):
        """움직이는발판을설정한다

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            enable (bool): _description_. Defaults to False.
        """
        pass

    def set_cinematic_intro(self, text: str=None):
        """SetCinematicIntro

        Args:
            text (str): _description_. Defaults to None.
        """
        pass

    def set_cinematic_ui(self, type: int=0, script: str=None, arg3: bool=False):
        """연출UI를설정한다

        Args:
            type (int): _description_. Defaults to 0.
            script (str): _description_. Defaults to None.
            arg3 (bool): _description_. Defaults to False.
        """
        pass

    def set_conversation(self, type: int=0, spawnId: int=0, script: str=None, arg4: int=0, arg5: int=0, align: str=None):
        """대화를설정한다

        Args:
            type (int): _description_. Defaults to 0.
            spawnId (int): _description_. Defaults to 0.
            script (str): _description_. Defaults to None.
            arg4 (int): _description_. Defaults to 0.
            arg5 (int): _description_. Defaults to 0.
            align (str): _description_. Defaults to None.
        """
        pass

    def set_cube(self, triggerIds: List[int]=[], isVisible: bool=False, randomCount: int=0):
        """SetCube

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            isVisible (bool): _description_. Defaults to False.
            randomCount (int): _description_. Defaults to 0.
        """
        pass

    def set_directional_light(self, diffuseColor: List[float]=[0,0,0], specularColor: List[float]=[0,0,0]):
        """SetDirectionalLight

        Args:
            diffuseColor (List[float]): _description_. Defaults to [0,0,0].
            specularColor (List[float]): _description_. Defaults to [0,0,0].
        """
        pass

    def set_effect(self, triggerIds: List[int]=[], visible: bool=False, arg3: int=0, arg4: int=0):
        """이펙트를설정한다

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
            arg3 (int): _description_. Defaults to 0.
            arg4 (int): _description_. Defaults to 0.
        """
        pass

    def set_event_ui(self, type: int=0, arg2: str=None, arg3: str=None, arg4: str=None):
        """이벤트UI를설정한다

        Args:
            type (int): _description_. Defaults to 0.
            arg2 (str): _description_. Defaults to None.
            arg3 (str): _description_. Defaults to None.
            arg4 (str): _description_. Defaults to None.
        """
        pass

    def set_gravity(self, gravity: float=0.0):
        """SetGravity

        Args:
            gravity (float): _description_. Defaults to 0.0.
        """
        pass

    def set_interact_object(self, triggerIds: List[int]=[], state: int=0, arg4: bool=False, arg3: bool=False):
        """오브젝트반응설정한다

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            state (int): _description_. Defaults to 0.
            arg4 (bool): _description_. Defaults to False.
            arg3 (bool): _description_. Defaults to False.
        """
        pass

    def set_ladder(self, triggerIds: List[int]=[], visible: bool=False, animationEffect: bool=False, animationDelay: int=0):
        """사다리를설정한다

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
            animationEffect (bool): _description_. Defaults to False.
            animationDelay (int): _description_. Defaults to 0.
        """
        pass

    def set_local_camera(self, cameraId: int=0, enable: bool=False):
        """SetLocalCamera

        Args:
            cameraId (int): _description_. Defaults to 0.
            enable (bool): _description_. Defaults to False.
        """
        pass

    def set_mesh(self, triggerIds: List[int]=[], visible: bool=False, arg3: int=0, delay: int=0, scale: float=0.0, desc: str=None):
        """메쉬를설정한다

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
            arg3 (int): _description_. Defaults to 0.
            delay (int): _description_. Defaults to 0.
            scale (float): _description_. Defaults to 0.0.
            desc (str): _description_. Defaults to None.
        """
        pass

    def set_mesh_animation(self, triggerIds: List[int]=[], visible: bool=False, arg3: int=0, arg4: int=0):
        """메쉬애니를설정한다

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
            arg3 (int): _description_. Defaults to 0.
            arg4 (int): _description_. Defaults to 0.
        """
        pass

    def set_mini_game_area_for_hack(self, boxId: int=0):
        """SetMiniGameAreaForHack

        Args:
            boxId (int): _description_. Defaults to 0.
        """
        pass

    def set_npc_duel_hp_bar(self, isOpen: bool=False, spawnId: List[int]=[], durationTick: int=0, npcHpStep: int=0):
        """SetNpcDuelHpBar

        Args:
            isOpen (bool): _description_. Defaults to False.
            spawnId (List[int]): _description_. Defaults to [].
            durationTick (int): _description_. Defaults to 0.
            npcHpStep (int): _description_. Defaults to 0.
        """
        pass

    def set_npc_emotion_loop(self, spawnId: int=0, sequenceName: str=None, duration: float=0.0, arg: str=None):
        """SetNpcEmotionLoop

        Args:
            spawnId (int): _description_. Defaults to 0.
            sequenceName (str): _description_. Defaults to None.
            duration (float): _description_. Defaults to 0.0.
            arg (str): _description_. Defaults to None.
        """
        pass

    def set_npc_emotion_sequence(self, spawnId: int=0, sequenceName: str=None, durationTick: int=0):
        """SetNpcEmotionSequence

        Args:
            spawnId (int): _description_. Defaults to 0.
            sequenceName (str): _description_. Defaults to None.
            durationTick (int): _description_. Defaults to 0.
        """
        pass

    def set_npc_rotation(self, spawnId: int=0, rotation: float=0.0):
        """SetNpcRotation

        Args:
            spawnId (int): _description_. Defaults to 0.
            rotation (float): _description_. Defaults to 0.0.
        """
        pass

    def set_onetime_effect(self, id: int=0, enable: bool=False, path: str=None):
        """SetOnetimeEffect

        Args:
            id (int): _description_. Defaults to 0.
            enable (bool): _description_. Defaults to False.
            path (str): _description_. Defaults to None.
        """
        pass

    def set_pc_emotion_loop(self, sequenceName: str=None, duration: float=0.0, arg3: bool=False):
        """SetPcEmotionLoop

        Args:
            sequenceName (str): _description_. Defaults to None.
            duration (float): _description_. Defaults to 0.0.
            arg3 (bool): _description_. Defaults to False.
        """
        pass

    def set_pc_emotion_sequence(self, sequenceNames: List[str]=[]):
        """SetPcEmotionSequence

        Args:
            sequenceNames (List[str]): _description_. Defaults to [].
        """
        pass

    def set_pc_rotation(self, rotation: List[float]=[0,0,0]):
        """SetPcRotation

        Args:
            rotation (List[float]): _description_. Defaults to [0,0,0].
        """
        pass

    def set_photo_studio(self, isEnable: bool=False):
        """SetPhotoStudio

        Args:
            isEnable (bool): _description_. Defaults to False.
        """
        pass

    def set_portal(self, portalId: int=0, visible: bool=False, enable: bool=False, minimapVisible: bool=False, arg5: bool=False):
        """포탈을설정한다

        Args:
            portalId (int): _description_. Defaults to 0.
            visible (bool): _description_. Defaults to False.
            enable (bool): _description_. Defaults to False.
            minimapVisible (bool): _description_. Defaults to False.
            arg5 (bool): _description_. Defaults to False.
        """
        pass

    def set_pvp_zone(self, boxId: int=0, arg2: int=0, duration: int=0, additionalEffectId: int=0, arg5: int=0, boxIds: List[int]=[]):
        """PVP존을설정한다

        Args:
            boxId (int): _description_. Defaults to 0.
            arg2 (int): _description_. Defaults to 0.
            duration (int): _description_. Defaults to 0.
            additionalEffectId (int): _description_. Defaults to 0.
            arg5 (int): _description_. Defaults to 0.
            boxIds (List[int]): _description_. Defaults to [].
        """
        pass

    def set_quest_accept(self, questId: int=0):
        """SetQuestAccept

        Args:
            questId (int): _description_. Defaults to 0.
        """
        pass

    def set_quest_complete(self, questId: int=0):
        """SetQuestComplete

        Args:
            questId (int): _description_. Defaults to 0.
        """
        pass

    def set_random_mesh(self, triggerIds: List[int]=[], visible: bool=False, meshCount: int=0, arg4: int=0, delay: int=0):
        """랜덤메쉬를설정한다

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
            meshCount (int): _description_. Defaults to 0.
            arg4 (int): _description_. Defaults to 0.
            delay (int): _description_. Defaults to 0.
        """
        pass

    def set_rope(self, triggerId: int=0, visible: bool=False, animationEffect: bool=False, animationDelay: int=0):
        """로프를설정한다

        Args:
            triggerId (int): _description_. Defaults to 0.
            visible (bool): _description_. Defaults to False.
            animationEffect (bool): _description_. Defaults to False.
            animationDelay (int): _description_. Defaults to 0.
        """
        pass

    def set_scene_skip(self, state: 'Trigger'=None, action: str=None):
        """SetSceneSkip

        Args:
            state ('Trigger'): _description_. Defaults to None.
            action (str): _description_. Defaults to None.
        """
        pass

    def set_skill(self, triggerIds: List[int]=[], enable: bool=False, isEnable: str=None):
        """스킬을설정한다

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            enable (bool): _description_. Defaults to False.
            isEnable (str): _description_. Defaults to None.
        """
        pass

    def set_skip(self, state: 'Trigger'=None):
        """스킵을설정한다

        Args:
            state ('Trigger'): _description_. Defaults to None.
        """
        pass

    def set_sound(self, triggerId: int=0, enable: bool=False):
        """사운드를설정한다

        Args:
            triggerId (int): _description_. Defaults to 0.
            enable (bool): _description_. Defaults to False.
        """
        pass

    def set_state(self, id: int=0, states: List[common.Trigger]=[], randomize: bool=False):
        """상태를설정한다

        Args:
            id (int): _description_. Defaults to 0.
            states (List[common.Trigger]): _description_. Defaults to [].
            randomize (bool): _description_. Defaults to False.
        """
        pass

    def set_time_scale(self, enable: bool=False, startScale: float=0.0, endScale: float=0.0, duration: float=0.0, interpolator: int=0):
        """SetTimeScale

        Args:
            enable (bool): _description_. Defaults to False.
            startScale (float): _description_. Defaults to 0.0.
            endScale (float): _description_. Defaults to 0.0.
            duration (float): _description_. Defaults to 0.0.
            interpolator (int): _description_. Defaults to 0.
        """
        pass

    def set_timer(self, timerId: str=None, seconds: int=0, startDelay: int=0, interval: int=0, vOffset: int=0, ara3: str=None, type: str=None, desc: str=None):
        """타이머를설정한다

        Args:
            timerId (str): _description_. Defaults to None.
            seconds (int): _description_. Defaults to 0.
            startDelay (int): _description_. Defaults to 0.
            interval (int): _description_. Defaults to 0.
            vOffset (int): _description_. Defaults to 0.
            ara3 (str): _description_. Defaults to None.
            type (str): _description_. Defaults to None.
            desc (str): _description_. Defaults to None.
        """
        pass

    def set_user_value(self, triggerId: int=0, key: str=None, value: int=0):
        """SetUserValue

        Args:
            triggerId (int): _description_. Defaults to 0.
            key (str): _description_. Defaults to None.
            value (int): _description_. Defaults to 0.
        """
        pass

    def set_user_value_from_dungeon_reward_count(self, key: str=None, dungeonRewardId: int=0):
        """SetUserValueFromDungeonRewardCount

        Args:
            key (str): _description_. Defaults to None.
            dungeonRewardId (int): _description_. Defaults to 0.
        """
        pass

    def set_user_value_from_guild_vs_game_score(self, teamId: int=0, key: str=None):
        """SetUserValueFromGuildVsGameScore

        Args:
            teamId (int): _description_. Defaults to 0.
            key (str): _description_. Defaults to None.
        """
        pass

    def set_user_value_from_user_count(self, triggerBoxId: int=0, key: str=None, userTagId: int=0):
        """SetUserValueFromUserCount

        Args:
            triggerBoxId (int): _description_. Defaults to 0.
            key (str): _description_. Defaults to None.
            userTagId (int): _description_. Defaults to 0.
        """
        pass

    def set_visible_breakable_object(self, triggerIds: List[int]=[], visible: bool=False):
        """SetVisibleBreakableObject

        Args:
            triggerIds (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
        """
        pass

    def set_visible_ui(self, uiNames: List[str]=[], visible: bool=False):
        """SetVisibleUI

        Args:
            uiNames (List[str]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
        """
        pass

    def shadow_expedition(self, type: str=None, maxGaugePoint: int=0, title: str=None):
        """ShadowExpedition

        Args:
            type (str): _description_. Defaults to None.
            maxGaugePoint (int): _description_. Defaults to 0.
            title (str): _description_. Defaults to None.
        """
        pass

    def show_caption(self, type: str=None, title: str=None, desc: str=None, align: str=None, offsetRateX: float=0.0, offsetRateY: float=0.0, duration: int=0, scale: float=0.0):
        """ShowCaption

        Args:
            type (str): _description_. Defaults to None.
            title (str): _description_. Defaults to None.
            desc (str): _description_. Defaults to None.
            align (str): _description_. Defaults to None.
            offsetRateX (float): _description_. Defaults to 0.0.
            offsetRateY (float): _description_. Defaults to 0.0.
            duration (int): _description_. Defaults to 0.
            scale (float): _description_. Defaults to 0.0.
        """
        pass

    def show_count_ui(self, text: str=None, stage: int=0, count: int=0, soundType: int=1):
        """ShowCountUI

        Args:
            text (str): _description_. Defaults to None.
            stage (int): _description_. Defaults to 0.
            count (int): _description_. Defaults to 0.
            soundType (int): _description_. Defaults to 1.
        """
        pass

    def show_event_result(self, type: str=None, text: str=None, duration: int=0, userTagId: int=0, triggerBoxId: int=0, isOutside: bool=False):
        """ShowEventResult

        Args:
            type (str): _description_. Defaults to None.
            text (str): _description_. Defaults to None.
            duration (int): _description_. Defaults to 0.
            userTagId (int): _description_. Defaults to 0.
            triggerBoxId (int): _description_. Defaults to 0.
            isOutside (bool): _description_. Defaults to False.
        """
        pass

    def show_guide_summary(self, entityId: int=0, textId: int=0, duration: int=0):
        """ShowGuideSummary

        Args:
            entityId (int): _description_. Defaults to 0.
            textId (int): _description_. Defaults to 0.
            duration (int): _description_. Defaults to 0.
        """
        pass

    def show_round_ui(self, round: int=0, duration: int=0, isFinalRound: bool=False):
        """ShowRoundUI

        Args:
            round (int): _description_. Defaults to 0.
            duration (int): _description_. Defaults to 0.
            isFinalRound (bool): _description_. Defaults to False.
        """
        pass

    def side_npc_talk(self, npcId: int=0, illust: str=None, duration: int=0, script: str=None, voice: str=None, type: str=None, usm: str=None):
        """SideNpcTalk

        Args:
            npcId (int): _description_. Defaults to 0.
            illust (str): _description_. Defaults to None.
            duration (int): _description_. Defaults to 0.
            script (str): _description_. Defaults to None.
            voice (str): _description_. Defaults to None.
            type (str): _description_. Defaults to None.
            usm (str): _description_. Defaults to None.
        """
        pass

    def sight_range(self, enable: bool=False, range: int=0, rangeZ: int=0, border: int=0):
        """SightRange

        Args:
            enable (bool): _description_. Defaults to False.
            range (int): _description_. Defaults to 0.
            rangeZ (int): _description_. Defaults to 0.
            border (int): _description_. Defaults to 0.
        """
        pass

    def spawn_item_range(self, rangeIds: List[int]=[], randomPickCount: int=0):
        """SpawnItemRange

        Args:
            rangeIds (List[int]): _description_. Defaults to [].
            randomPickCount (int): _description_. Defaults to 0.
        """
        pass

    def spawn_npc_range(self, rangeIds: List[int]=[], isAutoTargeting: bool=False, randomPickCount: int=0, score: int=0):
        """SpawnNpcRange

        Args:
            rangeIds (List[int]): _description_. Defaults to [].
            isAutoTargeting (bool): _description_. Defaults to False.
            randomPickCount (int): _description_. Defaults to 0.
            score (int): _description_. Defaults to 0.
        """
        pass

    def start_combine_spawn(self, groupId: List[int]=[], isStart: bool=False):
        """StartCombineSpawn

        Args:
            groupId (List[int]): _description_. Defaults to [].
            isStart (bool): _description_. Defaults to False.
        """
        pass

    def start_mini_game(self, boxId: int=0, round: int=0, gameName: str=None, isShowResultUI: bool=True):
        """StartMiniGame

        Args:
            boxId (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            gameName (str): _description_. Defaults to None.
            isShowResultUI (bool): _description_. Defaults to True.
        """
        pass

    def start_mini_game_round(self, boxId: int=0, round: int=0):
        """StartMiniGameRound

        Args:
            boxId (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
        """
        pass

    def start_tutorial(self):
        """startTutorial"""
        pass

    def talk_npc(self, spawnId: int=0):
        """TalkNpc

        Args:
            spawnId (int): _description_. Defaults to 0.
        """
        pass

    def unset_mini_game_area_for_hack(self):
        """UnSetMiniGameAreaForHack"""
        pass

    def use_state(self, arg1: int=0, arg2: bool=False):
        """상태를사용한다

        Args:
            arg1 (int): _description_. Defaults to 0.
            arg2 (bool): _description_. Defaults to False.
        """
        pass

    def user_tag_symbol(self, symbol1: str=None, symbol2: str=None):
        """UserTagSymbol

        Args:
            symbol1 (str): _description_. Defaults to None.
            symbol2 (str): _description_. Defaults to None.
        """
        pass

    def user_value_to_number_mesh(self, key: str=None, startMeshId: int=0, digitCount: int=0):
        """UserValueToNumberMesh

        Args:
            key (str): _description_. Defaults to None.
            startMeshId (int): _description_. Defaults to 0.
            digitCount (int): _description_. Defaults to 0.
        """
        pass

    def visible_my_pc(self, isVisible: bool=False):
        """VisibleMyPC

        Args:
            isVisible (bool): _description_. Defaults to False.
        """
        pass

    def weather(self, weatherType: str=None):
        """Weather

        Args:
            weatherType (str): _description_. Defaults to None.
        """
        pass

    def wedding_broken(self):
        """WeddingBroken"""
        pass

    def wedding_move_user(self, entryType: str=None, mapId: int=0, portalIds: List[int]=[], boxId: int=0):
        """WeddingMoveUser

        Args:
            entryType (str): _description_. Defaults to None.
            mapId (int): _description_. Defaults to 0.
            portalIds (List[int]): _description_. Defaults to [].
            boxId (int): _description_. Defaults to 0.
        """
        pass

    def wedding_mutual_agree(self, agreeType: str=None):
        """WeddingMutualAgree

        Args:
            agreeType (str): _description_. Defaults to None.
        """
        pass

    def wedding_mutual_cancel(self, agreeType: str=None):
        """WeddingMutualCancel

        Args:
            agreeType (str): _description_. Defaults to None.
        """
        pass

    def wedding_set_user_emotion(self, entryType: str=None, id: int=0):
        """WeddingSetUserEmotion

        Args:
            entryType (str): _description_. Defaults to None.
            id (int): _description_. Defaults to 0.
        """
        pass

    def wedding_set_user_look_at(self, entryType: str=None, lookAtEntryType: str=None, immediate: bool=False):
        """WeddingSetUserLookAt

        Args:
            entryType (str): _description_. Defaults to None.
            lookAtEntryType (str): _description_. Defaults to None.
            immediate (bool): _description_. Defaults to False.
        """
        pass

    def wedding_set_user_rotation(self, entryType: str=None, rotation: List[float]=[0,0,0], immediate: bool=False):
        """WeddingSetUserRotation

        Args:
            entryType (str): _description_. Defaults to None.
            rotation (List[float]): _description_. Defaults to [0,0,0].
            immediate (bool): _description_. Defaults to False.
        """
        pass

    def wedding_user_to_patrol(self, patrolName: str=None, entryType: str=None, patrolIndex: int=0):
        """WeddingUserToPatrol

        Args:
            patrolName (str): _description_. Defaults to None.
            entryType (str): _description_. Defaults to None.
            patrolIndex (int): _description_. Defaults to 0.
        """
        pass

    def wedding_vow_complete(self):
        """WeddingVowComplete"""
        pass

    def widget_action(self, type: str=None, func: str=None, widgetArg: str=None, desc: str=None, widgetArgNum: int=0):
        """WidgetAction

        Args:
            type (str): _description_. Defaults to None.
            func (str): _description_. Defaults to None.
            widgetArg (str): _description_. Defaults to None.
            desc (str): _description_. Defaults to None.
            widgetArgNum (int): _description_. Defaults to 0.
        """
        pass

    def write_log(self, logName: str=None, event: str=None, triggerId: int=0, subEvent: str=None, arg4: int=0):
        """로그를남긴다

        Args:
            logName (str): _description_. Defaults to None.
            event (str): _description_. Defaults to None.
            triggerId (int): _description_. Defaults to 0.
            subEvent (str): _description_. Defaults to None.
            arg4 (int): _description_. Defaults to 0.
        """
        pass

    def 공지를한다(self, arg1: str=None, arg2: str=None, arg3: str=None):
        """공지를한다

        Args:
            arg1 (str): _description_. Defaults to None.
            arg2 (str): _description_. Defaults to None.
            arg3 (str): _description_. Defaults to None.
        """
        pass

    def 전장점수를준다(self, arg1: str=None, arg2: str=None):
        """전장점수를준다

        Args:
            arg1 (str): _description_. Defaults to None.
            arg2 (str): _description_. Defaults to None.
        """
        pass


    """ Conditions """
    def bonus_game_reward_detected(self, boxId: int=0, arg2: bool=False) -> bool:
        """보너스게임보상받은유저를감지했으면

        Args:
            boxId (int): _description_. Defaults to 0.
            arg2 (bool): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
        return False

    def check_any_user_additional_effect(self, boxId: int=0, additionalEffectId: int=0, level: int=0) -> bool:
        """CheckAnyUserAdditionalEffect

        Args:
            boxId (int): _description_. Defaults to 0.
            additionalEffectId (int): _description_. Defaults to 0.
            level (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def check_dungeon_lobby_user_count(self) -> bool:
        """CheckDungeonLobbyUserCount

        Returns:
            bool: _description_
        """
        return False

    def check_npc_additional_effect(self, spawnId: int=0, additionalEffectId: int=0, level: int=0) -> bool:
        """CheckNpcAdditionalEffect

        Args:
            spawnId (int): _description_. Defaults to 0.
            additionalEffectId (int): _description_. Defaults to 0.
            level (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def check_npc_damage(self, spawnId: int=0, damageRate: float=0.0, operator: str='GreaterEqual') -> bool:
        """CheckNpcDamage

        Args:
            spawnId (int): _description_. Defaults to 0.
            damageRate (float): _description_. Defaults to 0.0.
            operator (str): _description_. Defaults to 'GreaterEqual'.

        Returns:
            bool: _description_
        """
        return False

    def check_npc_extra_data(self, spawnPointID: str=None, extraDataKey: str=None, extraDataValue: str=None, operator: str=None) -> bool:
        """CheckNpcExtraData

        Args:
            spawnPointID (str): _description_. Defaults to None.
            extraDataKey (str): _description_. Defaults to None.
            extraDataValue (str): _description_. Defaults to None.
            operator (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return False

    def check_npc_hp(self, compare: str=None, value: int=0, spawnId: int=0, isRelative: bool=False) -> bool:
        """CheckNpcHp

        Args:
            compare (str): _description_. Defaults to None.
            value (int): _description_. Defaults to 0.
            spawnId (int): _description_. Defaults to 0.
            isRelative (bool): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
        return False

    def check_same_user_tag(self, boxId: int=0) -> bool:
        """CheckSameUserTag

        Args:
            boxId (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def check_user(self) -> bool:
        """CheckUser

        Returns:
            bool: _description_
        """
        return False

    def check_user_count(self, checkCount: int=0) -> bool:
        """CheckUserCount

        Args:
            checkCount (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def count_users(self, boxId: int=0, minUsers: str=None, operator: str='GreaterEqual', userTagId: int=0) -> bool:
        """여러명의유저를감지했으면

        Args:
            boxId (int): _description_. Defaults to 0.
            minUsers (str): _description_. Defaults to None.
            operator (str): _description_. Defaults to 'GreaterEqual'.
            userTagId (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def day_of_week(self, dayOfWeeks: List[int]=[], desc: str=None) -> bool:
        """DayOfWeek

        Args:
            dayOfWeeks (List[int]): _description_. Defaults to [].
            desc (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return False

    def detect_liftable_object(self, boxIds: List[int]=[], itemId: int=0) -> bool:
        """DetectLiftableObject

        Args:
            boxIds (List[int]): _description_. Defaults to [].
            itemId (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def dungeon_check_play_time(self, playSeconds: int=0, operator: str='GreaterEqual') -> bool:
        """DungeonCheckPlayTime

        Args:
            playSeconds (int): _description_. Defaults to 0.
            operator (str): _description_. Defaults to 'GreaterEqual'.

        Returns:
            bool: _description_
        """
        return False

    def dungeon_check_state(self, checkState: str=None) -> bool:
        """DungeonCheckState

        Args:
            checkState (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return False

    def dungeon_first_user_mission_score(self, score: int=0, operator: str='GreaterEqual') -> bool:
        """DungeonFirstUserMissionScore

        Args:
            score (int): _description_. Defaults to 0.
            operator (str): _description_. Defaults to 'GreaterEqual'.

        Returns:
            bool: _description_
        """
        return False

    def dungeon_id(self, dungeonId: int=0) -> bool:
        """DungeonID

        Args:
            dungeonId (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def dungeon_level(self, level: int=0) -> bool:
        """DungeonLevel

        Args:
            level (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def dungeon_max_user_count(self, value: int=0) -> bool:
        """DungeonMaxUserCount

        Args:
            value (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def dungeon_round_require(self, round: int=0) -> bool:
        """DungeonRoundRequire

        Args:
            round (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def dungeon_time_out(self) -> bool:
        """DungeonTimeOut

        Returns:
            bool: _description_
        """
        return False

    def dungeon_variable(self, varId: int=0, value: int=0) -> bool:
        """DungeonVariable

        Args:
            varId (int): _description_. Defaults to 0.
            value (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def guild_vs_game_scored_team(self, teamId: int=0) -> bool:
        """GuildVsGameScoredTeam

        Args:
            teamId (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def guild_vs_game_winner_team(self, teamId: int=0) -> bool:
        """GuildVsGameWinnerTeam

        Args:
            teamId (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def is_dungeon_room(self) -> bool:
        """IsDungeonRoom

        Returns:
            bool: _description_
        """
        return False

    def is_playing_maple_survival(self) -> bool:
        """IsPlayingMapleSurvival

        Returns:
            bool: _description_
        """
        return False

    def monster_dead(self, boxIds: List[int]=[], arg2: bool=True) -> bool:
        """몬스터가죽어있으면

        Args:
            boxIds (List[int]): _description_. Defaults to [].
            arg2 (bool): _description_. Defaults to True.

        Returns:
            bool: _description_
        """
        return False

    def monster_in_combat(self, boxIds: List[int]=[]) -> bool:
        """몬스터가전투상태면

        Args:
            boxIds (List[int]): _description_. Defaults to [].

        Returns:
            bool: _description_
        """
        return False

    def npc_detected(self, boxId: int=0, spawnIds: List[int]=[]) -> bool:
        """NPC를감지했으면

        Args:
            boxId (int): _description_. Defaults to 0.
            spawnIds (List[int]): _description_. Defaults to [].

        Returns:
            bool: _description_
        """
        return False

    def npc_is_dead_by_string_id(self, stringID: str=None) -> bool:
        """NpcIsDeadByStringID

        Args:
            stringID (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return False

    def object_interacted(self, interactIds: List[int]=[], stateValue: int=0, ar2: str=None) -> bool:
        """오브젝트가반응했으면

        Args:
            interactIds (List[int]): _description_. Defaults to [].
            stateValue (int): _description_. Defaults to 0.
            ar2 (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return False

    def pvp_zone_ended(self, boxId: int=0) -> bool:
        """PVP존이종료했으면

        Args:
            boxId (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def quest_user_detected(self, boxIds: List[int]=[], questIds: List[int]=[], questStates: List[int]=[], jobCode: int=0) -> bool:
        """퀘스트유저를감지하면

        Args:
            boxIds (List[int]): _description_. Defaults to [].
            questIds (List[int]): _description_. Defaults to [].
            questStates (List[int]): _description_. Defaults to [].
            jobCode (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def random_condition(self, rate: float=0.0, desc: str=None) -> bool:
        """랜덤조건

        Args:
            rate (float): _description_. Defaults to 0.0.
            desc (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return False

    def score_board_compare(self, operator: str='GreaterEqual', score: int=0) -> bool:
        """ScoreBoardCompare

        Args:
            operator (str): _description_. Defaults to 'GreaterEqual'.
            score (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def shadow_expedition_reach_point(self, point: int=0) -> bool:
        """ShadowExpeditionReachPoint

        Args:
            point (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def time_expired(self, timerId: str=None) -> bool:
        """시간이경과했으면

        Args:
            timerId (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return False

    def true(self, arg1: bool=False) -> bool:
        """무조건

        Args:
            arg1 (bool): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
        return False

    def user_detected(self, boxIds: List[int]=[], jobCode: int=0) -> bool:
        """유저를감지했으면

        Args:
            boxIds (List[int]): _description_. Defaults to [].
            jobCode (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def user_value(self, key: str=None, value: int=0, operator: str='GreaterEqual') -> bool:
        """UserValue

        Args:
            key (str): _description_. Defaults to None.
            value (int): _description_. Defaults to 0.
            operator (str): _description_. Defaults to 'GreaterEqual'.

        Returns:
            bool: _description_
        """
        return False

    def wait_and_reset_tick(self, waitTick: int=0) -> bool:
        """WaitAndResetTick

        Args:
            waitTick (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def wait_seconds_user_value(self, key: str=None, desc: str=None) -> bool:
        """WaitSecondsUserValue

        Args:
            key (str): _description_. Defaults to None.
            desc (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return False

    def wait_tick(self, waitTick: int=0) -> bool:
        """WaitTick

        Args:
            waitTick (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return False

    def wedding_entry_in_field(self, entryType: str=None, isInField: bool=False) -> bool:
        """WeddingEntryInField

        Args:
            entryType (str): _description_. Defaults to None.
            isInField (bool): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
        return False

    def wedding_hall_state(self, hallState: str=None, success: bool=False) -> bool:
        """WeddingHallState

        Args:
            hallState (str): _description_. Defaults to None.
            success (bool): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
        return False

    def wedding_mutual_agree_result(self, agreeType: str=None, success: bool=False) -> bool:
        """WeddingMutualAgreeResult

        Args:
            agreeType (str): _description_. Defaults to None.
            success (bool): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
        return False

    def widget_condition(self, type: str=None, name: str=None, condition: str=None, desc: str=None) -> bool:
        """WidgetCondition

        Args:
            type (str): _description_. Defaults to None.
            name (str): _description_. Defaults to None.
            condition (str): _description_. Defaults to None.
            desc (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return False

