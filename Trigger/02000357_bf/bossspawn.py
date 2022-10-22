""" trigger/02000357_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[99], arg2=False)
        set_skip(state=종료체크)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 종료체크()

    def on_exit(self):
        select_camera(triggerId=301, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 종료체크(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20001945, textId=20001945, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 종료딜레이()


class 종료딜레이(state.State):
    def on_enter(self):
        set_achievement(triggerId=102, type='trigger', achieve='ClearPP')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


