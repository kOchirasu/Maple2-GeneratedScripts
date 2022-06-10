using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000221: Monica
/// </summary>
public class _11000221 : NpcScript {
    internal _11000221(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000966$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407000969$ 
                // - I love my dad more than anything else in the world. I just want to stay with him. 
                return true;
            default:
                return true;
        }
    }
}
