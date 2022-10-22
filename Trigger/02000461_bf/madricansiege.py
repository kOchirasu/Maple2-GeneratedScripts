""" trigger/02000461_bf/madricansiege.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99999102, key='cannon02', value=0)
        set_user_value(triggerId=99999103, key='cannon03', value=0)
        set_user_value(triggerId=99999104, key='cannon04', value=0)
        set_user_value(triggerId=99999105, key='cannon05', value=0)
        set_user_value(triggerId=99999102, key='Bosscannon02', value=0)
        set_user_value(triggerId=99999103, key='Bosscannon03', value=0)
        set_user_value(triggerId=99999104, key='Bosscannon04', value=0)
        set_user_value(triggerId=99999105, key='Bosscannon05', value=0)
        set_agent(triggerIds=[8001,8002,8003,8004,8005,8006], visible=True)
        set_agent(triggerIds=[8101,8102,8103,8104,8105,8106], visible=True)
        set_agent(triggerIds=[8201,8202,8203,8204,8205,8206], visible=True)
        select_camera(triggerId=300, enable=True)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[2000,2001], arg2=False)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3801,3802,3803,3804], visible=True, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=201, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=202, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=203, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=204, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=205, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=206, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=207, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=208, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=209, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=210, visible=False, initialSequence='Dead_A')
        remove_buff(boxId=199, skillId=99910150)
        set_interact_object(triggerIds=[12000045], state=2)
        set_interact_object(triggerIds=[12000046], state=2)
        set_interact_object(triggerIds=[12000054], state=2)
        remove_buff(boxId=199, skillId=99910140)
        set_interact_object(triggerIds=[12000047], state=2)
        set_interact_object(triggerIds=[12000048], state=2)
        set_interact_object(triggerIds=[12000049], state=2)
        set_interact_object(triggerIds=[12000050], state=2)
        set_interact_object(triggerIds=[12000055], state=2)
        remove_buff(boxId=199, skillId=99910130)
        set_interact_object(triggerIds=[12000051], state=2)
        set_interact_object(triggerIds=[12000052], state=2)
        set_interact_object(triggerIds=[12000056], state=2)
        set_effect(triggerIds=[601], visible=False)
        remove_buff(boxId=199, skillId=99910160)
        set_interact_object(triggerIds=[12000053], state=2)
        set_interact_object(triggerIds=[12000057], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003,3004], visible=False, arg3=0, arg4=0, arg5=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 던전시작()

state.DungeonStart = DungeonStart


class 던전시작(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_agent(triggerIds=[8001,8002,8003,8004,8005,8006], visible=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2000,2001]):
            set_mesh(triggerIds=[3101,3102,3103,3104,3105], visible=False, arg3=0, arg4=0, arg5=5)
            set_agent(triggerIds=[8101,8102,8103,8104,8105,8106], visible=False)
            return 차지원1()


class 차지원1(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020], isAutoTargeting=False)
        create_monster(spawnIds=[2002,2003,2004,2005], arg2=False)
        set_user_value(triggerId=99999101, key='cannon01', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2901]):
            destroy_monster(spawnIds=[2002])
            set_agent(triggerIds=[8201,8202,8203,8204,8205,8206], visible=False)
            set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207], visible=False, arg3=0, arg4=0, arg5=5)
            return 다리건넘()


class 다리건넘(state.State):
    def on_enter(self):
        shadow_expedition(type='OpenBossGauge', maxGaugePoint=1400)
        set_user_value(triggerId=99999102, key='cannon02', value=1)
        set_user_value(triggerId=99999103, key='cannon03', value=1)
        set_user_value(triggerId=99999104, key='cannon04', value=1)
        set_user_value(triggerId=99999105, key='cannon05', value=1)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=450):
            return 차지원2()


class 차지원2(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[2021,2022,2023,2024,2025,2026,2027,2028,2029,2030], isAutoTargeting=False)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=700):
            return 차지원3()


class 차지원3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2031,2032,2033,2034,2035,2036], arg2=False)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=1400):
            shadow_expedition(type='CloseBossGauge')
            return 보스등장_딜레이()


class 보스등장_딜레이(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2901,2902,2903,2904,2905], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2099], arg2=True)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=50, spawnId=2099, isRelative=True):
            return 보스_버프패턴()


class 보스_버프패턴(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000461_BF__MADRICANSIEGE__0$', arg3='5000')
        set_user_value(triggerId=99999102, key='Bosscannon02', value=1)
        set_user_value(triggerId=99999103, key='Bosscannon03', value=1)
        set_user_value(triggerId=99999104, key='Bosscannon04', value=1)
        set_user_value(triggerId=99999105, key='Bosscannon05', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099]):
            return 던전종료()


class 던전종료(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='Madracan01')
        set_achievement(triggerId=199, type='trigger', achieve='ClearMadracanSiege')
        dungeon_clear()
        set_actor(triggerId=201, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=202, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=203, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=204, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=205, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=206, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=207, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=208, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=209, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=210, visible=True, initialSequence='Dead_A')
        set_user_value(triggerId=99999099, key='DungeonClear', value=1)
        set_user_value(triggerId=99999098, key='DungeonClear', value=1)
        set_user_value(triggerId=99999097, key='DungeonClear', value=1)
        set_user_value(triggerId=99999096, key='DungeonClear', value=1)
        set_user_value(triggerId=99999102, key='DungeonClear', value=1)
        set_user_value(triggerId=99999103, key='DungeonClear', value=1)
        set_user_value(triggerId=99999104, key='DungeonClear', value=1)
        set_user_value(triggerId=99999105, key='DungeonClear', value=1)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


