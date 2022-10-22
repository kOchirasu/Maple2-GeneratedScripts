""" trigger/80000016_bonus/prize.xml """
from common import *
import state


class 입장(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154], visible=True)
        create_monster(spawnIds=[199], arg2=False)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        create_item(spawnIds=[201])
        create_item(spawnIds=[202])
        create_item(spawnIds=[203])
        create_item(spawnIds=[204])
        create_item(spawnIds=[205])
        create_item(spawnIds=[206])
        create_item(spawnIds=[207])
        create_item(spawnIds=[208])
        create_item(spawnIds=[209])
        create_item(spawnIds=[210])
        create_item(spawnIds=[211])
        create_item(spawnIds=[212])
        create_item(spawnIds=[213])
        create_item(spawnIds=[216])
        create_item(spawnIds=[217])
        create_item(spawnIds=[218])
        create_item(spawnIds=[219])
        create_item(spawnIds=[220])
        create_item(spawnIds=[221])
        create_item(spawnIds=[222])
        create_item(spawnIds=[226])
        create_item(spawnIds=[227])
        create_item(spawnIds=[228])
        create_item(spawnIds=[229])
        create_item(spawnIds=[230])
        create_item(spawnIds=[231])
        create_item(spawnIds=[232])
        create_item(spawnIds=[233])
        create_item(spawnIds=[234])
        create_item(spawnIds=[235])
        create_item(spawnIds=[243])
        create_item(spawnIds=[244])
        create_item(spawnIds=[245])
        create_item(spawnIds=[246])
        create_item(spawnIds=[247])
        create_item(spawnIds=[248])
        create_item(spawnIds=[250])
        create_item(spawnIds=[251])
        create_item(spawnIds=[255])
        create_item(spawnIds=[256])
        create_item(spawnIds=[257])
        create_item(spawnIds=[258])
        create_item(spawnIds=[259])
        create_item(spawnIds=[260])
        create_item(spawnIds=[261])
        create_item(spawnIds=[262])
        create_item(spawnIds=[263])
        create_item(spawnIds=[264])
        create_item(spawnIds=[265])
        create_item(spawnIds=[266])
        create_item(spawnIds=[267])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 몬스터체크()


class 몬스터체크(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154], visible=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[199]):
            return 포탈생성()


class 포탈생성(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료()


class 완료(state.State):
    pass


