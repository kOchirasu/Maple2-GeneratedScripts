using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003090: Orde
/// </summary>
public class _11003090 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0207122607007934$
    // - I guess field duty isn't that bad...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0207122607007935$
                // - It's hard to keep the Shadow Gate staffed with enough soldiers. If any more rifts like this open up, Maple World could be in serious trouble.
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
