""" trigger/02020063_bf/battle_1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='Battle_1_Clear', value=0)
        self.start_combine_spawn(groupId=[500], isStart=False)
        self.start_combine_spawn(groupId=[501], isStart=False)
        self.start_combine_spawn(groupId=[502], isStart=False)
        self.start_combine_spawn(groupId=[503], isStart=False)
        self.start_combine_spawn(groupId=[504], isStart=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml') # 웨이브 구간별, or 조건으로 타이머 설정, 개별 30초 정도 설정
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')
        self.reset_timer(timerId='3')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_SpawnStart', value=1):
            return 스폰_1_SE(self.ctx)


# 시작
class 스폰_1_SE(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.score_board_create(type='ShadowGauge', maxScore=800) # <ShadowExpedition 기능을 대체함>
        self.start_combine_spawn(groupId=[500], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 스폰_1(self.ctx)


class 스폰_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020063_BF__BATTLE_1__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 스폰_1_추가대사1(self.ctx)


class 스폰_1_추가대사1(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020063_BF__BATTLE_1__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 스폰_1_추가대사2(self.ctx)


class 스폰_1_추가대사2(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020063_BF__BATTLE_1__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 스폰_2_SE(self.ctx)


class 스폰_2_SE(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 스폰_2(self.ctx)


class 스폰_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=990, startDelay=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(groupId=[501], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.any_one():
            return 스폰_3_SE(self.ctx)
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)


class 스폰_3_SE(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 스폰_3(self.ctx)


class 스폰_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=990, startDelay=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(groupId=[502], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.any_one():
            return 스폰_4_SE(self.ctx)
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)


class 스폰_4_SE(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 스폰_4(self.ctx)


class 스폰_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=990, startDelay=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(groupId=[503], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.any_one():
            return 스폰_5_SE(self.ctx)
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)


class 스폰_5_SE(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 스폰_5(self.ctx)


class 스폰_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(groupId=[504], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.score_board_compare(operator='GreaterEqual', score=800):
            return 포탑페이즈(self.ctx)
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)


class 포탑페이즈(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[500], isStart=False)
        self.start_combine_spawn(groupId=[501], isStart=False)
        self.start_combine_spawn(groupId=[502], isStart=False)
        self.start_combine_spawn(groupId=[503], isStart=False)
        self.start_combine_spawn(groupId=[504], isStart=False)
        self.set_user_value(triggerId=99990001, key='Battle_1_Clear', value=1) # 1phase 끝
        self.score_board_remove()

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_SpawnStart', value=0):
            return 대기(self.ctx)


initial_state = 대기
