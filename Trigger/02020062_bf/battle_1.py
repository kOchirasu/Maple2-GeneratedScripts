""" trigger/02020062_bf/battle_1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='GaugeClear', value=0)
        start_combine_spawn(groupId=[490], isStart=False)
        start_combine_spawn(groupId=[491], isStart=False)
        start_combine_spawn(groupId=[492], isStart=False)
        start_combine_spawn(groupId=[493], isStart=False)
        start_combine_spawn(groupId=[495], isStart=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='SpawnStart', value=1):
            return 스폰_1_SE()


#   시작 
class 스폰_1_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[490], isStart=True)

    def on_tick(self) -> state.State:
        if user_value(key='SpawnStart', value=2):
            return 대기()
        if wait_tick(waitTick=5000):
            return 스폰_1()


class 스폰_1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020062_BF__BATTLE_1__0$')

    def on_tick(self) -> state.State:
        if user_value(key='SpawnStart', value=2):
            return 대기()
        if wait_tick(waitTick=5000):
            return 스폰_1_추가대사1()


class 스폰_1_추가대사1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020062_BF__BATTLE_1__1$')

    def on_tick(self) -> state.State:
        if user_value(key='SpawnStart', value=2):
            return 대기()
        if wait_tick(waitTick=5000):
            return 스폰_1_추가대사2()


class 스폰_1_추가대사2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020062_BF__BATTLE_1__2$')

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=120):
            return 스폰_2_SE()
        if user_value(key='SpawnStart', value=2):
            return 대기()


class 스폰_2_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='SpawnStart', value=2):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_2()


class 스폰_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[491], isStart=True)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=300):
            return 스폰_3_SE()
        if user_value(key='SpawnStart', value=2):
            return 대기()


class 스폰_3_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='SpawnStart', value=2):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_3()


class 스폰_3(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[492], isStart=True)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=450):
            return 스폰_4_SE()
        if user_value(key='SpawnStart', value=2):
            return 대기()


class 스폰_4_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='SpawnStart', value=2):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_4()


class 스폰_4(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[493], isStart=True)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=600):
            return 스폰_5_SE()
        if user_value(key='SpawnStart', value=2):
            return 대기()


class 스폰_5_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='SpawnStart', value=2):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_5()


class 스폰_5(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[495], isStart=True)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=750):
            return 오브젝트페이즈()
        if user_value(key='SpawnStart', value=2):
            return 대기()


class 오브젝트페이즈(state.State):
    def on_enter(self):
        shadow_expedition(type='CloseBossGauge')
        start_combine_spawn(groupId=[490], isStart=False)
        start_combine_spawn(groupId=[491], isStart=False)
        start_combine_spawn(groupId=[492], isStart=False)
        start_combine_spawn(groupId=[493], isStart=False)
        start_combine_spawn(groupId=[495], isStart=False)
        set_user_value(triggerId=99990001, key='GaugeClear', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='SpawnStart', value=2):
            return 대기()


