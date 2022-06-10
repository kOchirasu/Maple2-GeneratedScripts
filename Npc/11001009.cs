using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001009: Fachinni
/// </summary>
public class _11001009 : NpcScript {
    internal _11001009(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003442$ 
                // - Wah! Geez!
                return true;
            case 30:
                // $script:0831180407003445$ 
                // - Are you also here because of that beanstalk rumor?
                return true;
            default:
                return true;
        }
    }
}
