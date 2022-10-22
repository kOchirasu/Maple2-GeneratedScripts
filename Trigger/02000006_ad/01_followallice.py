""" trigger/02000006_ad/01_followallice.xml """
from common import *
import state


class 대기00(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[51,52,53,54])
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118], visible=False)
        set_effect(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218], visible=False)
        set_ladder(triggerIds=[151], visible=False, animationEffect=False)
        set_ladder(triggerIds=[152], visible=False, animationEffect=False)
        set_ladder(triggerIds=[153], visible=False, animationEffect=False)
        set_ladder(triggerIds=[154], visible=False, animationEffect=False)
        set_ladder(triggerIds=[155], visible=False, animationEffect=False)
        set_ladder(triggerIds=[156], visible=False, animationEffect=False)
        set_effect(triggerIds=[219,220,221,222,223,224], visible=False)
        set_interact_object(triggerIds=[10000449], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000449], arg2=0):
            return 대기01()


class 대기01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[51], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[51]):
            return 발판생성01()


class 몬스터수명설정(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기01()


class 발판생성01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101], visible=True)
        set_effect(triggerIds=[201], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성02()


class 발판생성02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[102], visible=True)
        set_effect(triggerIds=[202], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성03()


class 발판생성03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[103], visible=True)
        set_effect(triggerIds=[203], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성04()


class 발판생성04(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[104], visible=True)
        set_effect(triggerIds=[204], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성05()


class 발판생성05(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[105], visible=True)
        set_effect(triggerIds=[205], visible=True)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기02()


class 대기02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[52], arg2=True)
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118], visible=False)
        set_effect(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218], visible=False)
        set_timer(timerId='2', seconds=15)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[52]):
            return 발판생성06()
        if time_expired(timerId='2'):
            return 대기00()


class 발판생성06(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[106], visible=True)
        set_effect(triggerIds=[206], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성07()


class 발판생성07(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[107], visible=True)
        set_effect(triggerIds=[207], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성08()


class 발판생성08(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[108], visible=True)
        set_effect(triggerIds=[208], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성09()


class 발판생성09(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[109], visible=True)
        set_effect(triggerIds=[209], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성10()


class 발판생성10(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[110], visible=True)
        set_effect(triggerIds=[210], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성11()


class 발판생성11(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[111], visible=True)
        set_effect(triggerIds=[211], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성12()


class 발판생성12(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[112], visible=True)
        set_effect(triggerIds=[212], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성13()


class 발판생성13(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[113], visible=True)
        set_effect(triggerIds=[213], visible=True)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기03()


class 대기03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[53], arg2=True)
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118], visible=False)
        set_effect(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218], visible=False)
        set_timer(timerId='2', seconds=15)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[53]):
            return 발판생성14()
        if time_expired(timerId='2'):
            return 대기00()


class 발판생성14(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[114], visible=True)
        set_effect(triggerIds=[214], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성15()


class 발판생성15(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[115], visible=True)
        set_effect(triggerIds=[215], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성16()


class 발판생성16(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[116], visible=True)
        set_effect(triggerIds=[216], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성17()


class 발판생성17(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[117], visible=True)
        set_effect(triggerIds=[217], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발판생성18()


class 발판생성18(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[118], visible=True)
        set_effect(triggerIds=[218], visible=True)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기04()


class 대기04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[54], arg2=True)
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118], visible=False)
        set_effect(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218], visible=False)
        set_timer(timerId='2', seconds=15)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[54]):
            return 사다리등장()
        if time_expired(timerId='2'):
            return 대기00()


class 사다리등장(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[151], visible=True, animationEffect=True)
        set_ladder(triggerIds=[152], visible=True, animationEffect=True)
        set_ladder(triggerIds=[153], visible=True, animationEffect=True)
        set_ladder(triggerIds=[154], visible=True, animationEffect=True)
        set_ladder(triggerIds=[155], visible=True, animationEffect=True)
        set_ladder(triggerIds=[156], visible=True, animationEffect=True)
        set_effect(triggerIds=[219,220,221,222,223,224], visible=True)
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기00()


