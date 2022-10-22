""" trigger/02020065_bf/battle_1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='Battle_1_Clear', value=0)
        start_combine_spawn(groupId=[505], isStart=False)
        start_combine_spawn(groupId=[506], isStart=False)
        start_combine_spawn(groupId=[507], isStart=False)
        start_combine_spawn(groupId=[508], isStart=False)
        start_combine_spawn(groupId=[509], isStart=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml') # 웨이브 구간별, or 조건으로 타이머 설정, 개별 30초 정도 설정
        reset_timer(timerId='1')
        reset_timer(timerId='2')
        reset_timer(timerId='3')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_SpawnStart', value=1):
            return 스폰_1_SE()


#   시작 
class 스폰_1_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        score_board_create(type='ShadowGauge', maxScore=800) # <ShadowExpedition 기능을 대체함>
        start_combine_spawn(groupId=[505], isStart=True)

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=5000):
            return 스폰_1()


class 스폰_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020065_BF__BATTLE_1__0$')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=5000):
            return 스폰_1_추가대사1()


class 스폰_1_추가대사1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020065_BF__BATTLE_1__1$')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=5000):
            return 스폰_1_추가대사2()


class 스폰_1_추가대사2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020065_BF__BATTLE_1__2$')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=5000):
            return 스폰_2_SE()


class 스폰_2_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_2()


class 스폰_2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=990, clearAtZero=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[506], isStart=True)

    def on_tick(self) -> state.State:
        if any_one():
            return 스폰_3_SE()
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()


class 스폰_3_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_3()


class 스폰_3(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=990, clearAtZero=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[507], isStart=True)

    def on_tick(self) -> state.State:
        if any_one():
            return 스폰_4_SE()
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()


class 스폰_4_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_4()


class 스폰_4(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=990, clearAtZero=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[508], isStart=True)

    def on_tick(self) -> state.State:
        if any_one():
            return 스폰_5_SE()
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()


class 스폰_5_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_5()


class 스폰_5(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[509], isStart=True)

    def on_tick(self) -> state.State:
        if score_board_compare(compareOp='GreaterEqual', score=800):
            return 포탑페이즈()
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()


class 포탑페이즈(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[505], isStart=False)
        start_combine_spawn(groupId=[506], isStart=False)
        start_combine_spawn(groupId=[507], isStart=False)
        start_combine_spawn(groupId=[508], isStart=False)
        start_combine_spawn(groupId=[509], isStart=False)
        set_user_value(triggerId=99990001, key='Battle_1_Clear', value=1) # 1phase 끝
        score_board_remove()

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_SpawnStart', value=0):
            return 대기()


