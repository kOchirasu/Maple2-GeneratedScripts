""" trigger/02020019_bf/02020019_battle.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_user_value(triggerId=99990004, key='TimerReset', value=0)
        self.set_user_value(key='Success', value=0)
        self.set_user_value(triggerId=99990001, key='End', value=0)
        self.set_user_value(triggerId=99990003, key='5Phase', value=0)
        self.debug_string(feature='Develop', value='이건 Develop 환경에서 나오는 스트링 입니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='battlesetting', value=1):
            return 전투_1라운드세팅(self.ctx)


class 전투_1라운드세팅(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_reset_time(seconds=300)
        self.show_round_ui(round=1, duration=3000)
        self.set_event_ui(type=0, arg2='1,5')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_B', duration=4800)
        self.side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__0$', voice='ko/Npc/00002116')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투_1라운드시작(self.ctx)


class 전투_1라운드시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201]):
            return 전투_1라운드종료(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_1라운드종료(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=24093001)
        self.destroy_monster(spawnIds=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투_2라운드세팅(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_2라운드세팅(trigger_api.Trigger):
    def on_enter(self):
        self.show_round_ui(round=2, duration=3000)
        self.set_event_ui(type=0, arg2='2,5')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_B', duration=4800)
        self.side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__1$', voice='ko/Npc/00002121')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투_2라운드시작(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_2라운드시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[211], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[211]):
            return 전투_2라운드종료(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_2라운드종료(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=24093002)
        self.destroy_monster(spawnIds=[211])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투_3라운드세팅(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_3라운드세팅(trigger_api.Trigger):
    def on_enter(self):
        self.show_round_ui(round=3, duration=3000)
        self.set_event_ui(type=0, arg2='3,5')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_B', duration=4800)
        self.side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__2$', voice='ko/Npc/00002241')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투_3라운드시작(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_3라운드시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[221,222,223,224,225,226,227], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=221, isRelative=True):
            return 전투_3라운드버프(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_3라운드버프(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=24100001, illust='Neirin_serious', duration=5000, script='$02020019_BF__02020019_battle__3$', voice='ko/Npc/00002117')
        self.add_buff(boxIds=[221], skillId=49219001, level=1, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[221,222,223,224,225,226,227]):
            return 전투_3라운드종료(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_3라운드종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[221,222,223,224,225,226,227])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투_4라운드세팅(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_4라운드세팅(trigger_api.Trigger):
    def on_enter(self):
        self.show_round_ui(round=4, duration=3000)
        self.set_event_ui(type=0, arg2='4,5')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_B', duration=4800)
        self.side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__4$', voice='ko/Npc/00002242')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투_4라운드시작(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_4라운드시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[231,232,233,234,235,236,237], animationEffect=True)
        self.side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__5$', voice='ko/Npc/00002243')
        self.set_ai_extra_data(key='Autofire', value=1) # <대포 쏘기 시작 AI에 신호쏴주기>

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=231, isRelative=True):
            return 전투_4라운드버프(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_4라운드버프(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=24100001, illust='Neirin_serious', duration=5000, script='$02020019_BF__02020019_battle__6$', voice='ko/Npc/00002118')
        self.add_buff(boxIds=[231], skillId=49219001, level=1, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[231,232,233,234,235,236,237]):
            return 전투_4라운드종료(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_4라운드종료(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=24093003)
        self.destroy_monster(spawnIds=[231,232,233,234,235,236,237])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투_5라운드세팅(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_5라운드세팅(trigger_api.Trigger):
    def on_enter(self):
        self.show_round_ui(round=5, duration=3000)
        self.set_event_ui(type=0, arg2='5,5')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_B', duration=4800)
        self.side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__7$', voice='ko/Npc/00002122')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=99990003, key='5Phase', value=1)
            return 전투_5라운드시작(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_5라운드시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[241,242,243,244,245,246,247,248], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=241, isRelative=True):
            return 전투_5라운드버프(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=242, isRelative=True):
            return 전투_5라운드버프(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_5라운드버프(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=24100001, illust='Neirin_serious', duration=5000, script='$02020019_BF__02020019_battle__8$', voice='ko/Npc/00002119')
        self.add_buff(boxIds=[241], skillId=49219001, level=1, isPlayer=True)
        self.add_buff(boxIds=[242], skillId=49219001, level=1, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of(feature='FameChallengeBuff_01'):
            self.dungeon_mission_complete(missionId=24093004)
            self.dungeon_mission_complete(missionId=24093005)
            return 전투_종료(self.ctx)
        if self.all_of(feature='FameChallengeBuff_02'):
            self.dungeon_mission_complete(missionId=24093004)
            self.dungeon_mission_complete(missionId=24093006)
            return 전투_종료(self.ctx)
        if self.all_of(feature='FameChallengeBuff_03'):
            self.dungeon_mission_complete(missionId=24093004)
            self.dungeon_mission_complete(missionId=24093007)
            return 전투_종료(self.ctx)
        if self.monster_dead(boxIds=[241,242,243,244,245,246,247,248]):
            self.dungeon_mission_complete(missionId=24093004)
            return 전투_종료(self.ctx)
        if not self.user_detected(boxIds=[901]):
            return 전투_종료(self.ctx)
        if self.dungeon_check_play_time(playSeconds=300):
            return 전투_종료(self.ctx)


class 전투_종료(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        self.set_ai_extra_data(key='Autofire', value=0) # <대포 쏘기 중지 AI에 신호쏴주기>
        self.set_event_ui(type=0, arg2='0,0')
        self.init_npc_rotation(spawnIds=[102,103])
        self.destroy_monster(spawnIds=[201])
        self.destroy_monster(spawnIds=[211])
        self.destroy_monster(spawnIds=[221,222,223,224,225,226,227])
        self.destroy_monster(spawnIds=[231,232,233,234,235,236,237])
        self.destroy_monster(spawnIds=[241,242,243,244,245,246,247,248]) # <네이린이랑 대포가 NPC이기 때문에 선택적으로 소멸시킴>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료신호(self.ctx)


class 종료신호(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='End', value=1)


initial_state = 대기
