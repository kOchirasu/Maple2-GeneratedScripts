""" trigger/02000545_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,2071,2072,2073,2074,2075,2076,2077,2078,2079,2080,2081,2082,2083,2084,2085,2086,2087,2088,2089,2090,2091,2092,2093,2094,2095,2096,2097,2098,2099,2100,2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130,2131,2132], visible=True)
        self.set_mesh(triggerIds=[2141,2142], visible=True)
        self.set_mesh(triggerIds=[2133,2134], visible=False)
        self.set_mesh(triggerIds=[2150,2151], visible=False)
        self.set_mesh(triggerIds=[2999], visible=False)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_effect(triggerIds=[5007], visible=False)
        self.set_effect(triggerIds=[5008], visible=False)
        self.set_effect(triggerIds=[5009], visible=False)
        self.set_effect(triggerIds=[5010], visible=False)
        self.set_effect(triggerIds=[5011], visible=False)
        self.set_effect(triggerIds=[5012], visible=False)
        self.set_effect(triggerIds=[5013], visible=False)
        self.set_effect(triggerIds=[5014], visible=False)
        self.set_effect(triggerIds=[5015], visible=False)
        self.set_skill(triggerIds=[3000], enable=False)
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=104, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=105, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=106, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[703], jobCode=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[601,602,603,604,605,606,607], animationEffect=False)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000545_BF__MAIN__0$')
        self.add_balloon_talk(spawnId=604, duration=3500, delayTick=1000)
        self.set_npc_emotion_sequence(spawnId=602, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=603, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=604, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=605, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return 어이(self.ctx)


class 어이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004706, illust='PuppetBunnyBlue_normal', duration=5000, script='$02000545_BF__MAIN__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 몬스터웨이브안내토끼1(self.ctx)


class 몬스터웨이브안내토끼1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004706, illust='PuppetBunnyBlue_normal', duration=3000, script='$02000545_BF__MAIN__2$')
        self.add_balloon_talk(spawnId=602, msg='$02000545_BF__MAIN__3$', duration=3500, delayTick=500)
        self.add_balloon_talk(spawnId=603, msg='$02000545_BF__MAIN__4$', duration=3500, delayTick=1000)
        self.add_balloon_talk(spawnId=604, msg='$02000545_BF__MAIN__5$', duration=3500, delayTick=2000)
        self.set_npc_emotion_sequence(spawnId=602, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=603, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=604, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=605, sequenceName='Bore_A')
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_effect(triggerIds=[5005], visible=True)
        self.set_effect(triggerIds=[5006], visible=True)
        self.set_effect(triggerIds=[5007], visible=True)
        self.set_effect(triggerIds=[5008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 물가보여주기(self.ctx)


class 물가보여주기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.select_camera_path(pathIds=[7001], returnView=False)
        self.add_cinematic_talk(npcId=11004687, msg='$02000545_BF__MAIN__6$', align='left', duration=4000)
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_scene_skip(state=몬스터웨이브1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 몬스터웨이브1(self.ctx)


class 몬스터웨이브1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=2)
        self.set_event_ui(type=1, arg2='$02000545_BF__MAIN__7$', arg3='3000')
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.create_monster(spawnIds=[401,402,403,404,405], animationEffect=True)
        self.destroy_monster(spawnIds=[602,603,604,605])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 몬스터웨이브2(self.ctx)


class 몬스터웨이브2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004706, illust='PuppetBunnyBlue_normal', duration=3000, script='$02000545_BF__MAIN__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[401,402,403,404,405,201]):
            return 몬스터웨이브2시작안내(self.ctx)


class 몬스터웨이브2시작안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.side_npc_talk(npcId=11004706, illust='PuppetBunnyBlue_normal', duration=3000, script='$02000545_BF__MAIN__9$')
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_effect(triggerIds=[5007], visible=False)
        self.set_effect(triggerIds=[5008], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 엘리트스폰(self.ctx)


class 엘리트스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000545_BF__MAIN__10$', arg3='3000')
        self.set_onetime_effect(id=104, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.set_effect(triggerIds=[5009], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 엘리트스폰2(self.ctx)


class 엘리트스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000545_BF__MAIN__11$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[202]):
            return 엘리트사망(self.ctx)


class 엘리트사망(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004706, illust='PuppetBunnyBlue_normal', duration=3000, script='$02000545_BF__MAIN__12$')
        self.set_effect(triggerIds=[5009], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 보스시작전(self.ctx)


class 보스시작전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004706, illust='PuppetBunnyBlue_normal', duration=4000, script='$02000545_BF__MAIN__13$')
        self.set_onetime_effect(id=106, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 보스시작(self.ctx)


class 보스시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=2000545, portalId=3)
        self.set_scene_skip(state=거미여왕기어올라오기, action='nextState')
        self.select_camera_path(pathIds=[7004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 거미여왕스폰2(self.ctx)


class 거미여왕스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[608], animationEffect=True)
        self.add_cinematic_talk(npcId=11004687, msg='$02000545_BF__MAIN__14$', align='left', duration=3000)
        self.set_mesh(triggerIds=[2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,2071,2072,2073,2074,2075,2076,2077,2078,2079,2080,2081,2082,2083,2084,2085,2086,2087,2088,2089,2090,2091,2092,2093,2094,2095,2096,2097,2098,2099,2100,2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145,2146,2147], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 거미여왕스폰3(self.ctx)


class 거미여왕스폰3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050], visible=False)
        self.set_mesh(triggerIds=[2141,2142], visible=False)
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_effect(triggerIds=[5012], visible=True)
        self.set_effect(triggerIds=[5013], visible=True)
        self.set_effect(triggerIds=[5014], visible=True)
        self.set_effect(triggerIds=[5015], visible=True)
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npcId=11004687, msg='$02000545_BF__MAIN__15$', align='left', duration=3000)
        self.set_mesh(triggerIds=[2999], visible=True)
        self.set_effect(triggerIds=[5010], visible=True)
        self.destroy_monster(spawnIds=[606,607])
        self.set_npc_emotion_loop(spawnId=608, sequenceName='Stun_A', duration=10000000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 거미여왕스폰4(self.ctx)


class 거미여왕스폰4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[608])
        self.set_effect(triggerIds=[5010], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 거미여왕기어올라오기(self.ctx)


class 거미여왕기어올라오기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[7004,7005], returnView=False)
        self.set_effect(triggerIds=[5011], visible=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.add_cinematic_talk(npcId=23300010, msg='$02000545_BF__MAIN__16$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 거미여왕스폰5(self.ctx)


class 거미여왕스폰5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5011], visible=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5012], visible=False)
        self.set_effect(triggerIds=[5013], visible=False)
        self.set_effect(triggerIds=[5014], visible=False)
        self.set_effect(triggerIds=[5015], visible=False)
        self.destroy_monster(spawnIds=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 거미여왕스폰6(self.ctx)
        if self.monster_dead(boxIds=[102]):
            return 던전클리어(self.ctx)


class 거미여왕스폰6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004706, illust='PuppetBunnyBlue_normal', duration=3000, script='$02000545_BF__MAIN__17$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=90, spawnId=102, isRelative=True):
            return 쫄몬스터소환1(self.ctx)
        if self.monster_dead(boxIds=[102]):
            return 던전클리어(self.ctx)


class 쫄몬스터소환1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=23300010, illust='ArakiaDark_normal', duration=3000, script='$02000545_BF__MAIN__18$')
        self.create_monster(spawnIds=[301,302,303,304,305], animationEffect=False, animationDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=70, spawnId=102, isRelative=True):
            return 쫄몬스터소환2(self.ctx)
        if self.monster_dead(boxIds=[102]):
            return 던전클리어(self.ctx)


class 쫄몬스터소환2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=23300010, illust='ArakiaDark_normal', duration=3000, script='$02000545_BF__MAIN__19$')
        self.create_monster(spawnIds=[301,302,303,304,305], animationEffect=False, animationDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=29, spawnId=102, isRelative=True):
            return 쫄몬스터소환3(self.ctx)
        if self.monster_dead(boxIds=[102]):
            return 던전클리어(self.ctx)


class 쫄몬스터소환3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=23300010, illust='ArakiaDark_normal', duration=3000, script='$02000545_BF__MAIN__20$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102]):
            return 던전클리어(self.ctx)


class 던전클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000545_BF__MAIN__21$')
        self.destroy_monster(spawnIds=[301,302,303,304,305,501,502,505,507])
        self.create_monster(spawnIds=[602,603,604,605], animationEffect=False)
        self.add_balloon_talk(spawnId=602, msg='$02000545_BF__MAIN__22$', duration=3500, delayTick=500)
        self.add_balloon_talk(spawnId=603, msg='$02000545_BF__MAIN__23$', duration=3500, delayTick=800)
        self.add_balloon_talk(spawnId=604, msg='$02000545_BF__MAIN__24$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 던전클리어2(self.ctx)


class 던전클리어2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004706, illust='PuppetBunnyBlue_normal', duration=3000, script='$02000545_BF__MAIN__25$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 던전클리어3(self.ctx)


class 던전클리어3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = idle
