""" trigger/02000401_bf/faction_04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        remove_buff(boxId=199, skillId=99910160)
        set_interact_object(triggerIds=[12000029], state=2)
        set_interact_object(triggerIds=[12000040], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='faction04', value=1):
            return 인원수체크()


class 인원수체크(state.State):
    def on_enter(self):
        set_skip(state=반응대기)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[2902]) # action name="연출UI를설정한다" arg1="1"/>
			<action name="연출UI를설정한다" arg1="3"/
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)
        select_camera(triggerId=303, enable=True)
        create_monster(spawnIds=[1300], arg2=True)
        create_monster(spawnIds=[1301,1302,1303,1304,1305], arg2=False)
        set_conversation(type=1, spawnId=1301, script='$02000401_BF__FACTION_04__0$', arg4=5, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 반응대기()


class 반응대기(state.State):
    def on_enter(self):
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=20040104, textId=20040104, duration=2500)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        remove_buff(boxId=199, skillId=70000107)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if user_value(key='NPClanding', value=1):
            return 룸체크()


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 던전()
        if not is_dungeon_room():
            return 퀘스트()


class 던전(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000029], state=1)
        set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 보스소환()


class 퀘스트(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000040], state=1)
        set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보스소환()


class 보스소환(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20040107, textId=20040107, duration=3000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        create_monster(spawnIds=[2099], arg2=False)
        set_user_value(triggerId=99999100, key='bossSpawn', value=1)
        destroy_monster(spawnIds=[1300], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='DungeonClear', value=1):
            destroy_monster(spawnIds=[1300,1301,1302,1303,1304,1305], arg2=False)
            set_interact_object(triggerIds=[12000029], state=0)
            set_interact_object(triggerIds=[12000040], state=0)
            remove_buff(boxId=199, skillId=99910160)
            return 종료()


class 종료(state.State):
    pass


