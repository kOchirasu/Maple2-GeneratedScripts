""" trigger/02000533_bf/main2.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[703], jobCode=0):
            return 서브몬스터1(self.ctx)


class 서브몬스터1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[601,602,607,608,609,610], animationEffect=False)
        self.move_npc(spawnId=601, patrolName='MS2PatrolData_5000')
        self.move_npc(spawnId=602, patrolName='MS2PatrolData_5001')
        self.set_npc_emotion_loop(spawnId=607, sequenceName='Sit_Down_A', duration=10000000)
        self.set_npc_emotion_loop(spawnId=608, sequenceName='Sit_Down_A', duration=10000000)
        self.set_npc_emotion_loop(spawnId=610, sequenceName='Bore_A', duration=10000000)
        self.add_balloon_talk(spawnId=601, msg='$02000533_BF__MAIN2__0$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=602, msg='$02000533_BF__MAIN2__1$', duration=3500, delayTick=500)
        self.add_balloon_talk(spawnId=601, msg='$02000533_BF__MAIN2__2$', duration=3500, delayTick=1500)
        self.add_balloon_talk(spawnId=607, msg='$02000533_BF__MAIN2__3$', duration=3500, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 서브몬스터2(self.ctx)


class 서브몬스터2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[601,602,607,608,609,610])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 서브몬스터3(self.ctx)


class 서브몬스터3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[6601,6602,6607,6608,6609,6610], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[6601,6602,6607,6608,6609,6610]):
            return None # Missing State: State


initial_state = idle
