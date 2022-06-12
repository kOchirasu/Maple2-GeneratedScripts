using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004670: NPCNAME_11004670_NAME:[F]Event
/// </summary>
public class _11004670 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0603204607014967$
    // - SCRIPTNPCNAM_0603204607014967_NAME:[F]Event
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0613033007015007$
                // - SCRIPTNPCNAM_0613033007015007_NAME:[F]Event
                return 30;
            case (30, 1):
                // $script:0613033007015008$
                // - SCRIPTNPCNAM_0613033007015008_NAME:[F]Event
                return 30;
            case (30, 2):
                // $script:0613033007015009$
                // - SCRIPTNPCNAM_0613033007015009_NAME:[F]Event
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
