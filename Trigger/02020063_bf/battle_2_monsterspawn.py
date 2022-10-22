""" trigger/02020063_bf/battle_2_monsterspawn.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='Battle_2_Clear', value=0) # <웨이브 진행용 SetuserValue >
        start_combine_spawn(groupId=[500], isStart=False) # combinespawngroup 테이블 참조
        start_combine_spawn(groupId=[501], isStart=False)
        start_combine_spawn(groupId=[502], isStart=False)
        start_combine_spawn(groupId=[503], isStart=False)
        start_combine_spawn(groupId=[504], isStart=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml') # 웨이브 구간별 or 조건으로 타이머 설정, 개별 30초 정도 설정
        reset_timer(timerId='1')
        reset_timer(timerId='2')
        reset_timer(timerId='3')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_SpawnStart', value=1):
            return 스폰_1_SE()


#   시작 
class 스폰_1_SE(state.State):
    def on_enter(self):
        score_board_create(maxScore=800) # <ShadowExpedition 기능을 대체함>
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[500], isStart=True)

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=5000):
            return 스폰_1()


class 스폰_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=5000):
            return 스폰_2_SE()


class 스폰_2_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_2()


class 스폰_2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[501], isStart=True)

    def on_tick(self) -> state.State:
        if any_one():
            return 스폰_3_SE()
        if user_value(key='Battle_2_SpawnStart', value=0):
            return 대기()


class 스폰_3_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_3()


class 스폰_3(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=30, clearAtZero=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[502], isStart=True)

    def on_tick(self) -> state.State:
        if any_one():
            return 스폰_4_SE()
        if user_value(key='Battle_2_SpawnStart', value=0):
            return 대기()


class 스폰_4_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_4()


class 스폰_4(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=30, clearAtZero=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        start_combine_spawn(groupId=[503], isStart=True)

    def on_tick(self) -> state.State:
        if any_one():
            return 스폰_5_SE()
        if user_value(key='Battle_2_SpawnStart', value=0):
            return 대기()


class 스폰_5_SE(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_SpawnStart', value=0):
            return 대기()
        if wait_tick(waitTick=2000):
            return 스폰_5()


class 스폰_5(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[504], isStart=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        score_board_remove()

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_SpawnStart', value=0):
            return 대기()


