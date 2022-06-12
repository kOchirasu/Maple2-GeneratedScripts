using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000972: Sisel
/// </summary>
public class _11000972 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003364$
    // - This situation is more serious than I thought, but I'm not going to back down now!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003366$
                // - I'll do anything for the safety and peace of $map:02000076$. I'll fight as long as I can, for the honor of the Green Hoods.
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
