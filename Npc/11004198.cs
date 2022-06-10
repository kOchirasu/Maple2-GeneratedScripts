using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004198: Wolf Heart
/// </summary>
public class _11004198 : NpcScript {
    internal _11004198(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010644$ 
                // - May I help you?
                return true;
            case 10:
                // $script:0806025707010645$ 
                // - Our yearly pilgrimage through the Vayar Mountains has made the warriors of Murpagoth mighty. Perhaps you will join us on our next journey? That is of course, after we have proven ourselves on the fields of Mushtopia.
                return true;
            default:
                return true;
        }
    }
}
