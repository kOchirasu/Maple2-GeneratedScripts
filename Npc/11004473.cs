using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004473: Tenellus
/// </summary>
public class _11004473 : NpcScript {
    internal _11004473(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012145$ 
                // - Huh? Who're you?
                return true;
            case 10:
                // $script:1227192907012146$ 
                // - Huh? Who're you?
                // $script:1227192907012147$ 
                // - Wait, aren't you $MyPCName$? Wow! It really <i>is</i> you, in the flesh!
                switch (selection) {
                    // $script:1227192907012148$
                    // - Stop. You're making me blush.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012149$ 
                // - What, afraid of a little fame? How lame. This must be why they say you should never meet your heroes.
                return true;
            default:
                return true;
        }
    }
}
