""" trigger/02000244_bf/lever.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2003], visible=False)
        set_mesh(triggerIds=[899], visible=False)
        set_interact_object(triggerIds=[10000303], state=1)
        set_interact_object(triggerIds=[10000302], state=1)
        set_interact_object(triggerIds=[10000301], state=1)
        set_mesh(triggerIds=[801,802,803,804], visible=False)
        set_mesh(triggerIds=[805,806,807,808], visible=True)
        set_mesh(triggerIds=[809,810,811,812], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000303], arg2=0):
            return 단계1()


class 단계1(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000302], arg2=0):
            return 단계2()


class 단계2(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000301], arg2=0):
            return 오픈()


class 오픈(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8001,8002], returnView=True)
        set_effect(triggerIds=[2003], visible=True)
        # <action name="메쉬를설정한다" arg1="899" arg2="1"/>
        set_mesh(triggerIds=[801,802,803,804], visible=True)
        set_mesh(triggerIds=[805,806,807,808], visible=False)
        set_mesh(triggerIds=[809,810,811,812], visible=False)
        set_timer(timerId='1', seconds=180)
        set_mesh(triggerIds=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145,2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166,2167,2168,2169,2170,2171,2172,2173,2174,2175,2176,2177,2178,2179,2180,2181,2182,2183,2184,2185,2186,2187,2188,2189,2190,2191,2192,2193,2194,2195,2196,2197,2198,2199], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return end()

    def on_exit(self):
        set_mesh(triggerIds=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145,2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166,2167,2168,2169,2170,2171,2172,2173,2174,2175,2176,2177,2178,2179,2180,2181,2182,2183,2184,2185,2186,2187,2188,2189,2190,2191,2192,2193,2194,2195,2196,2197,2198,2199], visible=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class end(state.State):
    pass


