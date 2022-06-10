using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001077: Tantamomi
/// </summary>
public class _11001077 : NpcScript {
    internal _11001077(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003675$ 
                // - A full moon... The Kakas... Aw, please help me. Hah hah, hah hah hah!
                return true;
            case 30:
                // $script:0831180407003678$ 
                // - D-don't come near me. No! I need a friend. No, no... L-let's start again... Ha!
                return true;
            default:
                return true;
        }
    }
}
