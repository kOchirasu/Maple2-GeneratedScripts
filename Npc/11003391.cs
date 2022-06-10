using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003391: Evagor
/// </summary>
public class _11003391 : NpcScript {
    internal _11003391(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1122180007011902$ 
                // - You should stay put, stranger.
                return true;
            case 10:
                // $script:1122180007011903$ 
                // - You should stay put, stranger.
                return true;
            default:
                return true;
        }
    }
}
