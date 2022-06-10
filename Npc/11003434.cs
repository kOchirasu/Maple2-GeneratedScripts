using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003434: Einos
/// </summary>
public class _11003434 : NpcScript {
    internal _11003434(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0726013807008726$ 
                // - ...
                return true;
            case 10:
                // $script:0726013807008727$ 
                // - ...
                return true;
            default:
                return true;
        }
    }
}
