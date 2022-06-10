using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003965: Soul Binder
/// </summary>
public class _11003965 : NpcScript {
    internal _11003965(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010021$ 
                // - What a wondrous place.
                return true;
            case 20:
                // $script:0614143707010022$ 
                // - This place is beautiful. Don't you agree?
                return true;
            default:
                return true;
        }
    }
}
