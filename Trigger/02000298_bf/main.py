""" trigger/02000298_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000004], state=2)
        set_effect(triggerIds=[601], visible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3221,3222,3223], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[2099], arg2=False)
        set_npc_emotion_loop(spawnId=2099, sequenceName='Idle_A', duration=9999999)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=암호발급)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라이동()

state.DungeonStart = DungeonStart


class 카메라이동(state.State):
    def on_enter(self):
        set_skip()
        select_camera(triggerId=300, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라이동후UI노출()


class 카메라이동후UI노출(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)
        show_guide_summary(entityId=20002991, textId=20002991, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=2099, patrolName='MS2PatrolData_2099_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 던전안내01()


class 던전안내01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3221,3222,3223], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000372], state=1)
        show_guide_summary(entityId=20002980, textId=20002980, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        select_camera(triggerId=301, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 던전안내카메라이동()


class 던전안내카메라이동(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 던전안내02()


class 던전안내02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002981, textId=20002981, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_interact_object(triggerIds=[10000372], state=0)
            return 암호발급()


class 암호발급(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=70000107)
        destroy_monster(spawnIds=[2099])
        select_camera(triggerId=302, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[601], visible=True)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3221,3222,3223], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return 소환1279()
        if random_condition(rate=5):
            return 소환1238()
        if random_condition(rate=5):
            return 소환1358()
        if random_condition(rate=5):
            return 소환1489()
        if random_condition(rate=5):
            return 소환1567()
        if random_condition(rate=5):
            return 소환1679()
        if random_condition(rate=5):
            return 소환2389()
        if random_condition(rate=5):
            return 소환2347()
        if random_condition(rate=5):
            return 소환2478()
        if random_condition(rate=5):
            return 소환2456()
        if random_condition(rate=5):
            return 소환2569()
        if random_condition(rate=5):
            return 소환2678()
        if random_condition(rate=5):
            return 소환3458()
        if random_condition(rate=5):
            return 소환3589()
        if random_condition(rate=5):
            return 소환3679()
        if random_condition(rate=5):
            return 소환3789()
        if random_condition(rate=5):
            return 소환4567()
        if random_condition(rate=5):
            return 소환4578()
        if random_condition(rate=5):
            return 소환4689()
        if random_condition(rate=5):
            return 소환4789()


class 소환1279(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[1279], arg2=False)
            return 종료()


class 소환1238(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[1238], arg2=False)
            return 종료()


class 소환1358(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[1358], arg2=False)
            return 종료()


class 소환1489(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[1489], arg2=False)
            return 종료()


class 소환1567(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[1567], arg2=False)
            return 종료()


class 소환1679(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[1679], arg2=False)
            return 종료()


class 소환2389(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[2389], arg2=False)
            return 종료()


class 소환2347(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[2347], arg2=False)
            return 종료()


class 소환2478(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[2478], arg2=False)
            return 종료()


class 소환2456(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[2456], arg2=False)
            return 종료()


class 소환2569(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[2569], arg2=False)
            return 종료()


class 소환2678(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[2678], arg2=False)
            return 종료()


class 소환3458(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[3458], arg2=False)
            return 종료()


class 소환3589(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[3589], arg2=False)
            return 종료()


class 소환3679(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[3679], arg2=False)
            return 종료()


class 소환3789(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[3789], arg2=False)
            return 종료()


class 소환4567(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[4567], arg2=False)
            return 종료()


class 소환4578(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[4578], arg2=False)
            return 종료()


class 소환4689(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[4689], arg2=False)
            return 종료()


class 소환4789(state.State):
    def on_tick(self) -> state.State:
        if true():
            create_monster(spawnIds=[4789], arg2=False)
            return 종료()


class 종료(state.State):
    pass


