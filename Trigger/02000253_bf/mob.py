""" trigger/02000253_bf/mob.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002527)
        hide_guide_summary(entityId=20002528)
        hide_guide_summary(entityId=20002529)
        hide_guide_summary(entityId=20002530)
        hide_guide_summary(entityId=20002531)
        hide_guide_summary(entityId=20002532)
        set_ladder(triggerIds=[1701], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[1702], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[1703], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[1704], visible=False, animationEffect=False, animationDelay=0)
        set_interact_object(triggerIds=[13000005], state=2)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=906, boxId=1):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=8)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 몹1()


class 몹1(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002527, textId=20002527)
        set_timer(timerId='1', seconds=15)
        # <action name="몬스터를생성한다" arg1="4001" arg2="1"/>
        # <action name="몬스터를생성한다" arg1="4002" arg2="1"/>

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 몹2()
        if object_interacted(interactIds=[10001050], arg2=0):
            return 몹2()
        if object_interacted(interactIds=[10001051], arg2=0):
            return 몹2()
        if object_interacted(interactIds=[10001052], arg2=0):
            return 몹2()
        if object_interacted(interactIds=[10001053], arg2=0):
            return 몹2()
        """
        <condition name="몬스터가죽어있으면" arg1="4001,4003,4005,4007">
            <transition state="몹2" />
        </condition>
        """


class 몹2(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002528, textId=20002528)
        set_timer(timerId='1', seconds=20)
        # <action name="몬스터를생성한다" arg1="4001" arg2="1"/>
        create_monster(spawnIds=[4002], arg2=True)
        # <action name="몬스터를생성한다" arg1="4003" arg2="1"/>
        create_monster(spawnIds=[4004], arg2=True)
        # <action name="몬스터를생성한다" arg1="4005" arg2="1"/>
        create_monster(spawnIds=[4008], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4002,4004,4006,4008]):
            return 몹3()


class 몹3(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002529, textId=20002529)
        set_timer(timerId='1', seconds=20)
        create_monster(spawnIds=[4001], arg2=True)
        # <action name="몬스터를생성한다" arg1="4002" arg2="1"/>
        create_monster(spawnIds=[4003], arg2=True)
        # <action name="몬스터를생성한다" arg1="4004" arg2="1"/>
        create_monster(spawnIds=[4007], arg2=True)
        # <action name="몬스터를생성한다" arg1="4008" arg2="1"/>

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4001,4003,4005,4007]):
            return 몹4()


class 몹4(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002530, textId=20002530)
        set_timer(timerId='1', seconds=20)
        create_monster(spawnIds=[4001], arg2=True)
        create_monster(spawnIds=[4002], arg2=True)
        create_monster(spawnIds=[4003], arg2=True)
        create_monster(spawnIds=[4004], arg2=True)
        # <action name="몬스터를생성한다" arg1="4005" arg2="1"/>
        # <action name="몬스터를생성한다" arg1="4006" arg2="1"/>

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4001,4002,4003,4005,4006]):
            return 몹5()


class 몹5(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002531, textId=20002531)
        set_timer(timerId='1', seconds=20)
        # <action name="몬스터를생성한다" arg1="4001" arg2="1"/>
        create_monster(spawnIds=[4005], arg2=True)
        create_monster(spawnIds=[4006], arg2=True)
        create_monster(spawnIds=[4007], arg2=True)
        create_monster(spawnIds=[4008], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4003,4004,4005,4006,4007,4008]):
            return 몹6()


class 몹6(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002532, textId=20002532)
        set_timer(timerId='1', seconds=20)
        create_monster(spawnIds=[4001], arg2=True)
        create_monster(spawnIds=[4002], arg2=True)
        create_monster(spawnIds=[4003], arg2=True)
        create_monster(spawnIds=[4004], arg2=True)
        create_monster(spawnIds=[4005], arg2=True)
        # <action name="몬스터를생성한다" arg1="4006" arg2="1"/>

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4001,4002,4003,4004,4005,4006]):
            return 몹10()


class 몹7(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002533, textId=20002533)
        set_timer(timerId='1', seconds=20)
        create_monster(spawnIds=[4001], arg2=True)
        create_monster(spawnIds=[4002], arg2=True)
        create_monster(spawnIds=[4003], arg2=True)
        create_monster(spawnIds=[4004], arg2=True)
        create_monster(spawnIds=[4005], arg2=True)
        create_monster(spawnIds=[4006], arg2=True)
        create_monster(spawnIds=[4007], arg2=True)
        create_monster(spawnIds=[4008], arg2=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 몹8()


class 몹8(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=20)
        create_monster(spawnIds=[4001], arg2=True)
        create_monster(spawnIds=[4002], arg2=True)
        create_monster(spawnIds=[4003], arg2=True)
        create_monster(spawnIds=[4004], arg2=True)
        create_monster(spawnIds=[4005], arg2=True)
        create_monster(spawnIds=[4006], arg2=True)
        create_monster(spawnIds=[4007], arg2=True)
        create_monster(spawnIds=[4008], arg2=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 몹9()


class 몹9(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=20)
        create_monster(spawnIds=[4001], arg2=True)
        create_monster(spawnIds=[4002], arg2=True)
        create_monster(spawnIds=[4003], arg2=True)
        create_monster(spawnIds=[4004], arg2=True)
        create_monster(spawnIds=[4005], arg2=True)
        create_monster(spawnIds=[4006], arg2=True)
        create_monster(spawnIds=[4007], arg2=True)
        create_monster(spawnIds=[4008], arg2=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 몹10()


class 몹10(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002533, textId=20002533)
        set_timer(timerId='1', seconds=20)
        create_monster(spawnIds=[4009], arg2=True)
        create_monster(spawnIds=[4010], arg2=True)
        create_monster(spawnIds=[4011], arg2=True)
        create_monster(spawnIds=[4012], arg2=True)
        create_monster(spawnIds=[4013], arg2=True)
        create_monster(spawnIds=[4014], arg2=True)
        create_monster(spawnIds=[4015], arg2=True)
        create_monster(spawnIds=[4016], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4009,4010,4011,4012,4013,4014,4015,4016]):
            return 열려()


class 열려(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002524, textId=20002524)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        # <action name="오브젝트반응설정한다" arg1="13000005" arg2="1" />
        # <action name="아이템을생성한다" arg1="9001" arg2="999" />
        set_ladder(triggerIds=[1701], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1702], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1703], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1704], visible=True, animationEffect=True, animationDelay=2)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002524)


