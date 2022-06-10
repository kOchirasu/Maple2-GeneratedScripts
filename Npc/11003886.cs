using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003886: Landevian
/// </summary>
public class _11003886 : NpcScript {
    internal _11003886(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009924$ 
                // - What brings you here? 
                return true;
            case 20:
                // $script:0515102507009925$ 
                // - What brings you here? 
                return true;
            case 30:
                // $script:0515102507009926$ 
                // - You seem pretty handy, considering how you handled those tasks. If only Terrun Calibre had more people like you. 
                return true;
            default:
                return true;
        }
    }
}
