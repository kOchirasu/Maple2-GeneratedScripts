using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001116: Valle
/// </summary>
public class _11001116 : NpcScript {
    internal _11001116(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003746$ 
                // - What brings you to this place?
                return true;
            case 30:
                // $script:0908154107003749$ 
                // - Did Mom send you to bring me home? I feel bad saying this, but I can't leave yet. Not until the garden is back to normal.
                return true;
            default:
                return true;
        }
    }
}
