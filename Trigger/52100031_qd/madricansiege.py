""" trigger/52100031_qd/madricansiege.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8001,8002,8003,8004,8005,8006], visible=True)
        self.set_agent(triggerIds=[8101,8102,8103,8104,8105,8106], visible=True)
        self.set_agent(triggerIds=[8201,8202,8203,8204,8205,8206], visible=True)
        self.select_camera(triggerId=300, enable=True)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3101,3102,3103,3104,3105], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3801,3802,3803,3804], visible=True, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005], animationEffect=False)
        self.create_monster(spawnIds=[2000,2001], animationEffect=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return DungeonStart(self.ctx)


# <import path="./Data/Xml/Trigger/Dungeon_Common/CheckUserCount.xml" />
class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=연출종료)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_conversation(type=2, spawnId=11000015, script='$52100031_QD__MADRICANSIEGE__0$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004], visible=False, arg3=0, delay=0, scale=5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=300, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 던전시작(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_agent(triggerIds=[8001,8002,8003,8004,8005,8006], visible=False)
        self.set_conversation(type=1, spawnId=1001, script='$52100031_QD__MADRICANSIEGE__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2000,2001]):
            self.set_mesh(triggerIds=[3101,3102,3103,3104,3105], visible=False, arg3=0, delay=0, scale=5)
            self.set_agent(triggerIds=[8101,8102,8103,8104,8105,8106], visible=False)
            self.move_npc(spawnId=1102, patrolName='MS2PatrolData_1001A')
            return 차지원1(self.ctx)


class 차지원1(trigger_api.Trigger):
    def on_enter(self):
        self.spawn_npc_range(rangeIds=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030], isAutoTargeting=False)
        self.create_monster(spawnIds=[2002,2003,2004,2005], animationEffect=False)
        self.set_user_value(triggerId=99999101, key='cannon01', value=1)
        self.set_user_value(triggerId=99999099, key='faction01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2901]):
            self.destroy_monster(spawnIds=[2002])
            self.set_agent(triggerIds=[8201,8202,8203,8204,8205,8206], visible=False)
            self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207], visible=False, arg3=0, delay=0, scale=5)
            return 다리건넘(self.ctx)


class 다리건넘(trigger_api.Trigger):
    def on_enter(self):
        self.shadow_expedition(type='OpenBossGauge', maxGaugePoint=1000)
        self.set_user_value(triggerId=99999102, key='cannon02', value=1)
        self.set_user_value(triggerId=99999103, key='cannon03', value=1)
        self.set_user_value(triggerId=99999104, key='cannon04', value=1)
        self.set_user_value(triggerId=99999105, key='cannon05', value=1)
        # action name="몬스터를생성한다" arg1="2101" arg2="0" /

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=300):
            return 차지원2(self.ctx)


class 차지원2(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99999098, key='faction02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=600):
            return 차지원3(self.ctx)


class 차지원3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2031,2032,2033,2034,2035,2036], animationEffect=False)
        self.set_user_value(triggerId=99999097, key='faction03', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=1000):
            self.shadow_expedition(type='CloseBossGauge')
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2026,2027,2028,2029,2030], animationEffect=False)
        self.set_user_value(triggerId=99999096, key='faction04', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='bossSpawn', value=1):
            return 던전종료대기(self.ctx)


class 던전종료대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2099]):
            return 던전종료딜레이(self.ctx)


class 던전종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self):
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
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52100031, portalId=3)
        self.set_user_value(triggerId=99999099, key='DungeonClear', value=1)
        self.set_user_value(triggerId=99999098, key='DungeonClear', value=1)
        self.set_user_value(triggerId=99999097, key='DungeonClear', value=1)
        self.set_user_value(triggerId=99999096, key='DungeonClear', value=1)
        self.destroy_monster(spawnIds=[2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2099,2901,2902,2903,2904,2905], arg2=False)
        self.spawn_npc_range(rangeIds=[1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922], isAutoTargeting=False)
        self.set_portal(portalId=2, visible=True, enable=False, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 던전종료연출시작(self.ctx)


class 던전종료연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawnId=1922, sequenceName='Talk_A', duration=3000)
        self.add_cinematic_talk(npcId=11001567, illustId='11001567', msg='$52100031_QD__MADRICANSIEGE__2$', duration=3000, align='Right')
        self.set_skip(state=던전종료연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 던전종료연출01(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[3801,3802,3803,3804], visible=False, arg3=0, delay=0, scale=5)


class 던전종료연출01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=304, enable=True)
        self.set_npc_emotion_loop(spawnId=1921, sequenceName='Talk_A', duration=3000)
        self.add_cinematic_talk(npcId=11001566, illustId='11001566', msg='$52100031_QD__MADRICANSIEGE__3$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 던전종료연출02(self.ctx)


class 던전종료연출02(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_rotation(spawnId=1920, rotation=180)
        self.set_npc_emotion_loop(spawnId=1920, sequenceName='Talk_A', duration=3000)
        self.add_cinematic_talk(npcId=11001568, illustId='11001568', msg='$52100031_QD__MADRICANSIEGE__4$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 룬블레이더이동(self.ctx)


class 룬블레이더이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1920, patrolName='MS2PatrolData_1920')
        self.move_npc(spawnId=1921, patrolName='MS2PatrolData_1921')
        self.move_npc(spawnId=1922, patrolName='MS2PatrolData_1922')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 던전종료연출종료(self.ctx)


class 던전종료연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1920,1921,1922], arg2=False)
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트던전종료(self.ctx)


class 퀘스트던전종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
