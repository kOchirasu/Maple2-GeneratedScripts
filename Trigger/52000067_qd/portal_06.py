""" trigger/52000067_qd/portal_06.xml """
import common


# 포탈 파괴 연출
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return portal(self.ctx)


class portal(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[806], animationEffect=True) # 포탈

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[806]):
            return portal_off(self.ctx)


class portal_off(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=114, script='$52000067_QD__PORTAL_06__0$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=109, script='$52000067_QD__PORTAL_06__1$', arg4=3, arg5=1)
        self.set_effect(triggerIds=[7015], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7115], visible=True) # 다크 포탈 폭발


initial_state = idle
