using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004466: Richmonde Guard
/// </summary>
public class _11004466 : NpcScript {
    internal _11004466(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012101$ 
                // - All's we—Huh?! You're an outlander! 
                return true;
            case 10:
                // $script:1227192907012102$ 
                // - All's we—Huh?! You're an outlander! 
                return true;
            default:
                return true;
        }
    }
}
