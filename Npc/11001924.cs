using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001924: Fisher
/// </summary>
public class _11001924 : NpcScript {
    internal _11001924(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121140707007425$ 
                // - I caught a prize fish!
                return true;
            case 30:
                // $script:1121184207007436$ 
                // - <b>AHH!</b> I had a fish on the line, and it got away... thanks to you!
                return true;
            default:
                return true;
        }
    }
}
