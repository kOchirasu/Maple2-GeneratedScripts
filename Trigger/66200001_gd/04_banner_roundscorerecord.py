""" trigger/66200001_gd/04_banner_roundscorerecord.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[999], visible=True, arg3=0, delay=0, scale=0) # mark
        self.set_mesh(triggerIds=[1000], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1100], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1001,1002,1003], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1100,1101,1102,1103], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return Enter(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(triggerIds=[1000], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1100], visible=False, arg3=0, delay=0, scale=0)


class Enter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        self.set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        self.set_user_value(key='RoundScoreRecord', value=0)
        self.set_user_value(key='BlueteamScore', value=0)
        self.set_user_value(key='RedteamScore', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RoundScoreRecord', value=1):
            return R01BannerUpdate(self.ctx)


class R01BannerUpdate(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        self.set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        self.set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RoundScoreRecord', value=2):
            return R02BannerUpdate(self.ctx)


class R02BannerUpdate(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        self.set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        self.set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RoundScoreRecord', value=3):
            return R03BannerUpdate(self.ctx)


class R03BannerUpdate(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        self.set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        self.set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BlueteamScore', value=3):
            return BlueTeamWin(self.ctx)
        if self.user_value(key='RedteamScore', value=3):
            return RedTeamWin(self.ctx)
        if self.user_value(key='RoundScoreRecord', value=4):
            return R04BannerUpdate(self.ctx)


class R04BannerUpdate(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        self.set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        self.set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BlueteamScore', value=3):
            return BlueTeamWin(self.ctx)
        if self.user_value(key='RedteamScore', value=3):
            return RedTeamWin(self.ctx)
        if self.user_value(key='RoundScoreRecord', value=5):
            return R05BannerUpdate(self.ctx)


class R05BannerUpdate(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        self.user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        self.set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        self.user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        self.set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BlueteamScore', value=3):
            return BlueTeamWin(self.ctx)
        if self.user_value(key='RedteamScore', value=3):
            return RedTeamWin(self.ctx)
        if self.user_value(key='RoundScoreRecord', value=5):
            return EndGame(self.ctx)


class BlueTeamWin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='WinnerTeam', value=1)


class RedTeamWin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='WinnerTeam', value=2)


class EndGame(trigger_api.Trigger):
    pass


initial_state = Wait
