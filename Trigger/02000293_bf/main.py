""" trigger/02000293_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2028,2029,2030,2031,2032,2033,2034,2035,2036])
        self.destroy_monster(spawnIds=[25000,25001,25002,25003,25004,25005,25006,25007,25008])
        self.set_interact_object(triggerIds=[10000509], state=1) # IronDoor
        self.set_interact_object(triggerIds=[10000504], state=0) # set01
        self.set_interact_object(triggerIds=[10000505], state=0) # set02
        self.set_interact_object(triggerIds=[10000520], state=0) # set03
        self.set_interact_object(triggerIds=[10000521], state=0) # set04
        self.set_interact_object(triggerIds=[10000522], state=0) # set05
        self.set_interact_object(triggerIds=[10000523], state=0) # set01_answer
        self.set_interact_object(triggerIds=[10000524], state=0) # set02_answer
        self.set_interact_object(triggerIds=[10000529], state=0) # set03_answer
        self.set_interact_object(triggerIds=[10000530], state=0) # set04_answer
        self.set_interact_object(triggerIds=[10000531], state=0) # set05_answer
        self.set_portal(portalId=2, visible=True, enable=False, minimapVisible=True)
        self.set_mesh(triggerIds=[510000], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)
        self.set_skip(state=CameraWalk01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=600, enable=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=False, arg3=0, delay=100, scale=2)
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 온실에서 영혼 감옥 문을 열 수 있는 열쇠를 찾으세요.
        self.show_guide_summary(entityId=20002931, textId=20002931)
        self.create_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return 번생성1(self.ctx)
        if self.random_condition(rate=20):
            return 번생성2(self.ctx)
        if self.random_condition(rate=20):
            return 번생성3(self.ctx)
        if self.random_condition(rate=20):
            return 번생성4(self.ctx)
        if self.random_condition(rate=20):
            return 번생성5(self.ctx)


class 번생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000523], state=1)
        self.set_interact_object(triggerIds=[10000505], state=1)
        self.set_interact_object(triggerIds=[10000509], state=1)
        self.set_interact_object(triggerIds=[10000520], state=1)
        self.set_interact_object(triggerIds=[10000521], state=1)
        self.set_interact_object(triggerIds=[10000522], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000523], stateValue=0):
            return 번아이템1(self.ctx)


class 번아이템1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20002931)
        self.create_monster(spawnIds=[25000], animationEffect=False)
        self.set_conversation(type=1, spawnId=25000, script='$02000293_BF__MAIN__1$', arg4=2)
        self.create_item(spawnIds=[500001])
        self.show_guide_summary(entityId=20002932, textId=20002932)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_timer(timerId='181', seconds=181) # item_lifetime

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000509], stateValue=0):
            return 소멸대기(self.ctx)
        if self.time_expired(timerId='181'):
            return 소멸(self.ctx)


class 번생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000504], state=1)
        self.set_interact_object(triggerIds=[10000524], state=1)
        self.set_interact_object(triggerIds=[10000509], state=1)
        self.set_interact_object(triggerIds=[10000520], state=1)
        self.set_interact_object(triggerIds=[10000521], state=1)
        self.set_interact_object(triggerIds=[10000522], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000524], stateValue=0):
            return 번아이템2(self.ctx)


class 번아이템2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20002931)
        self.create_monster(spawnIds=[25001], animationEffect=False)
        self.set_conversation(type=1, spawnId=25001, script='$02000293_BF__MAIN__3$', arg4=2)
        self.create_item(spawnIds=[500002])
        self.show_guide_summary(entityId=20002932, textId=20002932)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_timer(timerId='181', seconds=181) # item_lifetime

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000509], stateValue=0):
            return 소멸대기(self.ctx)
        if self.time_expired(timerId='181'):
            return 소멸(self.ctx)


class 번생성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000504], state=1)
        self.set_interact_object(triggerIds=[10000505], state=1)
        self.set_interact_object(triggerIds=[10000509], state=1)
        self.set_interact_object(triggerIds=[10000529], state=1)
        self.set_interact_object(triggerIds=[10000521], state=1)
        self.set_interact_object(triggerIds=[10000522], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000529], stateValue=0):
            return 번아이템3(self.ctx)


class 번아이템3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20002931)
        self.create_monster(spawnIds=[25006], animationEffect=False)
        self.set_conversation(type=1, spawnId=25006, script='$02000293_BF__MAIN__13$', arg4=2)
        self.create_item(spawnIds=[500007])
        self.show_guide_summary(entityId=20002932, textId=20002932)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_timer(timerId='181', seconds=181) # item_lifetime

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000509], stateValue=0):
            return 소멸대기(self.ctx)
        if self.time_expired(timerId='181'):
            return 소멸(self.ctx)


class 번생성4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000504], state=1)
        self.set_interact_object(triggerIds=[10000505], state=1)
        self.set_interact_object(triggerIds=[10000509], state=1)
        self.set_interact_object(triggerIds=[10000520], state=1)
        self.set_interact_object(triggerIds=[10000530], state=1)
        self.set_interact_object(triggerIds=[10000522], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000530], stateValue=0):
            return 번아이템4(self.ctx)


class 번아이템4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20002931)
        self.create_monster(spawnIds=[25007], animationEffect=False)
        self.set_conversation(type=1, spawnId=25007, script='$02000293_BF__MAIN__15$', arg4=2)
        self.create_item(spawnIds=[500008])
        self.show_guide_summary(entityId=20002932, textId=20002932)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_timer(timerId='181', seconds=181) # item_lifetime

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000509], stateValue=0):
            return 소멸대기(self.ctx)
        if self.time_expired(timerId='181'):
            return 소멸(self.ctx)


class 번생성5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000504], state=1)
        self.set_interact_object(triggerIds=[10000505], state=1)
        self.set_interact_object(triggerIds=[10000509], state=1)
        self.set_interact_object(triggerIds=[10000520], state=1)
        self.set_interact_object(triggerIds=[10000521], state=1)
        self.set_interact_object(triggerIds=[10000531], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000531], stateValue=0):
            return 번아이템5(self.ctx)


class 번아이템5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20002931)
        self.create_monster(spawnIds=[25008], animationEffect=False)
        self.set_conversation(type=1, spawnId=25008, script='$02000293_BF__MAIN__17$', arg4=2)
        self.create_item(spawnIds=[500009])
        self.show_guide_summary(entityId=20002932, textId=20002932)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_timer(timerId='181', seconds=181) # item_lifetime

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000509], stateValue=0):
            return 소멸대기(self.ctx)
        if self.time_expired(timerId='181'):
            return 소멸(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[510000], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 소멸2(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20002932)
        self.destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2028,2029,2030,2031,2032,2033,2034,2035,2036])
        self.destroy_monster(spawnIds=[25000,25001,25002,25003,25004,25005,25006,25007,25008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 준비(self.ctx)


class 소멸2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20002932)
        self.destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2028,2029,2030,2031,2032,2033,2034,2035,2036])


initial_state = 대기
