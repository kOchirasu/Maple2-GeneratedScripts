using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004024: Bjorn
/// </summary>
public class _11004024 : NpcScript {
    internal _11004024(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010035$ 
                // - I haven't given up yet. 
                return true;
            case 20:
                // $script:0614185307010036$ 
                // - I will restore my kingdom. 
                return true;
            default:
                return true;
        }
    }
}
