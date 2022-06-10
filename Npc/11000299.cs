using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000299: Jake
/// </summary>
public class _11000299 : NpcScript {
    internal _11000299(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001188$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407001190$ 
                // - Things around here have never been THIS bad. Maybe it's time for a change of career.
                return true;
            default:
                return true;
        }
    }
}
