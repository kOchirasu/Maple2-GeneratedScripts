""" trigger/02010054_bf/guide_01.xml """
from common import *
import state


class 반응대기(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000856], arg2=0):
            return 가이드01()


class 가이드01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20105402, textId=20105402)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            hide_guide_summary(entityId=20105402)
            return 감지대기()


class 감지대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[108]):
            return 가이드02()


class 가이드02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=가이드02스킵)
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라이동02()


class 카메라이동02(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            select_camera(triggerId=303, enable=False)
            return 가이드02종료()


class 가이드02스킵(state.State):
    def on_enter(self):
        set_skip()
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 가이드02종료()


class 가이드02종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=20105403, textId=20105403)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000860,10000861], arg2=0):
            hide_guide_summary(entityId=20105403)
            return 가이드03()


class 가이드03(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000858], arg2=0):
            return 가이드03종료()


class 가이드03종료(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20105405, textId=20105405)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            hide_guide_summary(entityId=20105405)
            return 반응대기02()


class 반응대기02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[109]):
            return 반응대기02종료()


class 반응대기02종료(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20105403, textId=20105403)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            hide_guide_summary(entityId=20105403)
            return 가이드04()


class 가이드04(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000857], arg2=0):
            return 가이드04종료()


class 가이드04종료(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20105402, textId=20105402)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            hide_guide_summary(entityId=20105402)
            return 감지대기02()


class 감지대기02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[110]):
            set_event_ui(type=1, arg2='$02010054_BF__GUIDE_01__0$', arg3='5000', arg4='0')
            return 종료()


class 종료(state.State):
    pass


