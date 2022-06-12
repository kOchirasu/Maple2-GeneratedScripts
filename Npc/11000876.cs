using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000876: Belhi
/// </summary>
public class _11000876 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003184$
    // - Do you know how the fairfolk greet each other?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003186$
                // - Forests are the cradle of life for woodland creatures like us fairfolk. If they get cut down, we'll fall with them.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
