""" trigger/02020021_bf/battle.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[-1])
        self.set_ai_extra_data(key='Start', value=0)
        self.set_user_value(triggerId=99990003, key='TimerReset', value=0)
        self.set_user_value(triggerId=99990003, key='SpecialTimerReset', value=0)
        self.set_user_value(key='Success', value=0)
        self.set_user_value(triggerId=99990001, key='End', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='battlesetting', value=1):
            return 전투_1라운드(self.ctx)


class 전투_1라운드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_reset_time(seconds=300)
        self.set_npc_duel_hp_bar(isOpen=True, spawnId=[201], durationTick=300000, npcHpStep=100)
        self.set_ai_extra_data(key='Phase', value=1)
        # <샤텐 AI 제어>

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=80, spawnId=201, isRelative=True):
            return 전투_2라운드(self.ctx)


class 전투_2라운드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=23200085, illust='Schatten_normal', duration=4000, script='$02020021_BF__battle__0$', voice='ko/Npc/00002245')
        self.create_monster(spawnIds=[301], animationEffect=False)
        # <독바닥 깔기 몬스터 생성>

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=60, spawnId=201, isRelative=True):
            return 전투_3라운드(self.ctx)


class 전투_3라운드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=23200085, illust='Schatten_normal', duration=4000, script='$02020021_BF__battle__1$', voice='ko/Npc/00002246')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투_3라운드_시작(self.ctx)


class 전투_3라운드_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[301])
        self.create_monster(spawnIds=[302], animationEffect=False)
        # <독바닥 깔기 제어>
        self.set_ai_extra_data(key='Phase', value=2)
        # <샤텐 AI 제어>

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=40, spawnId=201, isRelative=True):
            return 전투_4라운드(self.ctx)


class 전투_4라운드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=23200085, illust='Schatten_normal', duration=4000, script='$02020021_BF__battle__2$', voice='ko/Npc/00002247')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투_4라운드_시작(self.ctx)


class 전투_4라운드_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[302])
        self.create_monster(spawnIds=[303], animationEffect=False)
        # <독바닥 깔기 제어>

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_check_play_time(playSeconds=180, operator='LessEqual') and self.monster_dead(boxIds=[201]):
            # <한국용 컨디션체크>
            self.dungeon_mission_complete(missionId=24095005)
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=70, operator='LessEqual') and self.monster_dead(boxIds=[201]):
            # <중국용 컨디션체크>
            self.dungeon_mission_complete(missionId=24095006)
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=270, operator='LessEqual') and self.monster_dead(boxIds=[201]):
            # <NA용 컨디션체크>
            self.dungeon_mission_complete(missionId=24095010)
            return 전투_종료(self.ctx)
        if self.monster_dead(boxIds=[201]):
            return 전투_종료(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_set_end_time()
        self.destroy_monster(spawnIds=[-1])
        # self.add_buff(boxIds=[901], skillId=72000050, level=1)
        # self.destroy_monster(spawnIds=[301,302,303])
        # self.set_npc_emotion_loop(spawnId=201, sequenceName='Attack_Idle_A', duration=60000)
        # self.set_user_value(triggerId=99990003, key='TimerReset', value=1)
        self.set_npc_duel_hp_bar(isOpen=False, spawnId=[201])
        self.side_npc_talk(npcId=23200085, illust='Schatten_normal', duration=4000, script='$02020021_BF__battle__3$', voice='ko/Npc/00002244')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 종료신호(self.ctx)


class 종료신호(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990001, key='End', value=1)


initial_state = 대기
