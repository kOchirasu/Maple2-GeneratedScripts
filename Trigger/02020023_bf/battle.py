""" trigger/02020023_bf/battle.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_user_value(triggerId=99990003, key='TimerReset', value=0)
        self.set_user_value(triggerId=99990004, key='SpecialTimerReset', value=0)
        self.set_user_value(key='Success', value=0)
        self.set_user_value(triggerId=99990001, key='End', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='battlesetting', value=1):
            return 전투_시작(self.ctx)


class 전투_시작(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_reset_time(seconds=300)
        self.set_npc_duel_hp_bar(isOpen=True, spawnId=[101], durationTick=300000, npcHpStep=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of(feature='FameChallengeBuff_01'):
            self.dungeon_mission_complete(missionId=24091005)
            return 전투_종료(self.ctx)
        if self.all_of(feature='FameChallengeBuff_02'):
            self.dungeon_mission_complete(missionId=24091006)
            return 전투_종료(self.ctx)
        if self.all_of(feature='FameChallengeBuff_03'):
            self.dungeon_mission_complete(missionId=24091010)
            return 전투_종료(self.ctx)
        if self.monster_dead(boxIds=[101]):
            return 전투_종료(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_종료(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_set_end_time()
        self.destroy_monster(spawnIds=[-1])
        # <action name="버프를걸어준다" arg1="901" arg2="72000050" arg3="1"/>
        self.set_npc_duel_hp_bar(isOpen=False, spawnId=[101], durationTick=300000)
        self.side_npc_talk(npcId=23200083, illust='Bliche_nomal', duration=4000, script='$02020023_BF__battle__0$', voice='ko/Npc/00002062')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료신호(self.ctx)


class 종료신호(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='End', value=1)


initial_state = 대기
