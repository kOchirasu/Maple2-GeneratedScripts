using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003088: Orde
/// </summary>
public class _11003088 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0207122607007930$
    // - Who would have thought places like this would still exist in Maple World?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0207122607007931$
                // - I'd love to jump into that hot spring... just not when you're watching me, $MyPCName$.
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
