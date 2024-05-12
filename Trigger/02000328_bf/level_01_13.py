""" trigger/02000328_bf/level_01_13.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[5113], is_visible=False)
        # self.spawn_monster(spawn_ids=[10013], auto_target=True)
        self.set_mesh(trigger_ids=[32301,32302,32303,32304,32305,32306,32307,32308,32309,32310,32311,32312,32313,32314,32315,32316,32317,32318,32319,32320,32321,32322,32323,32324,32325,32326,32327,32328,32329,32330,32331,32332,32333,32334,32335,32336,32337,32338,32339,32340,32341,32342,32343,32344,32345], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[], visible=True, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10015]):
            # self.set_cube(trigger_ids=[5113], is_visible=True)
            self.set_mesh(trigger_ids=[32301,32302,32303,32304,32305,32306,32307,32308,32309,32310,32311,32312,32313,32314,32315,32316,32317,32318,32319,32320,32321,32322,32323,32324,32325,32326,32327,32328,32329,32330,32331,32332,32333,32334,32335,32336,32337,32338,32339,32340,32341,32342,32343,32344,32345], visible=True, start_delay=0, interval=100, fade=1)
            self.set_mesh(trigger_ids=[42101,42102,42103,42104,42105,42106,42107,42108,42109,42110,42111,42112,42113,42114,42115,42116,42117,42118,42119,42120,42121,42122,42123,42124,42125,42126,42127,42128,42129,42130,42131,42132,42133,42134,42135,42136,42137,42138,42139,42140,42141,42142,42143,42144,42145,42146,42147,42148,42149,42150,42151,42152,42153,42154,42155,42156,42157,42158,42159,42160,42161,42162,42163,42164,42165,42166,42167,42168,42169,42170,42171,42172,42173,42174,42175,42176,42177,42178,42179,42180,42181,42182,42183,42184,42185,42186,42187,42188,42189,42190,42191,42192,42193,42194,42195,42196,42197,42198,42199,42200,42201,42202,42203,42204,42205,42206,42207,42208,42209,42210,42211,42212,42213,42214,42215,42216,42217,42218,42219,42220,42221,42222,42223,42224,42225,42226,42227,42228,42229,42230,42231,42232,42233,42234,42235,42236,42237,42238,42239,42240,42241,42242,42243,42244,42245,42246,42247,42248,42249,42250,42251,42252,42253,42254,42255,42256,42257,42258,42259,42260,42261,42262,42263,42264,42265,42266,42267,42268,42269,42270,42271,42272,42273,42274,42275,42276,42277,42278,42279,42280,42281,42282,42283,42284,42285,42286,42287,42288,42289,42290,42291,42292,42293,42294,42295,42296,42297,42298,42299,42300,42301,42302,42303], visible=False, start_delay=0, interval=0, fade=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
