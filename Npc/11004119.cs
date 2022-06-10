using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004119: Lumiknight Warrior
/// </summary>
public class _11004119 : NpcScript {
    internal _11004119(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010481$ 
                // - I've got a mission to complete.
                return true;
            case 10:
                // $script:0720125407010482$ 
                // - You have our full support.
                return true;
            default:
                return true;
        }
    }
}
