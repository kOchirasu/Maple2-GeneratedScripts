using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004685: NPCNAME_11004685_NAME:[F]Event
/// </summary>
public class _11004685 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0617094407015030$
    // - SCRIPTNPCNAM_0617094407015030_NAME:[F]Event
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0617094407015033$
                // - SCRIPTNPCNAM_0617094407015033_NAME:[F]Event
                switch (selection) {
                    // $script:0617094407015034$
                    // - SCRIPTNPCNAM_0617094407015034_NAME:[F]Event
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0617094407015035$
                // - SCRIPTNPCNAM_0617094407015035_NAME:[F]Event
                switch (selection) {
                    // $script:0617095907015039$
                    // - SCRIPTNPCNAM_0617095907015039_NAME:[F]Event
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0617094407015036$
                // - SCRIPTNPCNAM_0617094407015036_NAME:[F]Event
                return 32;
            case (32, 1):
                // $script:0617095907015038$
                // - SCRIPTNPCNAM_0617095907015038_NAME:[F]Event
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
