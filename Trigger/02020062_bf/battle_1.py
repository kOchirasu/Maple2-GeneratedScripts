""" trigger/02020062_bf/battle_1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='GaugeClear', value=0)
        self.start_combine_spawn(group_id=[490], is_start=False)
        self.start_combine_spawn(group_id=[491], is_start=False)
        self.start_combine_spawn(group_id=[492], is_start=False)
        self.start_combine_spawn(group_id=[493], is_start=False)
        self.start_combine_spawn(group_id=[495], is_start=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart', value=1):
            return 스폰_1_SE(self.ctx)


# 시작
class 스폰_1_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[490], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 스폰_1(self.ctx)


class 스폰_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(type='talk', npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020062_BF__BATTLE_1__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 스폰_1_추가대사1(self.ctx)


class 스폰_1_추가대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(type='talk', npc_id=11003533, illust='Bliche_normal', duration=5000, script='$02020062_BF__BATTLE_1__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 스폰_1_추가대사2(self.ctx)


class 스폰_1_추가대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(type='talk', npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02020062_BF__BATTLE_1__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=120):
            return 스폰_2_SE(self.ctx)
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)


class 스폰_2_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_2(self.ctx)


class 스폰_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[491], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=300):
            return 스폰_3_SE(self.ctx)
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)


class 스폰_3_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_3(self.ctx)


class 스폰_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[492], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=450):
            return 스폰_4_SE(self.ctx)
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)


class 스폰_4_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_4(self.ctx)


class 스폰_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[493], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=600):
            return 스폰_5_SE(self.ctx) # 스폰_5 추가 웨이브 예정
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)


class 스폰_5_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_5(self.ctx)


class 스폰_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[495], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=750):
            return 오브젝트페이즈(self.ctx)
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)


class 오브젝트페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition(type='CloseBossGauge')
        self.start_combine_spawn(group_id=[490], is_start=False)
        self.start_combine_spawn(group_id=[491], is_start=False)
        self.start_combine_spawn(group_id=[492], is_start=False)
        self.start_combine_spawn(group_id=[493], is_start=False)
        self.start_combine_spawn(group_id=[495], is_start=False)
        self.set_user_value(trigger_id=99990001, key='GaugeClear', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart', value=2):
            return 대기(self.ctx)


initial_state = 대기
