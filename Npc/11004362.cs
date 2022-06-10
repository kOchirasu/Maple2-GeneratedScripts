using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004362: Aiden
/// </summary>
public class _11004362 : NpcScript {
    internal _11004362(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011773$ 
                // - I never would have imagined that thing was real... 
                return true;
            case 10:
                // $script:1109213607011774$ 
                // - Life is full of surprises. Case in point, that creature in our living room, celebrating with us... 
                // $script:1120173007011851$ 
                // - ...I guess I could get used to this. 
                return true;
            default:
                return true;
        }
    }
}
