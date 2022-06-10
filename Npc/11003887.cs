using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003887: Ishura
/// </summary>
public class _11003887 : NpcScript {
    internal _11003887(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009927$ 
                // - Do you have something to say to me?
                return true;
            case 20:
                // $script:0515102507009928$ 
                // - Do you have something to say to me?
                return true;
            case 30:
                // $script:0515102507009929$ 
                // - Not bad.
                //   On behalf of Terrun Calibre, please accept my thanks.
                return true;
            default:
                return true;
        }
    }
}
