using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001318: Kabo
/// </summary>
public class _11001318 : NpcScript {
    internal _11001318(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005037$ 
                // - Do you need help? 
                return true;
            case 40:
                // $script:1227194507005704$ 
                // - The greatest threat is the one we do not see. We need divine guidance to find our path. 
                // $script:1227194507005705$ 
                // - We humans are weak and hopeless, but we have a will that is stronger than steel. 
                // $script:1227194507005706$ 
                // - The divine recognizes this and guides our hand. Remember that, and you will never know fear. 
                return true;
            default:
                return true;
        }
    }
}
