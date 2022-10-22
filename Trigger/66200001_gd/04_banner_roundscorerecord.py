""" trigger/66200001_gd/04_banner_roundscorerecord.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[999], visible=True, arg3=0, arg4=0, arg5=0) # mark
        set_mesh(triggerIds=[1000], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1100], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1001,1002,1003], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1100,1101,1102,1103], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if check_user():
            return Enter()

    def on_exit(self):
        set_mesh(triggerIds=[1000], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1100], visible=False, arg3=0, arg4=0, arg5=0)


class Enter(state.State):
    def on_enter(self):
        set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        set_user_value(key='RoundScoreRecord', value=0)
        set_user_value(key='BlueteamScore', value=0)
        set_user_value(key='RedteamScore', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RoundScoreRecord', value=1):
            return R01BannerUpdate()


class R01BannerUpdate(state.State):
    def on_enter(self):
        set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RoundScoreRecord', value=2):
            return R02BannerUpdate()


class R02BannerUpdate(state.State):
    def on_enter(self):
        set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RoundScoreRecord', value=3):
            return R03BannerUpdate()


class R03BannerUpdate(state.State):
    def on_enter(self):
        set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='BlueteamScore', value=3):
            return BlueTeamWin()
        if user_value(key='RedteamScore', value=3):
            return RedTeamWin()
        if user_value(key='RoundScoreRecord', value=4):
            return R04BannerUpdate()


class R04BannerUpdate(state.State):
    def on_enter(self):
        set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='BlueteamScore', value=3):
            return BlueTeamWin()
        if user_value(key='RedteamScore', value=3):
            return RedTeamWin()
        if user_value(key='RoundScoreRecord', value=5):
            return R05BannerUpdate()


class R05BannerUpdate(state.State):
    def on_enter(self):
        set_user_value_from_guild_vs_game_score(teamId=1, key='BlueteamScore')
        user_value_to_number_mesh(key='BlueteamScore', startMeshId=1000, digitCount=1)
        set_user_value_from_guild_vs_game_score(teamId=2, key='RedteamScore')
        user_value_to_number_mesh(key='RedteamScore', startMeshId=1100, digitCount=1)
        set_user_value(key='RoundScoreRecord', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='BlueteamScore', value=3):
            return BlueTeamWin()
        if user_value(key='RedteamScore', value=3):
            return RedTeamWin()
        if user_value(key='RoundScoreRecord', value=5):
            return EndGame()


class BlueTeamWin(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='WinnerTeam', value=1)


class RedTeamWin(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='WinnerTeam', value=2)


class EndGame(state.State):
    pass


