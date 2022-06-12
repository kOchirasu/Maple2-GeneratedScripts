using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004663: NPCNAME_11004663_NAME:[F]Event
/// </summary>
public class _11004663 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0603204607014946$
    // - SCRIPTNPCNAM_0603204607014946_NAME:[F]Event
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0603204607014947$
                // - SCRIPTNPCNAM_0603204607014947_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007014979$
                    // - SCRIPTNPCNAM_0613033007014979_NAME:[F]Event
                    case 0:
                        return 31;
                    // $script:0613033007014980$
                    // - SCRIPTNPCNAM_0613033007014980_NAME:[F]Event
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0613033007014981$
                // - SCRIPTNPCNAM_0613033007014981_NAME:[F]Event
                return 31;
            case (31, 1):
                // $script:0613033007014982$
                // - SCRIPTNPCNAM_0613033007014982_NAME:[F]Event
                return 31;
            case (31, 2):
                // $script:0613033007014983$
                // - SCRIPTNPCNAM_0613033007014983_NAME:[F]Event
                return 31;
            case (31, 3):
                // $script:0613033007014984$
                // - SCRIPTNPCNAM_0613033007014984_NAME:[F]Event
                return 31;
            case (31, 4):
                // $script:0613033007014985$
                // - SCRIPTNPCNAM_0613033007014985_NAME:[F]Event
                return 31;
            case (31, 5):
                // $script:0613033007014986$
                // - SCRIPTNPCNAM_0613033007014986_NAME:[F]Event
                return -1;
            case (32, 0):
                // $script:0613033007014987$
                // - SCRIPTNPCNAM_0613033007014987_NAME:[F]Event
                return 32;
            case (32, 1):
                // $script:0613033007014988$
                // - SCRIPTNPCNAM_0613033007014988_NAME:[F]Event
                return 32;
            case (32, 2):
                // $script:0613033007014989$
                // - SCRIPTNPCNAM_0613033007014989_NAME:[F]Event
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Next,
            (31, 2) => NpcTalkButton.Next,
            (31, 3) => NpcTalkButton.Next,
            (31, 4) => NpcTalkButton.Next,
            (31, 5) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Next,
            (32, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
