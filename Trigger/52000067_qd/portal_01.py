""" trigger/52000067_qd/portal_01.xml """
import trigger_api


# 포탈 파괴 연출
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return portal(self.ctx)


class portal(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[803], animationEffect=True) # 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[803]):
            return portal_off(self.ctx)


class portal_off(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$52000067_QD__PORTAL_01__0$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$52000067_QD__PORTAL_01__1$', arg4=3, arg5=2)
        self.set_effect(triggerIds=[7010], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7110], visible=True) # 다크 포탈 폭발


initial_state = idle
