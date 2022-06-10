using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004355: Evelyn
/// </summary>
public class _11004355 : NpcScript {
    internal _11004355(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011765$ 
                // - Why can't we just have a normal celebration? This is ridiculous!
                return true;
            case 10:
                // $script:1109213607011766$ 
                // - This isn't... It's not at all what I wanted...
                return true;
            default:
                return true;
        }
    }
}
