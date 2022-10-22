""" trigger/02000293_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2028,2029,2030,2031,2032,2033,2034,2035,2036])
        destroy_monster(spawnIds=[25000,25001,25002,25003,25004,25005,25006,25007,25008])
        set_interact_object(triggerIds=[10000509], state=1) # IronDoor
        set_interact_object(triggerIds=[10000504], state=0) # set01
        set_interact_object(triggerIds=[10000505], state=0) # set02
        set_interact_object(triggerIds=[10000520], state=0) # set03
        set_interact_object(triggerIds=[10000521], state=0) # set04
        set_interact_object(triggerIds=[10000522], state=0) # set05
        set_interact_object(triggerIds=[10000523], state=0) # set01_answer
        set_interact_object(triggerIds=[10000524], state=0) # set02_answer
        set_interact_object(triggerIds=[10000529], state=0) # set03_answer
        set_interact_object(triggerIds=[10000530], state=0) # set04_answer
        set_interact_object(triggerIds=[10000531], state=0) # set05_answer
        set_portal(portalId=2, visible=True, enabled=False, minimapVisible=True)
        set_mesh(triggerIds=[510000], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
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
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=600, enable=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=False, arg3=0, arg4=100, arg5=2)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002931, textId=20002931) # 온실에서 영혼 감옥 문을 열 수 있는 열쇠를 찾으세요.
        create_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025], arg2=False)

    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return 번생성1()
        if random_condition(rate=20):
            return 번생성2()
        if random_condition(rate=20):
            return 번생성3()
        if random_condition(rate=20):
            return 번생성4()
        if random_condition(rate=20):
            return 번생성5()


class 번생성1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000523], state=1)
        set_interact_object(triggerIds=[10000505], state=1)
        set_interact_object(triggerIds=[10000509], state=1)
        set_interact_object(triggerIds=[10000520], state=1)
        set_interact_object(triggerIds=[10000521], state=1)
        set_interact_object(triggerIds=[10000522], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000523], arg2=0):
            return 번아이템1()


class 번아이템1(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002931)
        create_monster(spawnIds=[25000], arg2=False)
        set_conversation(type=1, spawnId=25000, script='$02000293_BF__MAIN__1$', arg4=2)
        create_item(spawnIds=[500001])
        show_guide_summary(entityId=20002932, textId=20002932)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_timer(timerId='181', seconds=181) # item_lifetime

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000509], arg2=0):
            return 소멸대기()
        if time_expired(timerId='181'):
            return 소멸()


class 번생성2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000504], state=1)
        set_interact_object(triggerIds=[10000524], state=1)
        set_interact_object(triggerIds=[10000509], state=1)
        set_interact_object(triggerIds=[10000520], state=1)
        set_interact_object(triggerIds=[10000521], state=1)
        set_interact_object(triggerIds=[10000522], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000524], arg2=0):
            return 번아이템2()


class 번아이템2(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002931)
        create_monster(spawnIds=[25001], arg2=False)
        set_conversation(type=1, spawnId=25001, script='$02000293_BF__MAIN__3$', arg4=2)
        create_item(spawnIds=[500002])
        show_guide_summary(entityId=20002932, textId=20002932)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_timer(timerId='181', seconds=181) # item_lifetime

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000509], arg2=0):
            return 소멸대기()
        if time_expired(timerId='181'):
            return 소멸()


class 번생성3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000504], state=1)
        set_interact_object(triggerIds=[10000505], state=1)
        set_interact_object(triggerIds=[10000509], state=1)
        set_interact_object(triggerIds=[10000529], state=1)
        set_interact_object(triggerIds=[10000521], state=1)
        set_interact_object(triggerIds=[10000522], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000529], arg2=0):
            return 번아이템3()


class 번아이템3(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002931)
        create_monster(spawnIds=[25006], arg2=False)
        set_conversation(type=1, spawnId=25006, script='$02000293_BF__MAIN__13$', arg4=2)
        create_item(spawnIds=[500007])
        show_guide_summary(entityId=20002932, textId=20002932)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_timer(timerId='181', seconds=181) # item_lifetime

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000509], arg2=0):
            return 소멸대기()
        if time_expired(timerId='181'):
            return 소멸()


class 번생성4(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000504], state=1)
        set_interact_object(triggerIds=[10000505], state=1)
        set_interact_object(triggerIds=[10000509], state=1)
        set_interact_object(triggerIds=[10000520], state=1)
        set_interact_object(triggerIds=[10000530], state=1)
        set_interact_object(triggerIds=[10000522], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000530], arg2=0):
            return 번아이템4()


class 번아이템4(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002931)
        create_monster(spawnIds=[25007], arg2=False)
        set_conversation(type=1, spawnId=25007, script='$02000293_BF__MAIN__15$', arg4=2)
        create_item(spawnIds=[500008])
        show_guide_summary(entityId=20002932, textId=20002932)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_timer(timerId='181', seconds=181) # item_lifetime

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000509], arg2=0):
            return 소멸대기()
        if time_expired(timerId='181'):
            return 소멸()


class 번생성5(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000504], state=1)
        set_interact_object(triggerIds=[10000505], state=1)
        set_interact_object(triggerIds=[10000509], state=1)
        set_interact_object(triggerIds=[10000520], state=1)
        set_interact_object(triggerIds=[10000521], state=1)
        set_interact_object(triggerIds=[10000531], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000531], arg2=0):
            return 번아이템5()


class 번아이템5(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002931)
        create_monster(spawnIds=[25008], arg2=False)
        set_conversation(type=1, spawnId=25008, script='$02000293_BF__MAIN__17$', arg4=2)
        create_item(spawnIds=[500009])
        show_guide_summary(entityId=20002932, textId=20002932)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_timer(timerId='181', seconds=181) # item_lifetime

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000509], arg2=0):
            return 소멸대기()
        if time_expired(timerId='181'):
            return 소멸()


class 소멸대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[510000], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 소멸2()


class 소멸(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002932)
        destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2028,2029,2030,2031,2032,2033,2034,2035,2036])
        destroy_monster(spawnIds=[25000,25001,25002,25003,25004,25005,25006,25007,25008])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 준비()


class 소멸2(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002932)
        destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2028,2029,2030,2031,2032,2033,2034,2035,2036])


