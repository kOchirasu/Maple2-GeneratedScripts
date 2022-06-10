using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003435: Asimov
/// </summary>
public class _11003435 : NpcScript {
    internal _11003435(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0726013907008728$ 
                // - ... 
                return true;
            case 10:
                // $script:0726013907008729$ 
                // - ... 
                return true;
            default:
                return true;
        }
    }
}
