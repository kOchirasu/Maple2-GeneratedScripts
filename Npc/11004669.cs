using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004669: NPCNAME_11004669_NAME:[F]Event
/// </summary>
public class _11004669 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0603204607014964$
    // - SCRIPTNPCNAM_0603204607014964_NAME:[F]Event
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0603204607014966$
                // - SCRIPTNPCNAM_0603204607014966_NAME:[F]Event
                return 30;
            case (30, 1):
                // $script:0613033007015002$
                // - SCRIPTNPCNAM_0613033007015002_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007015003$
                    // - SCRIPTNPCNAM_0613033007015003_NAME:[F]Event
                    case 0:
                        return 31;
                    // $script:0613033007015004$
                    // - SCRIPTNPCNAM_0613033007015004_NAME:[F]Event
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0613033007015005$
                // - SCRIPTNPCNAM_0613033007015005_NAME:[F]Event
                return -1;
            case (32, 0):
                // $script:0613033007015006$
                // - SCRIPTNPCNAM_0613033007015006_NAME:[F]Event
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
