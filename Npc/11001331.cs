using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001331: Mrs. Arthur
/// </summary>
public class _11001331 : NpcScript {
    internal _11001331(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005244$ 
                // - Oww...
                return true;
            case 30:
                // $script:1217012607005247$ 
                // - One moment, I'm shopping on cloud nine. The next moment... I don't know if I ever want to go shopping again!
                return true;
            default:
                return true;
        }
    }
}
