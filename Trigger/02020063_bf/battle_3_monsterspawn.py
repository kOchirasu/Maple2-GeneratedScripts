""" trigger/02020063_bf/battle_3_monsterspawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='Battle_3_Clear', value=0)
        self.start_combine_spawn(groupId=[500], isStart=False)
        self.start_combine_spawn(groupId=[501], isStart=False)
        self.start_combine_spawn(groupId=[502], isStart=False)
        self.start_combine_spawn(groupId=[503], isStart=False)
        self.start_combine_spawn(groupId=[504], isStart=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')
        self.reset_timer(timerId='3')
        self.reset_timer(timerId='4')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_SpawnStart', value=1):
            return 스폰_1_SE(self.ctx)


# 시작
class 스폰_1_SE(trigger_api.Trigger):
    def on_enter(self):
        self.score_board_create(maxScore=900) # <ShadowExpedition 기능을 대체함>
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 스폰_1(self.ctx)


class 스폰_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=60, startDelay=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(groupId=[500], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.any_one():
            return 스폰_3_SE(self.ctx)


class 스폰_2_SE(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 스폰_2(self.ctx)


class 스폰_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=60, startDelay=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(groupId=[501], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.any_one():
            return 스폰_3_SE(self.ctx)
        if self.user_value(key='Battle_3_SpawnStart', value=0):
            return 대기(self.ctx)


class 스폰_3_SE(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 스폰_3(self.ctx)


class 스폰_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=60, startDelay=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(groupId=[502], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.any_one():
            return 스폰_4_SE(self.ctx)
        if self.user_value(key='Battle_3_SpawnStart', value=0):
            return 대기(self.ctx)


class 스폰_4_SE(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 스폰_4(self.ctx)


class 스폰_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=60, startDelay=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(groupId=[503], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.any_one():
            return 스폰_5_SE(self.ctx)
        if self.user_value(key='Battle_3_SpawnStart', value=0):
            return 대기(self.ctx)


class 스폰_5_SE(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 스폰_5(self.ctx)


class 스폰_5(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[504], isStart=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.score_board_remove()

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_SpawnStart', value=0):
            return 대기(self.ctx)


initial_state = 대기
