""" trigger/02000252_bf/elite_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8902], visible=False) # 가이드 화살표
        set_effect(triggerIds=[605], visible=False) # 벨라 음성
        set_mesh(triggerIds=[2113,2114,2115,2116,2117,2118], visible=True)
        set_mesh(triggerIds=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=904, boxId=1):
            return 딜레이()


class 대기2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2113,2114,2115,2116,2117,2118], visible=True)
        set_mesh(triggerIds=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=904, boxId=1):
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
        create_monster(spawnIds=[1003], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사()


class 벨라2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        create_monster(spawnIds=[1003], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사2()


class 벨라대사(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        set_conversation(type=1, spawnId=1003, script='$02000252_BF__ELITE_02__0$', arg4=2)
        set_scene_skip(state=이동, arg2='nextState') # action name="스킵을설정한다" arg1="이동" /

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라스킬()


class 벨라대사2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        set_conversation(type=1, spawnId=1003, script='$02000252_BF__ELITE_02__1$', arg4=2)
        set_scene_skip(state=이동, arg2='nextState') # action name="스킵을설정한다" arg1="이동" /

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라스킬2()


class 벨라스킬(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        move_npc(spawnId=1003, patrolName='MS2PatrolData_4')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 이동()


class 벨라스킬2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_scene_skip()
        move_npc(spawnId=1003, patrolName='MS2PatrolData_4')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 이동2()


class 이동(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        # <action name="무작위유저를이동시킨다" arg1="02000252" arg2="9998" arg3="904" arg4="1" />
        create_monster(spawnIds=[202], arg2=False)
        create_monster(spawnIds=[1102], arg2=False)
        create_monster(spawnIds=[1103], arg2=False)
        create_monster(spawnIds=[1104], arg2=False)
        create_monster(spawnIds=[1105], arg2=False)
        create_monster(spawnIds=[1106], arg2=False)
        create_monster(spawnIds=[1107], arg2=False)
        create_monster(spawnIds=[1108], arg2=False)
        create_monster(spawnIds=[1109], arg2=False)
        create_monster(spawnIds=[1110], arg2=False)
        set_mesh(triggerIds=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라삭제()


class 이동2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        # <action name="무작위유저를이동시킨다" arg1="02000252" arg2="9998" arg3="904" arg4="1" />
        set_mesh(triggerIds=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라삭제()


class 벨라삭제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1003])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[202]):
            return 개봉()


class 개봉(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8902], visible=True) # 가이드 화살표
        set_mesh(triggerIds=[2113,2114,2115,2116,2117,2118], visible=False)
        set_mesh(triggerIds=[2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145], visible=False)


