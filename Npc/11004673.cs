using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004673: NPCNAME_11004673_NAME:[F]Event
/// </summary>
public class _11004673 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0603204607014976$
    // - SCRIPTNPCNAM_0603204607014976_NAME:[F]Event
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0603204607014977$
                // - SCRIPTNPCNAM_0603204607014977_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007015021$
                    // - SCRIPTNPCNAM_0613033007015021_NAME:[F]Event
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0613033007015022$
                // - SCRIPTNPCNAM_0613033007015022_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007015023$
                    // - SCRIPTNPCNAM_0613033007015023_NAME:[F]Event
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0613033007015024$
                // - SCRIPTNPCNAM_0613033007015024_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007015025$
                    // - SCRIPTNPCNAM_0613033007015025_NAME:[F]Event
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0613033007015026$
                // - SCRIPTNPCNAM_0613033007015026_NAME:[F]Event
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
