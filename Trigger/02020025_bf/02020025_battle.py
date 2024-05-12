""" trigger/02020025_bf/02020025_battle.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Success', value=0)
        self.set_user_value(triggerId=99999001, key='End', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='battlesetting', value=1):
            return 전투_시작(self.ctx)


class 전투_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_reset_time(seconds=300)
        self.set_npc_duel_hp_bar(isOpen=True, spawnId=[201], durationTick=300000, npcHpStep=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_check_play_time(playSeconds=180, operator='LessEqual') and self.monster_dead(boxIds=[201]):
            # <한국용 컨디션체크>
            self.dungeon_mission_complete(missionId=24092005)
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=70, operator='LessEqual') and self.monster_dead(boxIds=[201]):
            # <중국용 컨디션체크>
            self.dungeon_mission_complete(missionId=24092006)
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=270, operator='LessEqual') and self.monster_dead(boxIds=[201]):
            # <NA용 컨디션체크>
            self.dungeon_mission_complete(missionId=24092010)
            return 전투_종료(self.ctx)
        if self.monster_dead(boxIds=[201]):
            # <5분내에 처치>
            return 전투_종료(self.ctx)
        if not self.user_detected(boxIds=[902]):
            # <pc 사망>
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            # <5분 다 지날 경우>
            return 전투_종료(self.ctx)


class 전투_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_set_end_time()
        self.destroy_monster(spawnIds=[-1])
        # self.add_buff(boxIds=[902], skillId=72000050, level=1)
        # self.set_npc_emotion_loop(spawnId=201, sequenceName='Attack_Idle_A', duration=60000)
        self.side_npc_talk(npcId=24110001, illust='Conder_normal', duration=4000, script='$02020025_BF__02020025_battle__0$', voice='ko/Npc/00002258')
        self.set_npc_duel_hp_bar(isOpen=False, spawnId=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료신호(self.ctx)


class 종료신호(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99999001, key='End', value=1)


initial_state = 대기
