using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004065: Rainbow Bridge
/// </summary>
public class _11004065 : NpcScript {
    internal _11004065(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010121$ 
                // - <font color="#909090">(This big, beautiful sculpture spans the lake at $map:02000038$. There's a plaque bearing an inscription on top.)</font> 
                return true;
            case 10:
                // $script:0619202207010122$ 
                // - <font color="#909090">(This big, beautiful sculpture spans the lake at $map:02000038$. There's a plaque bearing an inscription on top.)</font> 
                // $script:0619202207010123$ 
                // - <i>The "Rainbow Bridge" is the final work of Mandy, the genius architect responsible for the design of numerous famous buildings. Its purpose, and the significance of its design may never be known, as construction didn't start until after her death.</i> 
                // $script:0619202207010124$ 
                // - <i>The fact that the arch was constructed with such unusual materials—and that it is called a bridge despite functioning more as an obstacle than a pathway—are hallmarks of Mandy's famed eccentricity.</i> 
                // $script:0619202207010125$ 
                // - <i>Local legends tell of a portal to a magical land on the shore below the bridge's construction site.</i> 
                // $script:0619202207010126$ 
                // - <i>Whether you find this portal or not, we hope you enjoy the beautiful scenery here on the Rainbow Bridge.</i> 
                return true;
            default:
                return true;
        }
    }
}
