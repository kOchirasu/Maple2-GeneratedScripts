using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004029: Junta
/// </summary>
public class _11004029 : NpcScript {
    internal _11004029(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010045$ 
                // - Do you have something to tell me?
                return true;
            case 20:
                // $script:0614185307010046$ 
                // - Do you have something to tell me?
                return true;
            default:
                return true;
        }
    }
}
