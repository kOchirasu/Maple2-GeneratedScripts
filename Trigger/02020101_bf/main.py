""" trigger/02020101_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(boxId=1003, skillId=70002151, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1002]):
            return 보스전_시작(self.ctx)


class 보스전_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(type='talk', npcId=23501001, illust='Turned_Yuperia_normal', script='$02020101_BF__MAIN__0$', duration=5670, voice='ko/Npc/00002206')
        self.dungeon_reset_time(seconds=420)
        self.create_monster(spawnIds=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5670):
            return 조건추가(self.ctx)


class 조건추가(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]) and self.dungeon_check_play_time(playSeconds=420, operator='Less'):
            return 보스전_성공(self.ctx)
        if self.dungeon_check_play_time(playSeconds=420, operator='Equal'):
            return 보스전_타임어택실패(self.ctx)
        if self.user_value(key='SkillBreakFail', value=1):
            return 보스전_스킬브레이크실패(self.ctx)


class 보스전_스킬브레이크실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_stop_timer()
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 보스전_리셋세팅(self.ctx)


class 보스전_타임어택실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스전_타임어택실패세팅(self.ctx)


class 보스전_리셋세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[-1])
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.move_user(mapId=2020101, portalId=1, boxId=1002)
        self.remove_buff(boxId=1003, skillId=70002122, isPlayer=True)
        self.remove_buff(boxId=1003, skillId=70002151, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


class 보스전_타임어택실패세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        self.remove_buff(boxId=1003, skillId=70002151, isPlayer=True)


class 보스전_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(missionId=23038005)
        self.dungeon_set_end_time()
        # self.dungeon_close_timer()
        self.side_npc_talk(type='talk', npcId=23501001, illust='Turned_Yuperia_normal', script='$02020101_BF__MAIN__1$', duration=7940, voice='ko/Npc/00002207')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7940):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[-1])
        self.dungeon_clear()
        self.set_achievement(type='trigger', achieve='ClearGreenLapenta')
        self.remove_buff(boxId=1003, skillId=70002151, isPlayer=True)
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
