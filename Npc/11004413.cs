using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004413: Frosty Fairfolk
/// </summary>
public class _11004413 : NpcScript {
    internal _11004413(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1120173007011877$ 
                // - Come visit $map:63000072$!
                return true;
            case 10:
                // $script:1120173007011880$ 
                // - $map:63000072$ is bursting with joyous holiday cheer! People are happy! Fairfolk are happy! And it's SNOWING!!
                // $script:1120173007011881$ 
                // - Board this toy train if you want to go to $map:63000072$! Toot, toot!
                // $script:1120173007011882$ 
                // - The toy train is completely free because it's run by the fairfolk! We barely even know what money is! Come along to $map:63000072$!
                return true;
            default:
                return true;
        }
    }
}
