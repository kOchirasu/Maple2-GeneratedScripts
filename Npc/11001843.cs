using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001843: Eks
/// </summary>
public class _11001843 : NpcScript {
    internal _11001843(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1020165907007310$ 
                // - My head... My shoulders... My spleen... 
                return true;
            case 30:
                // $script:1020165907007311$ 
                // - The room's spinning. Who knows when I'll be ready for active duty? 
                return true;
            default:
                return true;
        }
    }
}
