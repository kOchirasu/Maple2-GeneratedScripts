using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004334: Claudine
/// </summary>
public class _11004334 : NpcScript {
    internal _11004334(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010140307011584$ 
                // - Wow... 
                return true;
            case 10:
                // $script:1010140307011585$ 
                // - This place has exceeded my every expectation. 
                // $script:1010140307011586$ 
                // - To think, we're standing in a land where magic has been made to serve technology. It's almost too good to be true! 
                // $script:1010140307011587$ 
                // - See how these magic stones have been reduced to mere tools, like the cogwheel and the level? 
                // $script:1010140307011588$ 
                // - I must learn everything about this place... 
                // $script:1010140307011589$ 
                // - Soon, the Resistance will dominate Maple World using the technology of Kritias! 
                return true;
            default:
                return true;
        }
    }
}
