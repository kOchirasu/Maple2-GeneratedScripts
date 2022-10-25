""" trigger/02000290_bf/main.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3000, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=3010, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=3020, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=3040, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002,3003,3004,3005,3006,3007,3008], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3011], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3012,3013,3014,3015,3016], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3021], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3041], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[5000], visible=False) # GuideUI
        self.destroy_monster(spawnIds=[1001])
        self.destroy_monster(spawnIds=[1002])
        self.destroy_monster(spawnIds=[1003])
        self.destroy_monster(spawnIds=[1004])
        self.destroy_monster(spawnIds=[2001])
        self.destroy_monster(spawnIds=[2002])
        self.enable_spawn_point_pc(spawnId=0, isEnable=True)
        self.enable_spawn_point_pc(spawnId=9991, isEnable=False)
        self.enable_spawn_point_pc(spawnId=9992, isEnable=False)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 로딩딜레이(self.ctx)


class 로딩딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # GuideUI
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[802,800], returnView=False)
        self.set_skip(state=CameraWalk01)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return CameraWalk01(self.ctx)


class CameraWalk01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[800,802], returnView=True)
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 준비(self.ctx)


class 준비(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[5000], visible=True) # GuideUI
        self.set_event_ui(type=1, arg2='$02000290_BF__MAIN__4$', arg3='5000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리거01시작(self.ctx)


# 첫 번째 문 열림
class 트리거01시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3000, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리거01진행(self.ctx)


class 트리거01진행(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3000, visible=False, initialSequence='Opened')
        self.set_mesh(triggerIds=[3002,3003,3004,3005,3006,3007,3008], visible=False, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1001]):
            return 트리거02시작(self.ctx)
        if self.wait_tick(waitTick=7000):
            return 트리거02시작(self.ctx)


# 두 번째 문 열림
class 트리거02시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3010, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3011], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1002], animationEffect=False)
        self.create_monster(spawnIds=[1003], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리거02진행(self.ctx)


class 트리거02진행(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3010, visible=False, initialSequence='Opened')
        self.set_mesh(triggerIds=[3012,3013,3014,3015,3016], visible=False, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1002,1003]):
            return 트리거03시작(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 트리거03시작(self.ctx)


# 세 번째 문 열림
class 트리거03시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3020, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3021], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리거03진행(self.ctx)


class 트리거03진행(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3020, visible=False, initialSequence='Opened')
        self.set_mesh(triggerIds=[3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033], visible=False, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1004]):
            return 트리거04시작(self.ctx)
        if self.wait_tick(waitTick=7000):
            return 트리거04시작(self.ctx)


class 트리거04시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3040, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3041], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리거04진행(self.ctx)


class 트리거04진행(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002902)
        self.set_actor(triggerId=3040, visible=False, initialSequence='Opened')
        self.set_mesh(triggerIds=[3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053], visible=False, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
