""" trigger/81000003_item/trigger_06.xml """
from common import *
import state


class 시간표등록(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 시간표확인()


class 시간표확인(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000226], state=1)
        set_interact_object(triggerIds=[10000227], state=1)
        set_interact_object(triggerIds=[10000228], state=1)
        set_interact_object(triggerIds=[10000229], state=1)
        set_interact_object(triggerIds=[10000230], state=1)
        set_interact_object(triggerIds=[10000231], state=1)
        set_effect(triggerIds=[711], visible=False)
        set_effect(triggerIds=[712], visible=False)
        set_effect(triggerIds=[713], visible=False)
        set_effect(triggerIds=[714], visible=False)
        set_effect(triggerIds=[715], visible=False)
        set_effect(triggerIds=[716], visible=False)
        set_effect(triggerIds=[717], visible=False)
        set_effect(triggerIds=[718], visible=False)
        set_effect(triggerIds=[719], visible=False)
        set_effect(triggerIds=[720], visible=False)
        set_effect(triggerIds=[721], visible=False)
        set_effect(triggerIds=[722], visible=False)
        set_skill(triggerIds=[811], isEnable=False)
        set_skill(triggerIds=[812], isEnable=False)
        set_skill(triggerIds=[813], isEnable=False)
        set_skill(triggerIds=[814], isEnable=False)
        set_skill(triggerIds=[815], isEnable=False)
        set_skill(triggerIds=[816], isEnable=False)
        set_skill(triggerIds=[817], isEnable=False)
        set_skill(triggerIds=[818], isEnable=False)
        set_skill(triggerIds=[819], isEnable=False)
        set_skill(triggerIds=[820], isEnable=False)
        set_skill(triggerIds=[821], isEnable=False)
        set_skill(triggerIds=[822], isEnable=False)
        set_skill(triggerIds=[823], isEnable=False)
        set_skill(triggerIds=[824], isEnable=False)
        set_skill(triggerIds=[825], isEnable=False)
        set_skill(triggerIds=[826], isEnable=False)
        set_skill(triggerIds=[827], isEnable=False)
        set_skill(triggerIds=[828], isEnable=False)
        set_skill(triggerIds=[911], isEnable=False)
        set_skill(triggerIds=[912], isEnable=False)
        set_skill(triggerIds=[913], isEnable=False)
        set_skill(triggerIds=[914], isEnable=False)
        set_skill(triggerIds=[915], isEnable=False)
        set_skill(triggerIds=[916], isEnable=False)
        set_skill(triggerIds=[917], isEnable=False)
        set_skill(triggerIds=[918], isEnable=False)
        set_skill(triggerIds=[919], isEnable=False)
        set_skill(triggerIds=[920], isEnable=False)
        set_skill(triggerIds=[921], isEnable=False)
        set_skill(triggerIds=[922], isEnable=False)
        set_skill(triggerIds=[923], isEnable=False)
        set_skill(triggerIds=[924], isEnable=False)
        set_skill(triggerIds=[925], isEnable=False)
        set_skill(triggerIds=[926], isEnable=False)
        set_skill(triggerIds=[927], isEnable=False)
        set_skill(triggerIds=[928], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 어나운스0()


class 어나운스0(state.State):
    def on_enter(self):
        set_state(arg1=1, arg2=['미로패턴01','미로패턴02','미로패턴03'], arg3=False)
        set_state(arg1=2, arg2=['점프패턴01','점프패턴02'], arg3=False)
        set_timer(timerId='89', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='89'):
            return 레버()


class 레버(state.State):
    def on_enter(self):
        set_state(arg1=1, arg2=['미로패턴01','미로패턴02','미로패턴03'], arg3=False)
        set_state(arg1=2, arg2=['점프패턴01','점프패턴02'], arg3=False)
        set_mesh(triggerIds=[527,528,529], visible=True)

    def on_tick(self) -> state.State:
        if true():
            return 패턴결정()


class 패턴결정(state.State):
    def on_enter(self):
        use_state(arg1='1', arg2=True)
        use_state(arg1='2', arg2=True)
        set_timer(timerId='12', seconds=240)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 시간표확인()


class 미로패턴01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[527], visible=False)


class 미로패턴02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[528], visible=False)


class 미로패턴03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[529], visible=False)


