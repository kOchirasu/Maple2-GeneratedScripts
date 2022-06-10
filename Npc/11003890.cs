using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003890: Katvan
/// </summary>
public class _11003890 : NpcScript {
    internal _11003890(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009936$ 
                // - It's been a while, Red Cape.
                return true;
            case 20:
                // $script:0515102507009937$ 
                // - It's been a while, Red Cape.
                return true;
            case 30:
                // $script:0515102507009938$ 
                // - I would give my life for the $npc:11003891[gender:0]$. He is the only reason I still live.
                return true;
            default:
                return true;
        }
    }
}
