using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003185: Shadow Crow
/// </summary>
public class _11003185 : NpcScript {
    internal _11003185(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0510143807008458$ 
                // - The shadows see all. 
                return true;
            case 10:
                // $script:0510145607008462$ 
                // - Tremble before the way of the shadow. 
                return true;
            default:
                return true;
        }
    }
}
