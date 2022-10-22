""" trigger/02000254_bf/elite.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[801], visible=False, animationEffect=False)
        set_ladder(triggerIds=[802], visible=False, animationEffect=False)
        set_ladder(triggerIds=[803], visible=False, animationEffect=False)
        set_ladder(triggerIds=[804], visible=False, animationEffect=False)
        set_ladder(triggerIds=[805], visible=False, animationEffect=False)
        set_ladder(triggerIds=[806], visible=False, animationEffect=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[903]):
            return 딜레이1()


class 딜레이1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 탄2()
        if monster_dead(boxIds=[106]):
            return 클리어딜레이()


class 탄2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        create_monster(spawnIds=[104])
        set_timer(timerId='1', seconds=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 탄3()
        if monster_dead(boxIds=[106]):
            return 클리어딜레이()


class 탄3(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104])
        create_monster(spawnIds=[105])
        set_timer(timerId='1', seconds=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 탄4()
        if monster_dead(boxIds=[106]):
            return 클리어딜레이()


class 탄4(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105])
        create_monster(spawnIds=[104])
        set_timer(timerId='1', seconds=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 탄5()
        if monster_dead(boxIds=[106]):
            return 클리어딜레이()


class 탄5(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104])
        create_monster(spawnIds=[103])
        set_timer(timerId='1', seconds=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 탄2()
        if monster_dead(boxIds=[106]):
            return 클리어딜레이()


class 클리어딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 클리어()


class 클리어(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if true():
            return 클리어2()


class 클리어2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_conversation(type=2, spawnId=11000057, script='$02000254_BF__ELITE__0$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 클리어3()


class 클리어3(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])
        destroy_monster(spawnIds=[105])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        # <action name="이벤트UI를설정한다" arg1="7" arg2="$02000254_BF__ELITE__1$" arg3="3000" arg4="0" />

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 사다리생성()


class 사다리생성(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[801], visible=True, animationEffect=True)
        set_ladder(triggerIds=[802], visible=True, animationEffect=True)
        set_ladder(triggerIds=[803], visible=True, animationEffect=True)
        set_ladder(triggerIds=[804], visible=True, animationEffect=True)
        set_ladder(triggerIds=[805], visible=True, animationEffect=True)
        set_ladder(triggerIds=[806], visible=True, animationEffect=True)
        dungeon_clear()
        hide_guide_summary(entityId=20002524)


