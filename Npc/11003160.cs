using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003160: Mindy
/// </summary>
public class _11003160 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0306155707008063$
    // - Oh, hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0306155707008066$
                // - I don't think anyone hates flowers, right? Everyone has to have a favorite flower or two.
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
