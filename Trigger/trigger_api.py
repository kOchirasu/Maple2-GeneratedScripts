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
    def add_balloon_talk(self, spawn_id: int=0, msg: str=None, duration: int=0, delay_tick: int=0, npc_id: int=0):
        """AddBalloonTalk

        Args:
            spawn_id (int): _description_. Defaults to 0.
            msg (str): _description_. Defaults to None.
            duration (int): _description_. Defaults to 0.
            delay_tick (int): _description_. Defaults to 0.
            npc_id (int): _description_. Defaults to 0.
        """
        self.ctx.AddBalloonTalk(spawn_id, msg, duration, delay_tick, npc_id)

    def add_buff(self, box_ids: List[int]=[], skill_id: int=0, level: int=0, is_player: bool=True, is_skill_set: bool=True, feature: str=None):
        """버프를걸어준다

        Args:
            box_ids (List[int]): _description_. Defaults to [].
            skill_id (int): _description_. Defaults to 0.
            level (int): _description_. Defaults to 0.
            is_player (bool): _description_. Defaults to True.
            is_skill_set (bool): _description_. Defaults to True.
            feature (str): _description_. Defaults to None.
        """
        self.ctx.AddBuff(box_ids, skill_id, level, is_player, is_skill_set, feature)

    def add_cinematic_talk(self, npc_id: int=0, illust_id: str=None, msg: str=None, duration: int=0, align: str=None, delay_tick: int=0, illust: str=None):
        """AddCinematicTalk

        Args:
            npc_id (int): _description_. Defaults to 0.
            illust_id (str): _description_. Defaults to None.
            msg (str): _description_. Defaults to None.
            duration (int): _description_. Defaults to 0.
            align (str): _description_. Defaults to None.
            delay_tick (int): _description_. Defaults to 0.
            illust (str): _description_. Defaults to None.
        """
        self.ctx.AddCinematicTalk(npc_id, illust_id, msg, duration, align, delay_tick, illust)

    def add_effect_nif(self, spawn_id: int=0, nif_path: str=None, is_outline: bool=False, scale: float=0.0, rotate_z: int=0):
        """AddEffectNif

        Args:
            spawn_id (int): _description_. Defaults to 0.
            nif_path (str): _description_. Defaults to None.
            is_outline (bool): _description_. Defaults to False.
            scale (float): _description_. Defaults to 0.0.
            rotate_z (int): _description_. Defaults to 0.
        """
        self.ctx.AddEffectNif(spawn_id, nif_path, is_outline, scale, rotate_z)

    def add_user_value(self, key: str=None, value: int=0):
        """AddUserValue

        Args:
            key (str): _description_. Defaults to None.
            value (int): _description_. Defaults to 0.
        """
        self.ctx.AddUserValue(key, value)

    def allocate_battlefield_points(self, box_id: int=0, points: int=0):
        """전장점수를준다

        Args:
            box_id (int): _description_. Defaults to 0.
            points (int): _description_. Defaults to 0.
        """
        self.ctx.AllocateBattlefieldPoints(box_id, points)

    def announce(self, type: int=0, content: str=None, arg3: bool=False):
        """공지를한다

        Args:
            type (int): _description_. Defaults to 0.
            content (str): _description_. Defaults to None.
            arg3 (bool): _description_. Defaults to False.
        """
        self.ctx.Announce(type, content, arg3)

    def arcade_boom_boom_ocean(self, type: str=None, life_count: int=0, id: int=0, score: int=0, round: int=0, round_duration: int=0, time_score_rate: int=0):
        """ArcadeBoomBoomOcean

        Args:
            type (str): _description_. Defaults to None.
            life_count (int): _description_. Defaults to 0.
            id (int): _description_. Defaults to 0.
            score (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            round_duration (int): _description_. Defaults to 0.
            time_score_rate (int): _description_. Defaults to 0.
        """
        self.ctx.ArcadeBoomBoomOcean(type, life_count, id, score, round, round_duration, time_score_rate)

    def arcade_spring_farm(self, type: str=None, life_count: int=0, id: int=0, score: int=0, spawn_ids: List[int]=[], ui_duration: int=0, round: int=0, time_score_type: str=None, time_score_rate: int=0, round_duration: int=0):
        """ArcadeSpringFarm

        Args:
            type (str): _description_. Defaults to None.
            life_count (int): _description_. Defaults to 0.
            id (int): _description_. Defaults to 0.
            score (int): _description_. Defaults to 0.
            spawn_ids (List[int]): _description_. Defaults to [].
            ui_duration (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            time_score_type (str): _description_. Defaults to None.
            time_score_rate (int): _description_. Defaults to 0.
            round_duration (int): _description_. Defaults to 0.
        """
        self.ctx.ArcadeSpringFarm(type, life_count, id, score, spawn_ids, ui_duration, round, time_score_type, time_score_rate, round_duration)

    def arcade_three_two_one(self, type: str=None, life_count: int=0, init_score: int=0, ui_duration: int=0, round: int=0, result_direction: int=0):
        """ArcadeThreeTwoOne

        Args:
            type (str): _description_. Defaults to None.
            life_count (int): _description_. Defaults to 0.
            init_score (int): _description_. Defaults to 0.
            ui_duration (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            result_direction (int): _description_. Defaults to 0.
        """
        self.ctx.ArcadeThreeTwoOne(type, life_count, init_score, ui_duration, round, result_direction)

    def arcade_three_two_one2(self, type: str=None, life_count: int=0, init_score: int=0, ui_duration: int=0, round: int=0, result_direction: int=0):
        """ArcadeThreeTwoOne2

        Args:
            type (str): _description_. Defaults to None.
            life_count (int): _description_. Defaults to 0.
            init_score (int): _description_. Defaults to 0.
            ui_duration (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            result_direction (int): _description_. Defaults to 0.
        """
        self.ctx.ArcadeThreeTwoOne2(type, life_count, init_score, ui_duration, round, result_direction)

    def arcade_three_two_one3(self, type: str=None, life_count: int=0, init_score: int=0, ui_duration: int=0, round: int=0, result_direction: int=0):
        """ArcadeThreeTwoOne3

        Args:
            type (str): _description_. Defaults to None.
            life_count (int): _description_. Defaults to 0.
            init_score (int): _description_. Defaults to 0.
            ui_duration (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            result_direction (int): _description_. Defaults to 0.
        """
        self.ctx.ArcadeThreeTwoOne3(type, life_count, init_score, ui_duration, round, result_direction)

    def change_background(self, dds: str=None):
        """ChangeBackground

        Args:
            dds (str): _description_. Defaults to None.
        """
        self.ctx.ChangeBackground(dds)

    def change_monster(self, from_spawn_id: int=0, to_spawn_id: int=0):
        """몬스터를변경한다

        Args:
            from_spawn_id (int): _description_. Defaults to 0.
            to_spawn_id (int): _description_. Defaults to 0.
        """
        self.ctx.ChangeMonster(from_spawn_id, to_spawn_id)

    def close_cinematic(self):
        """CloseCinematic"""
        self.ctx.CloseCinematic()

    def create_field_game(self, type: str=None, reset: bool=False):
        """CreateFieldGame

        Args:
            type (str): _description_. Defaults to None.
            reset (bool): _description_. Defaults to False.
        """
        self.ctx.CreateFieldGame(type, reset)

    def create_item(self, spawn_ids: List[int]=[], trigger_id: int=0, item_id: int=0, arg5: int=0):
        """아이템을생성한다

        Args:
            spawn_ids (List[int]): _description_. Defaults to [].
            trigger_id (int): _description_. Defaults to 0.
            item_id (int): _description_. Defaults to 0.
            arg5 (int): _description_. Defaults to 0.
        """
        self.ctx.CreateItem(spawn_ids, trigger_id, item_id, arg5)

    def create_widget(self, type: str=None):
        """CreateWidget

        Args:
            type (str): _description_. Defaults to None.
        """
        self.ctx.CreateWidget(type)

    def dark_stream(self, type: str=None, round: int=0, ui_duration: int=0, damage_penalty: int=0, spawn_ids: List[int]=[], score: int=0):
        """DarkStream

        Args:
            type (str): _description_. Defaults to None.
            round (int): _description_. Defaults to 0.
            ui_duration (int): _description_. Defaults to 0.
            damage_penalty (int): _description_. Defaults to 0.
            spawn_ids (List[int]): _description_. Defaults to [].
            score (int): _description_. Defaults to 0.
        """
        self.ctx.DarkStream(type, round, ui_duration, damage_penalty, spawn_ids, score)

    def debug_string(self, value: str=None, feature: str=None, string: str=None):
        """DebugString

        Args:
            value (str): _description_. Defaults to None.
            feature (str): _description_. Defaults to None.
            string (str): _description_. Defaults to None.
        """
        self.ctx.DebugString(value, feature, string)

    def destroy_monster(self, spawn_ids: List[int]=[], arg2: bool=True):
        """몬스터소멸시킨다

        Args:
            spawn_ids (List[int]): _description_. Defaults to [].
            arg2 (bool): _description_. Defaults to True.
        """
        self.ctx.DestroyMonster(spawn_ids, arg2)

    def dungeon_clear(self, ui_type: str=None):
        """DungeonClear

        Args:
            ui_type (str): _description_. Defaults to None.
        """
        self.ctx.DungeonClear(ui_type)

    def dungeon_clear_round(self, round: int=0):
        """DungeonClearRound

        Args:
            round (int): _description_. Defaults to 0.
        """
        self.ctx.DungeonClearRound(round)

    def dungeon_close_timer(self):
        """DungeonCloseTimer"""
        self.ctx.DungeonCloseTimer()

    def dungeon_disable_ranking(self):
        """DungeonDisableRanking"""
        self.ctx.DungeonDisableRanking()

    def dungeon_enable_give_up(self, is_enable: str=None):
        """DungeonEnableGiveUp

        Args:
            is_enable (str): _description_. Defaults to None.
        """
        self.ctx.DungeonEnableGiveUp(is_enable)

    def dungeon_fail(self):
        """DungeonFail"""
        self.ctx.DungeonFail()

    def dungeon_mission_complete(self, feature: str=None, mission_id: int=0):
        """DungeonMissionComplete

        Args:
            feature (str): _description_. Defaults to None.
            mission_id (int): _description_. Defaults to 0.
        """
        self.ctx.DungeonMissionComplete(feature, mission_id)

    def dungeon_move_lap_time_to_now(self, id: int=0):
        """DungeonMoveLapTimeToNow

        Args:
            id (int): _description_. Defaults to 0.
        """
        self.ctx.DungeonMoveLapTimeToNow(id)

    def dungeon_reset_time(self, seconds: int=0):
        """DungeonResetTime

        Args:
            seconds (int): _description_. Defaults to 0.
        """
        self.ctx.DungeonResetTime(seconds)

    def dungeon_set_end_time(self):
        """DungeonSetEndTime"""
        self.ctx.DungeonSetEndTime()

    def dungeon_set_lap_time(self, id: int=0, lap_time: int=0):
        """DungeonSetLapTime

        Args:
            id (int): _description_. Defaults to 0.
            lap_time (int): _description_. Defaults to 0.
        """
        self.ctx.DungeonSetLapTime(id, lap_time)

    def dungeon_stop_timer(self):
        """DungeonStopTimer"""
        self.ctx.DungeonStopTimer()

    def dungeon_variable(self, var_id: int=0, value: int=0):
        """DungeonVariable

        Args:
            var_id (int): _description_. Defaults to 0.
            value (int): _description_. Defaults to 0.
        """
        self.ctx.DungeonVariable(var_id, value)

    def enable_local_camera(self, is_enable: bool=False):
        """EnableLocalCamera

        Args:
            is_enable (bool): _description_. Defaults to False.
        """
        self.ctx.EnableLocalCamera(is_enable)

    def enable_spawn_point_pc(self, spawn_id: int=0, is_enable: bool=False):
        """EnableSpawnPointPC

        Args:
            spawn_id (int): _description_. Defaults to 0.
            is_enable (bool): _description_. Defaults to False.
        """
        self.ctx.EnableSpawnPointPc(spawn_id, is_enable)

    def end_mini_game(self, winner_box_id: int=0, game_name: str=None, is_only_winner: str=None):
        """EndMiniGame

        Args:
            winner_box_id (int): _description_. Defaults to 0.
            game_name (str): _description_. Defaults to None.
            is_only_winner (str): _description_. Defaults to None.
        """
        self.ctx.EndMiniGame(winner_box_id, game_name, is_only_winner)

    def end_mini_game_round(self, winner_box_id: int=0, exp_rate: float=0.0, meso: float=0.0, is_only_winner: bool=False, is_gain_loser_bonus: bool=False, game_name: str=None):
        """EndMiniGameRound

        Args:
            winner_box_id (int): _description_. Defaults to 0.
            exp_rate (float): _description_. Defaults to 0.0.
            meso (float): _description_. Defaults to 0.0.
            is_only_winner (bool): _description_. Defaults to False.
            is_gain_loser_bonus (bool): _description_. Defaults to False.
            game_name (str): _description_. Defaults to None.
        """
        self.ctx.EndMiniGameRound(winner_box_id, exp_rate, meso, is_only_winner, is_gain_loser_bonus, game_name)

    def face_emotion(self, spawn_id: int=0, emotion_name: str=None):
        """FaceEmotion

        Args:
            spawn_id (int): _description_. Defaults to 0.
            emotion_name (str): _description_. Defaults to None.
        """
        self.ctx.FaceEmotion(spawn_id, emotion_name)

    def field_game_constant(self, key: str=None, value: str=None, feature: str=None, locale: str=None):
        """FieldGameConstant

        Args:
            key (str): _description_. Defaults to None.
            value (str): _description_. Defaults to None.
            feature (str): _description_. Defaults to None.
            locale (str): _description_. Defaults to None.
        """
        self.ctx.FieldGameConstant(key, value, feature, locale)

    def field_game_message(self, custom: int=0, type: str=None, script: str=None, duration: int=0):
        """FieldGameMessage

        Args:
            custom (int): _description_. Defaults to 0.
            type (str): _description_. Defaults to None.
            script (str): _description_. Defaults to None.
            duration (int): _description_. Defaults to 0.
        """
        self.ctx.FieldGameMessage(custom, type, arg1, script, duration)

    def field_war_end(self, is_clear: bool=False):
        """FieldWarEnd

        Args:
            is_clear (bool): _description_. Defaults to False.
        """
        self.ctx.FieldWarEnd(is_clear)

    def give_exp(self, box_id: int=0, rate: float=1.0, arg3: str=None):
        """GiveExp

        Args:
            box_id (int): _description_. Defaults to 0.
            rate (float): _description_. Defaults to 1.0.
            arg3 (str): _description_. Defaults to None.
        """
        self.ctx.GiveExp(box_id, rate, arg3)

    def give_guild_exp(self, box_id: int=0, type: int=0):
        """GiveGuildExp

        Args:
            box_id (int): _description_. Defaults to 0.
            type (int): _description_. Defaults to 0.
        """
        self.ctx.GiveGuildExp(box_id, type)

    def give_reward_content(self, reward_id: int=0):
        """GiveRewardContent

        Args:
            reward_id (int): _description_. Defaults to 0.
        """
        self.ctx.GiveRewardContent(reward_id)

    def guide_event(self, event_id: int=0):
        """GuideEvent

        Args:
            event_id (int): _description_. Defaults to 0.
        """
        self.ctx.GuideEvent(event_id)

    def guild_vs_game_end_game(self):
        """GuildVsGameEndGame"""
        self.ctx.GuildVsGameEndGame()

    def guild_vs_game_give_contribution(self, team_id: int=0, is_win: bool=False, desc: str=None):
        """GuildVsGameGiveContribution

        Args:
            team_id (int): _description_. Defaults to 0.
            is_win (bool): _description_. Defaults to False.
            desc (str): _description_. Defaults to None.
        """
        self.ctx.GuildVsGameGiveContribution(team_id, is_win, desc)

    def guild_vs_game_give_reward(self, type: str=None, team_id: int=0, is_win: bool=False, desc: str=None):
        """GuildVsGameGiveReward

        Args:
            type (str): _description_. Defaults to None.
            team_id (int): _description_. Defaults to 0.
            is_win (bool): _description_. Defaults to False.
            desc (str): _description_. Defaults to None.
        """
        self.ctx.GuildVsGameGiveReward(type, team_id, is_win, desc)

    def guild_vs_game_log_result(self, desc: str=None):
        """GuildVsGameLogResult

        Args:
            desc (str): _description_. Defaults to None.
        """
        self.ctx.GuildVsGameLogResult(desc)

    def guild_vs_game_log_won_by_default(self, team_id: int=0, desc: str=None):
        """GuildVsGameLogWonByDefault

        Args:
            team_id (int): _description_. Defaults to 0.
            desc (str): _description_. Defaults to None.
        """
        self.ctx.GuildVsGameLogWonByDefault(team_id, desc)

    def guild_vs_game_result(self, desc: str=None):
        """GuildVsGameResult

        Args:
            desc (str): _description_. Defaults to None.
        """
        self.ctx.GuildVsGameResult(desc)

    def guild_vs_game_score_by_user(self, box_id: int=0, score: int=0, desc: str=None):
        """GuildVsGameScoreByUser

        Args:
            box_id (int): _description_. Defaults to 0.
            score (int): _description_. Defaults to 0.
            desc (str): _description_. Defaults to None.
        """
        self.ctx.GuildVsGameScoreByUser(box_id, score, desc)

    def hide_guide_summary(self, entity_id: int=0, text_id: int=0):
        """HideGuideSummary

        Args:
            entity_id (int): _description_. Defaults to 0.
            text_id (int): _description_. Defaults to 0.
        """
        self.ctx.HideGuideSummary(entity_id, text_id)

    def init_npc_rotation(self, spawn_ids: List[int]=[]):
        """InitNpcRotation

        Args:
            spawn_ids (List[int]): _description_. Defaults to [].
        """
        self.ctx.InitNpcRotation(spawn_ids)

    def kick_music_audience(self, box_id: int=0, portal_id: int=0):
        """KickMusicAudience

        Args:
            box_id (int): _description_. Defaults to 0.
            portal_id (int): _description_. Defaults to 0.
        """
        self.ctx.KickMusicAudience(box_id, portal_id)

    def limit_spawn_npc_count(self, limit_count: int=0, desc: str=None):
        """LimitSpawnNpcCount

        Args:
            limit_count (int): _description_. Defaults to 0.
            desc (str): _description_. Defaults to None.
        """
        self.ctx.LimitSpawnNpcCount(limit_count, desc)

    def lock_my_pc(self, is_lock: bool=False):
        """LockMyPC

        Args:
            is_lock (bool): _description_. Defaults to False.
        """
        self.ctx.LockMyPc(is_lock)

    def mini_game_camera_direction(self, box_id: int=0, camera_id: int=0):
        """MiniGameCameraDirection

        Args:
            box_id (int): _description_. Defaults to 0.
            camera_id (int): _description_. Defaults to 0.
        """
        self.ctx.MiniGameCameraDirection(box_id, camera_id)

    def mini_game_give_exp(self, box_id: int=0, exp_rate: float=1.0, is_outside: bool=False):
        """MiniGameGiveExp

        Args:
            box_id (int): _description_. Defaults to 0.
            exp_rate (float): _description_. Defaults to 1.0.
            is_outside (bool): _description_. Defaults to False.
        """
        self.ctx.MiniGameGiveExp(box_id, exp_rate, is_outside)

    def mini_game_give_reward(self, winner_box_id: int=0, content_type: str=None, game_name: str=None):
        """MiniGameGiveReward

        Args:
            winner_box_id (int): _description_. Defaults to 0.
            content_type (str): _description_. Defaults to None.
            game_name (str): _description_. Defaults to None.
        """
        self.ctx.MiniGameGiveReward(winner_box_id, content_type, game_name)

    def move_npc(self, spawn_id: int=0, patrol_name: str=None):
        """NPC를이동시킨다

        Args:
            spawn_id (int): _description_. Defaults to 0.
            patrol_name (str): _description_. Defaults to None.
        """
        self.ctx.MoveNpc(spawn_id, patrol_name)

    def move_npc_to_pos(self, spawn_id: int=0, pos: List[float]=[0,0,0], rot: List[float]=[0,0,0]):
        """MoveNpcToPos

        Args:
            spawn_id (int): _description_. Defaults to 0.
            pos (List[float]): _description_. Defaults to [0,0,0].
            rot (List[float]): _description_. Defaults to [0,0,0].
        """
        self.ctx.MoveNpcToPos(spawn_id, pos, rot)

    def move_random_user(self, map_id: int=0, portal_id: int=0, box_id: int=0, count: int=0):
        """무작위유저를이동시킨다

        Args:
            map_id (int): _description_. Defaults to 0.
            portal_id (int): _description_. Defaults to 0.
            box_id (int): _description_. Defaults to 0.
            count (int): _description_. Defaults to 0.
        """
        self.ctx.MoveRandomUser(map_id, portal_id, box_id, count)

    def move_to_portal(self, user_tag_id: int=0, portal_id: int=0, box_id: int=0):
        """MoveToPortal

        Args:
            user_tag_id (int): _description_. Defaults to 0.
            portal_id (int): _description_. Defaults to 0.
            box_id (int): _description_. Defaults to 0.
        """
        self.ctx.MoveToPortal(user_tag_id, portal_id, box_id)

    def move_user(self, map_id: int=0, portal_id: int=0, box_id: int=0):
        """유저를이동시킨다

        Args:
            map_id (int): _description_. Defaults to 0.
            portal_id (int): _description_. Defaults to 0.
            box_id (int): _description_. Defaults to 0.
        """
        self.ctx.MoveUser(map_id, portal_id, box_id)

    def move_user_path(self, patrol_name: str=None):
        """유저를경로이동시킨다

        Args:
            patrol_name (str): _description_. Defaults to None.
        """
        self.ctx.MoveUserPath(patrol_name)

    def move_user_to_box(self, box_id: int=0, portal_id: int=0):
        """MoveUserToBox

        Args:
            box_id (int): _description_. Defaults to 0.
            portal_id (int): _description_. Defaults to 0.
        """
        self.ctx.MoveUserToBox(box_id, portal_id)

    def move_user_to_pos(self, pos: List[float]=[0,0,0], rot: List[float]=[0,0,0]):
        """MoveUserToPos

        Args:
            pos (List[float]): _description_. Defaults to [0,0,0].
            rot (List[float]): _description_. Defaults to [0,0,0].
        """
        self.ctx.MoveUserToPos(pos, rot)

    def notice(self, type: int=0, script: str=None, arg3: bool=False):
        """Notice

        Args:
            type (int): _description_. Defaults to 0.
            script (str): _description_. Defaults to None.
            arg3 (bool): _description_. Defaults to False.
        """
        self.ctx.Notice(type, script, arg3)

    def npc_remove_additional_effect(self, spawn_id: int=0, additional_effect_id: int=0):
        """NpcRemoveAdditionalEffect

        Args:
            spawn_id (int): _description_. Defaults to 0.
            additional_effect_id (int): _description_. Defaults to 0.
        """
        self.ctx.NpcRemoveAdditionalEffect(spawn_id, additional_effect_id)

    def npc_to_patrol_in_box(self, box_id: int=0, npc_id: int=0, spawn_id: str=None, patrol_name: str=None):
        """NpcToPatrolInBox

        Args:
            box_id (int): _description_. Defaults to 0.
            npc_id (int): _description_. Defaults to 0.
            spawn_id (str): _description_. Defaults to None.
            patrol_name (str): _description_. Defaults to None.
        """
        self.ctx.NpcToPatrolInBox(box_id, npc_id, spawn_id, patrol_name)

    def patrol_condition_user(self, patrol_name: str=None, patrol_index: int=0, additional_effect_id: int=0):
        """PatrolConditionUser

        Args:
            patrol_name (str): _description_. Defaults to None.
            patrol_index (int): _description_. Defaults to 0.
            additional_effect_id (int): _description_. Defaults to 0.
        """
        self.ctx.PatrolConditionUser(patrol_name, patrol_index, additional_effect_id)

    def play_scene_movie(self, file_name: str=None, movie_id: int=0, skip_type: str=None):
        """PlaySceneMovie

        Args:
            file_name (str): _description_. Defaults to None.
            movie_id (int): _description_. Defaults to 0.
            skip_type (str): _description_. Defaults to None.
        """
        self.ctx.PlaySceneMovie(file_name, movie_id, skip_type)

    def play_system_sound_by_user_tag(self, user_tag_id: int=0, sound_key: str=None):
        """PlaySystemSoundByUserTag

        Args:
            user_tag_id (int): _description_. Defaults to 0.
            sound_key (str): _description_. Defaults to None.
        """
        self.ctx.PlaySystemSoundByUserTag(user_tag_id, sound_key)

    def play_system_sound_in_box(self, sound: str=None, box_ids: List[int]=[]):
        """PlaySystemSoundInBox

        Args:
            sound (str): _description_. Defaults to None.
            box_ids (List[int]): _description_. Defaults to [].
        """
        self.ctx.PlaySystemSoundInBox(sound, box_ids)

    def random_additional_effect(self, target: str=None, box_id: int=0, spawn_id: int=0, target_count: int=0, tick: int=0, wait_tick: int=0, target_effect: str=None, additional_effect_id: int=0):
        """RandomAdditionalEffect

        Args:
            target (str): _description_. Defaults to None.
            box_id (int): _description_. Defaults to 0.
            spawn_id (int): _description_. Defaults to 0.
            target_count (int): _description_. Defaults to 0.
            tick (int): _description_. Defaults to 0.
            wait_tick (int): _description_. Defaults to 0.
            target_effect (str): _description_. Defaults to None.
            additional_effect_id (int): _description_. Defaults to 0.
        """
        self.ctx.RandomAdditionalEffect(target, box_id, spawn_id, target_count, tick, wait_tick, target_effect, additional_effect_id)

    def remove_balloon_talk(self, spawn_id: int=0):
        """RemoveBalloonTalk

        Args:
            spawn_id (int): _description_. Defaults to 0.
        """
        self.ctx.RemoveBalloonTalk(spawn_id)

    def remove_buff(self, box_id: int=0, skill_id: int=0, is_player: bool=False):
        """버프를삭제한다

        Args:
            box_id (int): _description_. Defaults to 0.
            skill_id (int): _description_. Defaults to 0.
            is_player (bool): _description_. Defaults to False.
        """
        self.ctx.RemoveBuff(box_id, skill_id, is_player)

    def remove_cinematic_talk(self):
        """RemoveCinematicTalk"""
        self.ctx.RemoveCinematicTalk()

    def remove_effect_nif(self, spawn_id: int=0):
        """RemoveEffectNif

        Args:
            spawn_id (int): _description_. Defaults to 0.
        """
        self.ctx.RemoveEffectNif(spawn_id)

    def reset_camera(self, interpolation_time: float=0.0):
        """카메라리셋

        Args:
            interpolation_time (float): _description_. Defaults to 0.0.
        """
        self.ctx.ResetCamera(interpolation_time, arg1)

    def reset_timer(self, timer_id: str=None):
        """타이머를초기화한다

        Args:
            timer_id (str): _description_. Defaults to None.
        """
        self.ctx.ResetTimer(timer_id)

    def room_expire(self):
        """RoomExpire"""
        self.ctx.RoomExpire()

    def score_board_create(self, type: str=None, title: str=None, max_score: int=0):
        """ScoreBoardCreate

        Args:
            type (str): _description_. Defaults to None.
            title (str): _description_. Defaults to None.
            max_score (int): _description_. Defaults to 0.
        """
        self.ctx.ScoreBoardCreate(type, title, max_score)

    def score_board_remove(self):
        """ScoreBoardRemove"""
        self.ctx.ScoreBoardRemove()

    def score_board_set_score(self, score: int=0):
        """ScoreBoardSetScore

        Args:
            score (int): _description_. Defaults to 0.
        """
        self.ctx.ScoreBoardSetScore(score)

    def select_camera(self, trigger_id: int=0, enable: bool=True):
        """카메라를선택한다

        Args:
            trigger_id (int): _description_. Defaults to 0.
            enable (bool): _description_. Defaults to True.
        """
        self.ctx.SelectCamera(trigger_id, enable)

    def select_camera_path(self, path_ids: List[int]=[], return_view: bool=True):
        """카메라경로를선택한다

        Args:
            path_ids (List[int]): _description_. Defaults to [].
            return_view (bool): _description_. Defaults to True.
        """
        self.ctx.SelectCameraPath(path_ids, return_view)

    def set_achievement(self, trigger_id: int=0, type: str=None, achieve: str=None):
        """업적이벤트를발생시킨다

        Args:
            trigger_id (int): _description_. Defaults to 0.
            type (str): _description_. Defaults to None.
            achieve (str): _description_. Defaults to None.
        """
        self.ctx.SetAchievement(trigger_id, type, achieve)

    def set_actor(self, trigger_id: int=0, visible: bool=False, initial_sequence: str=None, arg4: bool=False, arg5: bool=False):
        """액터를설정한다

        Args:
            trigger_id (int): _description_. Defaults to 0.
            visible (bool): _description_. Defaults to False.
            initial_sequence (str): _description_. Defaults to None.
            arg4 (bool): _description_. Defaults to False.
            arg5 (bool): _description_. Defaults to False.
        """
        self.ctx.SetActor(trigger_id, visible, initial_sequence, arg4, arg5)

    def set_agent(self, trigger_ids: List[int]=[], visible: bool=False):
        """AGENT를설정한다

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
        """
        self.ctx.SetAgent(trigger_ids, visible)

    def set_ai_extra_data(self, key: str=None, value: int=0, is_modify: bool=False, box_id: int=0):
        """SetAiExtraData

        Args:
            key (str): _description_. Defaults to None.
            value (int): _description_. Defaults to 0.
            is_modify (bool): _description_. Defaults to False.
            box_id (int): _description_. Defaults to 0.
        """
        self.ctx.SetAiExtraData(key, value, is_modify, box_id)

    def set_ambient_light(self, primary: List[float]=[0,0,0], secondary: List[float]=[0,0,0], tertiary: List[float]=[0,0,0]):
        """SetAmbientLight

        Args:
            primary (List[float]): _description_. Defaults to [0,0,0].
            secondary (List[float]): _description_. Defaults to [0,0,0].
            tertiary (List[float]): _description_. Defaults to [0,0,0].
        """
        self.ctx.SetAmbientLight(primary, secondary, tertiary)

    def set_breakable(self, trigger_ids: List[int]=[], enable: bool=False):
        """움직이는발판을설정한다

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            enable (bool): _description_. Defaults to False.
        """
        self.ctx.SetBreakable(trigger_ids, enable)

    def set_cinematic_intro(self, text: str=None):
        """SetCinematicIntro

        Args:
            text (str): _description_. Defaults to None.
        """
        self.ctx.SetCinematicIntro(text)

    def set_cinematic_ui(self, type: int=0, script: str=None, arg3: bool=False):
        """연출UI를설정한다

        Args:
            type (int): _description_. Defaults to 0.
            script (str): _description_. Defaults to None.
            arg3 (bool): _description_. Defaults to False.
        """
        self.ctx.SetCinematicUi(type, script, arg3)

    def set_cube(self, trigger_ids: List[int]=[], is_visible: bool=False, random_count: int=0):
        """SetCube

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            is_visible (bool): _description_. Defaults to False.
            random_count (int): _description_. Defaults to 0.
        """
        self.ctx.SetCube(trigger_ids, is_visible, random_count)

    def set_dialogue(self, type: int=0, spawn_id: int=0, script: str=None, time: int=0, arg5: int=0, align: str=None):
        """대화를설정한다

        Args:
            type (int): _description_. Defaults to 0.
            spawn_id (int): _description_. Defaults to 0.
            script (str): _description_. Defaults to None.
            time (int): _description_. Defaults to 0.
            arg5 (int): _description_. Defaults to 0.
            align (str): _description_. Defaults to None.
        """
        self.ctx.SetDialogue(type, spawn_id, script, time, arg5, align)

    def set_directional_light(self, diffuse_color: List[float]=[0,0,0], specular_color: List[float]=[0,0,0]):
        """SetDirectionalLight

        Args:
            diffuse_color (List[float]): _description_. Defaults to [0,0,0].
            specular_color (List[float]): _description_. Defaults to [0,0,0].
        """
        self.ctx.SetDirectionalLight(diffuse_color, specular_color)

    def set_effect(self, trigger_ids: List[int]=[], visible: bool=False, start_delay: int=0, interval: int=0):
        """이펙트를설정한다

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
            start_delay (int): _description_. Defaults to 0.
            interval (int): _description_. Defaults to 0.
        """
        self.ctx.SetEffect(trigger_ids, visible, start_delay, interval)

    def set_event_ui(self, type: int=0, arg2: str=None, arg3: str=None, arg4: str=None):
        """이벤트UI를설정한다

        Args:
            type (int): _description_. Defaults to 0.
            arg2 (str): _description_. Defaults to None.
            arg3 (str): _description_. Defaults to None.
            arg4 (str): _description_. Defaults to None.
        """
        self.ctx.SetEventUi(type, arg2, arg3, arg4)

    def set_gravity(self, gravity: float=0.0):
        """SetGravity

        Args:
            gravity (float): _description_. Defaults to 0.0.
        """
        self.ctx.SetGravity(gravity)

    def set_interact_object(self, trigger_ids: List[int]=[], state: int=0, arg4: bool=False, arg3: bool=False):
        """오브젝트반응설정한다

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            state (int): _description_. Defaults to 0.
            arg4 (bool): _description_. Defaults to False.
            arg3 (bool): _description_. Defaults to False.
        """
        self.ctx.SetInteractObject(trigger_ids, state, arg4, arg3)

    def set_ladder(self, trigger_ids: List[int]=[], visible: bool=False, enable: bool=False, fade: int=0):
        """사다리를설정한다

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
            enable (bool): _description_. Defaults to False.
            fade (int): _description_. Defaults to 0.
        """
        self.ctx.SetLadder(trigger_ids, visible, enable, fade)

    def set_local_camera(self, camera_id: int=0, enable: bool=False):
        """SetLocalCamera

        Args:
            camera_id (int): _description_. Defaults to 0.
            enable (bool): _description_. Defaults to False.
        """
        self.ctx.SetLocalCamera(camera_id, enable)

    def set_mesh(self, trigger_ids: List[int]=[], visible: bool=False, start_delay: int=0, interval: int=0, fade: float=0.0, desc: str=None):
        """메쉬를설정한다

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
            start_delay (int): _description_. Defaults to 0.
            interval (int): _description_. Defaults to 0.
            fade (float): _description_. Defaults to 0.0.
            desc (str): _description_. Defaults to None.
        """
        self.ctx.SetMesh(trigger_ids, visible, start_delay, interval, fade, desc)

    def set_mesh_animation(self, trigger_ids: List[int]=[], visible: bool=False, start_delay: int=0, interval: int=0):
        """메쉬애니를설정한다

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
            start_delay (int): _description_. Defaults to 0.
            interval (int): _description_. Defaults to 0.
        """
        self.ctx.SetMeshAnimation(trigger_ids, visible, start_delay, interval)

    def set_mini_game_area_for_hack(self, box_id: int=0):
        """SetMiniGameAreaForHack

        Args:
            box_id (int): _description_. Defaults to 0.
        """
        self.ctx.SetMiniGameAreaForHack(box_id)

    def set_npc_duel_hp_bar(self, is_open: bool=False, spawn_id: List[int]=[], duration_tick: int=0, npc_hp_step: int=0):
        """SetNpcDuelHpBar

        Args:
            is_open (bool): _description_. Defaults to False.
            spawn_id (List[int]): _description_. Defaults to [].
            duration_tick (int): _description_. Defaults to 0.
            npc_hp_step (int): _description_. Defaults to 0.
        """
        self.ctx.SetNpcDuelHpBar(is_open, spawn_id, duration_tick, npc_hp_step)

    def set_npc_emotion_loop(self, spawn_id: int=0, sequence_name: str=None, duration: float=0.0, arg: str=None):
        """SetNpcEmotionLoop

        Args:
            spawn_id (int): _description_. Defaults to 0.
            sequence_name (str): _description_. Defaults to None.
            duration (float): _description_. Defaults to 0.0.
            arg (str): _description_. Defaults to None.
        """
        self.ctx.SetNpcEmotionLoop(spawn_id, sequence_name, duration, arg)

    def set_npc_emotion_sequence(self, spawn_id: int=0, sequence_name: str=None, duration_tick: int=0):
        """SetNpcEmotionSequence

        Args:
            spawn_id (int): _description_. Defaults to 0.
            sequence_name (str): _description_. Defaults to None.
            duration_tick (int): _description_. Defaults to 0.
        """
        self.ctx.SetNpcEmotionSequence(spawn_id, sequence_name, duration_tick)

    def set_npc_rotation(self, spawn_id: int=0, rotation: float=0.0):
        """SetNpcRotation

        Args:
            spawn_id (int): _description_. Defaults to 0.
            rotation (float): _description_. Defaults to 0.0.
        """
        self.ctx.SetNpcRotation(spawn_id, rotation)

    def set_onetime_effect(self, id: int=0, enable: bool=False, path: str=None):
        """SetOnetimeEffect

        Args:
            id (int): _description_. Defaults to 0.
            enable (bool): _description_. Defaults to False.
            path (str): _description_. Defaults to None.
        """
        self.ctx.SetOnetimeEffect(id, enable, path)

    def set_pc_emotion_loop(self, sequence_name: str=None, duration: float=0.0, arg3: bool=False):
        """SetPcEmotionLoop

        Args:
            sequence_name (str): _description_. Defaults to None.
            duration (float): _description_. Defaults to 0.0.
            arg3 (bool): _description_. Defaults to False.
        """
        self.ctx.SetPcEmotionLoop(sequence_name, duration, arg3)

    def set_pc_emotion_sequence(self, sequence_names: List[str]=[]):
        """SetPcEmotionSequence

        Args:
            sequence_names (List[str]): _description_. Defaults to [].
        """
        self.ctx.SetPcEmotionSequence(sequence_names)

    def set_pc_rotation(self, rotation: List[float]=[0,0,0]):
        """SetPcRotation

        Args:
            rotation (List[float]): _description_. Defaults to [0,0,0].
        """
        self.ctx.SetPcRotation(rotation)

    def set_photo_studio(self, is_enable: bool=False):
        """SetPhotoStudio

        Args:
            is_enable (bool): _description_. Defaults to False.
        """
        self.ctx.SetPhotoStudio(is_enable)

    def set_portal(self, portal_id: int=0, visible: bool=False, enable: bool=False, minimap_visible: bool=False, arg5: bool=False):
        """포탈을설정한다

        Args:
            portal_id (int): _description_. Defaults to 0.
            visible (bool): _description_. Defaults to False.
            enable (bool): _description_. Defaults to False.
            minimap_visible (bool): _description_. Defaults to False.
            arg5 (bool): _description_. Defaults to False.
        """
        self.ctx.SetPortal(portal_id, visible, enable, minimap_visible, arg5)

    def set_pvp_zone(self, box_id: int=0, prepare_time: int=0, match_time: int=0, additional_effect_id: int=0, type: int=0, box_ids: List[int]=[]):
        """PVP존을설정한다

        Args:
            box_id (int): _description_. Defaults to 0.
            prepare_time (int): _description_. Defaults to 0.
            match_time (int): _description_. Defaults to 0.
            additional_effect_id (int): _description_. Defaults to 0.
            type (int): _description_. Defaults to 0.
            box_ids (List[int]): _description_. Defaults to [].
        """
        self.ctx.SetPvpZone(box_id, prepare_time, match_time, additional_effect_id, type, box_ids)

    def set_quest_accept(self, quest_id: int=0):
        """SetQuestAccept

        Args:
            quest_id (int): _description_. Defaults to 0.
        """
        self.ctx.SetQuestAccept(quest_id)

    def set_quest_complete(self, quest_id: int=0):
        """SetQuestComplete

        Args:
            quest_id (int): _description_. Defaults to 0.
        """
        self.ctx.SetQuestComplete(quest_id)

    def set_random_mesh(self, trigger_ids: List[int]=[], visible: bool=False, start_delay: int=0, interval: int=0, fade: int=0):
        """랜덤메쉬를설정한다

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
            start_delay (int): _description_. Defaults to 0.
            interval (int): _description_. Defaults to 0.
            fade (int): _description_. Defaults to 0.
        """
        self.ctx.SetRandomMesh(trigger_ids, visible, start_delay, interval, fade)

    def set_rope(self, trigger_id: int=0, visible: bool=False, enable: bool=False, fade: int=0):
        """로프를설정한다

        Args:
            trigger_id (int): _description_. Defaults to 0.
            visible (bool): _description_. Defaults to False.
            enable (bool): _description_. Defaults to False.
            fade (int): _description_. Defaults to 0.
        """
        self.ctx.SetRope(trigger_id, visible, enable, fade)

    def set_scene_skip(self, state: 'Trigger'=None, action: str=None):
        """SetSceneSkip

        Args:
            state ('Trigger'): _description_. Defaults to None.
            action (str): _description_. Defaults to None.
        """
        self.ctx.SetSceneSkip(state, action)

    def set_skill(self, trigger_ids: List[int]=[], enable: bool=False, is_enable: str=None):
        """스킬을설정한다

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            enable (bool): _description_. Defaults to False.
            is_enable (str): _description_. Defaults to None.
        """
        self.ctx.SetSkill(trigger_ids, enable, is_enable)

    def set_skip(self, state: 'Trigger'=None):
        """스킵을설정한다

        Args:
            state ('Trigger'): _description_. Defaults to None.
        """
        self.ctx.SetSkip(state)

    def set_sound(self, trigger_id: int=0, enable: bool=False):
        """사운드를설정한다

        Args:
            trigger_id (int): _description_. Defaults to 0.
            enable (bool): _description_. Defaults to False.
        """
        self.ctx.SetSound(trigger_id, enable)

    def set_state(self, id: int=0, states: List['Trigger']=[], randomize: bool=False):
        """상태를설정한다

        Args:
            id (int): _description_. Defaults to 0.
            states (List['Trigger']): _description_. Defaults to [].
            randomize (bool): _description_. Defaults to False.
        """
        self.ctx.SetState(id, states, randomize)

    def set_time_scale(self, enable: bool=False, start_scale: float=0.0, end_scale: float=0.0, duration: float=0.0, interpolator: int=0):
        """SetTimeScale

        Args:
            enable (bool): _description_. Defaults to False.
            start_scale (float): _description_. Defaults to 0.0.
            end_scale (float): _description_. Defaults to 0.0.
            duration (float): _description_. Defaults to 0.0.
            interpolator (int): _description_. Defaults to 0.
        """
        self.ctx.SetTimeScale(enable, start_scale, end_scale, duration, interpolator)

    def set_timer(self, timer_id: str=None, seconds: int=0, start_delay: int=0, interval: int=0, v_offset: int=0, ara3: str=None, type: str=None, desc: str=None):
        """타이머를설정한다

        Args:
            timer_id (str): _description_. Defaults to None.
            seconds (int): _description_. Defaults to 0.
            start_delay (int): _description_. Defaults to 0.
            interval (int): _description_. Defaults to 0.
            v_offset (int): _description_. Defaults to 0.
            ara3 (str): _description_. Defaults to None.
            type (str): _description_. Defaults to None.
            desc (str): _description_. Defaults to None.
        """
        self.ctx.SetTimer(timer_id, seconds, start_delay, interval, v_offset, ara3, type, desc)

    def set_user_value(self, trigger_id: int=0, key: str=None, value: int=0):
        """SetUserValue

        Args:
            trigger_id (int): _description_. Defaults to 0.
            key (str): _description_. Defaults to None.
            value (int): _description_. Defaults to 0.
        """
        self.ctx.SetUserValue(trigger_id, key, value)

    def set_user_value_from_dungeon_reward_count(self, key: str=None, dungeon_reward_id: int=0):
        """SetUserValueFromDungeonRewardCount

        Args:
            key (str): _description_. Defaults to None.
            dungeon_reward_id (int): _description_. Defaults to 0.
        """
        self.ctx.SetUserValueFromDungeonRewardCount(key, dungeon_reward_id)

    def set_user_value_from_guild_vs_game_score(self, team_id: int=0, key: str=None):
        """SetUserValueFromGuildVsGameScore

        Args:
            team_id (int): _description_. Defaults to 0.
            key (str): _description_. Defaults to None.
        """
        self.ctx.SetUserValueFromGuildVsGameScore(team_id, key)

    def set_user_value_from_user_count(self, trigger_box_id: int=0, key: str=None, user_tag_id: int=0):
        """SetUserValueFromUserCount

        Args:
            trigger_box_id (int): _description_. Defaults to 0.
            key (str): _description_. Defaults to None.
            user_tag_id (int): _description_. Defaults to 0.
        """
        self.ctx.SetUserValueFromUserCount(trigger_box_id, key, user_tag_id)

    def set_visible_breakable_object(self, trigger_ids: List[int]=[], visible: bool=False):
        """SetVisibleBreakableObject

        Args:
            trigger_ids (List[int]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
        """
        self.ctx.SetVisibleBreakableObject(trigger_ids, visible)

    def set_visible_ui(self, ui_names: List[str]=[], visible: bool=False):
        """SetVisibleUI

        Args:
            ui_names (List[str]): _description_. Defaults to [].
            visible (bool): _description_. Defaults to False.
        """
        self.ctx.SetVisibleUi(ui_names, visible)

    def shadow_expedition(self, type: str=None, max_gauge_point: int=0, title: str=None):
        """ShadowExpedition

        Args:
            type (str): _description_. Defaults to None.
            max_gauge_point (int): _description_. Defaults to 0.
            title (str): _description_. Defaults to None.
        """
        self.ctx.ShadowExpedition(type, max_gauge_point, title)

    def show_caption(self, type: str=None, title: str=None, desc: str=None, align: str=None, offset_rate_x: float=0.0, offset_rate_y: float=0.0, duration: int=0, scale: float=0.0):
        """ShowCaption

        Args:
            type (str): _description_. Defaults to None.
            title (str): _description_. Defaults to None.
            desc (str): _description_. Defaults to None.
            align (str): _description_. Defaults to None.
            offset_rate_x (float): _description_. Defaults to 0.0.
            offset_rate_y (float): _description_. Defaults to 0.0.
            duration (int): _description_. Defaults to 0.
            scale (float): _description_. Defaults to 0.0.
        """
        self.ctx.ShowCaption(type, title, desc, align, offset_rate_x, offset_rate_y, duration, scale)

    def show_count_ui(self, text: str=None, stage: int=0, count: int=0, sound_type: int=1):
        """ShowCountUI

        Args:
            text (str): _description_. Defaults to None.
            stage (int): _description_. Defaults to 0.
            count (int): _description_. Defaults to 0.
            sound_type (int): _description_. Defaults to 1.
        """
        self.ctx.ShowCountUi(text, stage, count, sound_type)

    def show_event_result(self, type: str=None, text: str=None, duration: int=0, user_tag_id: int=0, trigger_box_id: int=0, is_outside: bool=False):
        """ShowEventResult

        Args:
            type (str): _description_. Defaults to None.
            text (str): _description_. Defaults to None.
            duration (int): _description_. Defaults to 0.
            user_tag_id (int): _description_. Defaults to 0.
            trigger_box_id (int): _description_. Defaults to 0.
            is_outside (bool): _description_. Defaults to False.
        """
        self.ctx.ShowEventResult(type, text, duration, user_tag_id, trigger_box_id, is_outside)

    def show_guide_summary(self, entity_id: int=0, text_id: int=0, duration: int=0):
        """ShowGuideSummary

        Args:
            entity_id (int): _description_. Defaults to 0.
            text_id (int): _description_. Defaults to 0.
            duration (int): _description_. Defaults to 0.
        """
        self.ctx.ShowGuideSummary(entity_id, text_id, duration)

    def show_round_ui(self, round: int=0, duration: int=0, is_final_round: bool=False):
        """ShowRoundUI

        Args:
            round (int): _description_. Defaults to 0.
            duration (int): _description_. Defaults to 0.
            is_final_round (bool): _description_. Defaults to False.
        """
        self.ctx.ShowRoundUi(round, duration, is_final_round)

    def side_npc_talk(self, npc_id: int=0, illust: str=None, duration: int=0, script: str=None, voice: str=None, type: str=None, usm: str=None):
        """SideNpcTalk

        Args:
            npc_id (int): _description_. Defaults to 0.
            illust (str): _description_. Defaults to None.
            duration (int): _description_. Defaults to 0.
            script (str): _description_. Defaults to None.
            voice (str): _description_. Defaults to None.
            type (str): _description_. Defaults to None.
            usm (str): _description_. Defaults to None.
        """
        self.ctx.SideNpcTalk(npc_id, illust, duration, script, voice, type, usm)

    def sight_range(self, enable: bool=False, range: int=0, range_z: int=0, border: int=0):
        """SightRange

        Args:
            enable (bool): _description_. Defaults to False.
            range (int): _description_. Defaults to 0.
            range_z (int): _description_. Defaults to 0.
            border (int): _description_. Defaults to 0.
        """
        self.ctx.SightRange(enable, range, range_z, border)

    def spawn_item_range(self, range_ids: List[int]=[], random_pick_count: int=0):
        """SpawnItemRange

        Args:
            range_ids (List[int]): _description_. Defaults to [].
            random_pick_count (int): _description_. Defaults to 0.
        """
        self.ctx.SpawnItemRange(range_ids, random_pick_count)

    def spawn_monster(self, spawn_ids: List[int]=[], auto_target: bool=True, delay: int=0, arg: str=None):
        """몬스터를생성한다

        Args:
            spawn_ids (List[int]): _description_. Defaults to [].
            auto_target (bool): _description_. Defaults to True.
            delay (int): _description_. Defaults to 0.
            arg (str): _description_. Defaults to None.
        """
        self.ctx.SpawnMonster(spawn_ids, auto_target, delay, arg)

    def spawn_npc_range(self, range_ids: List[int]=[], is_auto_targeting: bool=False, random_pick_count: int=0, score: int=0):
        """SpawnNpcRange

        Args:
            range_ids (List[int]): _description_. Defaults to [].
            is_auto_targeting (bool): _description_. Defaults to False.
            random_pick_count (int): _description_. Defaults to 0.
            score (int): _description_. Defaults to 0.
        """
        self.ctx.SpawnNpcRange(range_ids, is_auto_targeting, random_pick_count, score)

    def start_combine_spawn(self, group_id: List[int]=[], is_start: bool=False):
        """StartCombineSpawn

        Args:
            group_id (List[int]): _description_. Defaults to [].
            is_start (bool): _description_. Defaults to False.
        """
        self.ctx.StartCombineSpawn(group_id, is_start)

    def start_mini_game(self, box_id: int=0, round: int=0, game_name: str=None, is_show_result_ui: bool=True):
        """StartMiniGame

        Args:
            box_id (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
            game_name (str): _description_. Defaults to None.
            is_show_result_ui (bool): _description_. Defaults to True.
        """
        self.ctx.StartMiniGame(box_id, round, game_name, is_show_result_ui)

    def start_mini_game_round(self, box_id: int=0, round: int=0):
        """StartMiniGameRound

        Args:
            box_id (int): _description_. Defaults to 0.
            round (int): _description_. Defaults to 0.
        """
        self.ctx.StartMiniGameRound(box_id, round)

    def start_tutorial(self):
        """startTutorial"""
        self.ctx.StartTutorial()

    def talk_npc(self, spawn_id: int=0):
        """TalkNpc

        Args:
            spawn_id (int): _description_. Defaults to 0.
        """
        self.ctx.TalkNpc(spawn_id)

    def unset_mini_game_area_for_hack(self):
        """UnSetMiniGameAreaForHack"""
        self.ctx.UnsetMiniGameAreaForHack()

    def use_state(self, id: int=0, randomize: bool=False):
        """상태를사용한다

        Args:
            id (int): _description_. Defaults to 0.
            randomize (bool): _description_. Defaults to False.
        """
        self.ctx.UseState(id, randomize)

    def user_tag_symbol(self, symbol1: str=None, symbol2: str=None):
        """UserTagSymbol

        Args:
            symbol1 (str): _description_. Defaults to None.
            symbol2 (str): _description_. Defaults to None.
        """
        self.ctx.UserTagSymbol(symbol1, symbol2)

    def user_value_to_number_mesh(self, key: str=None, start_mesh_id: int=0, digit_count: int=0):
        """UserValueToNumberMesh

        Args:
            key (str): _description_. Defaults to None.
            start_mesh_id (int): _description_. Defaults to 0.
            digit_count (int): _description_. Defaults to 0.
        """
        self.ctx.UserValueToNumberMesh(key, start_mesh_id, digit_count)

    def visible_my_pc(self, is_visible: bool=False):
        """VisibleMyPC

        Args:
            is_visible (bool): _description_. Defaults to False.
        """
        self.ctx.VisibleMyPc(is_visible)

    def weather(self, weather_type: str=None):
        """Weather

        Args:
            weather_type (str): _description_. Defaults to None.
        """
        self.ctx.Weather(weather_type)

    def wedding_broken(self):
        """WeddingBroken"""
        self.ctx.WeddingBroken()

    def wedding_move_user(self, entry_type: str=None, map_id: int=0, portal_ids: List[int]=[], box_id: int=0):
        """WeddingMoveUser

        Args:
            entry_type (str): _description_. Defaults to None.
            map_id (int): _description_. Defaults to 0.
            portal_ids (List[int]): _description_. Defaults to [].
            box_id (int): _description_. Defaults to 0.
        """
        self.ctx.WeddingMoveUser(entry_type, map_id, portal_ids, box_id)

    def wedding_mutual_agree(self, agree_type: str=None):
        """WeddingMutualAgree

        Args:
            agree_type (str): _description_. Defaults to None.
        """
        self.ctx.WeddingMutualAgree(agree_type)

    def wedding_mutual_cancel(self, agree_type: str=None):
        """WeddingMutualCancel

        Args:
            agree_type (str): _description_. Defaults to None.
        """
        self.ctx.WeddingMutualCancel(agree_type)

    def wedding_set_user_emotion(self, entry_type: str=None, id: int=0):
        """WeddingSetUserEmotion

        Args:
            entry_type (str): _description_. Defaults to None.
            id (int): _description_. Defaults to 0.
        """
        self.ctx.WeddingSetUserEmotion(entry_type, id)

    def wedding_set_user_look_at(self, entry_type: str=None, look_at_entry_type: str=None, immediate: bool=False):
        """WeddingSetUserLookAt

        Args:
            entry_type (str): _description_. Defaults to None.
            look_at_entry_type (str): _description_. Defaults to None.
            immediate (bool): _description_. Defaults to False.
        """
        self.ctx.WeddingSetUserLookAt(entry_type, look_at_entry_type, immediate)

    def wedding_set_user_rotation(self, entry_type: str=None, rotation: List[float]=[0,0,0], immediate: bool=False):
        """WeddingSetUserRotation

        Args:
            entry_type (str): _description_. Defaults to None.
            rotation (List[float]): _description_. Defaults to [0,0,0].
            immediate (bool): _description_. Defaults to False.
        """
        self.ctx.WeddingSetUserRotation(entry_type, rotation, immediate)

    def wedding_user_to_patrol(self, patrol_name: str=None, entry_type: str=None, patrol_index: int=0):
        """WeddingUserToPatrol

        Args:
            patrol_name (str): _description_. Defaults to None.
            entry_type (str): _description_. Defaults to None.
            patrol_index (int): _description_. Defaults to 0.
        """
        self.ctx.WeddingUserToPatrol(patrol_name, entry_type, patrol_index)

    def wedding_vow_complete(self):
        """WeddingVowComplete"""
        self.ctx.WeddingVowComplete()

    def widget_action(self, type: str=None, func: str=None, widget_arg: str=None, desc: str=None, widget_arg_num: int=0):
        """WidgetAction

        Args:
            type (str): _description_. Defaults to None.
            func (str): _description_. Defaults to None.
            widget_arg (str): _description_. Defaults to None.
            desc (str): _description_. Defaults to None.
            widget_arg_num (int): _description_. Defaults to 0.
        """
        self.ctx.WidgetAction(type, func, widget_arg, desc, widget_arg_num)

    def write_log(self, log_name: str=None, event: str=None, trigger_id: int=0, sub_event: str=None, arg4: int=0):
        """로그를남긴다

        Args:
            log_name (str): _description_. Defaults to None.
            event (str): _description_. Defaults to None.
            trigger_id (int): _description_. Defaults to 0.
            sub_event (str): _description_. Defaults to None.
            arg4 (int): _description_. Defaults to 0.
        """
        self.ctx.WriteLog(log_name, event, trigger_id, sub_event, arg4)


    """ Conditions """
    def bonus_game_reward_detected(self, box_id: int=0, type: int=0) -> bool:
        """보너스게임보상받은유저를감지했으면

        Args:
            box_id (int): _description_. Defaults to 0.
            type (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.BonusGameRewardDetected(box_id, type)

    def check_any_user_additional_effect(self, box_id: int=0, additional_effect_id: int=0, level: int=0) -> bool:
        """CheckAnyUserAdditionalEffect

        Args:
            box_id (int): _description_. Defaults to 0.
            additional_effect_id (int): _description_. Defaults to 0.
            level (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.CheckAnyUserAdditionalEffect(box_id, additional_effect_id, level)

    def check_dungeon_lobby_user_count(self) -> bool:
        """CheckDungeonLobbyUserCount

        Returns:
            bool: _description_
        """
        return self.ctx.CheckDungeonLobbyUserCount()

    def check_npc_additional_effect(self, spawn_id: int=0, additional_effect_id: int=0, level: int=0) -> bool:
        """CheckNpcAdditionalEffect

        Args:
            spawn_id (int): _description_. Defaults to 0.
            additional_effect_id (int): _description_. Defaults to 0.
            level (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.CheckNpcAdditionalEffect(spawn_id, additional_effect_id, level)

    def check_npc_damage(self, spawn_id: int=0, damage_rate: float=0.0, operator: str='GreaterEqual') -> bool:
        """CheckNpcDamage

        Args:
            spawn_id (int): _description_. Defaults to 0.
            damage_rate (float): _description_. Defaults to 0.0.
            operator (str): _description_. Defaults to 'GreaterEqual'.

        Returns:
            bool: _description_
        """
        return self.ctx.CheckNpcDamage(spawn_id, damage_rate, operator)

    def check_npc_extra_data(self, spawn_point_id: str=None, extra_data_key: str=None, extra_data_value: str=None, operator: str=None) -> bool:
        """CheckNpcExtraData

        Args:
            spawn_point_id (str): _description_. Defaults to None.
            extra_data_key (str): _description_. Defaults to None.
            extra_data_value (str): _description_. Defaults to None.
            operator (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return self.ctx.CheckNpcExtraData(spawn_point_id, extra_data_key, extra_data_value, operator)

    def check_npc_hp(self, compare: str=None, value: int=0, spawn_id: int=0, is_relative: bool=False) -> bool:
        """CheckNpcHp

        Args:
            compare (str): _description_. Defaults to None.
            value (int): _description_. Defaults to 0.
            spawn_id (int): _description_. Defaults to 0.
            is_relative (bool): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
        return self.ctx.CheckNpcHp(compare, value, spawn_id, is_relative)

    def check_same_user_tag(self, box_id: int=0) -> bool:
        """CheckSameUserTag

        Args:
            box_id (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.CheckSameUserTag(box_id)

    def check_user(self) -> bool:
        """CheckUser

        Returns:
            bool: _description_
        """
        return self.ctx.CheckUser()

    def check_user_count(self, check_count: int=0) -> bool:
        """CheckUserCount

        Args:
            check_count (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.CheckUserCount(check_count)

    def count_users(self, box_id: int=0, min_users: str=None, operator: str='GreaterEqual', user_tag_id: int=0) -> bool:
        """여러명의유저를감지했으면

        Args:
            box_id (int): _description_. Defaults to 0.
            min_users (str): _description_. Defaults to None.
            operator (str): _description_. Defaults to 'GreaterEqual'.
            user_tag_id (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.CountUsers(box_id, min_users, operator, user_tag_id)

    def day_of_week(self, day_of_weeks: List[int]=[], desc: str=None) -> bool:
        """DayOfWeek

        Args:
            day_of_weeks (List[int]): _description_. Defaults to [].
            desc (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return self.ctx.DayOfWeek(day_of_weeks, desc)

    def detect_liftable_object(self, box_ids: List[int]=[], item_id: int=0) -> bool:
        """DetectLiftableObject

        Args:
            box_ids (List[int]): _description_. Defaults to [].
            item_id (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.DetectLiftableObject(box_ids, item_id)

    def dungeon_check_play_time(self, play_seconds: int=0, operator: str='GreaterEqual') -> bool:
        """DungeonCheckPlayTime

        Args:
            play_seconds (int): _description_. Defaults to 0.
            operator (str): _description_. Defaults to 'GreaterEqual'.

        Returns:
            bool: _description_
        """
        return self.ctx.DungeonCheckPlayTime(play_seconds, operator)

    def dungeon_check_state(self, check_state: str=None) -> bool:
        """DungeonCheckState

        Args:
            check_state (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return self.ctx.DungeonCheckState(check_state)

    def dungeon_first_user_mission_score(self, score: int=0, operator: str='GreaterEqual') -> bool:
        """DungeonFirstUserMissionScore

        Args:
            score (int): _description_. Defaults to 0.
            operator (str): _description_. Defaults to 'GreaterEqual'.

        Returns:
            bool: _description_
        """
        return self.ctx.DungeonFirstUserMissionScore(score, operator)

    def dungeon_id(self, dungeon_id: int=0) -> bool:
        """DungeonID

        Args:
            dungeon_id (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.DungeonId(dungeon_id)

    def dungeon_level(self, level: int=0) -> bool:
        """DungeonLevel

        Args:
            level (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.DungeonLevel(level)

    def dungeon_max_user_count(self, value: int=0) -> bool:
        """DungeonMaxUserCount

        Args:
            value (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.DungeonMaxUserCount(value)

    def dungeon_round_require(self, round: int=0) -> bool:
        """DungeonRoundRequire

        Args:
            round (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.DungeonRoundRequire(round)

    def dungeon_time_out(self) -> bool:
        """DungeonTimeOut

        Returns:
            bool: _description_
        """
        return self.ctx.DungeonTimeOut()

    def dungeon_variable(self, var_id: int=0, value: int=0) -> bool:
        """DungeonVariable

        Args:
            var_id (int): _description_. Defaults to 0.
            value (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.DungeonVariable(var_id, value)

    def guild_vs_game_scored_team(self, team_id: int=0) -> bool:
        """GuildVsGameScoredTeam

        Args:
            team_id (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.GuildVsGameScoredTeam(team_id)

    def guild_vs_game_winner_team(self, team_id: int=0) -> bool:
        """GuildVsGameWinnerTeam

        Args:
            team_id (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.GuildVsGameWinnerTeam(team_id)

    def is_dungeon_room(self) -> bool:
        """IsDungeonRoom

        Returns:
            bool: _description_
        """
        return self.ctx.IsDungeonRoom()

    def is_playing_maple_survival(self) -> bool:
        """IsPlayingMapleSurvival

        Returns:
            bool: _description_
        """
        return self.ctx.IsPlayingMapleSurvival()

    def monster_dead(self, spawn_ids: List[int]=[], arg2: bool=True) -> bool:
        """몬스터가죽어있으면

        Args:
            spawn_ids (List[int]): _description_. Defaults to [].
            arg2 (bool): _description_. Defaults to True.

        Returns:
            bool: _description_
        """
        return self.ctx.MonsterDead(spawn_ids, arg2)

    def monster_in_combat(self, spawn_ids: List[int]=[]) -> bool:
        """몬스터가전투상태면

        Args:
            spawn_ids (List[int]): _description_. Defaults to [].

        Returns:
            bool: _description_
        """
        return self.ctx.MonsterInCombat(spawn_ids)

    def npc_detected(self, box_id: int=0, spawn_ids: List[int]=[]) -> bool:
        """NPC를감지했으면

        Args:
            box_id (int): _description_. Defaults to 0.
            spawn_ids (List[int]): _description_. Defaults to [].

        Returns:
            bool: _description_
        """
        return self.ctx.NpcDetected(box_id, spawn_ids)

    def npc_is_dead_by_string_id(self, string_id: str=None) -> bool:
        """NpcIsDeadByStringID

        Args:
            string_id (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return self.ctx.NpcIsDeadByStringId(string_id)

    def object_interacted(self, interact_ids: List[int]=[], state: int=0, ar2: str=None) -> bool:
        """오브젝트가반응했으면

        Args:
            interact_ids (List[int]): _description_. Defaults to [].
            state (int): _description_. Defaults to 0.
            ar2 (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return self.ctx.ObjectInteracted(interact_ids, state, ar2)

    def pvp_zone_ended(self, box_id: int=0) -> bool:
        """PVP존이종료했으면

        Args:
            box_id (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.PvpZoneEnded(box_id)

    def quest_user_detected(self, box_ids: List[int]=[], quest_ids: List[int]=[], quest_states: List[int]=[], job_code: int=0) -> bool:
        """퀘스트유저를감지하면

        Args:
            box_ids (List[int]): _description_. Defaults to [].
            quest_ids (List[int]): _description_. Defaults to [].
            quest_states (List[int]): _description_. Defaults to [].
            job_code (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.QuestUserDetected(box_ids, quest_ids, quest_states, job_code)

    def random_condition(self, weight: float=0.0, desc: str=None) -> bool:
        """랜덤조건

        Args:
            weight (float): _description_. Defaults to 0.0.
            desc (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return self.ctx.RandomCondition(weight, desc)

    def score_board_compare(self, operator: str='GreaterEqual', score: int=0) -> bool:
        """ScoreBoardCompare

        Args:
            operator (str): _description_. Defaults to 'GreaterEqual'.
            score (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.ScoreBoardCompare(operator, score)

    def shadow_expedition_reach_point(self, point: int=0) -> bool:
        """ShadowExpeditionReachPoint

        Args:
            point (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.ShadowExpeditionReachPoint(point)

    def time_expired(self, timer_id: str=None) -> bool:
        """시간이경과했으면

        Args:
            timer_id (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return self.ctx.TimeExpired(timer_id)

    def user_detected(self, box_ids: List[int]=[], job_code: int=0) -> bool:
        """유저를감지했으면

        Args:
            box_ids (List[int]): _description_. Defaults to [].
            job_code (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.UserDetected(box_ids, job_code)

    def user_value(self, key: str=None, value: int=0, operator: str='GreaterEqual') -> bool:
        """UserValue

        Args:
            key (str): _description_. Defaults to None.
            value (int): _description_. Defaults to 0.
            operator (str): _description_. Defaults to 'GreaterEqual'.

        Returns:
            bool: _description_
        """
        return self.ctx.UserValue(key, value, operator)

    def wait_and_reset_tick(self, wait_tick: int=0) -> bool:
        """WaitAndResetTick

        Args:
            wait_tick (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.WaitAndResetTick(wait_tick)

    def wait_seconds_user_value(self, key: str=None, desc: str=None) -> bool:
        """WaitSecondsUserValue

        Args:
            key (str): _description_. Defaults to None.
            desc (str): _description_. Defaults to None.

        Returns:
            bool: _description_
        """
        return self.ctx.WaitSecondsUserValue(key, desc)

    def wait_tick(self, wait_tick: int=0) -> bool:
        """WaitTick

        Args:
            wait_tick (int): _description_. Defaults to 0.

        Returns:
            bool: _description_
        """
        return self.ctx.WaitTick(wait_tick)

    def wedding_entry_in_field(self, entry_type: str=None, is_in_field: bool=False) -> bool:
        """WeddingEntryInField

        Args:
            entry_type (str): _description_. Defaults to None.
            is_in_field (bool): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
        return self.ctx.WeddingEntryInField(entry_type, is_in_field)

    def wedding_hall_state(self, hall_state: str=None, success: bool=False) -> bool:
        """WeddingHallState

        Args:
            hall_state (str): _description_. Defaults to None.
            success (bool): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
        return self.ctx.WeddingHallState(hall_state, success)

    def wedding_mutual_agree_result(self, agree_type: str=None, success: bool=False) -> bool:
        """WeddingMutualAgreeResult

        Args:
            agree_type (str): _description_. Defaults to None.
            success (bool): _description_. Defaults to False.

        Returns:
            bool: _description_
        """
        return self.ctx.WeddingMutualAgreeResult(agree_type, success)

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
        return self.ctx.WidgetCondition(type, name, condition, desc)

