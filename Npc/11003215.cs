using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003215: Lennon
/// </summary>
public class _11003215 : NpcScript {
    internal _11003215(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008241$ 
                // - You've been following me. Why?
                return true;
            case 10:
                // $script:0404083307008242$ 
                // - I can tell you aren't one of $npcName:11000044$'s men.
                return true;
            default:
                return true;
        }
    }
}
