using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001574: Einos
/// </summary>
public class _11001574 : NpcScript {
    internal _11001574(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006062$ 
                // - Hello.
                return true;
            case 10:
                // $script:0515180307006116$ 
                // - The life force will protect everyone.
                return true;
            default:
                return true;
        }
    }
}
