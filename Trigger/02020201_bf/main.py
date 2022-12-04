""" trigger/02020201_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=103, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 페이카등장(self.ctx)


class 페이카등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False) # 페이카 등장
        self.side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020201_BF__MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 제단파괴(self.ctx)


class 제단파괴(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020201_BF__MAIN__1$')
        self.add_balloon_talk(spawnId=101, msg='$02020201_BF__MAIN__2$', duration=3000, delayTick=0)
        self.destroy_monster(spawnIds=[201,202,203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(type='trigger', achieve='PaikaKritiasClear')
        self.dungeon_clear()
        self.set_portal(portalId=103, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
