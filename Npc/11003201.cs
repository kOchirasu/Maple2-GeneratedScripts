using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003201: Katvan
/// </summary>
public class _11003201 : NpcScript {
    internal _11003201(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008228$ 
                // - What brings you here? 
                return true;
            case 10:
                // $script:0404083307008229$ 
                // - What brings you here? 
                return true;
            default:
                return true;
        }
    }
}
