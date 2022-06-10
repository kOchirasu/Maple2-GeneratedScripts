using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004150: Harry
/// </summary>
public class _11004150 : NpcScript {
    internal _11004150(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010571$ 
                // - What is it? 
                return true;
            case 10:
                // $script:0806025707010572$ 
                // - Are you here to participate in Mushking Royale too? I'm afraid we've already got a squad of four. I'll see you on the battlefield! 
                return true;
            default:
                return true;
        }
    }
}