class 점프패턴01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[711], visible=True)
        set_effect(triggerIds=[712], visible=False)
        set_effect(triggerIds=[713], visible=False)
        set_effect(triggerIds=[714], visible=True)
        set_effect(triggerIds=[715], visible=False)
        set_effect(triggerIds=[716], visible=True)
        set_effect(triggerIds=[717], visible=True)
        set_effect(triggerIds=[718], visible=False)
        set_effect(triggerIds=[719], visible=True)
        set_effect(triggerIds=[720], visible=False)
        set_effect(triggerIds=[721], visible=False)
        set_effect(triggerIds=[722], visible=True)
        set_skill(triggerIds=[811], isEnable=True)
        set_skill(triggerIds=[812], isEnable=True)
        set_skill(triggerIds=[813], isEnable=True)
        set_skill(triggerIds=[814], isEnable=False)
        set_skill(triggerIds=[815], isEnable=False)
        set_skill(triggerIds=[816], isEnable=False)
        set_skill(triggerIds=[817], isEnable=False)
        set_skill(triggerIds=[818], isEnable=False)
        set_skill(triggerIds=[819], isEnable=False)
        set_skill(triggerIds=[820], isEnable=True)
        set_skill(triggerIds=[821], isEnable=True)
        set_skill(triggerIds=[822], isEnable=True)
        set_skill(triggerIds=[823], isEnable=True)
        set_skill(triggerIds=[824], isEnable=True)
        set_skill(triggerIds=[825], isEnable=True)
        set_skill(triggerIds=[826], isEnable=False)
        set_skill(triggerIds=[827], isEnable=False)
        set_skill(triggerIds=[828], isEnable=False)
        set_skill(triggerIds=[911], isEnable=False)
        set_skill(triggerIds=[912], isEnable=False)
        set_skill(triggerIds=[913], isEnable=False)
        set_skill(triggerIds=[914], isEnable=True)
        set_skill(triggerIds=[915], isEnable=True)
        set_skill(triggerIds=[916], isEnable=True)
        set_skill(triggerIds=[917], isEnable=True)
        set_skill(triggerIds=[918], isEnable=True)
        set_skill(triggerIds=[919], isEnable=True)
        set_skill(triggerIds=[920], isEnable=False)
        set_skill(triggerIds=[921], isEnable=False)
        set_skill(triggerIds=[922], isEnable=False)
        set_skill(triggerIds=[923], isEnable=False)
        set_skill(triggerIds=[924], isEnable=False)
        set_skill(triggerIds=[925], isEnable=False)
        set_skill(triggerIds=[926], isEnable=True)
        set_skill(triggerIds=[927], isEnable=True)
        set_skill(triggerIds=[928], isEnable=True)


class 점프패턴02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[711], visible=False)
        set_effect(triggerIds=[712], visible=True)
        set_effect(triggerIds=[713], visible=True)
        set_effect(triggerIds=[714], visible=False)
        set_effect(triggerIds=[715], visible=False)
        set_effect(triggerIds=[716], visible=True)
        set_effect(triggerIds=[717], visible=True)
        set_effect(triggerIds=[718], visible=False)
        set_effect(triggerIds=[719], visible=True)
        set_effect(triggerIds=[720], visible=False)
        set_effect(triggerIds=[721], visible=False)
        set_effect(triggerIds=[722], visible=True)
        set_skill(triggerIds=[811], isEnable=False)
        set_skill(triggerIds=[812], isEnable=False)
        set_skill(triggerIds=[813], isEnable=False)
        set_skill(triggerIds=[814], isEnable=True)
        set_skill(triggerIds=[815], isEnable=True)
        set_skill(triggerIds=[816], isEnable=True)
        set_skill(triggerIds=[817], isEnable=False)
        set_skill(triggerIds=[818], isEnable=False)
        set_skill(triggerIds=[819], isEnable=False)
        set_skill(triggerIds=[820], isEnable=True)
        set_skill(triggerIds=[821], isEnable=True)
        set_skill(triggerIds=[822], isEnable=True)
        set_skill(triggerIds=[823], isEnable=True)
        set_skill(triggerIds=[824], isEnable=True)
        set_skill(triggerIds=[825], isEnable=True)
        set_skill(triggerIds=[826], isEnable=False)
        set_skill(triggerIds=[827], isEnable=False)
        set_skill(triggerIds=[828], isEnable=False)
        set_skill(triggerIds=[911], isEnable=True)
        set_skill(triggerIds=[912], isEnable=True)
        set_skill(triggerIds=[913], isEnable=True)
        set_skill(triggerIds=[914], isEnable=False)
        set_skill(triggerIds=[915], isEnable=False)
        set_skill(triggerIds=[916], isEnable=False)
        set_skill(triggerIds=[917], isEnable=True)
        set_skill(triggerIds=[918], isEnable=True)
        set_skill(triggerIds=[919], isEnable=True)
        set_skill(triggerIds=[920], isEnable=False)
        set_skill(triggerIds=[921], isEnable=False)
        set_skill(triggerIds=[922], isEnable=False)
        set_skill(triggerIds=[923], isEnable=False)
        set_skill(triggerIds=[924], isEnable=False)
        set_skill(triggerIds=[925], isEnable=False)
        set_skill(triggerIds=[926], isEnable=True)
        set_skill(triggerIds=[927], isEnable=True)
        set_skill(triggerIds=[928], isEnable=True)


