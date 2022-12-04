""" trigger/02020063_bf/battle_3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='Battle_3_Clear', value=0)
        self.start_combine_spawn(groupId=[10000600], isStart=False)
        self.start_combine_spawn(groupId=[10000604], isStart=False)
        self.set_user_value(triggerId=99990011, key='Battle3_TurretSpawn_1', value=0)
        self.set_user_value(triggerId=99990012, key='Battle3_TurretSpawn_2', value=0)
        self.set_user_value(triggerId=99990013, key='Battle3_TurretSpawn_3', value=0)
        self.set_user_value(triggerId=99990014, key='Battle3_TurretSpawn_4', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Start', value=1):
            return 보스_추가대사(self.ctx)


class 보스_추가대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_event_ui(type=1, arg2='$02020063_BF__BATTLE_3__0$', arg3='5000')
            return 보스소환(self.ctx)


class 보스소환(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[921], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Start', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[921]):
            return 보스군단_클리어(self.ctx)
        if self.all_of():
            return 보스_무적페이즈(self.ctx)


class 보스_무적페이즈(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020063_BF__BATTLE_3__1$', arg3='5000')
        self.set_user_value(triggerId=99990011, key='Battle3_TurretSpawn_1', value=1)
        self.set_user_value(triggerId=99990012, key='Battle3_TurretSpawn_2', value=1)
        self.set_user_value(triggerId=99990013, key='Battle3_TurretSpawn_3', value=1)
        self.set_user_value(triggerId=99990014, key='Battle3_TurretSpawn_4', value=1)
        # <action name="SetUserValue" triggerID="99990006" key="Battle_3_SpawnStart" value="1" />
        self.start_combine_spawn(groupId=[10000600], isStart=True)
        self.start_combine_spawn(groupId=[10000604], isStart=True)
        self.set_user_value(triggerId=99990006, key='Battle_3_SpawnStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Start', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[921]):
            return 보스군단_클리어(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 보스_추가대사1(self.ctx)


class 보스_추가대사1(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020063_BF__BATTLE_3__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Start', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[921]):
            return 보스군단_클리어(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 보스_추가대사2(self.ctx)


class 보스_추가대사2(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020063_BF__BATTLE_3__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Start', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[921]):
            return 보스군단_클리어(self.ctx)


class 보스군단_클리어(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='Battle_3_Clear', value=1)
        self.set_user_value(triggerId=99990006, key='Battle_3_SpawnStart', value=0)
        self.start_combine_spawn(groupId=[10000600], isStart=False)
        self.start_combine_spawn(groupId=[10000604], isStart=False)
        self.set_user_value(triggerId=99990011, key='Battle3_TurretSpawn_1', value=0)
        self.set_user_value(triggerId=99990012, key='Battle3_TurretSpawn_2', value=0)
        self.set_user_value(triggerId=99990013, key='Battle3_TurretSpawn_3', value=0)
        self.set_user_value(triggerId=99990014, key='Battle3_TurretSpawn_4', value=0)


initial_state = 대기
