""" trigger/02020061_bf/battle_3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='BossClear', value=0)
        self.set_user_value(trigger_id=99990013, key='BossClear', value=0)
        self.set_user_value(trigger_id=99990013, key='BombPhase', value=0)
        self.set_user_value(trigger_id=99990009, key='BossObjectStart', value=0)
        self.set_user_value(trigger_id=99990010, key='BossObjectStart', value=0)
        self.set_user_value(trigger_id=99990011, key='BossObjectStart', value=0)
        self.set_user_value(trigger_id=99990012, key='BossObjectStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=1):
            return 보스_추가대사(self.ctx)


class 보스_추가대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.side_npc_talk(type='talk', npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020061_BF__BATTLE_3__0$')
            return 보스랜덤픽(self.ctx)


class 보스랜덤픽(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9002], skill_id=70002371, level=1, is_skill_set=False)
        # <유저 웨폰 오브젝트 떨구기>

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=17):
            return 보스소환1(self.ctx)
        if self.random_condition(weight=16):
            return 보스소환2(self.ctx)
        if self.random_condition(weight=17):
            return 보스소환3(self.ctx)
        if self.random_condition(weight=16):
            return 보스소환4(self.ctx)
        if self.random_condition(weight=17):
            return 보스소환5(self.ctx)
        if self.random_condition(weight=17):
            return 보스소환6(self.ctx)


class 보스소환1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[921], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[921]):
            return 보스군단_클리어(self.ctx)
        if self.user_value(key='ObjectStart', value=2) and self.npc_detected(box_id=9099, spawn_ids=[921]):
            return 보스_무적페이즈(self.ctx)


class 보스소환2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[922], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[922]):
            return 보스군단_클리어(self.ctx)
        if self.user_value(key='ObjectStart', value=2) and self.npc_detected(box_id=9099, spawn_ids=[922]):
            return 보스_무적페이즈(self.ctx)


class 보스소환3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[923], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[923]):
            return 보스군단_클리어(self.ctx)
        if self.user_value(key='ObjectStart', value=2) and self.npc_detected(box_id=9099, spawn_ids=[923]):
            return 보스_무적페이즈(self.ctx)


class 보스소환4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[924], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[924]):
            return 보스군단_클리어(self.ctx)
        if self.user_value(key='ObjectStart', value=2) and self.npc_detected(box_id=9099, spawn_ids=[924]):
            return 보스_무적페이즈(self.ctx)


class 보스소환5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[925], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[925]):
            return 보스군단_클리어(self.ctx)
        if self.user_value(key='ObjectStart', value=2) and self.npc_detected(box_id=9099, spawn_ids=[925]):
            return 보스_무적페이즈(self.ctx)


class 보스소환6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[926], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[926]):
            return 보스군단_클리어(self.ctx)
        if self.user_value(key='ObjectStart', value=2) and self.npc_detected(box_id=9099, spawn_ids=[926]):
            return 보스_무적페이즈(self.ctx)


class 보스_무적페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020061_BF__BATTLE_3__1$', arg3='5000')
        self.spawn_monster(spawn_ids=[711,712,713,714], auto_target=False)
        self.set_user_value(trigger_id=99990009, key='BossObjectStart', value=1)
        self.set_user_value(trigger_id=99990010, key='BossObjectStart', value=1)
        self.set_user_value(trigger_id=99990011, key='BossObjectStart', value=1)
        self.set_user_value(trigger_id=99990012, key='BossObjectStart', value=1)
        self.set_user_value(trigger_id=99990013, key='BombPhase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]) and self.monster_dead(spawn_ids=[924]) and self.monster_dead(spawn_ids=[925]) and self.monster_dead(spawn_ids=[926]):
            return 보스군단_클리어(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 보스_무적페이즈_대사1(self.ctx)


class 보스_무적페이즈_대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(type='talk', npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02020061_BF__BATTLE_3__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]) and self.monster_dead(spawn_ids=[924]) and self.monster_dead(spawn_ids=[925]) and self.monster_dead(spawn_ids=[926]):
            return 보스군단_클리어(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 보스_무적페이즈_대사2(self.ctx)


class 보스_무적페이즈_대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(type='talk', npc_id=11003533, illust='Bliche_normal', duration=5000, script='$02020061_BF__BATTLE_3__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]) and self.monster_dead(spawn_ids=[924]) and self.monster_dead(spawn_ids=[925]) and self.monster_dead(spawn_ids=[926]):
            return 보스군단_클리어(self.ctx)


class 보스군단_클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='BossClear', value=1)
        self.set_user_value(trigger_id=99990013, key='BossClear', value=1)
        self.set_user_value(trigger_id=99990013, key='BombPhase', value=0)
        self.set_user_value(trigger_id=99990009, key='BossObjectStart', value=0)
        self.set_user_value(trigger_id=99990010, key='BossObjectStart', value=0)
        self.set_user_value(trigger_id=99990011, key='BossObjectStart', value=0)
        self.set_user_value(trigger_id=99990012, key='BossObjectStart', value=0)


initial_state = 대기
