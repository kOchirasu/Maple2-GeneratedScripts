using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001076: Slacky
/// </summary>
public class _11001076 : NpcScript {
    internal _11001076(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003671$ 
                // - Have you been to $map:02000051$?
                return true;
            case 30:
                // $script:0831180407003674$ 
                // - One day, I'm going to become as great a weaponsmith as my big brother!
                return true;
            default:
                return true;
        }
    }
}
