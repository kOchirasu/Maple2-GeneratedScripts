""" trigger/02020062_bf/battle_3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990001, key='BossClear', value=0)
        self.set_user_value(triggerId=99990013, key='BossClear', value=0)
        self.set_user_value(triggerId=99990013, key='BombPhase', value=0)
        self.set_user_value(triggerId=99990009, key='BossObjectStart', value=0)
        self.set_user_value(triggerId=99990010, key='BossObjectStart', value=0)
        self.set_user_value(triggerId=99990011, key='BossObjectStart', value=0)
        self.reset_timer(timerId='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=1):
            return 보스_추가대사(self.ctx)


class 보스_추가대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020062_BF__BATTLE_3__0$')
            return 보스랜덤픽(self.ctx)


class 보스랜덤픽(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[9002], skillId=70002371, level=1, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=17):
            return 보스소환1(self.ctx)
        if self.random_condition(rate=16):
            return 보스소환2(self.ctx)
        if self.random_condition(rate=17):
            return 보스소환3(self.ctx)


class 보스소환1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[921], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[921]):
            return 보스군단_클리어(self.ctx)
        if self.user_value(value=2, key='ObjectStart') and self.npc_detected(boxId=9099, spawnIds=[921]):
            return 보스_무적페이즈(self.ctx)


class 보스소환2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[922], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[922]):
            return 보스군단_클리어(self.ctx)
        if self.user_value(value=2, key='ObjectStart') and self.npc_detected(boxId=9099, spawnIds=[922]):
            return 보스_무적페이즈(self.ctx)


class 보스소환3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[923], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[923]):
            return 보스군단_클리어(self.ctx)
        if self.user_value(value=2, key='ObjectStart') and self.npc_detected(boxId=9099, spawnIds=[923]):
            return 보스_무적페이즈(self.ctx)


class 보스_무적페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020062_BF__BATTLE_3__2$', arg3='5000')
        self.create_monster(spawnIds=[711,712,713], animationEffect=False)
        self.create_monster(spawnIds=[811,812,821,822,831,832], animationEffect=False)
        self.set_user_value(triggerId=99990009, key='BossObjectStart', value=1)
        self.set_user_value(triggerId=99990010, key='BossObjectStart', value=1)
        self.set_user_value(triggerId=99990011, key='BossObjectStart', value=1)
        self.set_user_value(triggerId=99990013, key='BombPhase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[921]) and self.monster_dead(boxIds=[922]) and self.monster_dead(boxIds=[923]):
            return 보스군단_클리어(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 보스_추가대사1(self.ctx)


class 보스_추가대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020062_BF__BATTLE_3__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[921]) and self.monster_dead(boxIds=[922]) and self.monster_dead(boxIds=[923]):
            return 보스군단_클리어(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 보스_추가대사2(self.ctx)


class 보스_추가대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020062_BF__BATTLE_3__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossPhase', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[921]) and self.monster_dead(boxIds=[922]) and self.monster_dead(boxIds=[923]):
            return 보스군단_클리어(self.ctx)


class 보스군단_클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990001, key='BossClear', value=1)
        self.set_user_value(triggerId=99990013, key='BossClear', value=1)
        self.set_user_value(triggerId=99990013, key='BombPhase', value=0)
        self.set_user_value(triggerId=99990009, key='BossObjectStart', value=0)
        self.set_user_value(triggerId=99990010, key='BossObjectStart', value=0)
        self.set_user_value(triggerId=99990011, key='BossObjectStart', value=0)


initial_state = 대기
