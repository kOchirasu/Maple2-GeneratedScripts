""" trigger/02000312_bf/mobspawn_11.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Setting(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3005,3006,3007,3008,3009,3010], visible=True, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.set_ladder(triggerIds=[510], visible=False, animationEffect=False) # LadderEnterance
        self.set_ladder(triggerIds=[511], visible=False, animationEffect=False) # LadderEnterance
        self.set_ladder(triggerIds=[512], visible=False, animationEffect=False) # LadderEnterance
        self.set_ladder(triggerIds=[513], visible=False, animationEffect=False) # LadderEnterance
        self.set_mesh(triggerIds=[3002,3003,3004], visible=True, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108], visible=True, arg3=0, delay=0, scale=0) # 덩굴
        self.set_mesh(triggerIds=[1110,1111,1112,1113,1114,1115,1116,1117,1118,1119], visible=True, arg3=0, delay=0, scale=0) # 덩굴
        self.set_mesh(triggerIds=[1120,1121,1122,1123,1124,1125,1126], visible=True, arg3=0, delay=0, scale=0) # 덩굴
        self.set_mesh(triggerIds=[1130,1131,1132,1133,1134,1135,1136,1137], visible=True, arg3=0, delay=0, scale=0) # 덩굴
        self.set_mesh(triggerIds=[1140], visible=True, arg3=0, delay=0, scale=0) # 씨앗
        self.set_mesh_animation(triggerIds=[1140], visible=True, arg3=0, arg4=0) # 씨앗
        self.set_effect(triggerIds=[5000], visible=False) # UI
        self.set_effect(triggerIds=[5001], visible=False) # Vine
        self.set_user_value(key='MobWaveStop', value=0)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # GuideUI
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)
        self.set_skip(state=CameraWalk01)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CameraWalk01(self.ctx)


class CameraWalk01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=False)
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Battle01(self.ctx)

    def on_exit(self):
        self.set_ladder(triggerIds=[510], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[511], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[512], visible=True, animationEffect=True) # LadderEnterance
        self.set_ladder(triggerIds=[513], visible=True, animationEffect=True) # LadderEnterance
        self.set_mesh(triggerIds=[3005,3006,3007,3008,3009,3010], visible=False, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class Battle01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102,103], animationEffect=False)
        self.set_effect(triggerIds=[5000], visible=True) # UI
        self.show_guide_summary(entityId=20031201, textId=20031201) # 몬스터를 모두 처치하기

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101,102,103]):
            return Battle02(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[101,102,103])


class Battle02(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20031201)
        self.create_monster(spawnIds=[111,112,113,114], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[111,112,113,114]):
            return Battle03(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[111,112,113,114])


class Battle03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # UI
        self.show_guide_summary(entityId=20031202, textId=20031202) # 어둠의 씨앗 제거하기
        self.create_monster(spawnIds=[130], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[130]):
            return VineRemove01(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[130])


class VineRemove01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20031202)
        self.set_effect(triggerIds=[5001], visible=True) # Vine
        self.set_mesh(triggerIds=[3002,3003,3004], visible=False, arg3=500, delay=0, scale=0) # Invisible_Barrier
        self.set_random_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108], visible=False, meshCount=9, arg4=0, delay=50) # 덩굴
        self.set_random_mesh(triggerIds=[1110,1111,1112,1113,1114,1115,1116,1117,1118,1119], visible=False, meshCount=10, arg4=300, delay=50) # 덩굴
        self.set_random_mesh(triggerIds=[1120,1121,1122,1123,1124,1125,1126], visible=False, meshCount=7, arg4=200, delay=50) # 덩굴
        self.set_random_mesh(triggerIds=[1130,1131,1132,1133,1134,1135,1136,1137], visible=False, meshCount=8, arg4=100, delay=50) # 덩굴
        self.set_mesh(triggerIds=[1140], visible=False, arg3=200, delay=0, scale=10) # 씨앗
        self.set_mesh_animation(triggerIds=[1140], visible=False, arg3=0, arg4=0) # 씨앗

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            return MobWaveStart(self.ctx)


class MobWaveStart(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # UI
        self.show_guide_summary(entityId=20031203, textId=20031203) # 어둠의 씨앗 모두 제거하기
        self.create_monster(spawnIds=[121,122,123,124,125,126,127,128], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[121,122,123,124,125,126,127,128]):
            return MobWaveDelayRandom(self.ctx)
        if self.user_value(key='MobWaveStop', value=1):
            return Quit(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[121,122,123,124,125,126,127,128])


class MobWaveDelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=60):
            return MobWaveDelay01(self.ctx)
        if self.random_condition(rate=20):
            return MobWaveDelay02(self.ctx)
        if self.random_condition(rate=20):
            return MobWaveDelay03(self.ctx)
        if self.user_value(key='MobWaveStop', value=1):
            return Quit(self.ctx)


class MobWaveDelay01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return MobWaveStart(self.ctx)
        if self.user_value(key='MobWaveStop', value=1):
            return Quit(self.ctx)


class MobWaveDelay02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=17000):
            return MobWaveStart(self.ctx)
        if self.user_value(key='MobWaveStop', value=1):
            return Quit(self.ctx)


class MobWaveDelay03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return MobWaveStart(self.ctx)
        if self.user_value(key='MobWaveStop', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20031203)


initial_state = Setting
