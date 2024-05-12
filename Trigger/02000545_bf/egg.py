""" trigger/02000545_bf/egg.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702], jobCode=0):
            return 아르키아체력(self.ctx)


class 아르키아체력(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=55, spawnId=102, isRelative=True):
            return 알메쉬생성(self.ctx)


class 알메쉬생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=23300010, illust='ArakiaDark_normal', duration=4000, script='$02000545_BF__EGG__0$')
        self.set_mesh(triggerIds=[2133,2134], visible=True)
        self.create_monster(spawnIds=[501,502], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[501]):
            return 알파괴1(self.ctx)
        if self.monster_dead(boxIds=[502]):
            return 알파괴2(self.ctx)
        if self.monster_dead(boxIds=[501,502]):
            return 종료(self.ctx)


class 알파괴1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2133], visible=False)
        self.set_ai_extra_data(key='phase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[502]):
            return 알파괴2(self.ctx)
        if self.monster_dead(boxIds=[501,502]):
            return 종료(self.ctx)


class 알파괴2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2134], visible=False)
        self.set_ai_extra_data(key='phase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[501]):
            return 알파괴1(self.ctx)
        if self.monster_dead(boxIds=[501,502]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2133,2134], visible=False)


initial_state = idle
