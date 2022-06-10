using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000108: Roy
/// </summary>
public class _11000108 : NpcScript {
    internal _11000108(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000442$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407000445$ 
                // - I heard $map:02000001$ is filled with beautiful ladies, so I came here, all decked out. What a waste of time. And now I'm stuck here! 
                return true;
            default:
                return true;
        }
    }
}
