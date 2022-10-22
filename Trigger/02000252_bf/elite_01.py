""" trigger/02000252_bf/elite_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8901], visible=False) # 가이드 화살표
        set_effect(triggerIds=[604], visible=False) # 벨라 음성
        set_mesh(triggerIds=[2119,2120,2121,2122,2123,2124], visible=True)
        set_mesh(triggerIds=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=903, boxId=1):
            return 딜레이()


class 대기2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2119,2120,2121,2122,2123,2124], visible=True)
        set_mesh(triggerIds=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=903, boxId=1):
            return 딜레이2()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라()


class 딜레이2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라2()


class 벨라(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        create_monster(spawnIds=[1002], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사()


class 벨라2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        create_monster(spawnIds=[1002], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사2()


class 벨라대사(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        set_conversation(type=1, spawnId=1002, script='$02000252_BF__ELITE_01__0$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라스킬()


class 벨라대사2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        set_conversation(type=1, spawnId=1002, script='$02000252_BF__ELITE_01__1$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라스킬2()


class 벨라스킬(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_2')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 이동()


class 벨라스킬2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_2')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 이동2()


class 이동(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        # <action name="무작위유저를이동시킨다" arg1="02000252" arg2="9999" arg3="903" arg4="1" />
        create_monster(spawnIds=[201], arg2=False)
        create_monster(spawnIds=[1093], arg2=False)
        create_monster(spawnIds=[1094], arg2=False)
        create_monster(spawnIds=[1095], arg2=False)
        create_monster(spawnIds=[1096], arg2=False)
        create_monster(spawnIds=[1097], arg2=False)
        create_monster(spawnIds=[1098], arg2=False)
        create_monster(spawnIds=[1099], arg2=False)
        create_monster(spawnIds=[1100], arg2=False)
        create_monster(spawnIds=[1101], arg2=False)
        set_mesh(triggerIds=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라삭제()


class 이동2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        # <action name="무작위유저를이동시킨다" arg1="02000252" arg2="9999" arg3="903" arg4="1" />
        set_mesh(triggerIds=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라삭제()


class 벨라삭제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1002])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            return 개봉()


class 개봉(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8901], visible=True) # 가이드 화살표
        set_mesh(triggerIds=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=False)
        set_mesh(triggerIds=[2119,2120,2121,2122,2123,2124], visible=False)


