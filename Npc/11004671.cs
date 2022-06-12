using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004671: NPCNAME_11004671_NAME:[F]Event
/// </summary>
public class _11004671 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0603204607014970$
    // - SCRIPTNPCNAM_0603204607014970_NAME:[F]Event
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0613033007015010$
                // - SCRIPTNPCNAM_0613033007015010_NAME:[F]Event
                return 30;
            case (30, 1):
                // $script:0613033007015011$
                // - SCRIPTNPCNAM_0613033007015011_NAME:[F]Event
                return 30;
            case (30, 2):
                // $script:0613033007015012$
                // - SCRIPTNPCNAM_0613033007015012_NAME:[F]Event
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
