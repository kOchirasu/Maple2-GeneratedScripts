using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004153: Yentayo
/// </summary>
public class _11004153 : NpcScript {
    internal _11004153(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010577$ 
                // - What seems to be the problem?
                return true;
            case 10:
                // $script:0806025707010578$ 
                // - There are chests hidden all over Maple World, but the ones in $map:02000499$ are... different. Hehe, you'll see!
                return true;
            default:
                return true;
        }
    }
}
