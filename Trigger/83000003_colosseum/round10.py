""" trigger/83000003_colosseum/round10.xml """
import trigger_api
from System.Numerics import Vector3


# 10라운드 미카
class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=11000)
        self.set_sound(trigger_id=11001)
        self.set_sound(trigger_id=12000)
        self.set_sound(trigger_id=12001)
        self.set_sound(trigger_id=13000)
        self.set_sound(trigger_id=13001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound10') >= 1:
            return 시작딜레이(self.ctx)


class 시작딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라운드조건체크(self.ctx)


class 라운드조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_round() == 10:
            self.side_npc_talk(npc_id=11004288, illust='nagi_normal', script='$83000003_COLOSSEUM__ROUND10__0$', duration=5000)
            # self.set_event_ui(type=1, arg2='전투에서 승리하셨습니다. 이제 마지막 전투입니다. 끝까지 힘내십시오.', arg3='3000')
            return 라운드대기(self.ctx)
        self.side_npc_talk(npc_id=11004288, illust='nagi_switchon', script='$83000003_COLOSSEUM__ROUND10__1$', duration=3000)
        self.debug_string(value='던전 요구 아이템 점수를 달성 못해 실패 처리 됩니다.')
        return FailRound(self.ctx)


class 라운드대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=11000, enable=True)
        self.set_sound(trigger_id=11001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.side_npc_cutin(illust='Cutin_Mika_01', duration=3000)
            self.show_round_ui(round=10, duration=3000)
            return 몬스터스폰대기(self.ctx)


class 몬스터스폰대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터스폰(self.ctx)


class 몬스터스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.add_buff(box_ids=[110], skill_id=69000501, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$83000003_COLOSSEUM__ROUND10__2$', count=3, sound_type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 전투시작(self.ctx)


"""
class 카운트2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카운트3(self.ctx)
"""

"""
class 카운트3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전투시작(self.ctx)
"""

class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 기믹더미소환(self.ctx)


class 기믹더미소환(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[10000], auto_target=False)
            return 스폰대사(self.ctx)
        if self.random_condition(weight=50.0):
            self.spawn_monster(spawn_ids=[10001], auto_target=False)
            return 스폰대사(self.ctx)


class 스폰대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=110, msg='$83000003_COLOSSEUM__ROUND10__3$', duration=3000)
        self.set_timer(timer_id='LimitTimer', seconds=180, start_delay=1)
        self.set_npc_duel_hp_bar(is_open=True, spawn_id=110, duration_tick=180000, npc_hp_step=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[110]):
            self.add_balloon_talk(spawn_id=110, msg='$83000003_COLOSSEUM__ROUND10__4$', duration=3000)
            self.set_npc_duel_hp_bar(spawn_id=110)
            self.destroy_monster(spawn_ids=[10000])
            self.destroy_monster(spawn_ids=[10001])
            return ClearRoundDelay(self.ctx)
        if self.time_expired(timer_id='LimitTimer'):
            # self.set_event_ui(type=1, arg2='경기시간이 경과했습니다. 도전에 실패 하였습니다. 전투를 종료합니다.', arg3='3000')
            self.side_npc_talk(npc_id=11004288, illust='nagi_switchon', script='$83000003_COLOSSEUM__ROUND10__5$', duration=3000)
            self.destroy_monster(spawn_ids=[110])
            self.set_npc_duel_hp_bar(spawn_id=110)
            self.destroy_monster(spawn_ids=[10000])
            self.destroy_monster(spawn_ids=[10001])
            return FailRoundDelay(self.ctx)
        if self.user_detected(box_ids=[902]):
            # self.set_event_ui(type=1, arg2='경기장을 이탈했습니다. 전투가 종료됩니다. 다시 도전해 주세요.', arg3='3000')
            self.side_npc_talk(npc_id=11004288, illust='nagi_switchon', script='$83000003_COLOSSEUM__ROUND10__6$', duration=3000)
            self.destroy_monster(spawn_ids=[110])
            self.set_npc_duel_hp_bar(spawn_id=110)
            self.destroy_monster(spawn_ids=[10000])
            self.destroy_monster(spawn_ids=[10001])
            return FailRoundDelay(self.ctx)
        if not self.user_detected(box_ids=[904]):
            # self.set_event_ui(type=1, arg2='패배했습니다. 전투가 종료됩니다.', arg3='3000')
            self.side_npc_talk(npc_id=11004288, illust='nagi_switchon', script='$83000003_COLOSSEUM__ROUND10__7$', duration=3000)
            self.destroy_monster(spawn_ids=[110])
            self.set_npc_duel_hp_bar(spawn_id=110)
            self.destroy_monster(spawn_ids=[10000])
            self.destroy_monster(spawn_ids=[10001])
            return FailRoundDelay(self.ctx)


class ClearRoundDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.lock_my_pc(is_lock=True)
        self.set_sound(trigger_id=12000, enable=True)
        self.set_sound(trigger_id=12001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.add_buff(box_ids=[904], skill_id=69000503, level=1, is_player=False, is_skill_set=False)
            self.set_event_ui(type=3, arg2='$83000003_COLOSSEUM__ROUND10__8$', arg3='3000')
            return ClearRound(self.ctx)


class FailRoundDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=13000, enable=True)
        self.set_sound(trigger_id=13001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=5, arg2='$83000003_COLOSSEUM__ROUND10__9$', arg3='3000')
            return FailRound(self.ctx)


class ClearRound(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=7, arg2='SUCCESS', arg3='3000')
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.move_user_to_pos(pos=Vector3(300,-225,1500), rot=Vector3(0,0,270))
            # self.move_user_to_pos(pos=Vector3(300,-225,1500), rot=Vector3(0,0,270))
            # self.add_buff(box_ids=[904], skill_id=69000505, level=1, is_player=False, is_skill_set=False)
            self.side_npc_talk(npc_id=11004288, illust='nagi_normal', script='$83000003_COLOSSEUM__ROUND10__10$', duration=3000)
            self.set_user_value(trigger_id=900001, key='StartRound10', value=2)
            return 이동대기(self.ctx)


class 이동대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # self.move_user_path(patrol_name='MS2PatrolData_01')
            return 대기(self.ctx)


class FailRound(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=900001, key='StartRound10', value=3)
            return 대기(self.ctx)


initial_state = 대기
