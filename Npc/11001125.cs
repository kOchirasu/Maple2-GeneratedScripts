using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001125: ABT-2XO
/// </summary>
public class _11001125 : NpcScript {
    internal _11001125(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0910171307003844$ 
                // - Entering data...  
                return true;
            case 30:
                // $script:0915135007003944$ 
                // - Running database query on $MyPCName$... 
Zero entries found in $map:2000270$ personnel list... Creating new entry. 
                return true;
            default:
                return true;
        }
    }
}
