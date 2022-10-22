""" trigger/02000401_bf/faction_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=99910140)
        set_interact_object(triggerIds=[12000023], state=2)
        set_interact_object(triggerIds=[12000024], state=2)
        set_interact_object(triggerIds=[12000025], state=2)
        set_interact_object(triggerIds=[12000026], state=2)
        set_interact_object(triggerIds=[12000038], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='faction02', value=1):
            return 말준비()


class 말준비(state.State):
    def on_enter(self):
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1101,1102,1103,1104,1104], arg2=False)
        set_conversation(type=1, spawnId=1101, script='$02000401_BF__FACTION_02__0$', arg4=5, arg5=0)

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
        set_interact_object(triggerIds=[12000023], state=1)
        set_interact_object(triggerIds=[12000024], state=1)
        set_interact_object(triggerIds=[12000025], state=1)
        set_interact_object(triggerIds=[12000026], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 종료체크()


class 퀘스트(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000038], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 종료체크()


class 종료체크(state.State):
    def on_enter(self):
        set_skip()
        show_guide_summary(entityId=20040102, textId=20040102, duration=3000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        remove_buff(boxId=199, skillId=70000107)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차안내2()


class 차안내2(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20040105, textId=20040105, duration=3500)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        remove_buff(boxId=199, skillId=70000107)

    def on_tick(self) -> state.State:
        if user_value(key='DungeonClear', value=1):
            destroy_monster(spawnIds=[1101,1102,1103,1104,1104], arg2=False)
            set_interact_object(triggerIds=[12000023], state=0)
            set_interact_object(triggerIds=[12000024], state=0)
            set_interact_object(triggerIds=[12000025], state=0)
            set_interact_object(triggerIds=[12000026], state=0)
            set_interact_object(triggerIds=[12000038], state=0)
            remove_buff(boxId=199, skillId=99910140)
            return 종료()


class 종료(state.State):
    pass


