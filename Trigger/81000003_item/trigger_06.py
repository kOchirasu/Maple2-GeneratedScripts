""" trigger/81000003_item/trigger_06.xml """
import common


class 시간표등록(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return 시간표확인(self.ctx)


class 시간표확인(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000226], state=1)
        self.set_interact_object(triggerIds=[10000227], state=1)
        self.set_interact_object(triggerIds=[10000228], state=1)
        self.set_interact_object(triggerIds=[10000229], state=1)
        self.set_interact_object(triggerIds=[10000230], state=1)
        self.set_interact_object(triggerIds=[10000231], state=1)
        self.set_effect(triggerIds=[711], visible=False)
        self.set_effect(triggerIds=[712], visible=False)
        self.set_effect(triggerIds=[713], visible=False)
        self.set_effect(triggerIds=[714], visible=False)
        self.set_effect(triggerIds=[715], visible=False)
        self.set_effect(triggerIds=[716], visible=False)
        self.set_effect(triggerIds=[717], visible=False)
        self.set_effect(triggerIds=[718], visible=False)
        self.set_effect(triggerIds=[719], visible=False)
        self.set_effect(triggerIds=[720], visible=False)
        self.set_effect(triggerIds=[721], visible=False)
        self.set_effect(triggerIds=[722], visible=False)
        self.set_skill(triggerIds=[811], enable=False)
        self.set_skill(triggerIds=[812], enable=False)
        self.set_skill(triggerIds=[813], enable=False)
        self.set_skill(triggerIds=[814], enable=False)
        self.set_skill(triggerIds=[815], enable=False)
        self.set_skill(triggerIds=[816], enable=False)
        self.set_skill(triggerIds=[817], enable=False)
        self.set_skill(triggerIds=[818], enable=False)
        self.set_skill(triggerIds=[819], enable=False)
        self.set_skill(triggerIds=[820], enable=False)
        self.set_skill(triggerIds=[821], enable=False)
        self.set_skill(triggerIds=[822], enable=False)
        self.set_skill(triggerIds=[823], enable=False)
        self.set_skill(triggerIds=[824], enable=False)
        self.set_skill(triggerIds=[825], enable=False)
        self.set_skill(triggerIds=[826], enable=False)
        self.set_skill(triggerIds=[827], enable=False)
        self.set_skill(triggerIds=[828], enable=False)
        self.set_skill(triggerIds=[911], enable=False)
        self.set_skill(triggerIds=[912], enable=False)
        self.set_skill(triggerIds=[913], enable=False)
        self.set_skill(triggerIds=[914], enable=False)
        self.set_skill(triggerIds=[915], enable=False)
        self.set_skill(triggerIds=[916], enable=False)
        self.set_skill(triggerIds=[917], enable=False)
        self.set_skill(triggerIds=[918], enable=False)
        self.set_skill(triggerIds=[919], enable=False)
        self.set_skill(triggerIds=[920], enable=False)
        self.set_skill(triggerIds=[921], enable=False)
        self.set_skill(triggerIds=[922], enable=False)
        self.set_skill(triggerIds=[923], enable=False)
        self.set_skill(triggerIds=[924], enable=False)
        self.set_skill(triggerIds=[925], enable=False)
        self.set_skill(triggerIds=[926], enable=False)
        self.set_skill(triggerIds=[927], enable=False)
        self.set_skill(triggerIds=[928], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 어나운스0(self.ctx)


class 어나운스0(common.Trigger):
    def on_enter(self):
        self.set_state(id=1, states=[미로패턴01,미로패턴02,미로패턴03], randomize=False)
        self.set_state(id=2, states=[점프패턴01,점프패턴02], randomize=False)
        self.set_timer(timerId='89', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='89'):
            return 레버(self.ctx)


class 레버(common.Trigger):
    def on_enter(self):
        self.set_state(id=1, states=[미로패턴01,미로패턴02,미로패턴03], randomize=False)
        self.set_state(id=2, states=[점프패턴01,점프패턴02], randomize=False)
        self.set_mesh(triggerIds=[527,528,529], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 패턴결정(self.ctx)


class 패턴결정(common.Trigger):
    def on_enter(self):
        self.use_state(arg1=1, arg2=True)
        self.use_state(arg1=2, arg2=True)
        self.set_timer(timerId='12', seconds=240)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='12'):
            return 시간표확인(self.ctx)


class 미로패턴01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[527], visible=False)


class 미로패턴02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[528], visible=False)


class 미로패턴03(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[529], visible=False)


