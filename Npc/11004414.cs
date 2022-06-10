using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004414: Frosty Fairfolk
/// </summary>
public class _11004414 : NpcScript {
    internal _11004414(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1120173007011883$ 
                // - Don't you want to taste a fairfolk cake?
                return true;
            case 10:
                // $script:1120173007011886$ 
                // - There are many people who hunger for the fairfolk's cake. But it seems no two people have the same reaction to it! Isn't that interesting?
                // $script:1120173007011887$ 
                // - Some say it has no taste, others claim it's the most flavorful food they've ever eaten. Maybe it simply causes madness?
                // $script:1120173007011888$ 
                // - In any event, try some! Go on, eat it up!
                return true;
            default:
                return true;
        }
    }
}
