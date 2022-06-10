using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004167: Frey
/// </summary>
public class _11004167 : NpcScript {
    internal _11004167(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010589$ 
                // - Is there something I can help you with? 
                return true;
            case 10:
                // $script:0806025707010590$ 
                // - The Royal Guard protects the Empress and all of $map:02000001$. That is why we must never allow our skills to dull. So long as there are threats to peace in this world, we will not rest. 
                return true;
            default:
                return true;
        }
    }
}
