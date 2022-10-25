""" trigger/52000094_qd/52000094_trigger.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3003,3004], visible=False)
        self.destroy_monster(spawnIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009])

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9100], questIds=[50100500], questStates=[1]):
            return 진행중일때20002275(self.ctx)
        if self.quest_user_detected(boxIds=[9100], questIds=[20002275], questStates=[1]):
            return 진행중일때20002275(self.ctx)


class 진행중일때20002275(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009], animationEffect=False) # ,90537,90539

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]):
            return 진행중일때20002275(self.ctx)


initial_state = 대기
