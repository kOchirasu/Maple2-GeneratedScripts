""" trigger/02000248_bf/trigger_01.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110])
        set_effect(triggerIds=[2001], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=201, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[201]):
            return 시작()

state.DungeonStart = DungeonStart


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[798,799], visible=False)
        set_timer(timerId='89', seconds=3, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='89'):
            return 공격()


class 공격(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103], arg2=True)
        set_effect(triggerIds=[2001], visible=True)
        set_event_ui(type=1, arg2='$02000248_BF__TRIGGER_01__0$', arg3='5000', arg4='0')
        set_timer(timerId='1', seconds=9, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103]):
            return 공격1()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104,105], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[104,105]):
            return 공격2()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[106,107,108], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106,107,108]):
            return 공격2_2()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격2_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[109,110], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[109,110]):
            return 공격3()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[114,115,116], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[114,115,116]):
            return 공격3_2()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격3_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111,112,113], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,112,113]):
            return 공격3_3()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격3_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[117,118,119,120], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[117,118,119,120]):
            return 공격4()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[121,122,123,124,125], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[121,122,123,124,125]):
            return 공격4_2()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격4_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[126,127,128,129,130], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[126,127,128,129,130]):
            return 공격5()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[131,132,133,134,135,136], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[131,132,133,134,135,136]):
            return 공격5_2()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격5_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[137,138,139,140], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[137,138,139,140]):
            return 공격6()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[141,142,143,144,145,146,148], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[141,142,143,144,145,146,148]):
            return 공격7()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격7(state.State):
    def on_enter(self):
        create_monster(spawnIds=[151,153,154,155,156,157,158], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[151,153,154,155,156,157,158]):
            return 공격8()
        if not user_detected(boxIds=[999]):
            return 대기()


class 공격8(state.State):
    def on_enter(self):
        create_monster(spawnIds=[161,162,163,164,167,168,169,170], arg2=True)
        set_timer(timerId='1', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            destroy_monster(spawnIds=[161,162,163,164,167,168,169,170])
            return 끝연출()
        if not user_detected(boxIds=[999]):
            return 대기()


class 끝연출(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8001,8003,8002], returnView=False)
        set_timer(timerId='1', seconds=4, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        move_user(mapId=2000249, portalId=2)
        set_timer(timerId='1', seconds=3, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 차진입대기2()


class 차진입대기2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=15, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 끝()


