""" trigger/83000003_colosseum/round12.xml """
import trigger_api


# 9라운드 바사라 첸
class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=11000, enable=False)
        self.set_sound(triggerId=11001, enable=False)
        self.set_sound(triggerId=12000, enable=False)
        self.set_sound(triggerId=12001, enable=False)
        self.set_sound(triggerId=13000, enable=False)
        self.set_sound(triggerId=13001, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound12', value=1):
            return 시작딜레이(self.ctx)


class 시작딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라운드조건체크(self.ctx)


class 라운드조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_round_require(round=12):
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_normal', script='$83000003_COLOSSEUM__ROUND12__0$', duration=5000)
            return 라운드대기(self.ctx)
        if self.true():
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000003_COLOSSEUM__ROUND12__1$', duration=3000)
            self.debug_string(string='던전 요구 아이템 점수를 달성 못해 실패 처리 됩니다.')
            return FailRound(self.ctx)


class 라운드대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=11000, enable=True)
        self.set_sound(triggerId=11001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.side_npc_talk(type='cutin', illust='Madria_normal', duration=3000)
            self.show_round_ui(round=12, duration=3000)
            return 몬스터스폰대기(self.ctx)


class 몬스터스폰대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터스폰(self.ctx)


class 몬스터스폰(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.add_buff(boxIds=[112], skillId=69000501, level=1, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self):
        self.show_count_ui(text='$83000003_COLOSSEUM__ROUND12__2$', count=3, soundType=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self):
        self.lock_my_pc(isLock=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 스폰대사(self.ctx)


class 스폰대사(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=112, msg='$83000003_COLOSSEUM__ROUND12__3$', duration=3000)
        self.set_timer(timerId='LimitTimer', seconds=180, startDelay=1)
        self.set_npc_duel_hp_bar(isOpen=True, spawnId=[112], durationTick=180000, npcHpStep=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[112]):
            self.add_balloon_talk(spawnId=112, msg='$83000003_COLOSSEUM__ROUND12__4$', duration=3000)
            self.set_npc_duel_hp_bar(isOpen=False, spawnId=[112])
            self.destroy_monster(spawnIds=[10000])
            self.destroy_monster(spawnIds=[10001])
            return ClearRoundDelay(self.ctx)
        if self.time_expired(timerId='LimitTimer'):
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000003_COLOSSEUM__ROUND12__5$', duration=3000)
            self.destroy_monster(spawnIds=[112])
            self.set_npc_duel_hp_bar(isOpen=False, spawnId=[112])
            self.destroy_monster(spawnIds=[10000])
            self.destroy_monster(spawnIds=[10001])
            return FailRoundDelay(self.ctx)
        if self.user_detected(boxIds=[902]):
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000003_COLOSSEUM__ROUND12__6$', duration=3000)
            self.destroy_monster(spawnIds=[112])
            self.set_npc_duel_hp_bar(isOpen=False, spawnId=[112])
            self.destroy_monster(spawnIds=[10000])
            self.destroy_monster(spawnIds=[10001])
            return FailRoundDelay(self.ctx)
        if not self.user_detected(boxIds=[904]):
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000003_COLOSSEUM__ROUND12__7$', duration=3000)
            self.destroy_monster(spawnIds=[112])
            self.set_npc_duel_hp_bar(isOpen=False, spawnId=[112])
            self.destroy_monster(spawnIds=[10000])
            self.destroy_monster(spawnIds=[10001])
            return FailRoundDelay(self.ctx)


class ClearRoundDelay(trigger_api.Trigger):
    def on_enter(self):
        self.lock_my_pc(isLock=True)
        self.set_sound(triggerId=12000, enable=True)
        self.set_sound(triggerId=12001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.add_buff(boxIds=[904], skillId=69000503, level=1, isPlayer=False, isSkillSet=False)
            self.set_event_ui(type=3, arg2='$83000003_COLOSSEUM__ROUND12__8$', arg3='3000')
            return ClearRound(self.ctx)


class FailRoundDelay(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=13000, enable=True)
        self.set_sound(triggerId=13001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=5, arg2='$83000003_COLOSSEUM__ROUND12__9$', arg3='3000')
            return FailRound(self.ctx)


class ClearRound(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user_to_pos(pos=[300,-225,1500], rot=[0,0,270])
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_normal', script='$83000003_COLOSSEUM__ROUND12__10$', duration=3000)
            self.set_user_value(triggerId=900001, key='StartRound12', value=2)
            return 이동대기(self.ctx)


class 이동대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.move_user_path(patrolName='MS2PatrolData_01')
            return 대기(self.ctx)


class FailRound(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=900001, key='StartRound12', value=3)
            return 대기(self.ctx)


initial_state = 대기
