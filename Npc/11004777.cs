using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004777: Snowleaf Fairfolk
/// </summary>
public class _11004777 : NpcScript {
    internal _11004777(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1122135407015958$ 
                // - Travel to the festively-decorated <font color="#ffd200">$map:63000072$</font> using the <font color="#00a2ed">Go to Event Map</font> button!
                return true;
            case 10:
                // $script:1122135407015959$ 
                // - Click on the <font color="#00a2ed">Go to Event Map</font> button to go to <font color="#ffd200">$map:63000072$</font>.
                return true;
            default:
                return true;
        }
    }
}
