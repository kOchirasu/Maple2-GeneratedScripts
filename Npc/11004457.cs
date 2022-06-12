using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004457: Evian
/// </summary>
public class _11004457 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0109134107012662$
    // - Our first steps in a new world. I should be excited, but all I feel is nervous...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0109134107012663$
                // - Our first steps in a new world. I should be excited, but all I feel is nervous...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
