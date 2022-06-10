using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001362: Startz
/// </summary>
public class _11001362 : NpcScript {
    internal _11001362(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215222907005045$ 
                // - No one toys with my people and gets away with it.
                return true;
            case 40:
                // $script:1227194507005711$ 
                // - You saved us all, but I'm not going to thank you twice.
                // $script:1227194507005712$ 
                // - <i>Maybe</i> I'll treat you to a meal.
                return true;
            default:
                return true;
        }
    }
}
