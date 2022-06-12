using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000125: Benjamin
/// </summary>
public class _11000125 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000540$
    // - How did it come to this?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000542$
                // - I've got to determine whether the mutated DNA strand was an outside contaminant, or was somehow mistakenly synthesized inside our test subjects...
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
