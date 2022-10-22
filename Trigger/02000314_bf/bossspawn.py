""" trigger/02000314_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 딜레이()


class 딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003140, textId=20003140, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        select_camera(triggerId=301, enable=True)
        add_buff(boxIds=[102], skillId=70000107, level=1, arg4=False, arg5=False)
        create_monster(spawnIds=[99], arg2=False)
        set_skip(state=종료체크)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 종료체크()

    def on_exit(self):
        select_camera(triggerId=301, enable=False)
        remove_buff(boxId=102, skillId=70000107)


class 종료체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 종료딜레이()


class 종료딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=12, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13, visible=True, enabled=True, minimapVisible=True)


