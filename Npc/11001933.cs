using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001933: Apprentice Vava
/// </summary>
public class _11001933 : NpcScript {
    internal _11001933(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1122150407007456$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:1122214707007478$ 
                // - I'm <i>trying</i> to focus here!
                return true;
            default:
                return true;
        }
    }
}
