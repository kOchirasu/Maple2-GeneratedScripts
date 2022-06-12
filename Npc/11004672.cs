using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004672: NPCNAME_11004672_NAME:[F]Event
/// </summary>
public class _11004672 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0603204607014973$
    // - SCRIPTNPCNAM_0603204607014973_NAME:[F]Event
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0613034407015027$
                // - SCRIPTNPCNAM_0613034407015027_NAME:[F]Event
                switch (selection) {
                    // $script:0613034407015028$
                    // - SCRIPTNPCNAM_0613034407015028_NAME:[F]Event
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0613033007015015$
                // - SCRIPTNPCNAM_0613033007015015_NAME:[F]Event
                switch (selection) {
                    // $script:0613034407015029$
                    // - SCRIPTNPCNAM_0613034407015029_NAME:[F]Event
                    case 0:
                        return 32;
                    // $script:0613033007015017$
                    // - SCRIPTNPCNAM_0613033007015017_NAME:[F]Event
                    case 1:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:0613033007015018$
                // - SCRIPTNPCNAM_0613033007015018_NAME:[F]Event
                return -1;
            case (33, 0):
                // $script:0613033007015019$
                // - SCRIPTNPCNAM_0613033007015019_NAME:[F]Event
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
