using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003893: Madria
/// </summary>
public class _11003893 : NpcScript {
    internal _11003893(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009945$ 
                // - Why is the $npc:11003894[gender:0]$ constantly calling meetings? What a chore!
                return true;
            case 20:
                // $script:0515102507009946$ 
                // - Why is the $npc:11003894[gender:0]$ constantly calling meetings? What a chore!
                return true;
            case 30:
                // $script:0515102507009947$ 
                // - Gah, I'm so bored. I want to head back to the castle soon.
                return true;
            default:
                return true;
        }
    }
}
