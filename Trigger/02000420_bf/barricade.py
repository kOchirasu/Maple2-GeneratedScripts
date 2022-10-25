""" trigger/02000420_bf/barricade.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[99]):
            return None # Missing State: 카운트


initial_state = 대기
