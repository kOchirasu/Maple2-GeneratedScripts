using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004139: Einos
/// </summary>
public class _11004139 : NpcScript {
    internal _11004139(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010549$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:0806025707010550$ 
                // - It is all well and good to forget one's troubles in a cheerful place such as this, but we cannot lose sight of what's real. A dark storm gathers over Maple World. Now more than ever, we need heroes. Will you answer the call?
                return true;
            default:
                return true;
        }
    }
}
