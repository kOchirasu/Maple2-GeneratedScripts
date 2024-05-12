""" trigger/52000067_qd/portal_07.xml """
import trigger_api


# 포탈 파괴 연출
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, minUsers='1'):
            return portal(self.ctx)


class portal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[807], animationEffect=True) # 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[807]):
            return portal_off(self.ctx)


class portal_off(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7016], visible=False) # 다크 포탈
        self.set_effect(triggerIds=[7116], visible=True) # 다크 포탈 폭발


initial_state = idle
