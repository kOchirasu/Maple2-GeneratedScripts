using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000375: Luvar
/// </summary>
public class _11000375 : NpcScript {
    internal _11000375(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001541$ 
                // - What seems to be the problem?
                return true;
            case 20:
                // $script:0831180407001543$ 
                // - Enoki mushrooms grow here. They require clean, undisturbed areas to flourish. I suppose no one ever comes to this valley, then.
                return true;
            default:
                return true;
        }
    }
}
