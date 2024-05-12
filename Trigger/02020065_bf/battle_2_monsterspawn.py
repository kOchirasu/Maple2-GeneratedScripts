""" trigger/02020065_bf/battle_2_monsterspawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='Battle_2_Clear', value=0) # <웨이브 진행용 SetuserValue >
        # combinespawngroup 테이블 참조
        self.start_combine_spawn(group_id=[505], is_start=False)
        self.start_combine_spawn(group_id=[506], is_start=False)
        self.start_combine_spawn(group_id=[507], is_start=False)
        self.start_combine_spawn(group_id=[508], is_start=False)
        self.start_combine_spawn(group_id=[509], is_start=False)
        # 웨이브 구간별 or 조건으로 타이머 설정, 개별 30초 정도 설정
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='2')
        self.reset_timer(timer_id='3')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_SpawnStart') >= 1:
            return 스폰_1_SE(self.ctx)


# 시작
class 스폰_1_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # <ShadowExpedition 기능을 대체함>
        self.score_board_create(max_score=800)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[505], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_SpawnStart') >= 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 스폰_1(self.ctx)


class 스폰_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_SpawnStart') >= 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 스폰_2_SE(self.ctx)


class 스폰_2_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_SpawnStart') >= 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_2(self.ctx)


class 스폰_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=45, start_delay=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[506], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1') or self.score_board_score() >= 150:
            return 스폰_3_SE(self.ctx)
        if self.user_value(key='Battle_2_SpawnStart') >= 0:
            return 대기(self.ctx)


class 스폰_3_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_SpawnStart') >= 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_3(self.ctx)


class 스폰_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=45, start_delay=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[507], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2') or self.score_board_score() >= 300:
            return 스폰_4_SE(self.ctx)
        if self.user_value(key='Battle_2_SpawnStart') >= 0:
            return 대기(self.ctx)


class 스폰_4_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_SpawnStart') >= 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_4(self.ctx)


class 스폰_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=45, start_delay=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[508], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3') or self.score_board_score() >= 450:
            return 스폰_5_SE(self.ctx)
        if self.user_value(key='Battle_2_SpawnStart') >= 0:
            return 대기(self.ctx)


class 스폰_5_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_SpawnStart') >= 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_5(self.ctx)


class 스폰_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[509], is_start=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.score_board_remove()

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_SpawnStart') >= 0:
            return 대기(self.ctx)


initial_state = 대기
