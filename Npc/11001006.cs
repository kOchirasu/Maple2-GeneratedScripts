using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001006: Edith
/// </summary>
public class _11001006 : NpcScript {
    internal _11001006(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003429$ 
                // - I haven't seen any strangers here for a long time. 
                return true;
            case 30:
                // $script:0831180407003432$ 
                // - Most people steer clear of this place because of the monsters. 
                return true;
            default:
                return true;
        }
    }
}
