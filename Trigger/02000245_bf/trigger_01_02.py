""" trigger/02000245_bf/trigger_01_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[802], visible=True)
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
        self.set_mesh(trigger_ids=[802])
        self.set_skill(trigger_ids=[7021])
        self.set_skill(trigger_ids=[7022])
        self.set_skill(trigger_ids=[7023])
        self.set_skill(trigger_ids=[7024])
        self.set_skill(trigger_ids=[7025])
        self.set_skill(trigger_ids=[7026])
        self.set_skill(trigger_ids=[7027])
        self.set_skill(trigger_ids=[7028])
        self.set_skill(trigger_ids=[7029])
        self.set_skill(trigger_ids=[7030])
        self.set_skill(trigger_ids=[7031])
        self.set_skill(trigger_ids=[7032])
        self.set_skill(trigger_ids=[7033])
        self.set_skill(trigger_ids=[7034])
        self.set_skill(trigger_ids=[7035])
        self.set_skill(trigger_ids=[7036])
        self.set_skill(trigger_ids=[7037])
        self.set_skill(trigger_ids=[7038])
        self.set_skill(trigger_ids=[7039])
        self.set_skill(trigger_ids=[7040])
        self.set_effect(trigger_ids=[921])
        self.set_effect(trigger_ids=[922])
        self.set_effect(trigger_ids=[923])
        self.set_effect(trigger_ids=[924])
        self.set_effect(trigger_ids=[925])
        self.set_effect(trigger_ids=[926])
        self.set_effect(trigger_ids=[927])
        self.set_effect(trigger_ids=[928])
        self.set_effect(trigger_ids=[929])
        self.set_effect(trigger_ids=[930])
        self.set_effect(trigger_ids=[931])
        self.set_effect(trigger_ids=[932])
        self.set_effect(trigger_ids=[933])
        self.set_effect(trigger_ids=[934])
        self.set_effect(trigger_ids=[935])
        self.set_effect(trigger_ids=[936])
        self.set_effect(trigger_ids=[937])
        self.set_effect(trigger_ids=[938])
        self.set_effect(trigger_ids=[939])
        self.set_effect(trigger_ids=[940])


initial_state = 대기
