""" trigger/02000461_bf/madricansiege.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99999102, key='cannon02', value=0)
        self.set_user_value(triggerId=99999103, key='cannon03', value=0)
        self.set_user_value(triggerId=99999104, key='cannon04', value=0)
        self.set_user_value(triggerId=99999105, key='cannon05', value=0)
        self.set_user_value(triggerId=99999102, key='Bosscannon02', value=0)
        self.set_user_value(triggerId=99999103, key='Bosscannon03', value=0)
        self.set_user_value(triggerId=99999104, key='Bosscannon04', value=0)
        self.set_user_value(triggerId=99999105, key='Bosscannon05', value=0)
        self.set_agent(triggerIds=[8001,8002,8003,8004,8005,8006], visible=True)
        self.set_agent(triggerIds=[8101,8102,8103,8104,8105,8106], visible=True)
        self.set_agent(triggerIds=[8201,8202,8203,8204,8205,8206], visible=True)
        self.select_camera(triggerId=300, enable=True)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[2000,2001], animationEffect=False)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3101,3102,3103,3104,3105], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3801,3802,3803,3804], visible=True, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=201, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=202, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=203, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=204, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=205, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=206, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=207, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=208, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=209, visible=False, initialSequence='Dead_A')
        self.set_actor(triggerId=210, visible=False, initialSequence='Dead_A')
        self.remove_buff(boxId=199, skillId=99910150)
        self.set_interact_object(triggerIds=[12000045], state=2)
        self.set_interact_object(triggerIds=[12000046], state=2)
        self.set_interact_object(triggerIds=[12000054], state=2)
        self.remove_buff(boxId=199, skillId=99910140)
        self.set_interact_object(triggerIds=[12000047], state=2)
        self.set_interact_object(triggerIds=[12000048], state=2)
        self.set_interact_object(triggerIds=[12000049], state=2)
        self.set_interact_object(triggerIds=[12000050], state=2)
        self.set_interact_object(triggerIds=[12000055], state=2)
        self.remove_buff(boxId=199, skillId=99910130)
        self.set_interact_object(triggerIds=[12000051], state=2)
        self.set_interact_object(triggerIds=[12000052], state=2)
        self.set_interact_object(triggerIds=[12000056], state=2)
        self.set_effect(triggerIds=[601], visible=False)
        self.remove_buff(boxId=199, skillId=99910160)
        self.set_interact_object(triggerIds=[12000053], state=2)
        self.set_interact_object(triggerIds=[12000057], state=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004], visible=False, arg3=0, delay=0, scale=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 던전시작(self.ctx)


class 던전시작(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)
        self.set_agent(triggerIds=[8001,8002,8003,8004,8005,8006], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2000,2001]):
            self.set_mesh(triggerIds=[3101,3102,3103,3104,3105], visible=False, arg3=0, delay=0, scale=5)
            self.set_agent(triggerIds=[8101,8102,8103,8104,8105,8106], visible=False)
            return 차지원1(self.ctx)


class 차지원1(common.Trigger):
    def on_enter(self):
        self.spawn_npc_range(rangeIds=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020], isAutoTargeting=False)
        self.create_monster(spawnIds=[2002,2003,2004,2005], animationEffect=False)
        self.set_user_value(triggerId=99999101, key='cannon01', value=1)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2901]):
            self.destroy_monster(spawnIds=[2002])
            self.set_agent(triggerIds=[8201,8202,8203,8204,8205,8206], visible=False)
            self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207], visible=False, arg3=0, delay=0, scale=5)
            return 다리건넘(self.ctx)


class 다리건넘(common.Trigger):
    def on_enter(self):
        self.shadow_expedition(type='OpenBossGauge', maxGaugePoint=1400)
        self.set_user_value(triggerId=99999102, key='cannon02', value=1)
        self.set_user_value(triggerId=99999103, key='cannon03', value=1)
        self.set_user_value(triggerId=99999104, key='cannon04', value=1)
        self.set_user_value(triggerId=99999105, key='cannon05', value=1)

    def on_tick(self) -> common.Trigger:
        if self.shadow_expedition_reach_point(point=450):
            return 차지원2(self.ctx)


class 차지원2(common.Trigger):
    def on_enter(self):
        self.spawn_npc_range(rangeIds=[2021,2022,2023,2024,2025,2026,2027,2028,2029,2030], isAutoTargeting=False)

    def on_tick(self) -> common.Trigger:
        if self.shadow_expedition_reach_point(point=700):
            return 차지원3(self.ctx)


class 차지원3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2031,2032,2033,2034,2035,2036], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.shadow_expedition_reach_point(point=1400):
            self.shadow_expedition(type='CloseBossGauge')
            return 보스등장_딜레이(self.ctx)


class 보스등장_딜레이(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2901,2902,2903,2904,2905], arg2=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2099], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=2099, isRelative=True):
            return 보스_버프패턴(self.ctx)


class 보스_버프패턴(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000461_BF__MADRICANSIEGE__0$', arg3='5000')
        self.set_user_value(triggerId=99999102, key='Bosscannon02', value=1)
        self.set_user_value(triggerId=99999103, key='Bosscannon03', value=1)
        self.set_user_value(triggerId=99999104, key='Bosscannon04', value=1)
        self.set_user_value(triggerId=99999105, key='Bosscannon05', value=1)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2099]):
            return 던전종료(self.ctx)


class 던전종료(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='Madracan01')
        self.set_achievement(triggerId=199, type='trigger', achieve='ClearMadracanSiege')
        self.dungeon_clear()
        self.set_actor(triggerId=201, visible=True, initialSequence='Dead_A')
        self.set_actor(triggerId=202, visible=True, initialSequence='Dead_A')
        self.set_actor(triggerId=203, visible=True, initialSequence='Dead_A')
        self.set_actor(triggerId=204, visible=True, initialSequence='Dead_A')
        self.set_actor(triggerId=205, visible=True, initialSequence='Dead_A')
        self.set_actor(triggerId=206, visible=True, initialSequence='Dead_A')
        self.set_actor(triggerId=207, visible=True, initialSequence='Dead_A')
        self.set_actor(triggerId=208, visible=True, initialSequence='Dead_A')
        self.set_actor(triggerId=209, visible=True, initialSequence='Dead_A')
        self.set_actor(triggerId=210, visible=True, initialSequence='Dead_A')
        self.set_user_value(triggerId=99999099, key='DungeonClear', value=1)
        self.set_user_value(triggerId=99999098, key='DungeonClear', value=1)
        self.set_user_value(triggerId=99999097, key='DungeonClear', value=1)
        self.set_user_value(triggerId=99999096, key='DungeonClear', value=1)
        self.set_user_value(triggerId=99999102, key='DungeonClear', value=1)
        self.set_user_value(triggerId=99999103, key='DungeonClear', value=1)
        self.set_user_value(triggerId=99999104, key='DungeonClear', value=1)
        self.set_user_value(triggerId=99999105, key='DungeonClear', value=1)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
