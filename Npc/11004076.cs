using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004076: Yellow Butterfly
/// </summary>
public class _11004076 : NpcScript {
    internal _11004076(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010213$ 
                // - Look at that dumb wormy-worm! 
                return true;
            case 10:
                // $script:0619202207010214$ 
                // - Look at that dumb wormy-worm! 
                // $script:0619202207010215$ 
                // - You see that fat little bug over there? Do <i>you</i> think he can become a butterfly? 
                switch (selection) {
                    // $script:0619202207010216$
                    // - That's correct.
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0619202207010217$
                    // - No.
                    case 1:
                        Id = 41;
                        return false;
                }
                return true;
            case 40:
                // $script:0619202207010218$ 
                // - Pssh! You think that's how a real caterpillar looks? You must have a tiny brain. 
                return true;
            case 41:
                // $script:0619202207010219$ 
                // - Yeah, exactly. Yet that poor creature actually think it's gonna be a butterfly. Can you believe that? 
                return true;
            default:
                return true;
        }
    }
}
