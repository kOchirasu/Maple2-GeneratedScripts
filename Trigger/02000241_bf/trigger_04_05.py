""" trigger/02000241_bf/trigger_04_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[308], visible=True, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[408]):
            return 버튼눌림(self.ctx)


class 버튼눌림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[308], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[707,708], visible=False)
        self.set_mesh(trigger_ids=[309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324], visible=False)


initial_state = 대기
