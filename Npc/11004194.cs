using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004194: Eupheria
/// </summary>
public class _11004194 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0813101707010956$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0813101707010957$
                // - The Green Lapenta... The flow of life... All these memories...
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
