using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004057: Blackeye
/// </summary>
public class _11004057 : NpcScript {
    internal _11004057(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010087$ 
                // - We will aid you with your search.
                return true;
            case 10:
                // $script:0614185307010088$ 
                // - Talk to me whenever you need assistance.
                return true;
            default:
                return true;
        }
    }
}
