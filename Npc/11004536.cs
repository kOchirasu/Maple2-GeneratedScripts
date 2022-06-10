using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004536: Barricade Patrolman
/// </summary>
public class _11004536 : NpcScript {
    internal _11004536(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0104170807012607$ 
                // - Don't worry. I've got my eye on the enemy movements. 
                return true;
            case 10:
                // $script:0104170807012608$ 
                // - Don't worry. I've got my eye on the enemy movements. 
                // $script:0104170807012609$ 
                // - There are no signs of an enemy attack, but that can change in an instant. That's why we can't slack off on our patrols! 
                return true;
            default:
                return true;
        }
    }
}
