""" trigger/02000328_bf/main.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[7001], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[7002], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[7003], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[7004], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[7005], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[7006], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[7007], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[7008], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[7009], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[7010], visible=False, animationEffect=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,2067,2068,2069,2070,2071,2072,2073,2074,2075,2076,2077,2078,2079,2080,2081,2082,2083,2084,2085,2086,2087,2088,2089,2090,2091,2092,2093,2094,2095,2096,2097,2098,2099,2100,2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145,2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166,2167,2168,2169,2170,2171,2172,2173,2174,2175,2176,2177,2178,2179,2180,2181,2182,2183,2184,2185,2186,2187,2188,2189,2190,2191,2192,2193,2194,2195,2196,2197,2198,2199,2200,2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220,2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240,2241,2242,2243,2244,2245,2246,2247,2248,2249,2250,2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270,2271], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2301,2302,2303,2304,2305,2306,2307,2308,2309,2310,2311,2312,2313,2314,2315,2316,2317,2318,2319,2320,2321,2322,2323,2324,2325,2326,2327,2328,2329,2330,2331,2332,2333,2334,2335,2336,2337,2338,2339,2340,2341,2342,2343], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[90000], visible=True) # monochrome
        self.set_effect(triggerIds=[84000], visible=False)
        self.set_effect(triggerIds=[84001], visible=False)
        self.set_effect(triggerIds=[84002], visible=False)
        self.create_monster(spawnIds=[10002,10006,10015], animationEffect=False)
        self.create_monster(spawnIds=[1101,1102,1103,1104,1105], animationEffect=False)
        self.create_monster(spawnIds=[1201,1202,1203,1204,1205], animationEffect=False)
        self.create_monster(spawnIds=[1301,1302,1303,1304,1305], animationEffect=False)
        self.create_monster(spawnIds=[1401,1402,1403,1404,1405], animationEffect=False)
        self.set_cube(triggerIds=[5001,5002,5003,5004], isVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[999998]):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 하층시작(self.ctx)


class 하층시작(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[999998], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.show_guide_summary(entityId=20003285, textId=20003285, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.select_camera(triggerId=60000, enable=True)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=False, arg3=500, delay=100, scale=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라줌인(self.ctx)


class 카메라줌인(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=60001, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.show_guide_summary(entityId=20003286, textId=20003286, duration=5000)
            self.remove_buff(boxId=999998, skillId=70000107)
            self.select_camera(triggerId=60001, enable=False)
            return 웨폰오브젝트대기(self.ctx)


class 웨폰오브젝트대기(common.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5001,5002,5003,5004], isVisible=True)
        self.create_monster(spawnIds=[2001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[999997]):
            self.set_effect(triggerIds=[84002], visible=True)
            self.set_conversation(type=1, spawnId=2001, script='$02000328_BF__MAIN__6$', arg4=5, arg5=0)
            return 하층클리어대기(self.ctx)


class 하층클리어대기(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20003286, textId=20003286, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[10000,10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015]):
            return 상층시작딜레이(self.ctx)


class 상층시작딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 상층시작(self.ctx)


class 상층시작(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[7001], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[7002], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[7003], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[7004], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[7005], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[7006], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[7007], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[7008], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[7009], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[7010], visible=True, animationEffect=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20003282, textId=20003282)
        self.select_camera(triggerId=60002, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            self.select_camera(triggerId=60002, enable=False)
            return 보스소환조건(self.ctx)


class 보스소환조건(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1101,1102,1103,1104,1201,1202,1203,1204,1205,1301,1302,1303,1304,1401,1402,1403,1404,1405,1105,1305]):
            return 보스소환딜레이(self.ctx)


class 보스소환딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스소환(self.ctx)


class 보스소환(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20003282)
        self.show_guide_summary(entityId=20003283, textId=20003283, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.add_buff(boxIds=[999998], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=60003, enable=True)
        self.create_monster(spawnIds=[1501], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 진행3(self.ctx)


class 진행3(common.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=999998, skillId=70000107)
        self.select_camera(triggerId=60003, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1501]):
            return 진행4(self.ctx)


class 진행4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 진행5(self.ctx)


class 진행5(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999996, key='clearafter', value=1)
        self.create_monster(spawnIds=[2000], animationEffect=False)
        self.move_npc(spawnId=2000, patrolName='MS2PatrolData0')
        self.set_conversation(type=1, spawnId=2000, script='$02000328_BF__MAIN__5$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 진행6(self.ctx)


class 진행6(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=60002, enable=True)
        self.set_conversation(type=1, spawnId=2000, script='$02000328_BF__MAIN__4$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 진행7(self.ctx)


class 진행7(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[90000], visible=False)
        self.set_effect(triggerIds=[84000], visible=True)
        self.set_effect(triggerIds=[84001], visible=True)
        self.set_mesh(triggerIds=[413,414,419,420], visible=True, arg3=100, delay=50, scale=2)
        self.set_mesh(triggerIds=[406,407,408,409,412,415,418,421,424,425,426,427], visible=True, arg3=200, delay=50, scale=2)
        self.set_mesh(triggerIds=[401,402,403,404,405,410,411,416,417,422,423,428,429,430,431,432], visible=True, arg3=300, delay=50, scale=2)
        self.set_mesh(triggerIds=[2301,2302,2303,2304,2305,2306,2307,2308,2309,2310,2311,2312], visible=False, arg3=300, delay=50, scale=2)
        self.set_mesh(triggerIds=[2313,2314,2315,2316,2317,2318,2319,2320,2321,2322,2323], visible=False, arg3=400, delay=50, scale=2)
        self.set_mesh(triggerIds=[2324,2325,2326,2327,2328,2329,2330,2331,2332,2333,2334], visible=False, arg3=500, delay=50, scale=2)
        self.set_mesh(triggerIds=[2335,2336,2337,2338,2339,2340,2341,2342,2343], visible=False, arg3=600, delay=50, scale=2)
        self.set_mesh(triggerIds=[601,602,603,604,605,606,607], visible=True, arg3=300, delay=50, scale=2)
        self.set_mesh(triggerIds=[608,609,610,611,612,613], visible=True, arg3=400, delay=50, scale=2)
        self.set_mesh(triggerIds=[614,615,616,617,618,619,620], visible=True, arg3=500, delay=50, scale=2)
        self.set_mesh(triggerIds=[621,622,623,624,625,626,627,628,629,630], visible=True, arg3=600, delay=50, scale=2)
        self.set_mesh(triggerIds=[631,632,633,634,635], visible=True, arg3=700, delay=50, scale=2)
        self.set_mesh(triggerIds=[701,702,703,704,705,706,707], visible=True, arg3=300, delay=50, scale=2)
        self.set_mesh(triggerIds=[708,709,710,711,712,713], visible=True, arg3=400, delay=50, scale=2)
        self.set_mesh(triggerIds=[714,715,716,717,718,719,720], visible=True, arg3=500, delay=50, scale=2)
        self.set_mesh(triggerIds=[721,722,723,724,725,726,727,728,729,730], visible=True, arg3=600, delay=50, scale=2)
        self.set_mesh(triggerIds=[726], visible=True, arg3=600, delay=50, scale=2)
        self.set_mesh(triggerIds=[731,732,733,734], visible=True, arg3=700, delay=50, scale=2)
        self.set_mesh(triggerIds=[801,802,803,804,805,806,807], visible=True, arg3=300, delay=50, scale=2)
        self.set_mesh(triggerIds=[808,809,810,811,812,813], visible=True, arg3=400, delay=50, scale=2)
        self.set_mesh(triggerIds=[814,815,816,817,818,819,820], visible=True, arg3=500, delay=50, scale=2)
        self.set_mesh(triggerIds=[821,822,823,824,825,826,827,828,829,830], visible=True, arg3=600, delay=50, scale=2)
        self.set_mesh(triggerIds=[831,832,833,834,835,836], visible=True, arg3=700, delay=50, scale=2)
        self.set_mesh(triggerIds=[901,902,903,904,905,906,907], visible=True, arg3=300, delay=50, scale=2)
        self.set_mesh(triggerIds=[908,909,910,911,912,913], visible=True, arg3=400, delay=50, scale=2)
        self.set_mesh(triggerIds=[914,915,916,917,918,919,920], visible=True, arg3=500, delay=50, scale=2)
        self.set_mesh(triggerIds=[921,922,923,924,925,926,927,928,929,930], visible=True, arg3=600, delay=50, scale=2)
        self.set_mesh(triggerIds=[931,932,933,934,935,936], visible=True, arg3=700, delay=50, scale=2)
        self.set_mesh(triggerIds=[636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656], visible=True, arg3=800, delay=50, scale=2)
        self.set_mesh(triggerIds=[735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755], visible=True, arg3=800, delay=50, scale=2)
        self.set_mesh(triggerIds=[837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857], visible=True, arg3=800, delay=50, scale=2)
        self.set_mesh(triggerIds=[937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957], visible=True, arg3=800, delay=50, scale=2)
        self.set_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021], visible=True, arg3=1000, delay=50, scale=2)
        self.set_mesh(triggerIds=[2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,2042], visible=True, arg3=1200, delay=50, scale=2)
        self.set_mesh(triggerIds=[2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,2054,2055,2056,2057,2058,2059,2060,2061,2062,2063], visible=True, arg3=1400, delay=50, scale=2)
        self.set_mesh(triggerIds=[2064,2065,2066,2067,2068,2069,2070,2071,2072,2073,2074,2075,2076,2077,2078,2079,2080,2081,2082,2083,2084], visible=True, arg3=1600, delay=50, scale=2)
        self.set_mesh(triggerIds=[2085,2086,2087,2088,2089,2090,2091,2092,2093,2094,2095,2096,2097,2098,2099,2100,2101,2102,2103,2104,2105], visible=True, arg3=1800, delay=50, scale=2)
        self.set_mesh(triggerIds=[2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126], visible=True, arg3=1000, delay=50, scale=2)
        self.set_mesh(triggerIds=[2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145,2146,2147], visible=True, arg3=1200, delay=50, scale=2)
        self.set_mesh(triggerIds=[2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166,2167,2168], visible=True, arg3=2400, delay=50, scale=2)
        self.set_mesh(triggerIds=[2169,2170,2171,2172,2173,2174,2175,2176,2177,2178,2179,2180,2181,2182,2183,2184,2185,2186,2187,2188,2189], visible=True, arg3=2600, delay=50, scale=2)
        self.set_mesh(triggerIds=[2190,2191,2192,2193,2194,2195,2196,2197,2198,2199,2200,2201,2202,2203,2204,2205,2206,2207,2208,2209,2210], visible=True, arg3=2800, delay=50, scale=2)
        self.set_mesh(triggerIds=[2211,2212,2213,2214,2215,2216,2217,2218,2219,2220,2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231], visible=True, arg3=3000, delay=50, scale=2)
        self.set_mesh(triggerIds=[2232,2233,2234,2235,2236,2237,2238,2239,2240,2241,2242,2243,2244,2245,2246,2247,2248,2249,2250,2251,2252], visible=True, arg3=3200, delay=50, scale=2)
        self.set_mesh(triggerIds=[2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270,2271], visible=True, arg3=3400, delay=50, scale=2)
        self.set_mesh(triggerIds=[450], visible=False, arg3=3600, delay=50, scale=2)
        self.set_mesh(triggerIds=[451], visible=False, arg3=3700, delay=50, scale=2)
        self.set_mesh(triggerIds=[452], visible=False, arg3=3800, delay=50, scale=2)
        self.set_mesh(triggerIds=[453], visible=False, arg3=3900, delay=50, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            self.select_camera(triggerId=60002, enable=False)
            return 진행8(self.ctx)


class 진행8(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 진행9(self.ctx)


class 진행9(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=999998, type='trigger', achieve='ClearPollutedgarden') # ClearPollutedgarden 퀘스트
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.dungeon_clear()
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20003284, textId=20003284)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.hide_guide_summary(entityId=20003284)
            return 종료2(self.ctx)


class 종료2(common.Trigger):
    pass


initial_state = 대기
