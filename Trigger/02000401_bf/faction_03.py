""" trigger/02000401_bf/faction_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=99910130)
        set_interact_object(triggerIds=[12000027], state=2)
        set_interact_object(triggerIds=[12000028], state=2)
        set_interact_object(triggerIds=[12000039], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='faction03', value=1):
            return 탱크준비()


class 탱크준비(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2903])
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)
        show_guide_summary(entityId=20040103, textId=20040103, duration=3500)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        select_camera(triggerId=302, enable=True)
        create_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208], arg2=False)
        set_conversation(type=1, spawnId=1201, script='$02000401_BF__FACTION_03__0$', arg4=5, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 룸체크()


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 던전()
        if not is_dungeon_room():
            return 퀘스트()


class 던전(state.State):
    def on_enter(self):
        set_skip(state=종료체크)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_interact_object(triggerIds=[12000027], state=1)
        set_interact_object(triggerIds=[12000028], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 종료체크()


class 퀘스트(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000039], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 종료체크()


class 종료체크(state.State):
    def on_enter(self):
        set_skip()
        show_guide_summary(entityId=20040106, textId=20040106, duration=3500)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        remove_buff(boxId=199, skillId=70000107)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if user_value(key='DungeonClear', value=1):
            destroy_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208], arg2=False)
            set_interact_object(triggerIds=[12000027], state=0)
            set_interact_object(triggerIds=[12000028], state=0)
            set_interact_object(triggerIds=[12000039], state=0)
            remove_buff(boxId=199, skillId=99910130)
            return 종료()


class 종료(state.State):
    pass


