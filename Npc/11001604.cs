using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001604: Oska
/// </summary>
public class _11001604 : NpcScript {
    internal _11001604(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006092$ 
                // - What seems to be the problem? 
                return true;
            case 10:
                // $script:0515180307006141$ 
                // - We've agreed to accept each other as comrades. That means we must trust and respect one another. 
                return true;
            default:
                return true;
        }
    }
}
