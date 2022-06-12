using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000397: Adrienne
/// </summary>
public class _11000397 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001610$
    // - May I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001612$
                // - It may not look it, but my house is the most expensive in the neighborhood. There's nothing quite like living up so high. I hope my daughter appreciates how hard it was for me to get this place for us.
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
