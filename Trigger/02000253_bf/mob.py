""" trigger/02000253_bf/mob.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002527)
        self.hide_guide_summary(entityId=20002528)
        self.hide_guide_summary(entityId=20002529)
        self.hide_guide_summary(entityId=20002530)
        self.hide_guide_summary(entityId=20002531)
        self.hide_guide_summary(entityId=20002532)
        self.set_ladder(triggerIds=[1701], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1702], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1703], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1704], visible=False, animationEffect=False, animationDelay=0)
        self.set_interact_object(triggerIds=[13000005], state=2)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=906, boxId=1):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=8)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 몹1(self.ctx)


class 몹1(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002527, textId=20002527)
        self.set_timer(timerId='1', seconds=15)
        # <action name="몬스터를생성한다" arg1="4001" arg2="1"/>
        # <action name="몬스터를생성한다" arg1="4002" arg2="1"/>

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 몹2(self.ctx)
        if self.object_interacted(interactIds=[10001050], stateValue=0):
            return 몹2(self.ctx)
        if self.object_interacted(interactIds=[10001051], stateValue=0):
            return 몹2(self.ctx)
        if self.object_interacted(interactIds=[10001052], stateValue=0):
            return 몹2(self.ctx)
        if self.object_interacted(interactIds=[10001053], stateValue=0):
            return 몹2(self.ctx)
        """
        <condition name="몬스터가죽어있으면" arg1="4001,4003,4005,4007">
            <transition state="몹2" />
        </condition>
        """


class 몹2(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002528, textId=20002528)
        self.set_timer(timerId='1', seconds=20)
        # <action name="몬스터를생성한다" arg1="4001" arg2="1"/>
        self.create_monster(spawnIds=[4002], animationEffect=True)
        # <action name="몬스터를생성한다" arg1="4003" arg2="1"/>
        self.create_monster(spawnIds=[4004], animationEffect=True)
        # <action name="몬스터를생성한다" arg1="4005" arg2="1"/>
        self.create_monster(spawnIds=[4008], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[4002,4004,4006,4008]):
            return 몹3(self.ctx)


class 몹3(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002529, textId=20002529)
        self.set_timer(timerId='1', seconds=20)
        self.create_monster(spawnIds=[4001], animationEffect=True)
        # <action name="몬스터를생성한다" arg1="4002" arg2="1"/>
        self.create_monster(spawnIds=[4003], animationEffect=True)
        # <action name="몬스터를생성한다" arg1="4004" arg2="1"/>
        self.create_monster(spawnIds=[4007], animationEffect=True)
        # <action name="몬스터를생성한다" arg1="4008" arg2="1"/>

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[4001,4003,4005,4007]):
            return 몹4(self.ctx)


class 몹4(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002530, textId=20002530)
        self.set_timer(timerId='1', seconds=20)
        self.create_monster(spawnIds=[4001], animationEffect=True)
        self.create_monster(spawnIds=[4002], animationEffect=True)
        self.create_monster(spawnIds=[4003], animationEffect=True)
        self.create_monster(spawnIds=[4004], animationEffect=True)
        # <action name="몬스터를생성한다" arg1="4005" arg2="1"/>
        # <action name="몬스터를생성한다" arg1="4006" arg2="1"/>

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[4001,4002,4003,4005,4006]):
            return 몹5(self.ctx)


class 몹5(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002531, textId=20002531)
        self.set_timer(timerId='1', seconds=20)
        # <action name="몬스터를생성한다" arg1="4001" arg2="1"/>
        self.create_monster(spawnIds=[4005], animationEffect=True)
        self.create_monster(spawnIds=[4006], animationEffect=True)
        self.create_monster(spawnIds=[4007], animationEffect=True)
        self.create_monster(spawnIds=[4008], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[4003,4004,4005,4006,4007,4008]):
            return 몹6(self.ctx)


class 몹6(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002532, textId=20002532)
        self.set_timer(timerId='1', seconds=20)
        self.create_monster(spawnIds=[4001], animationEffect=True)
        self.create_monster(spawnIds=[4002], animationEffect=True)
        self.create_monster(spawnIds=[4003], animationEffect=True)
        self.create_monster(spawnIds=[4004], animationEffect=True)
        self.create_monster(spawnIds=[4005], animationEffect=True)
        # <action name="몬스터를생성한다" arg1="4006" arg2="1"/>

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[4001,4002,4003,4004,4005,4006]):
            return 몹10(self.ctx)


class 몹7(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002533, textId=20002533)
        self.set_timer(timerId='1', seconds=20)
        self.create_monster(spawnIds=[4001], animationEffect=True)
        self.create_monster(spawnIds=[4002], animationEffect=True)
        self.create_monster(spawnIds=[4003], animationEffect=True)
        self.create_monster(spawnIds=[4004], animationEffect=True)
        self.create_monster(spawnIds=[4005], animationEffect=True)
        self.create_monster(spawnIds=[4006], animationEffect=True)
        self.create_monster(spawnIds=[4007], animationEffect=True)
        self.create_monster(spawnIds=[4008], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 몹8(self.ctx)


class 몹8(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=20)
        self.create_monster(spawnIds=[4001], animationEffect=True)
        self.create_monster(spawnIds=[4002], animationEffect=True)
        self.create_monster(spawnIds=[4003], animationEffect=True)
        self.create_monster(spawnIds=[4004], animationEffect=True)
        self.create_monster(spawnIds=[4005], animationEffect=True)
        self.create_monster(spawnIds=[4006], animationEffect=True)
        self.create_monster(spawnIds=[4007], animationEffect=True)
        self.create_monster(spawnIds=[4008], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 몹9(self.ctx)


class 몹9(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=20)
        self.create_monster(spawnIds=[4001], animationEffect=True)
        self.create_monster(spawnIds=[4002], animationEffect=True)
        self.create_monster(spawnIds=[4003], animationEffect=True)
        self.create_monster(spawnIds=[4004], animationEffect=True)
        self.create_monster(spawnIds=[4005], animationEffect=True)
        self.create_monster(spawnIds=[4006], animationEffect=True)
        self.create_monster(spawnIds=[4007], animationEffect=True)
        self.create_monster(spawnIds=[4008], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 몹10(self.ctx)


class 몹10(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002533, textId=20002533)
        self.set_timer(timerId='1', seconds=20)
        self.create_monster(spawnIds=[4009], animationEffect=True)
        self.create_monster(spawnIds=[4010], animationEffect=True)
        self.create_monster(spawnIds=[4011], animationEffect=True)
        self.create_monster(spawnIds=[4012], animationEffect=True)
        self.create_monster(spawnIds=[4013], animationEffect=True)
        self.create_monster(spawnIds=[4014], animationEffect=True)
        self.create_monster(spawnIds=[4015], animationEffect=True)
        self.create_monster(spawnIds=[4016], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[4009,4010,4011,4012,4013,4014,4015,4016]):
            return 열려(self.ctx)


class 열려(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002524, textId=20002524)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        # <action name="오브젝트반응설정한다" arg1="13000005" arg2="1" />
        # <action name="아이템을생성한다" arg1="9001" arg2="999" />
        self.set_ladder(triggerIds=[1701], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1702], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1703], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1704], visible=True, animationEffect=True, animationDelay=2)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002524)


initial_state = 대기
