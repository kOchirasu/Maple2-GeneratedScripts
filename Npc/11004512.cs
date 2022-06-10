using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004512: Mannstad Pilot
/// </summary>
public class _11004512 : NpcScript {
    internal _11004512(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012465$ 
                // - Hey, you're that outlander!
                return true;
            case 10:
                // $script:1228182607012466$ 
                // - Hey, you're that outlander!
                // $script:1228182607012467$ 
                // - This is the hub of all of our mobile forces, by land and air. But ever since the enemy pushed to our doorstep, we haven't been able to secure a supply line for the life of us.
                return true;
            default:
                return true;
        }
    }
}
