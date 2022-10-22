""" trigger/02020025_bf/dungeonmission.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 던전미션체크대기()


class 던전미션체크대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=904, spawnIds=[201]):
            return 체력90이하체크()


class 체력90이하체크(state.State):
    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=90, spawnId=201, isRelative=True):
            return 지하1층()


class 지하1층(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=24092001)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=70, spawnId=201, isRelative=True):
            return 지하2층()


class 지하2층(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=24092002)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=55, spawnId=201, isRelative=True):
            return 지하3층()


class 지하3층(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=24092003)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=40, spawnId=201, isRelative=True):
            return 지하4층()


class 지하4층(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=24092004)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


