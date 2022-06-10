using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001110: Marr
/// </summary>
public class _11001110 : NpcScript {
    internal _11001110(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003732$ 
                // - What's up?
                return true;
            case 30:
                // $script:0908154107003735$ 
                // - I knew $npcName:11000064[gender:0]$ didn't betray us!
                return true;
            default:
                return true;
        }
    }
}
