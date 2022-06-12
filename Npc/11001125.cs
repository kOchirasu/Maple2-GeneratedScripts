using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001125: ABT-2XO
/// </summary>
public class _11001125 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0910171307003844$
    // - Entering data... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0915135007003944$
                // - Running database query on $MyPCName$... 
                //   Zero entries found in $map:2000270$ personnel list... Creating new entry.
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