class 점프패턴01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[711], visible=True)
        self.set_effect(triggerIds=[712], visible=False)
        self.set_effect(triggerIds=[713], visible=False)
        self.set_effect(triggerIds=[714], visible=True)
        self.set_effect(triggerIds=[715], visible=False)
        self.set_effect(triggerIds=[716], visible=True)
        self.set_effect(triggerIds=[717], visible=True)
        self.set_effect(triggerIds=[718], visible=False)
        self.set_effect(triggerIds=[719], visible=True)
        self.set_effect(triggerIds=[720], visible=False)
        self.set_effect(triggerIds=[721], visible=False)
        self.set_effect(triggerIds=[722], visible=True)
        self.set_skill(triggerIds=[811], enable=True)
        self.set_skill(triggerIds=[812], enable=True)
        self.set_skill(triggerIds=[813], enable=True)
        self.set_skill(triggerIds=[814], enable=False)
        self.set_skill(triggerIds=[815], enable=False)
        self.set_skill(triggerIds=[816], enable=False)
        self.set_skill(triggerIds=[817], enable=False)
        self.set_skill(triggerIds=[818], enable=False)
        self.set_skill(triggerIds=[819], enable=False)
        self.set_skill(triggerIds=[820], enable=True)
        self.set_skill(triggerIds=[821], enable=True)
        self.set_skill(triggerIds=[822], enable=True)
        self.set_skill(triggerIds=[823], enable=True)
        self.set_skill(triggerIds=[824], enable=True)
        self.set_skill(triggerIds=[825], enable=True)
        self.set_skill(triggerIds=[826], enable=False)
        self.set_skill(triggerIds=[827], enable=False)
        self.set_skill(triggerIds=[828], enable=False)
        self.set_skill(triggerIds=[911], enable=False)
        self.set_skill(triggerIds=[912], enable=False)
        self.set_skill(triggerIds=[913], enable=False)
        self.set_skill(triggerIds=[914], enable=True)
        self.set_skill(triggerIds=[915], enable=True)
        self.set_skill(triggerIds=[916], enable=True)
        self.set_skill(triggerIds=[917], enable=True)
        self.set_skill(triggerIds=[918], enable=True)
        self.set_skill(triggerIds=[919], enable=True)
        self.set_skill(triggerIds=[920], enable=False)
        self.set_skill(triggerIds=[921], enable=False)
        self.set_skill(triggerIds=[922], enable=False)
        self.set_skill(triggerIds=[923], enable=False)
        self.set_skill(triggerIds=[924], enable=False)
        self.set_skill(triggerIds=[925], enable=False)
        self.set_skill(triggerIds=[926], enable=True)
        self.set_skill(triggerIds=[927], enable=True)
        self.set_skill(triggerIds=[928], enable=True)


class 점프패턴02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[711], visible=False)
        self.set_effect(triggerIds=[712], visible=True)
        self.set_effect(triggerIds=[713], visible=True)
        self.set_effect(triggerIds=[714], visible=False)
        self.set_effect(triggerIds=[715], visible=False)
        self.set_effect(triggerIds=[716], visible=True)
        self.set_effect(triggerIds=[717], visible=True)
        self.set_effect(triggerIds=[718], visible=False)
        self.set_effect(triggerIds=[719], visible=True)
        self.set_effect(triggerIds=[720], visible=False)
        self.set_effect(triggerIds=[721], visible=False)
        self.set_effect(triggerIds=[722], visible=True)
        self.set_skill(triggerIds=[811], enable=False)
        self.set_skill(triggerIds=[812], enable=False)
        self.set_skill(triggerIds=[813], enable=False)
        self.set_skill(triggerIds=[814], enable=True)
        self.set_skill(triggerIds=[815], enable=True)
        self.set_skill(triggerIds=[816], enable=True)
        self.set_skill(triggerIds=[817], enable=False)
        self.set_skill(triggerIds=[818], enable=False)
        self.set_skill(triggerIds=[819], enable=False)
        self.set_skill(triggerIds=[820], enable=True)
        self.set_skill(triggerIds=[821], enable=True)
        self.set_skill(triggerIds=[822], enable=True)
        self.set_skill(triggerIds=[823], enable=True)
        self.set_skill(triggerIds=[824], enable=True)
        self.set_skill(triggerIds=[825], enable=True)
        self.set_skill(triggerIds=[826], enable=False)
        self.set_skill(triggerIds=[827], enable=False)
        self.set_skill(triggerIds=[828], enable=False)
        self.set_skill(triggerIds=[911], enable=True)
        self.set_skill(triggerIds=[912], enable=True)
        self.set_skill(triggerIds=[913], enable=True)
        self.set_skill(triggerIds=[914], enable=False)
        self.set_skill(triggerIds=[915], enable=False)
        self.set_skill(triggerIds=[916], enable=False)
        self.set_skill(triggerIds=[917], enable=True)
        self.set_skill(triggerIds=[918], enable=True)
        self.set_skill(triggerIds=[919], enable=True)
        self.set_skill(triggerIds=[920], enable=False)
        self.set_skill(triggerIds=[921], enable=False)
        self.set_skill(triggerIds=[922], enable=False)
        self.set_skill(triggerIds=[923], enable=False)
        self.set_skill(triggerIds=[924], enable=False)
        self.set_skill(triggerIds=[925], enable=False)
        self.set_skill(triggerIds=[926], enable=True)
        self.set_skill(triggerIds=[927], enable=True)
        self.set_skill(triggerIds=[928], enable=True)


initial_state = 시간표등록
