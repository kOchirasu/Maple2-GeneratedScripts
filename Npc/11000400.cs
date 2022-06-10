using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000400: Newton
/// </summary>
public class _11000400 : NpcScript {
    internal _11000400(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001619$ 
                // - How can I help you? 
                return true;
            case 20:
                // $script:0831180407001621$ 
                // - Dark Wind told me to take some time off, so I thought I'd take a vacation to the dam. Then I noticed that... thing... under the water. How am I supposed to rest now? 
                return true;
            case 30:
                // $script:0831180407001622$ 
                // - Dark Wind told me to take some time off, so I thought I'd take a vacation to the dam. Then I noticed that... thing... under the water. How am I supposed to rest now? 
                return true;
            default:
                return true;
        }
    }
}
