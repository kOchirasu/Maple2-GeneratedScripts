using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000705: Moya
/// </summary>
public class _11000705 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002837$
    // - What? If you have something to say, say it.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002840$
                // - What? Do you have business with me?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
