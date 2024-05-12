""" trigger/83000003_colosseum/round7.xml """
import trigger_api


# 7라운드 구르는천둥
class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=11000, enable=False)
        self.set_sound(triggerId=11001, enable=False)
        self.set_sound(triggerId=12000, enable=False)
        self.set_sound(triggerId=12001, enable=False)
        self.set_sound(triggerId=13000, enable=False)
        self.set_sound(triggerId=13001, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound7', value=1):
            return 시작딜레이(self.ctx)


class 시작딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라운드조건체크(self.ctx)


class 라운드조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_round_require(round=7):
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND7__0$', duration=5000)
            # self.set_event_ui(type=1, arg2='승리하셨습니다. 다음 전투에서 승리한 더 강한 도전자들을 만납니다. 긴장하세요.', arg3='3000')
            return 라운드대기(self.ctx)
        if self.true():
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND7__1$', duration=3000)
            self.debug_string(string='던전 요구 아이템 점수를 달성 못해 실패 처리 됩니다.')
            return FailRound(self.ctx)


class 라운드대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=11000, enable=True)
        self.set_sound(triggerId=11001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.side_npc_talk(type='cutin', illust='RollingThunder_normal', duration=3000)
            self.show_round_ui(round=7, duration=3000)
            return 몬스터스폰대기(self.ctx)


class 몬스터스폰대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터스폰(self.ctx)


class 몬스터스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.add_buff(boxIds=[107], skillId=69000501, level=1, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$83000002_COLOSSEUM__ROUND7__2$', count=3, soundType=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 전투시작(self.ctx)


# <state name="카운트2">
# <onEnter>
# <action name="이벤트UI를설정한다" arg1="1" arg2="2" arg3="1000" />
# </onEnter>
# <condition name="WaitTick" waitTick="1000" >
# <transition state="카운트3"/>
# </condition>
# </state>
# <state name="카운트3">
# <onEnter>
# <action name="이벤트UI를설정한다" arg1="1" arg2="1" arg3="1000" />
# </onEnter>
# <condition name="WaitTick" waitTick="2000" >
# <transition state="전투시작"/>
# </condition>
# </state>
class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.lock_my_pc(isLock=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 스폰대사(self.ctx)


class 스폰대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=107, msg='$83000002_COLOSSEUM__ROUND7__3$', duration=3000)
        self.set_timer(timerId='LimitTimer', seconds=120, startDelay=1)
        self.set_npc_duel_hp_bar(isOpen=True, spawnId=[107], durationTick=120000, npcHpStep=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[107]):
            self.add_balloon_talk(spawnId=107, msg='$83000002_COLOSSEUM__ROUND7__4$', duration=3000)
            self.set_npc_duel_hp_bar(isOpen=False, spawnId=[107])
            return ClearRoundDelay(self.ctx)
        if self.time_expired(timerId='LimitTimer'):
            # self.set_event_ui(type=1, arg2='경기시간이 경과했습니다. 도전에 실패 하였습니다. 전투를 종료합니다.', arg3='3000')
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND7__5$', duration=3000)
            self.destroy_monster(spawnIds=[107])
            self.set_npc_duel_hp_bar(isOpen=False, spawnId=[107])
            return FailRoundDelay(self.ctx)
        if self.user_detected(boxIds=[902]):
            # self.set_event_ui(type=1, arg2='경기장을 이탈했습니다. 전투가 종료됩니다. 다시 도전해 주세요.', arg3='3000')
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND7__6$', duration=3000)
            self.destroy_monster(spawnIds=[107])
            self.set_npc_duel_hp_bar(isOpen=False, spawnId=[107])
            return FailRoundDelay(self.ctx)
        if not self.user_detected(boxIds=[904]):
            # self.set_event_ui(type=1, arg2='패배했습니다. 전투가 종료됩니다.', arg3='3000')
            self.side_npc_talk(type='talk', npcId=11004288, illust='nagi_switchon', script='$83000002_COLOSSEUM__ROUND7__7$', duration=3000)
            self.destroy_monster(spawnIds=[107])
            self.set_npc_duel_hp_bar(isOpen=False, spawnId=[107])
            return FailRoundDelay(self.ctx)


class ClearRoundDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.lock_my_pc(isLock=True)
        self.set_sound(triggerId=12000, enable=True)
        self.set_sound(triggerId=12001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.add_buff(boxIds=[904], skillId=69000503, level=1, isPlayer=False, isSkillSet=False)
            self.set_event_ui(type=3, arg2='$83000002_COLOSSEUM__ROUND7__8$', arg3='3000')
            return ClearRound(self.ctx)


class FailRoundDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=13000, enable=True)
        self.set_sound(triggerId=13001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=5, arg2='$83000002_COLOSSEUM__ROUND7__9$', arg3='3000')
            return FailRound(self.ctx)


class ClearRound(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=7, arg2='SUCCESS', arg3='3000')
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user_to_pos(pos=[300,-225,1500], rot=[0,0,270])
            # self.add_buff(boxIds=[904], skillId=69000505, level=1, isPlayer=False, isSkillSet=False)
            self.side_npc_talk(type='talk', npcId=11004285, illust='Queencbean_Normal', script='$83000002_COLOSSEUM__ROUND7__10$', duration=3000)
            self.set_user_value(triggerId=900001, key='StartRound7', value=2)
            return 이동대기(self.ctx)


class 이동대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.move_user_path(patrolName='MS2PatrolData_01')
            return 대기(self.ctx)


class FailRound(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=900001, key='StartRound7', value=3)
            return 대기(self.ctx)


initial_state = 대기
