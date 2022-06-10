using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001379: Zenka
/// </summary>
public class _11001379 : NpcScript {
    internal _11001379(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217144507005373$ 
                // - You called? 
                return true;
            case 30:
                // $script:1217144507005376$ 
                // - Where in the world did they come from? Of course they chose <i>today</i> to cause a mess. When the dust clears, it'll be us security guards who take the fall for this. 
                return true;
            default:
                return true;
        }
    }
}
