""" trigger/52000067_qd/portal_03.xml """
import trigger_api


# 포탈 파괴 연출
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return portal(self.ctx)


class portal(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[801], animationEffect=True) # 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[801]):
            return portal_off(self.ctx)


class portal_off(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=108, script='$52000067_QD__PORTAL_03__0$', arg4=3, arg5=1)
        self.set_conversation(type=1, spawnId=115, script='$52000067_QD__PORTAL_03__1$', arg4=3, arg5=1)
        self.set_effect(triggerIds=[7012], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7112], visible=True) # 다크 포탈 폭발


initial_state = idle
