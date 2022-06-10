using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004182: Ishura
/// </summary>
public class _11004182 : NpcScript {
    internal _11004182(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010626$ 
                // - What is it? 
                return true;
            case 10:
                // $script:0806025707010627$ 
                // - Simply hiding is no strategy for victory. Especially up against the likes of an expert tracker like Arazaad. 
                return true;
            default:
                return true;
        }
    }
}
