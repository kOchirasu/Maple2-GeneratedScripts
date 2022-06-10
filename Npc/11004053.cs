using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004053: Blackeye
/// </summary>
public class _11004053 : NpcScript {
    internal _11004053(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010079$ 
                // - We are ready to head out at a moment's notice.
                return true;
            case 10:
                // $script:0614185307010080$ 
                // - We are ready to head out at a moment's notice.
                return true;
            default:
                return true;
        }
    }
}
