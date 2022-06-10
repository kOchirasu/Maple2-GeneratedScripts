using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003884: Pemberton
/// </summary>
public class _11003884 : NpcScript {
    internal _11003884(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009918$ 
                // - Hmm...
My duty is to look after lady $npcName:11003883[gender:0]$. 
                return true;
            case 20:
                // $script:0515102507009919$ 
                // - I will not forgive those who would dishonor my lady! 
                return true;
            case 30:
                // $script:0515102507009920$ 
                // - This is the first time I've seen $npcName:11003883[gender:0]$ so active. Whether or not this goes on depends on $MyPCName$'s role. 
                return true;
            default:
                return true;
        }
    }
}
