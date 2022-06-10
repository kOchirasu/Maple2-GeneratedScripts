using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003847: Schatten
/// </summary>
public class _11003847 : NpcScript {
    internal _11003847(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0117175907009809$ 
                // - I am the shadow that evil fears.
                return true;
            case 10:
                // $script:0117175907009810$ 
                // - Hey there. Did you miss me?
                return true;
            default:
                return true;
        }
    }
}
