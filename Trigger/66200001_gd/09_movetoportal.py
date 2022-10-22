""" trigger/66200001_gd/09_movetoportal.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='MoveToTeamPortal', value=0)
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False) # LeavePortal_Safe (arg3=작동여부)

    def on_tick(self) -> state.State:
        if user_value(key='MoveToTeamPortal', value=1):
            return MoveUserbyTag()


class MoveUserbyTag(state.State):
    def on_enter(self):
        move_to_portal(boxId=9900, userTagId=1, portalId=11) # Tag1=Blue
        move_to_portal(boxId=9900, userTagId=2, portalId=12) # Tag2=Red
        set_user_value(triggerId=11, key='BannerCheckIn', value=1) # TheNumberOfBlueTeamWaiting
        set_user_value(triggerId=13, key='BannerCheckIn', value=1) # TheNumberOfRedTeamWaiting

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return MoveUserbyTag()
        if user_value(key='MoveToTeamPortal', value=2):
            return QuitDelay()


class QuitDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_portal(portalId=6, visible=False, enabled=True, minimapVisible=False) # 게임 시작 후 입장한 유저 퇴장 조치


