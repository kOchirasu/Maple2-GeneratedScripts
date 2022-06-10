using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003154: Ruly
/// </summary>
public class _11003154 : NpcScript {
    internal _11003154(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0306155707008039$ 
                // - What is it?
                return true;
            case 30:
                // $script:0306155707008042$ 
                // - If you're troubled, come look at these flowers. It helps. Really!
                return true;
            default:
                return true;
        }
    }
}
