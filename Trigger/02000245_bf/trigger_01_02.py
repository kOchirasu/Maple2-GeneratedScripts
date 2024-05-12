""" trigger/02000245_bf/trigger_01_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[802], visible=True, start_delay=0, interval=0, fade=0)
        self.set_skill(trigger_ids=[7021], enable=True)
        self.set_skill(trigger_ids=[7022], enable=True)
        self.set_skill(trigger_ids=[7023], enable=True)
        self.set_skill(trigger_ids=[7024], enable=True)
        self.set_skill(trigger_ids=[7025], enable=True)
        self.set_skill(trigger_ids=[7026], enable=True)
        self.set_skill(trigger_ids=[7027], enable=True)
        self.set_skill(trigger_ids=[7028], enable=True)
        self.set_skill(trigger_ids=[7029], enable=True)
        self.set_skill(trigger_ids=[7030], enable=True)
        self.set_skill(trigger_ids=[7031], enable=True)
        self.set_skill(trigger_ids=[7032], enable=True)
        self.set_skill(trigger_ids=[7033], enable=True)
        self.set_skill(trigger_ids=[7034], enable=True)
        self.set_skill(trigger_ids=[7035], enable=True)
        self.set_skill(trigger_ids=[7036], enable=True)
        self.set_skill(trigger_ids=[7037], enable=True)
        self.set_skill(trigger_ids=[7038], enable=True)
        self.set_skill(trigger_ids=[7039], enable=True)
        self.set_skill(trigger_ids=[7040], enable=True)
        self.set_effect(trigger_ids=[921], visible=True)
        self.set_effect(trigger_ids=[922], visible=True)
        self.set_effect(trigger_ids=[923], visible=True)
        self.set_effect(trigger_ids=[924], visible=True)
        self.set_effect(trigger_ids=[925], visible=True)
        self.set_effect(trigger_ids=[926], visible=True)
        self.set_effect(trigger_ids=[927], visible=True)
        self.set_effect(trigger_ids=[928], visible=True)
        self.set_effect(trigger_ids=[929], visible=True)
        self.set_effect(trigger_ids=[930], visible=True)
        self.set_effect(trigger_ids=[931], visible=True)
        self.set_effect(trigger_ids=[932], visible=True)
        self.set_effect(trigger_ids=[933], visible=True)
        self.set_effect(trigger_ids=[934], visible=True)
        self.set_effect(trigger_ids=[935], visible=True)
        self.set_effect(trigger_ids=[936], visible=True)
        self.set_effect(trigger_ids=[937], visible=True)
        self.set_effect(trigger_ids=[938], visible=True)
        self.set_effect(trigger_ids=[939], visible=True)
        self.set_effect(trigger_ids=[940], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[208]):
            return 단계1(self.ctx)


class 단계1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[802], visible=False, start_delay=0, interval=0, fade=0)
        self.set_skill(trigger_ids=[7021], enable=False)
        self.set_skill(trigger_ids=[7022], enable=False)
        self.set_skill(trigger_ids=[7023], enable=False)
        self.set_skill(trigger_ids=[7024], enable=False)
        self.set_skill(trigger_ids=[7025], enable=False)
        self.set_skill(trigger_ids=[7026], enable=False)
        self.set_skill(trigger_ids=[7027], enable=False)
        self.set_skill(trigger_ids=[7028], enable=False)
        self.set_skill(trigger_ids=[7029], enable=False)
        self.set_skill(trigger_ids=[7030], enable=False)
        self.set_skill(trigger_ids=[7031], enable=False)
        self.set_skill(trigger_ids=[7032], enable=False)
        self.set_skill(trigger_ids=[7033], enable=False)
        self.set_skill(trigger_ids=[7034], enable=False)
        self.set_skill(trigger_ids=[7035], enable=False)
        self.set_skill(trigger_ids=[7036], enable=False)
        self.set_skill(trigger_ids=[7037], enable=False)
        self.set_skill(trigger_ids=[7038], enable=False)
        self.set_skill(trigger_ids=[7039], enable=False)
        self.set_skill(trigger_ids=[7040], enable=False)
        self.set_effect(trigger_ids=[921], visible=False)
        self.set_effect(trigger_ids=[922], visible=False)
        self.set_effect(trigger_ids=[923], visible=False)
        self.set_effect(trigger_ids=[924], visible=False)
        self.set_effect(trigger_ids=[925], visible=False)
        self.set_effect(trigger_ids=[926], visible=False)
        self.set_effect(trigger_ids=[927], visible=False)
        self.set_effect(trigger_ids=[928], visible=False)
        self.set_effect(trigger_ids=[929], visible=False)
        self.set_effect(trigger_ids=[930], visible=False)
        self.set_effect(trigger_ids=[931], visible=False)
        self.set_effect(trigger_ids=[932], visible=False)
        self.set_effect(trigger_ids=[933], visible=False)
        self.set_effect(trigger_ids=[934], visible=False)
        self.set_effect(trigger_ids=[935], visible=False)
        self.set_effect(trigger_ids=[936], visible=False)
        self.set_effect(trigger_ids=[937], visible=False)
        self.set_effect(trigger_ids=[938], visible=False)
        self.set_effect(trigger_ids=[939], visible=False)
        self.set_effect(trigger_ids=[940], visible=False)


initial_state = 대기
