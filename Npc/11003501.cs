using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003501: Rosa
/// </summary>
public class _11003501 : NpcScript {
    internal _11003501(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115008978$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0816160115008979$ 
                // - If I'm going to get into Team Mushroom, I've got to study hard!
                return true;
            case 50:
                // $script:0816160115008981$ 
                // - I want to be best friends with all kinds of monsters. That's what Team Mushroom is all about, right?
                return true;
            default:
                return true;
        }
    }
}
