using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004297: Ghost
/// </summary>
public class _11004297 : NpcScript {
    internal _11004297(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1002141907011375$ 
                // - I said I wanted the best. <i>The best!</i>
                return true;
            case 30:
                // $script:1002141907011378$ 
                // - I told my son to book me a room in the empire's finest hotel, and he put me up in <i>this</i> dump. Lo and behold, a picture frame dropped on my head while I slept, and now I'm dead! The other ghosts will laugh me out of town when they hear about this...
                switch (selection) {
                    // $script:1002141907011379$
                    // - There, there. It's okay.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1002141907011380$ 
                // - Just be careful around anything that hangs on a wall, okay? You never know when it'll fall!
                return true;
            default:
                return true;
        }
    }
}
