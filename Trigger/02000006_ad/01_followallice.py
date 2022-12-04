""" trigger/02000006_ad/01_followallice.xml """
import trigger_api


class 대기00(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[51,52,53,54])
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118], visible=False)
        self.set_effect(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218], visible=False)
        self.set_ladder(triggerIds=[151], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[152], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[153], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[154], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[155], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[156], visible=False, animationEffect=False)
        self.set_effect(triggerIds=[219,220,221,222,223,224], visible=False)
        self.set_interact_object(triggerIds=[10000449], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000449], stateValue=0):
            return 대기01(self.ctx)


class 대기01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[51], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[51]):
            return 발판생성01(self.ctx)


class 몬스터수명설정(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기01(self.ctx)


class 발판생성01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101], visible=True)
        self.set_effect(triggerIds=[201], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성02(self.ctx)


class 발판생성02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[102], visible=True)
        self.set_effect(triggerIds=[202], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성03(self.ctx)


class 발판생성03(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[103], visible=True)
        self.set_effect(triggerIds=[203], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성04(self.ctx)


class 발판생성04(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[104], visible=True)
        self.set_effect(triggerIds=[204], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성05(self.ctx)


class 발판생성05(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[105], visible=True)
        self.set_effect(triggerIds=[205], visible=True)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기02(self.ctx)


class 대기02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[52], animationEffect=True)
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118], visible=False)
        self.set_effect(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218], visible=False)
        self.set_timer(timerId='2', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[52]):
            return 발판생성06(self.ctx)
        if self.time_expired(timerId='2'):
            return 대기00(self.ctx)


class 발판생성06(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[106], visible=True)
        self.set_effect(triggerIds=[206], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성07(self.ctx)


class 발판생성07(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[107], visible=True)
        self.set_effect(triggerIds=[207], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성08(self.ctx)


class 발판생성08(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[108], visible=True)
        self.set_effect(triggerIds=[208], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성09(self.ctx)


class 발판생성09(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[109], visible=True)
        self.set_effect(triggerIds=[209], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성10(self.ctx)


class 발판생성10(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[110], visible=True)
        self.set_effect(triggerIds=[210], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성11(self.ctx)


class 발판생성11(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[111], visible=True)
        self.set_effect(triggerIds=[211], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성12(self.ctx)


class 발판생성12(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[112], visible=True)
        self.set_effect(triggerIds=[212], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성13(self.ctx)


class 발판생성13(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[113], visible=True)
        self.set_effect(triggerIds=[213], visible=True)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기03(self.ctx)


class 대기03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[53], animationEffect=True)
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118], visible=False)
        self.set_effect(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218], visible=False)
        self.set_timer(timerId='2', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[53]):
            return 발판생성14(self.ctx)
        if self.time_expired(timerId='2'):
            return 대기00(self.ctx)


class 발판생성14(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[114], visible=True)
        self.set_effect(triggerIds=[214], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성15(self.ctx)


class 발판생성15(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[115], visible=True)
        self.set_effect(triggerIds=[215], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성16(self.ctx)


class 발판생성16(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[116], visible=True)
        self.set_effect(triggerIds=[216], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성17(self.ctx)


class 발판생성17(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[117], visible=True)
        self.set_effect(triggerIds=[217], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 발판생성18(self.ctx)


class 발판생성18(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[118], visible=True)
        self.set_effect(triggerIds=[218], visible=True)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기04(self.ctx)


class 대기04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[54], animationEffect=True)
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118], visible=False)
        self.set_effect(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218], visible=False)
        self.set_timer(timerId='2', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[54]):
            return 사다리등장(self.ctx)
        if self.time_expired(timerId='2'):
            return 대기00(self.ctx)


class 사다리등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[151], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[152], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[153], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[154], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[155], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[156], visible=True, animationEffect=True)
        self.set_effect(triggerIds=[219,220,221,222,223,224], visible=True)
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기00(self.ctx)


initial_state = 대기00
