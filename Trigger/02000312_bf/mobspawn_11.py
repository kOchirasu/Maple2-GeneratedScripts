""" trigger/02000312_bf/mobspawn_11.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class Setting(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3005,3006,3007,3008,3009,3010], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        set_ladder(triggerIds=[510], visible=False, animationEffect=False) # LadderEnterance
        set_ladder(triggerIds=[511], visible=False, animationEffect=False) # LadderEnterance
        set_ladder(triggerIds=[512], visible=False, animationEffect=False) # LadderEnterance
        set_ladder(triggerIds=[513], visible=False, animationEffect=False) # LadderEnterance
        set_mesh(triggerIds=[3002,3003,3004], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108], visible=True, arg3=0, arg4=0, arg5=0) # 덩굴
        set_mesh(triggerIds=[1110,1111,1112,1113,1114,1115,1116,1117,1118,1119], visible=True, arg3=0, arg4=0, arg5=0) # 덩굴
        set_mesh(triggerIds=[1120,1121,1122,1123,1124,1125,1126], visible=True, arg3=0, arg4=0, arg5=0) # 덩굴
        set_mesh(triggerIds=[1130,1131,1132,1133,1134,1135,1136,1137], visible=True, arg3=0, arg4=0, arg5=0) # 덩굴
        set_mesh(triggerIds=[1140], visible=True, arg3=0, arg4=0, arg5=0) # 씨앗
        set_mesh_animation(triggerIds=[1140], visible=True, arg3=0, arg4=0) # 씨앗
        set_effect(triggerIds=[5000], visible=False) # UI
        set_effect(triggerIds=[5001], visible=False) # Vine
        set_user_value(key='MobWaveStop', value=0)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # GuideUI
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)
        set_skip(state=CameraWalk01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CameraWalk01()

state.DungeonStart = DungeonStart


class CameraWalk01(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=False)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Battle01()

    def on_exit(self):
        set_ladder(triggerIds=[510], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[511], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[512], visible=True, animationEffect=True) # LadderEnterance
        set_ladder(triggerIds=[513], visible=True, animationEffect=True) # LadderEnterance
        set_mesh(triggerIds=[3005,3006,3007,3008,3009,3010], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class Battle01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103], arg2=False)
        set_effect(triggerIds=[5000], visible=True) # UI
        show_guide_summary(entityId=20031201, textId=20031201) # 몬스터를 모두 처치하기

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103]):
            return Battle02()

    def on_exit(self):
        destroy_monster(spawnIds=[101,102,103])


class Battle02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20031201)
        create_monster(spawnIds=[111,112,113,114], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,112,113,114]):
            return Battle03()

    def on_exit(self):
        destroy_monster(spawnIds=[111,112,113,114])


class Battle03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # UI
        show_guide_summary(entityId=20031202, textId=20031202) # 어둠의 씨앗 제거하기
        create_monster(spawnIds=[130], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[130]):
            return VineRemove01()

    def on_exit(self):
        destroy_monster(spawnIds=[130])


class VineRemove01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20031202)
        set_effect(triggerIds=[5001], visible=True) # Vine
        set_mesh(triggerIds=[3002,3003,3004], visible=False, arg3=500, arg4=0, arg5=0) # Invisible_Barrier
        set_random_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108], visible=False, meshCount=9, arg4=0, delay=50) # 덩굴
        set_random_mesh(triggerIds=[1110,1111,1112,1113,1114,1115,1116,1117,1118,1119], visible=False, meshCount=10, arg4=300, delay=50) # 덩굴
        set_random_mesh(triggerIds=[1120,1121,1122,1123,1124,1125,1126], visible=False, meshCount=7, arg4=200, delay=50) # 덩굴
        set_random_mesh(triggerIds=[1130,1131,1132,1133,1134,1135,1136,1137], visible=False, meshCount=8, arg4=100, delay=50) # 덩굴
        set_mesh(triggerIds=[1140], visible=False, arg3=200, arg4=0, arg5=10) # 씨앗
        set_mesh_animation(triggerIds=[1140], visible=False, arg3=0, arg4=0) # 씨앗

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return MobWaveStart()


class MobWaveStart(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # UI
        show_guide_summary(entityId=20031203, textId=20031203) # 어둠의 씨앗 모두 제거하기
        create_monster(spawnIds=[121,122,123,124,125,126,127,128], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[121,122,123,124,125,126,127,128]):
            return MobWaveDelayRandom()
        if user_value(key='MobWaveStop', value=1):
            return Quit()

    def on_exit(self):
        destroy_monster(spawnIds=[121,122,123,124,125,126,127,128])


class MobWaveDelayRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=60):
            return MobWaveDelay01()
        if random_condition(rate=20):
            return MobWaveDelay02()
        if random_condition(rate=20):
            return MobWaveDelay03()
        if user_value(key='MobWaveStop', value=1):
            return Quit()


class MobWaveDelay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return MobWaveStart()
        if user_value(key='MobWaveStop', value=1):
            return Quit()


class MobWaveDelay02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=17000):
            return MobWaveStart()
        if user_value(key='MobWaveStop', value=1):
            return Quit()


class MobWaveDelay03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return MobWaveStart()
        if user_value(key='MobWaveStop', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20031203)


