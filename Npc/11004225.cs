using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004225: Riol
/// </summary>
public class _11004225 : NpcScript {
    internal _11004225(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010799$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:0806222707010800$ 
                // - When I think back on that audition at $map:52000061$, I can't help but smile. That day changed my life.
                return true;
            default:
                return true;
        }
    }
}
