using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003885: Eupheria
/// </summary>
public class _11003885 : NpcScript {
    internal _11003885(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009921$ 
                // - Our investigation continues.
                return true;
            case 20:
                // $script:0515102507009922$ 
                // - Our investigation continues.
                return true;
            case 30:
                // $script:0515102507009923$ 
                // - Thank you. I think I've started to unravel the truth.
                return true;
            default:
                return true;
        }
    }
}
