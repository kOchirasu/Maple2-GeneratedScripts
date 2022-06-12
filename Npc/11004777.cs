using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004777: Snowleaf Fairfolk
/// </summary>
public class _11004777 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1122135407015958$
    // - Travel to the festively-decorated <font color="#ffd200">$map:63000072$</font> using the <font color="#00a2ed">Go to Event Map</font> button!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1122135407015959$
                // - Click on the <font color="#00a2ed">Go to Event Map</font> button to go to <font color="#ffd200">$map:63000072$</font>.
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
