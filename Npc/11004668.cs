using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004668: NPCNAME_11004668_NAME:[F]Event
/// </summary>
public class _11004668 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0603204607014961$
    // - SCRIPTNPCNAM_0603204607014961_NAME:[F]Event
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0613033007014996$
                // - SCRIPTNPCNAM_0613033007014996_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007014997$
                    // - SCRIPTNPCNAM_0613033007014997_NAME:[F]Event
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0613033007014998$
                // - SCRIPTNPCNAM_0613033007014998_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007014999$
                    // - SCRIPTNPCNAM_0613033007014999_NAME:[F]Event
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0603204607014962$
                // - SCRIPTNPCNAM_0603204607014962_NAME:[F]Event
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
