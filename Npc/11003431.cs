using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003431: Rutatimo Karr
/// </summary>
public class _11003431 : NpcScript {
    internal _11003431(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008649$ 
                // - It can't be... I lost...?
                return true;
            case 10:
                // $script:0706160807008650$ 
                // - It can't be... I lost...?
                return true;
            default:
                return true;
        }
    }
}
