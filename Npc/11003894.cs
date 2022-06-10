using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003894: Black Mage
/// </summary>
public class _11003894 : NpcScript {
    internal _11003894(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009948$ 
                // - ... 
                return true;
            case 20:
                // $script:0515102507009949$ 
                // - ... 
                return true;
            case 30:
                // $script:0515102507009950$ 
                // - ... 
                return true;
            default:
                return true;
        }
    }
}
