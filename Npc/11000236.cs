using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000236: Jerome
/// </summary>
public class _11000236 : NpcScript {
    internal _11000236(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001007$ 
                // - What? 
                return true;
            case 30:
                // $script:0831180407001010$ 
                // - Don't say anything. Just go. 
                switch (selection) {
                    // $script:0831180407001011$
                    // - What are you doing?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407001012$ 
                // - I said go. Geez, this is such a mess!  
                return true;
            default:
                return true;
        }
    }
}
